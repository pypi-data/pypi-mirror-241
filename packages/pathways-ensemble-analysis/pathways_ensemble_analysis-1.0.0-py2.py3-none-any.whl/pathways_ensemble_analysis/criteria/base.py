import pandas as pd
import pyam
from typing import Callable, Optional, Union, Iterable, List, Type, Dict

from ..utils import format_value_series, select_vars


class Criterion:
    """Basic criterion class

    Parameters
    ----------
    criterion_name : str
        Name of the criterion
    region : Union[str, Dict[str, List[str]]]
        Name of the investigated region, if a dict is passed, e.g. {"macro_region": "my_macro_region", "subregions": ["region_a", "region_b"]} 
        the subregions are aggregated to the macro_region
    rating_function : Callable, optional
        Rating function
    region_aggregation_weight: Optional[str], optional
        Name of the weight passed to pyam's aggregate_region function
    rating_weight : float, optional
        Rating weight
    """

    def __init__(
        self,
        criterion_name: str,
        region: Union[str, Dict[str, List[str]]],
        rating_function: Callable = lambda x: x,
        region_aggregation_weight: Optional[str] = None,
        rating_weight: float = 1,
    ):
        self.criterion_name = criterion_name
        self.region = region
        self.rating_function = rating_function
        self.region_aggregation_weight = region_aggregation_weight
        self.rating_weight = rating_weight

    def get_values(
        self,
        file: pyam.IamDataFrame,
    ) -> pd.Series:
        raise NotImplementedError

    def rate(self, s: pd.Series) -> pd.Series:
        """Rates the share for each pathway

        Parameters
        ----------
        s : pd.Series
            Series containing the share for each pathway

        Returns
        -------
        pd.Series
            Series containing the rating for each pathway
        """

        s = self.rating_weight * s.apply(self.rating_function)

        return s


