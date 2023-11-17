from typing import Optional
import warnings
import pandas as pd
from grid_tariff_calculator.grid_tariff_dataclasses import (
    ElFeeTariff,
    EnergyTariff,
    EnovaFee,
    FixedTariff,
    PeakTariffLargeConsumers,
    PeakTariffSmallConsumers,
)
import datetime
from grid_tariff_calculator.analysis import monthly_maximums, monthly_averages
import calendar
import logging

"""
tariffs = [
    PeakTariffLargeConsumers(
        distributor_name="ELVIA AS",
        price_NOK_per_kWh=0.34,
        start_time=datetime.datetime(2020, 1, 1, 0, 0, 0),
        end_time=datetime.datetime(2020, 12, 31, 23, 59, 59),
    ),
    PeakTariffLargeConsumers(
        distributor_name="ELVIA AS",
        price_NOK_per_kWh=0.44,
        start_time=datetime.datetime(2021, 1, 1, 0, 0, 0),
        end_time=datetime.datetime(2021, 12, 31, 23, 59, 59),
    ),
]

tariffs_small_consumers = [
    PeakTariffSmallConsumers(
        distributor_name="BKK AS",
        price_NOK=116.0,
        start_time=datetime.datetime(2020, 1, 1, 0, 0, 0),
        end_time=datetime.datetime(2020, 12, 31, 23, 59, 59),
        lower_limit=0,
        upper_limit=2.0,
    ),
    PeakTariffSmallConsumers(
        distributor_name="BKK AS",
        price_NOK=191.0,
        start_time=datetime.datetime(2020, 1, 1, 0, 0, 0),
        end_time=datetime.datetime(2020, 12, 31, 23, 59, 59),
        lower_limit=2.0,
        upper_limit=5.0,
    ),
    PeakTariffSmallConsumers(
        distributor_name="BKK AS",
        price_NOK=320.0,
        start_time=datetime.datetime(2020, 1, 1, 0, 0, 0),
        end_time=datetime.datetime(2020, 12, 31, 23, 59, 59),
        lower_limit=5.0,
        upper_limit=10.0,
    ),
    PeakTariffSmallConsumers(
        distributor_name="BKK AS",
        price_NOK=456.0,
        start_time=datetime.datetime(2020, 1, 1, 0, 0, 0),
        end_time=datetime.datetime(2020, 12, 31, 23, 59, 59),
        lower_limit=10.0,
        upper_limit=15.0,
    ),
    PeakTariffSmallConsumers(
        distributor_name="BKK AS",
        price_NOK=588.0,
        start_time=datetime.datetime(2020, 1, 1, 0, 0, 0),
        end_time=datetime.datetime(2020, 12, 31, 23, 59, 59),
        lower_limit=15.0,
        upper_limit=20.0,
    ),
    PeakTariffSmallConsumers(
        distributor_name="BKK AS",
        price_NOK=720.0,
        start_time=datetime.datetime(2020, 1, 1, 0, 0, 0),
        end_time=datetime.datetime(2020, 12, 31, 23, 59, 59),
        lower_limit=20.0,
        upper_limit=25.0,
    ),
    PeakTariffSmallConsumers(
        distributor_name="BKK AS",
        price_NOK=1380.0,
        start_time=datetime.datetime(2020, 1, 1, 0, 0, 0),
        end_time=datetime.datetime(2020, 12, 31, 23, 59, 59),
        lower_limit=25.0,
        upper_limit=50.0,
    ),
    PeakTariffSmallConsumers(
        distributor_name="BKK AS",
        price_NOK=2040.0,
        start_time=datetime.datetime(2020, 1, 1, 0, 0, 0),
        end_time=datetime.datetime(2020, 12, 31, 23, 59, 59),
        lower_limit=50.0,
        upper_limit=75.0,
    ),
    PeakTariffSmallConsumers(
        distributor_name="BKK AS",
        price_NOK=2700.0,
        start_time=datetime.datetime(2020, 1, 1, 0, 0, 0),
        end_time=datetime.datetime(2020, 12, 31, 23, 59, 59),
        lower_limit=75.0,
        upper_limit=100.0,
    ),
    PeakTariffSmallConsumers(
        distributor_name="BKK AS",
        price_NOK=3360.0,
        start_time=datetime.datetime(2020, 1, 1, 0, 0, 0),
        end_time=datetime.datetime(2020, 12, 31, 23, 59, 59),
        lower_limit=100.0,
        upper_limit=float("inf"),
    ),
    PeakTariffSmallConsumers(
        distributor_name="BKK AS",
        price_NOK=100.0,
        start_time=datetime.datetime(2021, 1, 1, 0, 0, 0),
        end_time=datetime.datetime(2021, 12, 31, 23, 59, 59),
        lower_limit=0,
        upper_limit=2.0,
    ),
    PeakTariffSmallConsumers(
        distributor_name="BKK AS",
        price_NOK=165.0,
        start_time=datetime.datetime(2021, 1, 1, 0, 0, 0),
        end_time=datetime.datetime(2021, 12, 31, 23, 59, 59),
        lower_limit=2.0,
        upper_limit=5.0,
    ),
    PeakTariffSmallConsumers(
        distributor_name="BKK AS",
        price_NOK=280.0,
        start_time=datetime.datetime(2021, 1, 1, 0, 0, 0),
        end_time=datetime.datetime(2021, 12, 31, 23, 59, 59),
        lower_limit=5.0,
        upper_limit=10.0,
    ),
    PeakTariffSmallConsumers(
        distributor_name="BKK AS",
        price_NOK=395.0,
        start_time=datetime.datetime(2021, 1, 1, 0, 0, 0),
        end_time=datetime.datetime(2021, 12, 31, 23, 59, 59),
        lower_limit=10.0,
        upper_limit=15.0,
    ),
    PeakTariffSmallConsumers(
        distributor_name="BKK AS",
        price_NOK=510.0,
        start_time=datetime.datetime(2021, 1, 1, 0, 0, 0),
        end_time=datetime.datetime(2021, 12, 31, 23, 59, 59),
        lower_limit=15.0,
        upper_limit=20.0,
    ),
    PeakTariffSmallConsumers(
        distributor_name="BKK AS",
        price_NOK=625.0,
        start_time=datetime.datetime(2021, 1, 1, 0, 0, 0),
        end_time=datetime.datetime(2021, 12, 31, 23, 59, 59),
        lower_limit=20.0,
        upper_limit=25.0,
    ),
    PeakTariffSmallConsumers(
        distributor_name="BKK AS",
        price_NOK=1200.0,
        start_time=datetime.datetime(2021, 1, 1, 0, 0, 0),
        end_time=datetime.datetime(2021, 12, 31, 23, 59, 59),
        lower_limit=25.0,
        upper_limit=50.0,
    ),
    PeakTariffSmallConsumers(
        distributor_name="BKK AS",
        price_NOK=1775.0,
        start_time=datetime.datetime(2021, 1, 1, 0, 0, 0),
        end_time=datetime.datetime(2021, 12, 31, 23, 59, 59),
        lower_limit=50.0,
        upper_limit=75.0,
    ),
    PeakTariffSmallConsumers(
        distributor_name="BKK AS",
        price_NOK=2350.0,
        start_time=datetime.datetime(2021, 1, 1, 0, 0, 0),
        end_time=datetime.datetime(2021, 12, 31, 23, 59, 59),
        lower_limit=75.0,
        upper_limit=100.0,
    ),
    PeakTariffSmallConsumers(
        distributor_name="BKK AS",
        price_NOK=4650.0,
        start_time=datetime.datetime(2021, 1, 1, 0, 0, 0),
        end_time=datetime.datetime(2021, 12, 31, 23, 59, 59),
        lower_limit=100.0,
        upper_limit=float("inf"),
    ),
]

energy_tariffs = [
    EnergyTariff(
        distributor_name="ELVIA AS",
        price_NOK_per_kWh=0.54,
        start_time=datetime.datetime(2020, 1, 1, 0, 0, 0),
        end_time=datetime.datetime(2020, 12, 31, 23, 59, 59),
    ),
    EnergyTariff(
        distributor_name="ELVIA AS",
        price_NOK_per_kWh=0.64,
        start_time=datetime.datetime(2021, 1, 1, 0, 0, 0),
        end_time=datetime.datetime(2021, 12, 31, 23, 59, 59),
    ),
]

fixed_tariffs = [
    FixedTariff(
        distributor_name="ELVIA AS",
        price_NOK_per_year=10000,
        start_time=datetime.datetime(2020, 1, 1, 0, 0, 0),
        end_time=datetime.datetime(2020, 12, 31, 23, 59, 59),
    ),
    FixedTariff(
        distributor_name="ELVIA AS",
        price_NOK_per_year=20000,
        start_time=datetime.datetime(2021, 1, 1, 0, 0, 0),
        end_time=datetime.datetime(2021, 12, 31, 23, 59, 59),
    ),
]

enova_fee = [
    EnovaFee(
        price_NOK_per_year=800,
        start_time=datetime.datetime(2020, 1, 1, 0, 0, 0),
        end_time=datetime.datetime(2020, 12, 31, 23, 59, 59),
    ),
    EnovaFee(
        price_NOK_per_year=800,
        start_time=datetime.datetime(2021, 1, 1, 0, 0, 0),
        end_time=datetime.datetime(2021, 12, 31, 23, 59, 59),
    ),
    EnovaFee(
        price_NOK_per_year=3000,
        start_time=datetime.datetime(2022, 1, 1, 0, 0, 0),
        end_time=datetime.datetime(2022, 12, 31, 23, 59, 59),
    ),
]
"""

