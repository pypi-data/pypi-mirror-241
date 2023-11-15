"""
    Dummy conftest.py for pathways_ensemble_analysis.

    If you don't know what this is for, just leave it empty.
    Read more about conftest.py under:
    - https://docs.pytest.org/en/stable/fixture.html
    - https://docs.pytest.org/en/stable/writing_plugins.html
"""

import pytest
import numpy as np
import pandas as pd
import pyam

from pathways_ensemble_analysis.criteria import base, library


@pytest.fixture
def data():
    region_model_scenario = [
        ("World", f"model_{x}", f"scenario_{y}") for x in [1, 2] for y in [1, 2]
    ]

    unit_variable = [
        ("TWh/yr", "Secondary Energy|Electricity"),
        ("TWh/yr", "Secondary Energy|Electricity|Coal"),
        ("TWh/yr", "Secondary Energy|Electricity|Gas"),
        ("TWh/yr", "Secondary Energy|Electricity|Non-Biomass Renewables"),
        ("Gt CO2/yr", "Emissions|Kyoto Gases"),
        ("Gt CO2/yr", "Carbon Sequestration|CCS|Fossil"),
        ("Gt CO2/yr", "Carbon Sequestration|CCS|Biomass"),
        ("Gt CO2/yr", "Emissions|CO2|AFOLU"),
        ("Gt CO2/yr", "Carbon Sequestration|Land Use"),
        ("EJ/yr", "Primary Energy|Biomass"),
        ("", "AR6 climate diagnostics|Exceedance Probability 1.5C|MAGICCv7.5.3"),
        ("", "Temperature|Global temperature MAGICC 50th percentile"),
    ]

    names = ["region", "model", "scenario", "unit", "variable"]
    index = [rms + uv for rms in region_model_scenario for uv in unit_variable]
    columns = range(2010, 2105, 10)

    # fmt: off
    values = [
        [80, 110, 130, 190, 240, 270, 310, 350, 390, 420],
        [30, 20, 8, 6, 5, 0, 0, 0, 0, 0],
        [10, 7, 5, 1, 0, 0, 0, 0, 0, 0],
        [20, 30, 90, 160, 200, 230, 270, 310, 340, 380],
        [49, 57, 32, 17, 6.6, 2.4, -0.0, -1.5, -2.5, -3.1],
        [0.0, 0.0, 0.6, 1.8, 1.6, 1.3, 1.2, 0.9, 0.6, 0.5],
        [0.0, 0.0, 0.6, 0.5, 3.0, 6.0, 7.5, 9.0, 12, 12],
        [4.2, 4.3, 0.8, 0.7, 0.6, -0.1, -0.3, -0.4, -0.4, -0.3],
        [-4.2, -4.3, -0.8, -0.7, -0.6, 0.1, 0.3, 0.4, 0.4, 0.3],
        [50, 60, 80, 140, 220, 270, 290, 290, 300, 300],
        [0.0, 0.02, 0.47, 0.61, 0.58, 0.49, 0.4, 0.31, 0.23, 0.18],
        [1.2, 1.3, 1.4, 1.5, 1.6, 1.5, 1.4, 1.3, 1.2, 1.1],
        
        [80, 100, 110, 120, 160, 190, 220, 240, 250, 260],
        [30, 15, 17, 10, 0, 0, 0, 0, 0, 0],
        [10, 7, 5, 0, 0, 0, 0, 0, 0, 0],
        [10, 20, 30, 70, 80, 100, 110, 130, 150, 180],
        [49, 55, 47, 17, 4.5, -1.9, -1.9, -1.5, -1.3, -1.8],
        [0.0, 0.0, 0.7, 4.3, 9.2, 13, 16, 16, 17, 15],
        [0.0, 0.0, 0.2, 5.0, 9.3, 11, 11, 10, 10, 10],
        [5.6, 3.5, 0.4, -2.5, -2.2, -3.7, -2.5, -1.9, -1.3, -1.0],
        [-5.6, -3.5, -0.4, 2.5, 2.2, 3.7, 2.5, 1.9, 1.3, 1.0],
        [50, 60, 80, 150, 190, 200, 210, 200, 200, 200],
        [0.0, 0.02, 0.46, 0.64, 0.44, 0.31, 0.25, 0.21, 0.2, 0.18],
        [1.2, 1.3, 1.4, 1.5, 1.75, 1.5, 1.4, 1.3, 1.2, 1.1],
        
        [80, 90, 120, 180, 240, 310, 370, 410, 440, 470],
        [30, 15, 10, 10, 1, 0, 0, 0, 0, 0],
        [10, 7, 5, 1, 0, 0, 0, 0, 0, 0],
        [20, 20, 60, 100, 130, 180, 220, 270, 320, 390],
        [49, 52, 22, 12, 4.6, -4.4, -6.8, -8.9, -9.9, -10.3],
        [0.0, 0.0, 0.1, 0.1, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.2, 1.0, 4.5, 6.7, 7, 8, 9, 9],
        [6.9, 6.1, -0.1, -1.4, -2.0, -3.5, -3.8, -4.4, -4.4, -4.2],
        [-6.9, -6.1, 0.1, 1.4, 2.0, 3.5, 3.8, 4.4, 4.4, 4.2],
        [50, 60, 100, 110, 150, 180, 200, 210, 220, 230],
        [0.0, 0.02, 0.5, 0.6, 0.56, 0.48, 0.36, 0.25, 0.18, 0.14],
        [1.2, 1.3, 1.4, 1.45, 1.45, 1.45, 1.4, 1.3, 1.2, 1.1],
        
        [80, 100, 140, 200, 250, 280, 300, 300, 300, 290],
        [30, 30, 30, 15, 10, 1, 0, 0, 0, 0],
        [20, 20, 12, 0, 0, 0, 0, 0, 0, 0],
        [10, 20, 80, 140, 190, 230, 240, 240, 240, 240],
        [49, 52, 25, 12, 4.7, 0.3, -1.4, -2.0, -2.1, -2.3],
        [0.0, 0.0, 1.5, 3.6, 4.9, 5.4, 4.9, 2.3, 2.2, 2.0],
        [0.0, 0.0, 0.0, 0.5, 1.4, 2.3, 2.9, 3.0, 3.2, 3.2],
        [4.6, 3.6, -0.1, -3.0, -3.8, -4.1, -4.3, -4.1, -3.9, -3.6],
        [-4.6, -3.6, 0.1, 3.0, 3.8, 4.1, 4.3, 4.1, 3.9, 3.6],
        [40, 40, 40, 60, 70, 80, 90, 90, 90, 90],
        [0.0, 0.02, 0.44, 0.51, 0.45, 0.32, 0.26, 0.2, 0.17, 0.16],
        [1.2, 1.3, 1.4, 1.5, 1.65, 1.5, 1.4, 1.3, 1.2, 1.1],
    ]
    # fmt: on

    data = pyam.IamDataFrame(
        pd.DataFrame(
            values,
            index=pd.MultiIndex.from_tuples(index, names=names),
            columns=pd.Index(columns, name="year"),
        )
    )
    return data


