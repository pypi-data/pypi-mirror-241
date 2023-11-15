import pytest

import pathways_ensemble_analysis

import pandas as pd
import numpy as np


def get_index(variable, models=[1, 2], scenarios=[1, 2]):
    return pd.MultiIndex.from_tuples(
        [
            (
                f"model_{x}",
                f"scenario_{y}",
                variable,
            )
            for x in models
            for y in scenarios
        ],
        names=["model", "scenario", "variable"],
    )


def test_change_over_time_criterion(criteria, data):
    s1 = criteria["ghg_red"].get_values(data)
    s2 = pd.Series(
        [-1.0, -1.03878, -1.13878, -1.02857],
        get_index("GHG emissions in 2070 relative to 2010"),
    )
    pd.testing.assert_series_equal(s1, s2)

    s3 = criteria["ghg_red"].rate(s1)
    pd.testing.assert_series_equal(s3, -s2)


def test_share_criterion(criteria, data):
    s1 = criteria["non_bio_res_share"].get_values(data)
    s2 = pd.Series(
        [0.83333, 0.5, 0.54167, 0.76], get_index("Non-biomass RES share 2050")
    )
    pd.testing.assert_series_equal(s1, s2)

    s3 = criteria["non_bio_res_share"].rate(s1)
    pd.testing.assert_series_equal(s3, s2)

    s4 = criteria["coal_gas_share"].get_values(data)
    s5 = pd.Series([0.1, 0.2, 0.125, 0.3], get_index("Coal and gas share 2030"))
    pd.testing.assert_series_equal(s4, s5)

    s6 = criteria["coal_gas_share"].rate(s4)
    pd.testing.assert_series_equal(s6, 1 - s5)


def test_mean_biomass_primary_energy(criteria, data):

    for criterion in [criteria["mean_bio_pe"]]:

        s1 = criterion.get_values(data)
        s2 = pd.Series(
            [212.142857, 182.142857, 147.380952, 70.0],
            get_index("Average Biomass Demand"),
        )
        np.testing.assert_allclose(s1, s2, rtol=1e-05, atol=1e-08, equal_nan=False)

        s3 = criterion.rate(s1)
        s4 = pd.Series(
            [0.0, 0.0, 0.0, 0.3], get_index("Average Biomass Demand")
        )
        np.testing.assert_allclose(s3, s4, rtol=1e-05, atol=1e-08, equal_nan=False)


def test_mean_carbon_sequestration_landuse(
    criteria, criteria_single, data, data_landuse

):
    # Test "Emissions|CO2|AFOLU" version
    s1 = criteria["seq_landuse"].get_values(data)
    s2 = pd.Series(
        [0.4428571, -2.6714285, -2.2357142, -3.669047],
        get_index("Average CO2 emissions via A/R"),
    )
    np.testing.assert_allclose(s1, s2, rtol=1e-05, atol=1e-08, equal_nan=False)

    s3 = criteria["seq_landuse"].rate(s1)
    s4 = pd.Series(
        [0.0, 1.0, 1.0, 0.953969], get_index("Average CO2 emissions via A/R")
    )
    np.testing.assert_allclose(s3, s4, rtol=1e-05, atol=1e-08, equal_nan=False)

    # Test "Carbon Sequestration|Land Use" version
    s1 = criteria_single["seq_landuse"].get_values(data)
    np.testing.assert_allclose(s1, -s2, rtol=1e-05, atol=1e-08, equal_nan=False)

    s3 = criteria_single["seq_landuse"].rate(s1)
    np.testing.assert_allclose(s3, s4, rtol=1e-05, atol=1e-08, equal_nan=False)

    # Test wrong unit
    s1 = criteria_single["seq_landuse_wrong_unit"].get_values(data)
    s2 = pd.Series(
        [0.4428571, -2.6714285, -2.2357142, -3.669047],
        get_index("Average CO2 emissions via A/R"),
    )
    np.testing.assert_allclose(s1, s2, rtol=1e-05, atol=1e-08, equal_nan=False)

    # Test user-defined rating function

    s1 = criteria_single["seq_landuse_rating_function"].get_values(data)
    s3 = criteria_single["seq_landuse_rating_function"].rate(s1)
    pd.testing.assert_series_equal(s3, s2)

    # Test other data ranges

    s1 = criteria["seq_landuse"].get_values(data_landuse)
    s2 = criteria["seq_landuse"].rate(s1)
    s3 = pd.Series(
        [0, 0, 0.5, 1, 0.6, 0],
        get_index("Average CO2 emissions via A/R", scenarios=[1, 2, 3]),
    )

    pd.testing.assert_series_equal(s2, s3)

    s1 = criteria_single["seq_landuse"].get_values(data_landuse)
    s2 = criteria_single["seq_landuse"].rate(s1)

    pd.testing.assert_series_equal(s2, s3)