logger = logging.getLogger(__name__)


def _weight_by_nr_days(row, col_name: str) -> float:
    """Function to weight fixed yearly fees by the number of days in the month.

    Expects a row from a dataframe with columns "year" and "month", and the name of the column to be weighted.
    """

    days_in_year = 366 if calendar.isleap(int(row["year"])) else 365
    days_in_month = calendar.monthrange(int(row["year"]), int(row["month"]))[1]
    value = row[col_name] * (days_in_month / days_in_year)

    return value


def _valid_time(year: int, month: int, tariff):
    """Function to check if a tariff is valid for a given month.

    Assumes that the tariff has datetime attributes "start_time" and "end_time".
    """

    return (
        datetime.datetime(year, month, 1) >= tariff.start_time
        and datetime.datetime(year, month, 1) <= tariff.end_time
    )


def _valid_time_and_tier(year: int, month: int, max: float, tariff):
    """Function to check if a tariff is valid for a given month and tier.

    Assumes that the tariff has datetime attributes "start_time" and "end_time",
    and float attributes "lower_limit" and "upper_limit".
    """

    return (
        _valid_time(year, month, tariff)
        and max >= tariff.lower_limit
        and max < tariff.upper_limit
    )


def _is_valid(
    has_tiers: bool, year: int, month: int, tariff, max: Optional[float] = None
):
    """Function to check if a tariff is valid for a given month and tier.

    Assumes that the tariff has datetime attributes "start_time" and "end_time",
    but only assumes float attributes "lower_limit" and "upper_limit" if
    it needs to take tiers into account.
    """

    if has_tiers:
        return _valid_time_and_tier(year, month, max, tariff)
    else:
        return _valid_time(year, month, tariff)


