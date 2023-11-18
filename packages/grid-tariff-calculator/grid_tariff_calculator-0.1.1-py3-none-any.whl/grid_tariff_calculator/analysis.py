import datetime
import pandas as pd


def _get_daily_maximums(consumption_df: pd.DataFrame) -> pd.DataFrame:
    """Private function to only keep the maximum value of each date in the consumption dataframe.

    Expects a dataframe with a column named "start_time" containing datetime objects and
    a column named "value" containing the consumption during the hour starting at "start_time".
    """

    filtered_df = (
        consumption_df.groupby([consumption_df["start_time"].dt.date])
        .agg({"value": "max"})
        .reset_index()
    )
    filtered_df["start_time"] = pd.to_datetime(filtered_df["start_time"])

    return filtered_df


def _get_top_n_values(consumption_df: pd.DataFrame, top_n_values: int):
    """Private function to only keep the top n values of each month in the consumption dataframe.

    Expects a dataframe with a column named "start_time" containing datetime objects and
    a column named "value" containing the consumption during the hour starting at "start_time".
    """

    top_values = (
        consumption_df.groupby(
            [
                consumption_df["start_time"].dt.year,
                consumption_df["start_time"].dt.month,
            ]
        )
        .apply(lambda grp: grp.nlargest(top_n_values, "value"))
        .reset_index(drop=True)
    )
    return top_values


def _average_groups(consumption_df: pd.DataFrame):  # a.k.a max_value_dates
    """Private function to average the values from each month in a new column "maximum",
    while keeping the dates of the aggregated values in a new column called "maximums_occured_on".

    Expects a dataframe with a column named "start_time" containing datetime objects and
    a column named "value" containing the consumption during the hour starting at "start_time".
    """

    max_value_dates = (
        consumption_df.groupby(
            [
                consumption_df["start_time"].dt.year.rename("year"),
                consumption_df["start_time"].dt.month.rename("month"),
            ]
        )
        .agg({"value": "mean", "start_time": lambda grp: list(grp.dt.date)})
        .rename(columns={"value": "maximum", "start_time": "maximums_occured_on"})
        .reset_index()
    )
    return max_value_dates


def _get_monthly_totals(consumption_df: pd.DataFrame):
    """Private function to calculate the total consumption of each month in a new column 'total_consumption'."""

    monthly_totals = (
        consumption_df.copy()
        .groupby(
            [
                consumption_df["start_time"].dt.year.rename("year"),
                consumption_df["start_time"].dt.month.rename("month"),
            ]
        )
        .agg({"value": "sum"})
        .rename(columns={"value": "total_consumption"})
        .reset_index()
    )
    return monthly_totals


def monthly_maximums(
    curve: [(datetime.datetime, float)],
    top_n_averaged: int = 1,
    single_max_per_day: bool = False,
) -> pd.DataFrame:
    """Function to get the maximum value of each month in the consumption curve.
    top_n_averaged determines how many of the largest values are averaged per month.
    single_max_per_day determines if only the maximum value of each day is kept before
    finding the largest values of each month and averaging.

    Expects a list of tuples containing datetimes and corresponding consumption values in kWH during the hour starting at the datetime,
    an integer for top_n_averaged and a boolean for single_max_per_day.
    """

    # assert top_n_averaged >= 1
    curve_df = pd.DataFrame(curve, columns=["start_time", "value"])

    with_total_consumption = _get_monthly_totals(curve_df)

    if single_max_per_day:
        curve_df = _get_daily_maximums(curve_df)

    curve_df = _get_top_n_values(curve_df, top_n_averaged)

    curve_df = _average_groups(curve_df)

    curve_df = curve_df.merge(with_total_consumption, on=["year", "month"])

    return curve_df


dates = [
    datetime.datetime(2022, 12, 31),
    datetime.datetime(2022, 12, 31, 3),
    datetime.datetime(2022, 12, 18, 2),
    datetime.datetime(2022, 12, 17, 3),
    datetime.datetime(2022, 12, 17, 6),
    datetime.datetime(2022, 12, 9, 14),
    datetime.datetime(2022, 12, 22),
    datetime.datetime(2023, 3, 12),
    datetime.datetime(2023, 12, 5),
]
vals = [12, 17, 0, 21, 24, 18, 15, 16, 9]

curve = list(zip(dates, vals))
test_result = monthly_maximums(curve, 3)


def _add_threshold_values(
    consumption_df: pd.DataFrame, threshold: float
) -> pd.DataFrame:
    """Private function to add a column with the threshold values to the consumption dataframe.
    The threshold determines the fraction of the maximum value that is used as the new threshold.

    Expects a dataframe with a column named "maximum" containing the maximum consumption value of each month, and
    a float between 0 and 1 for the threshold.
    """

    consumption_df["threshold"] = threshold * consumption_df["maximum"]

    return consumption_df


def monthly_averages(curve: [(datetime.datetime, float)]) -> pd.DataFrame:
    curve_df = pd.DataFrame(curve, columns=["start_time", "value"])

    monthly_averages = (
        curve_df.groupby(
            [
                curve_df["start_time"].dt.year.rename("year"),
                curve_df["start_time"].dt.month.rename("month"),
            ]
        )
        .agg({"value": "mean"})
        .rename(columns={"value": "average"})
        .reset_index()
    )
    return monthly_averages


_add_threshold_values(test_result, 0.5)