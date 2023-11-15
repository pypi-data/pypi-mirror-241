from asyncio.log import logger
from typing import Callable, Optional, List, Union, Dict
import numpy as np

from .base import AggregateCriterion


class Mean_CarbonSequestration_Fossil(AggregateCriterion):
    """Evaluates the average amount of fossil CCS within a given time period and for a given region

    Parameters
    ----------
    criterion_name : str, optional
        Name of the criterion
    region : Union[str, Dict[str, List[str]]]
        Region for which the criterion should be evaluated, if a dict is passed, the regions (items) are aggregated to the macro region (key)
    years : Optional[List[int]]
        Years for which the criterion should be evaluated, if None: list(range(2040, 2060 + 1, 10))
    variable : str, optional
        Name of the variable in the file which quantifies the amount of fossil CCS
    aggregation_function : Callable, optional
        Aggregation function, default np.mean
    unit: str, optional
        Unit in which the evaluated variable should be returned
    rating_function : Callable, optional
        Rating function, levels come from https://www.ipcc.ch/report/ar6/wg3/downloads/report/IPCC_AR6_WGIII_Annex-III.pdf
        p.59 which are again based on Budinis et al. (2018) (https://doi.org/10.1016/j.esr.2018.08.003)
        This suggests that fossil CCS > 3.8 GtCO2/yr poses medium feasibility challenges,
        and fossil CCS > 8.8 GtCO2/yr poses high feasibility challenges.

        Two initial rating functions then emerge:
        STRICT (default): lambda x: np.clip(1 - x / 3.8, 0, 1):
            Rates pathways linearly from 1 to 0, with pathways displaying fossil CCS > medium feasibility threshold ranked as zero.

        RELAXED: lambda x: np.clip(1 - ((x - 3.8) / (8.8 - 3.8)), 0, 1)): 
            Rates pathways with < medium feasibility challenges as 1, with the rating then declining linearly to zero over 
            the [medium feasibility challenges, high feasibility challenge] interval.
            Pathways displaying high feasibility challenges are ranked as zero.

        Depending on which pathways you are attempting to distinguish between, different rating functions may be necessary.

    kwargs : dict
        Other kwargs passed to the AggregateCriterion class
    """

    def __init__(
        self,
        criterion_name: str = "Average amount of sequestered fossil carbon",
        region: Union[str, Dict[str, List[str]]] = "World",
        years: Optional[List[int]] = None,
        variable: str = "Carbon Sequestration|CCS|Fossil",
        aggregation_function: Callable = np.mean,
        unit: str = "Gt CO2/yr",
        rating_function: Callable = lambda x: np.clip(
            1 - (x / 3.8), 0, 1
        ),
        **kwargs,
    ):
        if years is None:  # pragma: no cover
            years = list(range(2040, 2060 + 1, 10))

        super().__init__(
            criterion_name=criterion_name,
            region=region,
            years=years,
            variable=variable,
            aggregation_function=aggregation_function,
            unit=unit,
            rating_function=rating_function,
            **kwargs,
        )


class Mean_CarbonSequestration_Biomass(AggregateCriterion):
    """Evaluates the average amount of sequestered carbon via BECCS within a given time period and for a given region

    Parameters
    ----------
    criterion_name : str, optional
        Name of the criterion
    region : Union[str, Dict[str, List[str]]]
        Region for which the criterion should be evaluated, if a dict is passed, the regions (items) are aggregated to the macro region (key)
    years : List[int], optional
        Years for which the criterion should be evaluated, if None [2040, 2050, 2060]
    variable : str, optional
        Name of the variable in the file which quantifies the amount of sequestered carbon via BECCS,
        by default "Carbon Sequestration|CCS|Biomass"
    aggregation_function : Callable, optional
        Aggregation function, default np.mean
    unit: str, optional
        Unit in which the evaluated variable should be returned
    rating_function : Callable, optional
        Rating function, levels come from https://www.ipcc.ch/report/ar6/wg3/downloads/report/IPCC_AR6_WGIII_Annex-III.pdf

        This suggests that BECCS > 3 GtCO2/yr poses medium feasibility challenges,
        and BECCS > 7 GtCO2/yr poses high feasibility challenges.

        Two initial rating functions then emerge:
        STRICT (default): lambda x: np.clip(1 - x / 3, 0, 1). 
            Rates pathways linearly from 1 to 0, with pathways displaying BECCS > medium feasibility threshold ranked as zero.

        RELAXED: lambda x: np.clip(1 - ((x - 3) / (7 - 3)), 0, 1)): 
            Rates pathways with < medium feasibility challenges as 1, with the rating then declining linearly to zero over 
            the [medium feasibility challenges, high feasibility challenge] interval.
            Pathways displaying high feasibility challenges are ranked as zero.

        Depending on which pathways you are attempting to distinguish between, different rating functions may be necessary.

    kwargs : dict
        Other kwargs passed to the AggregateCriterion class
    """

    def __init__(
        self,
        criterion_name: str = "Average amount of sequestered carbon via BECCS",
        region: Union[str, Dict[str, List[str]]] = "World",
        years: Optional[List[int]] = None,
        variable: str = "Carbon Sequestration|CCS|Biomass",
        aggregation_function: Callable = np.mean,
        unit: str = "Gt CO2/yr",
        rating_function: Callable = lambda x: np.clip(1 - (x / 3), 0, 1),
        **kwargs,
    ):
        if years is None:  # pragma: no cover
            years = [2040, 2050, 2060]

        super().__init__(
            criterion_name=criterion_name,
            region=region,
            years=years,
            variable=variable,
            aggregation_function=aggregation_function,
            unit=unit,
            rating_function=rating_function,
            **kwargs,
        )