def _find_valid_tariff_attr(
    row, attr_name, tariffs: [], has_tiers=False  # TODO: add type hint for tariffs
) -> float:
    """Function to find the valid tariff for a given month and return the requested attribute.

    Expects a row from a dataframe with columns "year" and "month", and a list of tariff objects with datetime attributes "start_time" and "end_time".
    All tariff objects in the list must have the same type.
    """

    if not tariffs:
        raise ValueError("The provided tariff list is empty.")

    if not all(isinstance(tariff, type(tariffs[0])) for tariff in tariffs):
        raise TypeError(
            "All tariff objects in the tariff list must be of the same type. The provided list har several types."
        )

    year = int(row["year"])
    month = int(row["month"])

    value = next(
        (
            getattr(tariff, attr_name)
            for tariff in tariffs
            if _is_valid(has_tiers, year, month, tariff, row["maximum"])
        ),
        None,
    )
    if value is None:
        warnings.warn(
            f"None of the provided {type(tariffs[0]).__name__}-objects are valid for {calendar.month_name[month]} {year}."
        )

    return value


def _get_peak_tariff_large_consumers(
    consumption_df: pd.DataFrame, tariffs: [PeakTariffLargeConsumers]
) -> pd.Series:
    """Function to get a column with the peak tariff prices for each month of the dataframe.

    Expects a dateframe with columns "year" and "month", and a list of tariff objects with a float attribute "price_NOK_per_kWh"
    and datetime attributes "start_time" and "end_time".
    """

    peak_tariff = consumption_df.apply(
        _find_valid_tariff_attr, axis=1, args=("price_NOK_per_kWh", tariffs, False)
    )

    return peak_tariff


