import pytest

import pathways_ensemble_analysis
from pathways_ensemble_analysis.utils import select_vars
from pathways_ensemble_analysis.plot import heatmap, compare_ensembles, polar_chart
from pathways_ensemble_analysis.assessment import add_temperature_categories

from pathways_ensemble_analysis.evaluation import (
    get_values,
    filter_values,
    rate,
)


import pandas as pd
import matplotlib.pyplot as plt


def test_version():
    assert pathways_ensemble_analysis.__version__ is not None


def test_select_vars(data):
    with pytest.raises(ValueError):
        select_vars(
            data,
            variables="Variable|Available|Not",
            region="World",
            year=2050,
            region_aggregation_weight=None,
        )


def test_compare_ensembles_plot(data, criteria):

    criterion = "Coal and gas share 2030"
    values = get_values(data, criteria.values())
    values_filtered = filter_values(values, {criterion: {"mode": "<=", "value": 0.11}})

    _ = compare_ensembles(
        {"unfiltered": values, "filtered": values_filtered}, criterion
    )

    ax = plt.gca()
    _ = compare_ensembles(
        {"unfiltered": values, "filtered": values_filtered}, criterion, ax=ax, legend=False,
    )


def test_heatmap_plot(data, criteria):

    values = get_values(data, criteria.values())
    rated_values = rate(values, criteria.values())

    _ = heatmap(rated_values)
    _ = heatmap(rated_values, figsize=(6, 4))
    _ = heatmap(
        rated_values,
        gridspec_kw={"height_ratios": [9, 1], "width_ratios": [4, 1]},
    )

    _ = heatmap(rated_values.iloc[:-1], rated_values.iloc[-1:])
    _ = heatmap(rated_values.iloc[:-1], rated_values.iloc[-1:], figsize=(6, 4))
    _ = heatmap(
        rated_values.iloc[:-1],
        rated_values.iloc[-1:],
        gridspec_kw={"height_ratios": [8, 1, 1, 1], "width_ratios": [4, 1]},
    )


def test_polar_chart(data, criteria):
    values = get_values(data, criteria.values())
    rated_values = rate(values, criteria.values())

    _ = polar_chart(rated_values, [], [])


def test_add_temperature_categories(data_exceedance_probability):

    data_test = data_exceedance_probability.filter(scenario=["*1", "*2", "*3"])
    add_temperature_categories(data_test)

    s1 = data_test.meta.loc[
        [(f"model_{x}", f"scenario_{y}") for x in [1, 2] for y in [1, 2, 3]],
        "category",
    ]

    s2 = pd.Series(
        [
            "Below 1.5C",
            "1.5C low overshoot",
            "1.5C high overshoot",
            "Lower 2C",
            "Higher 2C",
            "Above 2C",
        ],
        index=pd.MultiIndex.from_tuples(
            [(f"model_{x}", f"scenario_{y}") for x in [1, 2] for y in [1, 2, 3]],
            names=["model", "scenario"],
        ),
    ).rename("category")

    pd.testing.assert_series_equal(s1, s2)

    add_temperature_categories(data_exceedance_probability)

    s3 = data_exceedance_probability.meta.loc[
        [(f"model_{x}", f"scenario_{y}") for x in [1, 2] for y in [1, 2, 3, 4, 5]],
        "category",
    ]

    s4 = pd.Series(
        [
            "Below 1.5C",
            "1.5C low overshoot",
            "1.5C high overshoot",
            "uncategorized",
            "no-climate-assesssment",
            "Lower 2C",
            "Higher 2C",
            "Above 2C",
            "uncategorized",
            "no-climate-assesssment",
        ],
        index=pd.MultiIndex.from_tuples(
            [(f"model_{x}", f"scenario_{y}") for x in [1, 2] for y in [1, 2, 3, 4, 5]],
            names=["model", "scenario"],
        ),
    ).rename("category")

    pd.testing.assert_series_equal(s3, s4)