@pytest.fixture
def data_landuse():
    region_model_scenario = [
        ("World", f"model_{x}", f"scenario_{y}") for x in [1, 2] for y in [1, 2, 3]
    ]

    unit_variable = [
        ("Gt CO2/yr", "Emissions|CO2|AFOLU"),
        ("Gt CO2/yr", "Carbon Sequestration|Land Use"),
    ]

    names = ["region", "model", "scenario", "unit", "variable"]
    index = [rms + uv for rms in region_model_scenario for uv in unit_variable]
    columns = range(2040, 2060 + 1, 10)

    values = [
        [0, 0, 0],
        [0, 0, 0],
        [1, 1, 1],
        [-1, -1, -1],
        [-1.1, -1.1, -1.1],
        [1.1, 1.1, 1.1],
        [-3, -3, -3],
        [3, 3, 3],
        [-4.2, -4.2, -4.2],
        [4.2, 4.2, 4.2],
        [-8, -8, -8],
        [8, 8, 8],
    ]

    data_landuse = pyam.IamDataFrame(
        pd.DataFrame(
            values,
            index=pd.MultiIndex.from_tuples(index, names=names),
            columns=pd.Index(columns, name="year"),
        )
    )

    return data_landuse


@pytest.fixture
def criteria():
    criteria = {}

    criteria["ghg_red"] = base.ChangeOverTimeCriterion(
        criterion_name="GHG emissions in 2070 relative to 2010",
        region="World",
        year=2070,
        variable="Emissions|Kyoto Gases",
        reference_year=2010,
        rating_function=lambda x: -x,
    )

    criteria["coal_gas_share"] = base.ShareCriterion(
        criterion_name="Coal and gas share 2030",
        region="World",
        year=2030,
        variable_component=[
            "Secondary Energy|Electricity|Coal",
            "Secondary Energy|Electricity|Gas",
        ],
        variable_total="Secondary Energy|Electricity",
        rating_function=lambda x: 1 - x,
    )

    criteria["non_bio_res_share"] = base.ShareCriterion(
        criterion_name="Non-biomass RES share 2050",
        region="World",
        year=2050,
        variable_component="Secondary Energy|Electricity|Non-Biomass Renewables",
        variable_total="Secondary Energy|Electricity",
        rating_function=lambda x: x,
    )

    criteria["mean_bio_pe"] = library.Mean_Biomass_PrimaryEnergy()
    criteria["seq_landuse"] = library.Mean_CarbonSequestration_LandUse()
    criteria["seq_bio"] = library.Mean_CarbonSequestration_Biomass()
    criteria["seq_fossil"] = library.Mean_CarbonSequestration_Fossil()
    criteria["exceed"] = library.Max_ExceedanceProbability()
    criteria["max_1o5C_overshoot"] = library.Max_1o5C_Overshoot()

    return criteria