class SingleVariableCriterion(Criterion):
    """Evaluates the value of a variable for a given year and a given region

    Parameters
    ----------
    year : int
        Year for which the criterion should be evaluated
    variable : str
        Name of the variable in the file which quantifies the variable
    unit: Optional[str]
        Unit the drop_rating['value'] is referring to
    kwargs : dict
        Kwargs passed to the Criterion class
    """

    def __init__(
        self,
        year: int,
        variable: str,
        unit: Optional[str],
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.year = year
        self.variable = variable
        self.unit = unit

    def get_values(
        self,
        file: pyam.IamDataFrame,
    ) -> pd.Series:
        """Rates the level of total emissions for each pathway

        Parameters
        ----------
        s : pd.Series
            Series containing the total emissions for each pathway
        mapping : function, optional
            Rating function

        Returns
        -------
        pd.Series
            Series containing the total emissions rating for each pathway
        """

        sel = select_vars(
            file,
            {self.variable: self.criterion_name},
            region=self.region,
            year=self.year,
            region_aggregation_weight=self.region_aggregation_weight,
            unit=self.unit,
        )
        s = sel.timeseries().loc[:, self.year]

        s_formatted = format_value_series(s)
        return s_formatted


class AggregateCriterion(Criterion):
    """Evaluates the aggregate of a variable, e.g. the average / min / max, for given years in a given region

    Parameters
    ----------
    years : int
        Years for which the criterion should be evaluated, None means the aggregation functions is applied across all years
    variable : str
        Name of the variable in the file for which the aggregate should be computed
    aggregation_function : Callable
        Aggregation function, e.g. np.mean, np.min or np.max
    unit: Optional[str]
        Unit in which the evaluated variable should be returned
    kwargs : dict
        Kwargs passed to the Criterion class
    """

    def __init__(
        self,
        years: Optional[Iterable[int]],
        variable: str,
        aggregation_function: Callable,
        unit: Optional[str],
        **kwargs,
    ):

        super().__init__(**kwargs)

        self.years = years
        self.variable = variable
        self.unit = unit
        self.aggregation_function = aggregation_function

    def get_values(
        self,
        file: pyam.IamDataFrame,
    ) -> pd.Series:
        """Evaluates the criterion

        Parameters
        ----------
        file : pyam.IamDataFrame
            IamDataFrame containing the to be evaluated pathways with the variable variable_component
            and variable_total

        Returns
        -------
        pd.Series
            Series containing the evaluated criterion for each pathways
        """

        years = self.years if self.years else file.year

        sel = select_vars(
            file,
            {self.variable: self.criterion_name},
            region=self.region,
            year=years,
            region_aggregation_weight=self.region_aggregation_weight,
            unit=self.unit,
        )

        s = sel.timeseries().T.reindex(range(years[0], years[-1] + 1))
        s = s.interpolate().T
        s = s.apply(self.aggregation_function, axis=1)

        s_formatted = format_value_series(s)

        return s_formatted


class ChangeOverTimeCriterion(Criterion):
    """Evaluates the change of a component for a given year and a given region with respect to a base year

    Parameters
    ----------
    year : int
        Year for which the criterion should be evaluated
    variable : str
        Name of the variable in the file for which the change should be quantified
    reference_year: int
        Reference year
    kwargs : dict
        Kwargs passed to the Criterion class
    """

    def __init__(
        self,
        year: int,
        variable: str,
        reference_year: int,
        **kwargs,
    ):

        super().__init__(**kwargs)

        self.year = year
        self.variable = variable
        self.reference_year = reference_year

    def get_values(
        self,
        file: pyam.IamDataFrame,
    ) -> pd.Series:
        """Evaluates the change of a variable for a given year and a given region with respect to a reference year

        Parameters
        ----------
        file : pyam.IamDataFrame
            IamDataFrame containing the to be evaluated pathways with the variables variable_component
            and variable_total

        Returns
        -------
        pd.Series
            Series containing the evaluated criterion for each pathways
        """

        sel = select_vars(
            file,
            [self.variable],
            region=self.region,
            year=[self.reference_year, self.year],
            region_aggregation_weight=self.region_aggregation_weight,
        ).rename(variable={self.variable: self.criterion_name})

        change = (
            sel.timeseries()[self.year] - sel.timeseries()[self.reference_year]
        ) / sel.timeseries()[self.reference_year]

        s_formatted = format_value_series(change)

        return s_formatted


class ShareCriterion(Criterion):
    """Evaluates the share of a component on the total for a given year and a given region

    Parameters
    ----------
    year : int
        Year for which the criterion should be evaluated
    variable_component : Union[str, List[str]]
        Name of the variable(s) in the file which quantify the components
    variable_total: str
        Name of the variable in the file which quantifies the total
    kwargs : dict
        Kwargs passed to the Criterion class
    """

    def __init__(
        self,
        year: int,
        variable_component: Union[str, List[str]],
        variable_total: str,
        **kwargs,
    ):

        super().__init__(**kwargs)

        self.year = year
        self.variable_component = variable_component
        self.variable_total = variable_total

        self.unit = "uniform"

    def get_values(
        self,
        file: pyam.IamDataFrame,
    ) -> pd.Series:
        """Evaluates the share of a component on the total for a given year and a given region

        Parameters
        ----------
        file : pyam.IamDataFrame
            IamDataFrame containing the to be evaluated pathways with the variables variable_component
            and variable_total

        Returns
        -------
        pd.Series
            Series containing the evaluated criterion for each pathways
        """

        if isinstance(self.variable_component, list):
            variables = self.variable_component + [self.variable_total]
        else:
            variables = [self.variable_total, self.variable_component]

        sel = select_vars(
            file,
            variables,
            region=self.region,
            year=self.year,
            region_aggregation_weight=self.region_aggregation_weight,
            unit=self.unit,
        )

        if isinstance(self.variable_component, list):
            numerator_name = "aggregated_variables"
            sel.aggregate(numerator_name, self.variable_component, append=True)
        else:
            numerator_name = self.variable_component

        share = sel.divide(numerator_name, self.variable_total, self.criterion_name)

        s = share.timeseries().loc[:, self.year]
        s_formatted = format_value_series(s)

        return s_formatted


class CompareRegionsCriterion(Criterion):
    """Takes a given criterion and evaluates how two different regions compare

    Parameters
    ----------
    criterion_class : Type[Criterion]
        The criterion class which is going to be evaluated across two regions (already defined)
    kwargs_criterion: Dict
        Kwargs which will be passed to the defined criterion class
    region1 : Union[str, Dict[str, List[str]]]
        First region for which the criterion should be evaluated, if a dict is passed, the regions (items) are aggregated to the macro region (key)
    region2 : Union[str, Dict[str, List[str]]]
        Second region for which the criterion should be evaluated, if a dict is passed, the regions (items) are aggregated to the macro region (key)
    method : str
        Choice of method of how to compare two regions - "subtract" and "divide" are current options
    kwargs : dict
        Kwargs passed to the Criterion class; the kwarg region and the kwarg region_aggregation_weight cannot be passed
    """

    def __init__(
        self,
        criterion_class: Type[Criterion],
        kwargs_criterion: Dict,
        region_1: str,
        region_2: str,
        method: str,
        **kwargs,
    ):
        super().__init__(
            region=f"{region_1}_{region_2}", region_aggregation_weight=None, **kwargs
        )

        self.criterion_region_1 = criterion_class(region=region_1, **kwargs_criterion)
        self.criterion_region_2 = criterion_class(region=region_2, **kwargs_criterion)

        self.method = method

    def get_values(
        self,
        file: pyam.IamDataFrame,
    ) -> pd.Series:
        """Calculates the indicator for each region, and then subtracts them from another

        Parameters
        ----------
        file : pyam.IamDataFrame
            IamDataFrame containing the to be evaluated pathways and variables

        Returns
        -------
        pd.Series
            Series containing the difference between the two regions
        """

        values_region_1 = self.criterion_region_1.get_values(file)
        values_region_2 = self.criterion_region_2.get_values(file)

        if self.method == "subtract":
            sel = values_region_1 - values_region_2
        elif self.method == "divide":
            sel = values_region_1 / values_region_2
        else:
            raise ValueError("`method` parameter can either be 'subtract' or 'divide'")

        sel.rename(
            index={self.criterion_region_1.criterion_name: self.criterion_name},
            inplace=True,
        )

        return sel