class Mean_CarbonSequestration_LandUse(AggregateCriterion):
    """Evaluates the average CO2 emissions via A/R within a given time period and for a given region

    Parameters
    ----------
    criterion_name : str, optional
        Name of the criterion
    region : Union[str, Dict[str, List[str]]], optional
        Region for which the criterion should be evaluated, if a dict is passed, the regions (items) are aggregated to the macro region (key)
    years : List[int], optional
        Years for which the criterion should be evaluated, if None [2040, 2050, 2060]
    variable : str, optional
        Name of the variable in the file, default Emissions|CO2|AFOLU (a proxy for often not available LULUCF emissions data)
    aggregation_function : Callable, optional
        Aggregation function, default np.mean
    unit: str, optional
        Unit in which the evaluated variable should be returned
    rating_function : Callable, optional
        If None, a rating function based on the following studies is used:
        - Fuss et al. (2018) (https://doi.org/10.1088/1748-9326/aabf9f) - 3.6 Gt
        - Grant et al. (2021) (https://doi.org/10.1016/j.joule.2021.09.004) - estimate on range (2.2-5.1 Gt)
        Values:
        - below -5.1 Gt and above 0 Gt are mapped to 0
        - between -3.6 and -2.2 Gt are mapped to 1
        - remaing are lineraly interpolated between 0 and 1

        -3.6 _____ -2.2    rating = 1
            /     \\
           /       \\
        __/         \\____  rating = 0
        -5.1         0
    kwargs : dict
        Other kwargs passed to the AggregateCriterion class          
    """

    def __init__(
        self,
        criterion_name: str = "Average CO2 emissions via A/R",
        region: Union[str, Dict[str, List[str]]] = "World",
        years: Optional[List[int]] = None,
        variable: str = "Emissions|CO2|AFOLU",
        aggregation_function: Callable = np.mean,
        unit: str = "Gt CO2/yr",
        rating_function_overwrite: Optional[Callable] = None,
        **kwargs,
    ):
        if years is None:  # pragma: no cover
            years = [2040, 2050, 2060]

        if rating_function_overwrite is None:
            if unit != "Gt CO2/yr":
                logger.info("Setting the unit kwarg to 'Gt CO2/yr'")
                unit = "Gt CO2/yr"

            # Alternative option for if raw sequestration data is used instead of Emissions|CO2|AFOLU
            if variable.startswith("Carbon Sequestration|Land Use"):

                def rating_function_land_use(x):
                    if x <= 0:
                        return 0
                    elif x <= 2.2:
                        return x / 2.2
                    elif x <= 3.6:
                        return 1
                    elif x <= 5.1:
                        return (5.1 - x) / (5.1 - 3.6)
                    else:
                        return 0

                rating_function = rating_function_land_use

            else:

                def rating_function_afolu(x):
                    if x >= 0:
                        return 0
                    elif x >= -2.2:
                        return -x / 2.2
                    elif x >= -3.6:
                        return 1
                    elif x >= -5.1:
                        return (x + 5.1) / (5.1 - 3.6)
                    else:
                        return 0

                rating_function = rating_function_afolu

        else:
            rating_function = rating_function_overwrite

        super().__init__(
            criterion_name=criterion_name,
            region=region,
            years=years,
            variable=variable,
            aggregation_function=aggregation_function,
            unit=unit,
            rating_function=rating_function,
            **kwargs,
        )