def _get_peak_tariff_small_consumers(
    consumption_df: pd.DataFrame, tariffs: [PeakTariffSmallConsumers]
) -> pd.Series:
    """Function to get a column with the peak tariff prices for each month of the dataframe.

    Expects a dateframe with columns "year" and "month".
    Expects a list of tariff objects with a float attribute "price_NOK",
    float attributes "lower_limit" and "upper_limit" for the tiers,
    and datetime attributes "start_time" and "end_time".
    """

    peak_tariff = consumption_df.apply(
        _find_valid_tariff_attr, axis=1, args=("price_NOK", tariffs, True)
    )

    return peak_tariff


def _get_energy_tariff(
    consumption_df: pd.DataFrame, tariffs: [EnergyTariff]
) -> pd.Series:
    """Function to get a column with the energy tariff prices for each month of the dataframe.

    Expects a dateframe with columns "year" and "month", and a list of tariff objects with a float attribute "price_NOK_per_kWh"
    and datetime attributes "start_time" and "end_time".
    """

    # TODO: implement day/night tariff
    energy_tariff = consumption_df.apply(
        _find_valid_tariff_attr, axis=1, args=("price_NOK_per_kWh", tariffs)
    )

    return energy_tariff


def _get_fixed_tariff(
    consumption_df: pd.DataFrame, tariffs: [FixedTariff]
) -> pd.Series:
    """Function to get a column with the fixed tariff prices for each month of the dataframe.

    Expects a dateframe with columns "year" and "month", and a list of tariff objects with a float attribute "price_NOK_per_year"
    and datetime attributes "start_time" and "end_time".
    """

    fixed_tariff = consumption_df.apply(
        _find_valid_tariff_attr, axis=1, args=("price_NOK_per_year", tariffs)
    )

    return fixed_tariff


def _get_peak_costs_large_consumers(
    grid_rental_df: pd.DataFrame, tariffs: [PeakTariffLargeConsumers]
) -> pd.Series:
    """Function to get a column with the peak cost for each month of the dataframe.

    Expects a dateframe with columns "year", "month" and "maximum" and a list of tariff objects with a float attribute "price_NOK_per_year"
    and datetime attributes "start_time" and "end_time".
    """

    peak_tariff = _get_peak_tariff_large_consumers(grid_rental_df, tariffs)
    peak_cost = grid_rental_df["maximum"] * peak_tariff

    return peak_cost


def _get_energy_costs(
    grid_rental_df: pd.DataFrame, tariffs: [EnergyTariff]
) -> pd.Series:
    """Function to get a column with the energy cost for each month of the dataframe.

    Expects a dateframe with columns "year", "month" and "total_consumption" and a list of tariff objects with a float attribute "price_NOK_per_year"
    and datetime attributes "start_time" and "end_time".
    """

    energy_tariff = _get_energy_tariff(grid_rental_df, tariffs)
    energy_cost = grid_rental_df["total_consumption"] * energy_tariff

    return energy_cost


def _find_lowest_possible_threshold(consumption_df: pd.DataFrame) -> (int, pd.Series):
    """Function to find the lowest possible threshold for each month for a given consumption curve.
    Also returns the index of the month with the largest lower threshold, which is the limiting factor for the threshold.

    Expects a dataframe with columns "maximum" and "average" for each month.
    """

    lowest_thresholds = consumption_df["average"] / consumption_df["maximum"]

    return lowest_thresholds.idxmax(), lowest_thresholds