@pytest.fixture
def criteria_single():
    criteria_single = {}

    criteria_single[
        "seq_landuse_wrong_unit"
    ] = library.Mean_CarbonSequestration_LandUse(unit="Mt CO2/yr")

    criteria_single[
        "seq_landuse_rating_function"
    ] = library.Mean_CarbonSequestration_LandUse(rating_function_overwrite=lambda x: x)

    criteria_single["seq_landuse"] = library.Mean_CarbonSequestration_LandUse(
        criterion_name="Average CO2 emissions via A/R",
        variable="Carbon Sequestration|Land Use",
    )

    criteria_single["exceed"] = base.SingleVariableCriterion(
        criterion_name="Exceedance Probability",
        region="World",
        year=2050,
        variable="AR6 climate diagnostics|Exceedance Probability 1.5C|MAGICCv7.5.3",
        unit="",
        rating_function=lambda x: 1 - x,
    )

    return criteria_single


@pytest.fixture
def data_exceedance_probability():
    region_model_scenario = [
        ("World", f"model_{x}", f"scenario_{y}") for x in [1, 2] for y in [1, 2, 3, 4]
    ]

    unit_variable = [
        ("", "AR6 climate diagnostics|Exceedance Probability 1.5C|MAGICCv7.5.3"),
        ("", "AR6 climate diagnostics|Exceedance Probability 2.0C|MAGICCv7.5.3"),
    ]

    names = ["region", "model", "scenario", "unit", "variable"]
    index = [rms + uv for rms in region_model_scenario for uv in unit_variable]
    columns = [2050, 2100]

    values = [
        [0.4, 0.3],
        [0.05, 0.03],
        [0.6, 0.5],
        [0.1, 0.1],
        [0.7, 0.5],
        [0.2, 0.1],
        [0.99, 0.99],
        [0.6, 1.6],
        [0.9, 0.9],
        [0.3, 0.3],
        [0.95, 0.95],
        [0.4, 0.4],
        [0.99, 0.99],
        [0.6, 0.6],
        [0.99, 0.99],
        [0.6, 1.6],
    ]

    data_exceed = pyam.IamDataFrame(
        pd.DataFrame(
            values,
            index=pd.MultiIndex.from_tuples(index, names=names),
            columns=pd.Index(columns, name="year"),
        )
    )

    data_add = pyam.IamDataFrame(
        pd.DataFrame(
            [0, 0],
            index=pd.MultiIndex.from_tuples(
                [
                    ("World", "model_1", "scenario_5", "", "v"),
                    ("World", "model_2", "scenario_5", "", "v"),
                ],
                names=names,
            ),
            columns=[2030],
        )
    )

    data_exceed.append(data_add, inplace=True)

    return data_exceed


@pytest.fixture
def data_regions():
    region_model_scenario = [
        (f"region_{x}", "model", f"scenario_{y}") for x in [1, 2] for y in [1, 2]
    ]

    unit_variable = [("Gt CO2/yr", "Emissions|Kyoto Gases")]

    names = ["region", "model", "scenario", "unit", "variable"]
    index = [rms + uv for rms in region_model_scenario for uv in unit_variable]
    columns = range(2010, 2105, 10)

    # fmt: off
    values = [
        [30, 36, 18, 15, 10, 5, 0.0, -1.5, -2.5, -3.1],
        [30, 36, 18, 15, 10, 5, 0.0, -1.5, -2.5, -3.1],
        [19, 22, 5.5, 5.5, 0, -1.9, -1.9, -1.5, -1.3, -1.8],
        [19, 22, 16.5, 11, 5.5, 0, -1.9, -1.5, -1.3, -1.8],]
    # fmt: on

    data_regions = pyam.IamDataFrame(
        pd.DataFrame(
            values,
            index=pd.MultiIndex.from_tuples(index, names=names),
            columns=pd.Index(columns, name="year"),
        )
    )
    return data_regions


@pytest.fixture
def criteria_regions():
    criteria_regions = {}

    kwargs_criterion = dict(
        criterion_name="GHG emissions in 2030 relative to 2020",
        year=2030,
        variable="Emissions|Kyoto Gases",
        reference_year=2020,
        rating_function=lambda x: -x,
    )

    criteria_regions["relative_decarbonisation"] = base.CompareRegionsCriterion(
        criterion_name="relative_decarbonisation_over_2020",
        criterion_class=base.ChangeOverTimeCriterion,
        kwargs_criterion=kwargs_criterion,
        region_1="region_1",
        region_2="region_2",
        method="subtract",
        rating_function=lambda x: x,
    )

    return criteria_regions
