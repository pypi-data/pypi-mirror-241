import pyam
import logging

logger = logging.getLogger(__name__)


def add_temperature_categories(df, meta_column="category"):
    """Add temperature categories according to SR1.5 definitions

    Parameters
    ----------
    df : IamDataFrame

    meta_column : str, optional
        Column in meta where to save temperature categories

    Note
    ----
    Adds column in-place

    Adapted from https://github.com/iiasa/ipcc_sr15_scenario_analysis/blob/master/assessment/sr15_2.0_categories_indicators.ipynb
    """

    def exceed_prob(t):
        return f"*climate diagnostic*Exceedance Probability*{t}*MAGICC*"

    for t in (1.5, 2.0):
        df.require_variable(variable=exceed_prob(t))

    exc15 = (
        df.filter(variable=exceed_prob(1.5))
        .timeseries()
        .droplevel(["region", "variable", "unit"])
    )
    exc15_max = exc15.max(axis=1)
    eoc15 = exc15[2100] <= 0.5
    exc20_max = (
        df.filter(variable=exceed_prob(2.0))
        .timeseries()
        .droplevel(["region", "variable", "unit"])
        .max(axis=1)
    )

    df.set_meta("uncategorized", meta_column)
    df.set_meta("no-climate-assesssment", meta_column, df.index.difference(exc15.index))
    df.set_meta("Below 1.5C", meta_column, exc15.index[exc15_max <= 0.5])
    df.set_meta(
        "1.5C low overshoot",
        meta_column,
        exc15.index[exc15_max.between(0.5, 0.67) & eoc15],
    )
    df.set_meta(
        "1.5C high overshoot",
        meta_column,
        exc15.index[(exc15_max > 0.67) & eoc15],
    )
    df.set_meta(
        "Lower 2C",
        meta_column,
        exc20_max.index[(exc20_max <= 0.34) & ~eoc15],
    )
    df.set_meta(
        "Higher 2C",
        meta_column,
        exc20_max.index[exc20_max.between(0.34, 0.5, inclusive="right") & ~eoc15],
    )
    df.set_meta(
        "Above 2C",
        meta_column,
        exc20_max.index[exc20_max.between(0.5, 1.0, inclusive="right") & ~eoc15],
    )

    pyam.run_control()["color"][meta_column] = {
        "Below 1.5C": "xkcd:baby blue",
        "1.5C low overshoot": "xkcd:bluish",
        "1.5C high overshoot": "xkcd:darkish blue",
        "Lower 2C": "xkcd:orange",
        "Higher 2C": "xkcd:red",
        "Above 2C": "darkgrey",
    }

    logger.info(
        "Scenarios are categorized: %s", df.meta[meta_column].value_counts().to_dict()
    )

    if any(df[meta_column] == "uncategorized"):
        logger.warning(
            "There are scenarios that are no yet categorized: %s",
            ", ".join(
                [
                    ix[0] + " " + ix[1]
                    for ix in df.meta.loc[df[meta_column] == "uncategorized"].index
                ]
            ),
        )

    if any(df[meta_column] == "no-climate-assesssment"):
        logger.warning(
            "There are scenarios without a climate assessment (missing exceedance probability variable): %s",
            ", ".join(
                [
                    ix[0] + " " + ix[1]
                    for ix in df.meta.loc[
                        df[meta_column] == "no-climate-assesssment"
                    ].index
                ]
            ),
        )