def _set_to_threshold(
    curve: [(datetime.datetime, float)],
    consumption_df: pd.DataFrame,
    threshold: float,
    load_shifting: bool = True,
) -> pd.DataFrame:
    """Function to reduce maximum and possibly total consumption according to a threshold.

    Expects a threshold value (float) between 0 and 1, a boolean for load shifting,
    the consumption curve, and a dataframe with columns "year", "month", "maximum" and "total_consumption".
    The maximums are reduced to the threshold (fraction of original value).
    If load shifting is True, it is assumed that the total consumption remains unchanged. Throws an error if the threshold is too low to achieve with load shifting.
    If load shifting is False, it is assumed the entire curve is reduced to the threshold.
    """

    if not load_shifting:
        consumption_df["total_consumption"] *= threshold
    else:
        # Implement threshold finder with is_large_consumer as input
        with_averages = monthly_averages(curve)
        df_with_avgs = consumption_df.merge(with_averages, on=["year", "month"])

        idx_lowest_possible, lowest_monthly = _find_lowest_possible_threshold(
            df_with_avgs
        )

        lowest_possible = lowest_monthly.iloc[idx_lowest_possible]
        if threshold < lowest_possible:
            month = int(consumption_df.iloc[idx_lowest_possible]["month"])
            year = int(consumption_df.iloc[idx_lowest_possible]["year"])
            raise ValueError(
                f"""The provided threshold of {threshold} is lower than the lowest possible threshold.
                With load-shifting, a threshold of {lowest_possible} is enough to result in a completely
                flat profile for {calendar.month_name[month]} {year}, and lowering the threshold further 
                is not possible for this month."""
            )

    consumption_df["maximum"] *= threshold

    return consumption_df


def calculate_costs_under_100k(
    curve: [(datetime.datetime, float)],
    threshold: float,
    load_shifting: bool = True,
    peak_tariffs_small_consumers: [PeakTariffSmallConsumers] = [],
    el_fee: [ElFeeTariff] = [],
) -> pd.DataFrame:
    """Function to calculate the grid rental costs of a consumption curve.
    Assumes estimated yearly consumption is under 100k kWh.

    Returns a dataframe with columns "year", "month", "maximum", "total_consumption" and "peak_cost".
    """

    monthly_max_df = monthly_maximums(curve, top_n_averaged=3, single_max_per_day=True)[
        ["year", "month", "maximum", "total_consumption"]
    ]

    monthly_max_df = _set_to_threshold(curve, monthly_max_df, threshold, load_shifting)

    if peak_tariffs_small_consumers:
        monthly_max_df["peak_cost"] = _get_peak_tariff_small_consumers(
            monthly_max_df, peak_tariffs_small_consumers
        )
    else:
        logger.warning(
            "No peak tariffs for small consumers provided. Peak cost will not be calculated."
        )

    return monthly_max_df


def calculate_costs_over_100k(
    curve: [(datetime.datetime, float)],
    threshold: float,
    load_shifting: bool = True,
    fixed_tariffs: [FixedTariff] = [],
    peak_tariffs_large_consumers: [PeakTariffLargeConsumers] = [],
    el_fee: [ElFeeTariff] = [],
) -> pd.DataFrame:
    """Function to calculate the grid rental costs of a consumption curve.
    Assumes estimated yearly consumption is over 100k kWh.

    Returns a dataframe with columns "year", "month", "maximum", "total_consumption", "peak_cost" and "fixed_cost".
    """

    monthly_max_df = monthly_maximums(
        curve, top_n_averaged=1, single_max_per_day=False
    )[["year", "month", "maximum", "total_consumption"]]

    _set_to_threshold(curve, monthly_max_df, threshold, load_shifting)

    monthly_max_df["peak_cost"] = _get_peak_costs_large_consumers(
        monthly_max_df, peak_tariffs_large_consumers
    )

    monthly_max_df["fixed_cost"] = _get_fixed_tariff(monthly_max_df, fixed_tariffs)
    monthly_max_df["fixed_cost"] = monthly_max_df.apply(
        _weight_by_nr_days, axis=1, col_name="fixed_cost"
    )

    return monthly_max_df


