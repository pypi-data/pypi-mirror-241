from typing import Union, Iterable, Dict, Optional, List
import pandas as pd
import pyam
import logging

logger = logging.getLogger(__name__)


def format_value_series(values: pd.Series) -> pd.Series:
    """Formats a pd.Series with index levels 'model', 'scenario', 'variable', 'region', 'unit'
    by dropping the 'region' and 'unit' level

    Parameters
    ----------
    values : Union[pd.Series, pd.DataFrame]
        Values in form of a Series or DataFrame with index levels 'model', 'scenario',
        'variable', 'region', 'unit'

    Returns
    -------
    pd.Series
        A Series with index levels 'model', 'scenario', 'variable', 'criterion_name'
    """

    values = values.droplevel(["region", "unit"]).rename(None)

    return values


def require_variables(
    df: pyam.IamDataFrame, variables: Iterable[str], **kwargs
) -> None:
    """Warn about missing required variables

    Parameters
    ----------
    df : pyam.IamDataFrame
    variables : Iterable[str]
    exclude : bool, optional
        Exclude pathways with missing variables
        (mark them as exclude=True in meta)
    """
    for v in variables:
        df.require_variable(variable=v, **kwargs)


def select_vars(
    df: pyam.IamDataFrame,
    variables: Union[Dict[str, str], Iterable[str]],
    region: Union[str, Dict[str, List[str]]],
    year: Union[int, List[int]],
    region_aggregation_weight: Optional[str],
    unit: Optional[str] = None,
) -> pyam.IamDataFrame:
    """Convenience method to select, rename variables

    Gives an indication of how many pathways have the variables.

    Parameters
    ----------
    df : pyam.IamDataFrame
        IAM data
    variables : Union[Dict[str, str], Iterable[str]]
        Variables for filtering
        (in the case of a dictionary renames)
    region : Union[str, Dict[str, List[str]]]
        Region filtered for, if List[str] the subregions are aggregated to one macro region
    year : Union[int, List[int]]
        Years filtered for
    unit : Optional[str], optional
        Unit to convert variables to, by default None


    Returns
    -------
    pyam.IamDataFrame
        Filtered IAM data
    """
    require_variables(df, list(variables), year=year)

    if isinstance(region, dict):
        sel = df.aggregate_region(
            list(variables),
            region["macro_region"],
            region["subregions"],
            weight=region_aggregation_weight,
        ).filter(year=year)
    else:
        sel = df.filter(
            variable=list(variables),
            year=year,
            region=region,
        )

    if isinstance(variables, dict):
        rename_dict = {}
        for key, value in variables.items():
            if "*" in key:
                variable_avail = df.filter(variable=key).variable
                assert len(variable_avail) == 1
                rename_dict[variable_avail[0]] = value
            else:
                rename_dict[key] = value

        sel.rename(variable=rename_dict, inplace=True)

    if unit is not None:
        if unit == "uniform":
            unit = sel.unit[0]

        for from_unit in sel.unit:
            sel.convert_unit(from_unit, unit, inplace=True)

    if sel.empty:
        raise ValueError(
            f"The variable(s) {variables} is/are not available in the provided pyam.IamDataFrame."
        )

    return sel
