import pytest

from pathways_ensemble_analysis.evaluation import (
    filter_rating,
    filter_values,
    get_values,
    rate,
)

import os
import pandas as pd
import numpy as np


def test_get_values(data, criteria):
    data.to_csv("data.csv")

    for file in [data, "data.csv"]:
        values = get_values(file, criteria.values())

        assert values.index.name == "variable"
        assert values.columns.names == ["model", "scenario"]

        assert set(values.index) == set([c.criterion_name for c in criteria.values()])
        assert set(data.index) == set(values.columns)

        assert isinstance(values, pd.DataFrame)

        assert values.sum().sum().round() == 644.0

    os.remove("data.csv")


def test_filter_values(data, criteria):
    criterion_name = "Coal and gas share 2030"
    values = get_values(data, criteria.values())

    for mode, value, nb_pathways in [("<=", 0.11, 3), (">=", 0.11, 1)]:
        values_filtered = filter_values(
            values, {criterion_name: {"mode": mode, "value": value}}
        )

        assert len(values_filtered.columns) == nb_pathways
        assert values.index.name == "variable"
        assert set(values.index) == set([c.criterion_name for c in criteria.values()])
        assert isinstance(values_filtered, pd.DataFrame)

    for mode, value, nb_pathways, total in [("<=", 0.11, 3, 1), (">=", 0.11, 1, 0)]:
        values_filtered = filter_values(
            values.loc[[criterion_name]],
            {criterion_name: {"mode": mode, "value": value}},
        )

        assert len(values_filtered.columns) == nb_pathways
        assert values_filtered.sum().sum().round() == total

    # Test 'outside' mode
    values_filtered = filter_values(
        values, {criterion_name: {"mode": "outside", "value": [0.11,0.2]}}
    )
    assert len(values_filtered.columns) == 1

    # Test 'inside' mode
    values_filtered = filter_values(
        values, {criterion_name: {"mode": "inside", "value": [0.11,0.2]}}
    )
    assert len(values_filtered.columns) == 2

    # Test error raising
    with pytest.raises(ValueError):
        filter_values(values, {criterion_name: {"mode": "wrong_mode", "value": 0}})


def test_rate(data, criteria):
    values = get_values(data, criteria.values())
    values_rated = rate(values, criteria.values())

    assert values_rated.index.name == "variable"
    assert values_rated.columns.names == ["model", "scenario"]

    assert set(values_rated.index) == set([c.criterion_name for c in criteria.values()])
    assert set(data.index) == set(values_rated.columns)

    assert isinstance(values_rated, pd.DataFrame)

    assert values_rated.loc["Coal and gas share 2030"].sum().round(3) == 3.275


def test_filter(data, criteria):
    criteria_sel = {"coal_gas_share": criteria["coal_gas_share"]}
    value_matrix = get_values(data, criteria_sel.values())
    rating_matrix = rate(value_matrix, criteria_sel.values())

    filtered_rating_matrix = filter_rating(rating_matrix, [None, 0.8])
    assert len(filtered_rating_matrix.columns) == 2

    filtered_rating_matrix = filter_rating(rating_matrix, [0.9, None])
    assert len(filtered_rating_matrix.columns) == 1

    filtered_rating_matrix = filter_rating(rating_matrix, [0.75, 0.85])
    assert len(filtered_rating_matrix.columns) == 1

    filtered_rating_matrix = filter_rating(rating_matrix, pathways_max=2)
    assert len(filtered_rating_matrix.columns) == 2

    filtered_rating_matrix = filter_rating(rating_matrix, [0.75, 0.9], pathways_max=2)
    assert len(filtered_rating_matrix.columns) == 2

    value_matrix = get_values(data, criteria.values())
    rating_matrix = rate(value_matrix, criteria.values())
    filtered_rating_matrix = filter_rating(rating_matrix, [0.75, 0.9], pathways_max=2)

    assert filtered_rating_matrix.index.name == "variable"
    assert filtered_rating_matrix.columns.names == ["model", "scenario"]

    assert set(filtered_rating_matrix.index) == set(
        [c.criterion_name for c in criteria.values()]
    )

    assert isinstance(filtered_rating_matrix, pd.DataFrame)
