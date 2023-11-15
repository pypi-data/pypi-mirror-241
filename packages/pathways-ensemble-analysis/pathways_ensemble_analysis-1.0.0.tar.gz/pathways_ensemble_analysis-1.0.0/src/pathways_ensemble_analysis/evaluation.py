import os
from numpy import mod
import pyam
import pandas as pd
from typing import Dict, Union, List, Optional
import importlib
import logging

from .criteria.base import Criterion

logger = logging.getLogger(__name__)


def get_values(
    file: Union[os.PathLike, pyam.IamDataFrame],
    criteria: List[Criterion],
) -> pd.DataFrame:
    """Get values for specified criteria

    Parameters
    ----------
    file : Union[os.PathLike, pyam.IamDataFrame]
        path to a csv file holding a pyam.IamDataFrame
    criteria : List[Criterion]
        List of Criterion objects

    Returns
    -------
    pd.DataFrame
        DataFrame holding the values of the evaluated criteria with index levels 'module' and 'variable'
        and column levels 'model' and 'scenario'
    """

    if not isinstance(file, pyam.IamDataFrame):
        file = pyam.IamDataFrame(pd.read_csv(file))

    values = []
    for criterion in criteria:
        logger.info(f"Determining values for: {criterion.criterion_name}")
        values.append(criterion.get_values(file))

    value_matrix = pd.concat(values).unstack("variable").T

    return value_matrix


def filter_values(
    value_matrix: pd.DataFrame,
    drop_conditions: Dict[str, Dict[str, Union[float, List[float]]]],
) -> pd.DataFrame:
    """Filters a value_matrix as obtained via the get_values function based on specified drop criteria

    Parameters
    ----------
    value_matrix : pd.DataFrame
        DataFrame holding the values of the evaluated criteria with index levels 'module' and 'variable'
        and column levels 'model' and 'scenario'
    drop_conditions : Dict[str, Dict[str, Union[float, List[float]]]], optional
        Dictionary: keys - criteria names (based on the module names in which the criteria are implemented);
        values - dictionaries with keys 'mode' (can be '<=',`>=`,'outside','inside') and 'value' (either as a float or a tuple of floats);
        Examples:
        - {'non_bio_res_share': {'mode': '<=', 'value': 0.5}} - values smaller or equal to 0.5 are dropped for the criterion 'non_bio_res_share'
        - {'historical_emissions': {'mode': 'outside', 'value': (30000, 45000)}} - values outside of the given range are dropped for the criterion 'historical_emissions'

    Returns
    -------
    pd.DataFrame
        Filtered value_matrix
    """

    value_matrix = value_matrix.transpose()

    keep = pd.Series(True, value_matrix.index)
    for criterion, drop_condition in drop_conditions.items():
        values = value_matrix[[criterion]]
        mode, drop_value = drop_condition["mode"], drop_condition["value"]

        if mode == "<=":
            assert isinstance(drop_value, float) | isinstance(drop_value, int)
            drop = values <= drop_value
        elif mode == ">=":
            assert isinstance(drop_value, float) | isinstance(drop_value, int)
            drop = values >= drop_value
        elif mode == "inside":
            assert isinstance(drop_value, List)
            drop = (values >= drop_value[0]) & (values <= drop_value[1])
        elif mode == "outside":
            assert isinstance(drop_value, List)
            drop = (values <= drop_value[0]) | (values >= drop_value[1])
        else:
            raise ValueError(
                f"{mode} is not an eligible mode, options are: '<=', `>=`, 'outside', 'inside'"
            )

        drop = drop.any(axis=1)
        keep &= ~drop

        logger.info(
            "%d Pathways with values %s %s in criterion %s and will be dropped (%d left).",
            drop.sum(),
            mode,
            "[{:.5g}, {:.5g}]".format(drop_value[0], drop_value[1]) if isinstance(drop_value, List) else str(drop_value),
            criterion,
            keep.sum(),
        )
        logger.debug(
            "Dropped pathways:\n%s",
            "\n".join([m + "|" + s for m, s in value_matrix.loc[drop].index]),
        )

    filtered_value_matrix = value_matrix.loc[keep].transpose()
    return filtered_value_matrix


def rate(value_matrix: pd.DataFrame, criteria: List[Criterion]) -> pd.DataFrame:
    """Rates the values obtained per criterion based on the rating logic defined in their respective modules

    Parameters
    ----------
    value_matrix : pd.DataFrame
        DataFrame holding the values of the evaluated criteria with index level 'variable' and column levels 'model' and 'scenario'
    criteria : List[Criterion]
        List of Criterion objects

    Returns
    -------
    pd.DataFrame
        DataFrame holding the rated criteria with index level 'variable' and column levels 'model' and 'scenario'
    """

    ratings = []
    for criterion in criteria:
        logger.info(f"Determining values for: {criterion.criterion_name}")

        row = value_matrix.loc[[criterion.criterion_name]].stack().stack()
        ratings.append(criterion.rate(row))

    rating_matrix = pd.concat(ratings).unstack(["model", "scenario"]).sort_index(axis=1)

    # Order best on highest rating
    rating_matrix = rating_matrix.loc[
        :, rating_matrix.sum().sort_values(ascending=False).index
    ]

    return rating_matrix


def filter_rating(
    rating_matrix: pd.DataFrame,
    rating_limits: List[Optional[float]] = [None, None],
    pathways_max: Optional[int] = None,
) -> pd.DataFrame:
    """Filters rating matrix based on either rating_limits and or the highest rated X pathways
    (X specified via pathways_max)

    Parameters
    ----------
    rating_matrix : pd.DataFrame
        DataFrame holding the rated criteria with index levels 'module' and 'variable'
        and column levels 'model' and 'scenario'
    rating_limits : List[Optional[float]], optional
        Minimum and maximum total rating of pathways being displayed, by default [None, None]
    pathways_max : Optional[int], optional
        Maximum number of pathways being displayed in the figure, by default None

    Returns
    -------
    pd.DataFrame
        Filtered rating_matrix
    """

    filtered_rating_matrix = rating_matrix.copy()
    filtered_rating_matrix = filtered_rating_matrix.loc[
        :, filtered_rating_matrix.sum().sort_values(ascending=False).index
    ]
    logger.info(f"Number of pathways: {len(filtered_rating_matrix.columns)}")

    s = "Number of pathways after applying"
    if rating_limits[0] is not None:
        keep = filtered_rating_matrix.sum() >= rating_limits[0]
        filtered_rating_matrix = filtered_rating_matrix.loc[:, keep]
        logger.info(f"{s} lower rating limit: {len(filtered_rating_matrix.columns)}")
    if rating_limits[1] is not None:
        keep = filtered_rating_matrix.sum() <= rating_limits[1]
        filtered_rating_matrix = filtered_rating_matrix.loc[:, keep]
        logger.info(f"{s} upper rating limit: {len(filtered_rating_matrix.columns)}")
    if pathways_max is not None:
        filtered_rating_matrix = filtered_rating_matrix.iloc[:, :pathways_max]
        logger.info(f"{s} max_pathways limit: {len(filtered_rating_matrix.columns)}")

    return filtered_rating_matrix