def _calculate_costs(
    curve: [(datetime.datetime, float)],
    estimated_yearly_cons,
    threshold: float,
    load_shifting: bool = True,
    energy_tariffs: [EnergyTariff] = [],
    enova_fee: [EnovaFee] = [],
    fixed_tariffs: [FixedTariff] = [],
    peak_tariffs_large_consumers: [PeakTariffLargeConsumers] = [],
    peak_tariffs_small_consumers: [PeakTariffSmallConsumers] = [],
    el_fee: [ElFeeTariff] = [],
) -> pd.DataFrame:
    """Function to calculate the grid rental costs of a consumption curve.

    Expects a list of tuples with datetime and consumption values, a threshold value (float) between 0 and 1, and a boolean for load shifting.
    The maximums are reduced to the threshold (fraction of original value).
    If load shifting is True, it is assumed that the total consumption remains unchanged. If load shifting is False,
    the entire curve is reduced to the threshold.
    """

    is_large_consumer = estimated_yearly_cons > 100000

    if is_large_consumer:
        monthly_max_df = calculate_costs_over_100k(
            curve,
            threshold,
            load_shifting,
            fixed_tariffs,
            peak_tariffs_large_consumers,
            el_fee,
        )
    else:
        monthly_max_df = calculate_costs_under_100k(
            curve, threshold, load_shifting, peak_tariffs_small_consumers, el_fee
        )

    monthly_max_df["energy_cost"] = _get_energy_costs(monthly_max_df, energy_tariffs)

    if enova_fee:
        monthly_max_df["enova_fee"] = _get_fixed_tariff(monthly_max_df, enova_fee)
        monthly_max_df["enova_fee"] = monthly_max_df.apply(
            _weight_by_nr_days, axis=1, col_name="enova_fee"
        )
    else: 
        logger.warning("No Enova fee provided. Enova fee will not be calculated.")

    return monthly_max_df


def calculate_grid_rental(
    curve: [(datetime.datetime, float)],
    load_shifting: bool = True,
    estimated_yearly_cons: float = 100000,
    energy_tariffs: [EnergyTariff] = [],
    enova_fee: [EnovaFee] = [],
    fixed_tariffs: [FixedTariff] = [],
    peak_tariffs_large_consumers: [PeakTariffLargeConsumers] = [],
    peak_tariffs_small_consumers: [PeakTariffSmallConsumers] = [],
    el_fee: [ElFeeTariff] = [],
) -> pd.DataFrame:
    """Function to get the grid rental costs of the original consumption curve."""

    monthly_grid_rental = _calculate_costs(
        curve,
        estimated_yearly_cons,
        threshold=1,
        load_shifting=load_shifting,
        energy_tariffs=energy_tariffs,
        enova_fee=enova_fee,
        fixed_tariffs=fixed_tariffs,
        peak_tariffs_large_consumers=peak_tariffs_large_consumers,
        peak_tariffs_small_consumers=peak_tariffs_small_consumers,
        el_fee=el_fee,
    )
    return monthly_grid_rental


def calculate_threshold_grid_rental(
    curve: [(datetime.datetime, float)],
    threshold: float,
    load_shifting: bool = True,
    estimated_yearly_cons: float = 100000,
    energy_tariffs: [EnergyTariff] = [],
    enova_fee: [EnovaFee] = [],
    fixed_tariffs: [FixedTariff] = [],
    peak_tariffs_large_consumers: [PeakTariffLargeConsumers] = [],
    peak_tariffs_small_consumers: [PeakTariffSmallConsumers] = [],
    el_fee: [ElFeeTariff] = [],
) -> pd.DataFrame:
    """Function to get the grid rental costs of a consumption curve that's lowered to a threshold."""

    monthly_grid_rental = _calculate_costs(
        curve,
        estimated_yearly_cons,
        threshold=threshold,
        load_shifting=load_shifting,
        energy_tariffs=energy_tariffs,
        enova_fee=enova_fee,
        fixed_tariffs=fixed_tariffs,
        peak_tariffs_large_consumers=peak_tariffs_large_consumers,
        peak_tariffs_small_consumers=peak_tariffs_small_consumers,
        el_fee=el_fee,
    )

    return monthly_grid_rental


dates = [
    datetime.datetime(2021, 12, 31),
    datetime.datetime(2021, 12, 31, 3),
    datetime.datetime(2021, 12, 18, 2),
    datetime.datetime(2021, 12, 17, 3),
    datetime.datetime(2021, 12, 17, 6),
    datetime.datetime(2021, 12, 9, 14),
    datetime.datetime(2021, 12, 22),
    datetime.datetime(2022, 12, 22),
    datetime.datetime(2022, 12, 17, 6),
    datetime.datetime(2020, 3, 12),
    datetime.datetime(2020, 3, 8),
    datetime.datetime(2020, 12, 7),
    datetime.datetime(2020, 12, 5),
]
vals = [12, 17, 0, 21, 24, 18, 15, 16, 9, 2, 5, 24, 30]

curve = list(zip(dates, vals))
# calculate_grid_rental(curve)
"""calculate_threshold_grid_rental(
    curve, threshold=0.8, load_shifting=True, estimated_yearly_cons=100001
)"""