def test_mean_carbonsequestration_biomass(criteria, data):
    s1 = criteria["seq_bio"].get_values(data)
    s2 = pd.Series(
        [3.130952, 8.619048, 4.159524, 1.4],
        get_index("Average amount of sequestered carbon via BECCS"),
    )
    np.testing.assert_allclose(s1, s2, rtol=1e-05, atol=1e-08, equal_nan=False)

    s3 = criteria["seq_bio"].rate(s1)
    s4 = pd.Series(
        [0.0, 0.0, 0.0, 0.53333333],
        get_index("Average amount of sequestered carbon via BECCS"),
    )
    np.testing.assert_allclose(s3, s4, rtol=1e-05, atol=1e-08, equal_nan=False)


def test_mean_carbonsequestration_fossil(criteria, data):
    s1 = criteria["seq_fossil"].get_values(data)
    s2 = pd.Series(
        [1.57381, 8.911905, 0.073810, 4.690476],
        get_index("Average amount of sequestred fossil carbon"),
    )
    np.testing.assert_allclose(s1, s2, rtol=1e-05, atol=1e-08, equal_nan=False)

    s3 = criteria["seq_fossil"].rate(s1)
    s4 = pd.Series(
        [0.585839473, 0.0, 0.980576315, 0.0],
        get_index("Average amount of sequestred fossil carbon"),
    )
    np.testing.assert_allclose(s3, s4, rtol=1e-05, atol=1e-08, equal_nan=False)


def test_max_exceedanceprobability(criteria, data):
    s1 = criteria["exceed"].get_values(data)
    s2 = pd.Series([0.61, 0.64, 0.6, 0.51], get_index("1.5°C Exceedance probability"))
    pd.testing.assert_series_equal(s1, s2)

    s3 = criteria["exceed"].rate(s1)
    s4 = pd.Series([0.78, 0.72, 0.8, 0.98], get_index("1.5°C Exceedance probability"))
    pd.testing.assert_series_equal(s3, s4)


def test_max_1o5c_overshoot(criteria, data):
    s1 = criteria["max_1o5C_overshoot"].get_values(data)
    s2 = pd.Series([1.6, 1.75, 1.45, 1.65], get_index("Maximum 1o5p overshoot"))
    pd.testing.assert_series_equal(s1, s2)

    s3 = criteria["max_1o5C_overshoot"].rate(s1)
    s4 = pd.Series([0.5, -0.25, 1.25, 0.25], get_index("Maximum 1o5p overshoot"))
    pd.testing.assert_series_equal(s3, s4)


def test_single_variable_criterion(criteria_single, data):
    s1 = criteria_single["exceed"].get_values(data)
    s2 = pd.Series([0.58, 0.44, 0.56, 0.45], get_index("Exceedance Probability"))
    pd.testing.assert_series_equal(s1, s2)

    s3 = criteria_single["exceed"].rate(s1)
    s4 = pd.Series([0.42, 0.56, 0.44, 0.55], get_index("Exceedance Probability"))
    pd.testing.assert_series_equal(s3, s4)


def test_regional_comparison(criteria_regions, data_regions):
    s1 = criteria_regions["relative_decarbonisation"].get_values(data_regions)
    s2 = pd.Series(
        [0.25, -0.25],
        index=pd.MultiIndex.from_arrays(
            [
                ["model", "model"],
                ["scenario_1", "scenario_2"],
                ["relative_decarbonisation_over_2020"] * 2,
            ],
            names=["model", "scenario", "variable"],
        ),
    )

    np.testing.assert_allclose(s1, s2, rtol=1e-5, atol=1e-8, equal_nan=False)

    s3 = criteria_regions["relative_decarbonisation"].rate(s1)
    s4 = pd.Series(
        [0.25, -0.25],
        index=pd.MultiIndex.from_arrays(
            [
                ["model", "model"],
                ["scenario_1", "scenario_2"],
                ["relative_decarbonisation_over_2020"] * 2,
            ],
            names=["model", "scenario", "variable"],
        ),
    )
    np.testing.assert_allclose(s3, s4, rtol=1e-05, atol=1e-08, equal_nan=False)

    # Test divide method
    criterion = criteria_regions["relative_decarbonisation"]
    criterion.method = "divide"
    s5 = criterion.get_values(data_regions)

    s6 = pd.Series(
        [2/3, 2],
        index=pd.MultiIndex.from_arrays(
            [
                ["model", "model"],
                ["scenario_1", "scenario_2"],
                ["relative_decarbonisation_over_2020"] * 2,
            ],
            names=["model", "scenario", "variable"],
        ),
    )    
    print(s5)
    np.testing.assert_allclose(s5, s6, rtol=1e-5, atol=1e-8, equal_nan=False)


    # Test wrong method
    with pytest.raises(ValueError):
        criterion = criteria_regions["relative_decarbonisation"]
        criterion.method = "wrong method"
        criterion.get_values(data_regions)    