class Mean_Biomass_PrimaryEnergy(AggregateCriterion):
    """Evaluates the mean amount of biomass use in primary energy within a given time period and for a given region

    Parameters
    ----------
    criterion_name : str, optional
        Name of the criterion
    region : Union[str, Dict[str, List[str]]], optional
        Region for which the criterion should be evaluated, if a dict is passed, the regions (items) are aggregated to the macro region (key)
    years : List[int], optional
        Years for which the criterion should be evaluated, if None [2040, 2050, 2060]
    variable : str, optional
        Name of the variable in the file
    aggregation_function : Callable, optional
        Aggregation function, default np.mean
    unit: str, optional
        Unit in which the evaluated variable should be returned
    rating_function : Callable, optional
        Rating function, levels come from https://www.ipcc.ch/report/ar6/wg3/downloads/report/IPCC_AR6_WGIII_Annex-III.pdf
        which in turn draws from Creutzig et al. (2014) (https://doi.org/10.1111/gcbb.12205)
        
        This suggests that Primary Energy|Biomass  > 100 EJ/yr poses medium feasibility challenges,
        and Primary Energy|Biomass > 245 EJ/yr poses high feasibility challenges.
        
        Two initial rating functions then emerge:
        STRICT (default): lambda x: np.clip(1 - x / 100, 0, 1):
            Rates pathways linearly from 1 to 0, with pathways displaying Primary Energy|Biomass > medium feasibility threshold ranked as zero.
        RELAXED: lambda x: np.clip(1 - ((x - 100) / (245 - 100)), 0, 1)): 
            Rates pathways with < medium feasibility challenges as 1, with the rating then declining linearly to zero over 
            the [medium feasibility challenges, high feasibility challenge] interval. 
            Pathways displaying high feasibility challenges are ranked as zero.

        Depending on which pathways you are attempting to distinguish between, different rating functions may be necessary.

    kwargs : dict
        Other kwargs passed to the AggregateCriterion class
    """

    def __init__(
        self,
        criterion_name: str = "Average Biomass Demand",
        region: Union[str, Dict[str, List[str]]] = "World",
        years: Optional[List[int]] = None,
        variable: str = "Primary Energy|Biomass",
        aggregation_function: Callable = np.mean,
        unit: str = "EJ/yr",
        rating_function: Callable = lambda x: np.clip(
            1 - x / 100,
            0,
            1,
        ),
        **kwargs,
    ):
        if years is None:  # pragma: no cover
            years = [2040, 2050, 2060]

        super().__init__(
            criterion_name=criterion_name,
            region=region,
            years=years,
            variable=variable,
            aggregation_function=aggregation_function,
            unit=unit,
            rating_function=rating_function,
            **kwargs,
        )


class Max_ExceedanceProbability(AggregateCriterion):
    """Rates the peak exceedance probability of a given temperature

    Parameters
    ----------
    criterion_name : str, optional
        Name of the criterion
    region : str, optional
        Region for which the criterion should be evaluated
    years : Optional[List[int]], optional
        Years for which the criterion should be evaluated (None means all)
    variable : str, optional
        Name of the temperature variable
        Note: for other temperature targets or dataset versions try for example
        - "AR6 climate diagnostics|Exceedance Probability 2.0C|MAGICCv7.5.3"
        - "AR5 climate diagnostics|Temperature|Exceedance Probability|1.5 degC|MAGICC6"
    aggregation_function : Callable, optional
        Aggregation function, default np.max
    rating_function : Callable, optional
        Rating function, default: np.clip(1 - ((x - 0.5) / (1 - 0.5)), 0, 1)
    kwargs : dict
        Other kwargs passed to the AggregateCriterion class
    """

    def __init__(
        self,
        criterion_name: str = "1.5°C Exceedance probability",
        region: str = "World",
        years: Optional[List[int]] = None,
        variable: str = "*climate diagnostics*Exceedance Probability*1.5C*MAGICC*",
        aggregation_function: Callable = np.max,
        rating_function: Callable = lambda x: np.clip(
            1 - ((x - 0.5) / (1 - 0.5)),
            0,
            1,
        ),
        **kwargs,
    ):
        super().__init__(
            criterion_name=criterion_name,
            region=region,
            years=years,
            variable=variable,
            aggregation_function=aggregation_function,
            unit=None,
            rating_function=rating_function,
            **kwargs,
        )


class Max_1o5C_Overshoot(AggregateCriterion):
    """Rates the maximum temperature overshoot in reference to 1.5°C

    Parameters
    ----------
    criterion_name : str, optional
        Name of the criterion
    region : str, optional
        Region for which the criterion should be evaluated
    years : Optional[List[int]], optional
        Years for which the criterion should be evaluated (None means all)
    variable : str, optional
        Name of the temperature variable
    aggregation_function : Callable, optional
        Aggregation function, default np.max
    rating_function : Callable, optional
        Rating function, default: lambda x: 1 - ((x - 1.5) / (1.7 - 1.5))
    kwargs : dict
        Other kwargs passed to the AggregateCriterion class
    """

    def __init__(
        self,
        criterion_name: str = "Maximum 1o5p overshoot",
        region: str = "World",
        years: Optional[List[int]] = None,
        variable: str = "Temperature|Global temperature MAGICC 50th percentile",
        aggregation_function: Callable = np.max,
        rating_function: Callable = lambda x: 1 - ((x - 1.5) / (1.7 - 1.5)),
        **kwargs,
    ):
        super().__init__(
            criterion_name=criterion_name,
            region=region,
            years=years,
            variable=variable,
            aggregation_function=aggregation_function,
            unit=None,
            rating_function=rating_function,
            **kwargs,
        )
