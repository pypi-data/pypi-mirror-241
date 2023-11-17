#!/usr/bin/env python
"""Tests for `grid_tariff_calculator` package."""
# pylint: disable=redefined-outer-name

import datetime
import pandas as pd
import pytest

from grid_tariff_calculator.grid_tariff_dataclasses import (
    ElFeeTariff,
    EnergyTariff,
    EnovaFee,
    FixedTariff,
    PeakTariffLargeConsumers,
    PeakTariffSmallConsumers,
)
from grid_tariff_calculator.analysis import monthly_maximums
from grid_tariff_calculator.tariff_calculator import (
    _get_peak_tariff_small_consumers,
    calculate_grid_rental,
)


@pytest.fixture
def small_consumer_data():
    """
    Load consumption for meter below 100MWh from csv file.

    Meter ID: 707057500027547039
    Customer: BKOLON AS
    """
    small_consumer_data = pd.read_csv("tests/data/test_meter_small.csv")
    small_consumer_data["date"] = pd.to_datetime(small_consumer_data["date"])
    return list(small_consumer_data.itertuples(index=False, name=None))


@pytest.fixture
def large_consumer_data():
    """
    Load consumption for meter above 100MWh from csv file.

    Meter ID: 707057500055374973
    Customer: BI-BYGGET D-BLOKKA AS
    """

    large_consumer_data = pd.read_csv("tests/data/test_meter_large.csv")
    large_consumer_data["date"] = pd.to_datetime(large_consumer_data["date"])
    return list(large_consumer_data.itertuples(index=False, name=None))


def test_data_format_large(large_consumer_data):
    """Check that large consumer data is in correct format"""
    assert all(isinstance(x[0], datetime.datetime) for x in large_consumer_data)
    assert all(isinstance(x[1], float) for x in large_consumer_data)
    assert all(isinstance(x, tuple) for x in large_consumer_data)


def test_data_format_small(small_consumer_data):
    """Check that small consumer data is in correct format"""
    assert all(isinstance(x[0], datetime.datetime) for x in small_consumer_data)
    assert all(isinstance(x[1], float) for x in small_consumer_data)
    assert all(isinstance(x, tuple) for x in small_consumer_data)


@pytest.fixture
def small_consumer_data_july_22(small_consumer_data):
    """Small consumer data from July 2022 only"""
    small_consumer_data_2020 = [
        x for x in small_consumer_data if x[0].year == 2022 and x[0].month == 7
    ]
    return small_consumer_data_2020


@pytest.fixture
def large_consumer_data_july_22(large_consumer_data):
    """Large consumer data from July 2022 only"""
    large_consumer_data_2020 = [
        x for x in large_consumer_data if x[0].year == 2022 and x[0].month == 7
    ]
    return large_consumer_data_2020


@pytest.fixture
def invoiced_energy_price_large():
    """Invoiced energy price for large consumer BI-BYGGET D-BLOKKA AS in july 2022"""
    invoiced_energy_price_large = [
        EnergyTariff(
            distributor_name="test",
            price_NOK_per_kWh=0.06,
            start_time=datetime.datetime(2022, 7, 1),
            end_time=datetime.datetime(2022, 7, 31),
        )
    ]
    return invoiced_energy_price_large


@pytest.fixture
def invoiced_peak_price_large():
    """Invoiced peak price for large consumer BI-BYGGET D-BLOKKA AS in july 2022"""
    invoiced_peak_price_large = [
        PeakTariffLargeConsumers(
            distributor_name="test",
            price_NOK_per_kWh=40.0,
            start_time=datetime.datetime(2022, 7, 1),
            end_time=datetime.datetime(2022, 7, 31),
        )
    ]
    return invoiced_peak_price_large


@pytest.fixture
def invoiced_fixed_price_large():
    """Invoiced fixed price for large consumer BI-BYGGET D-BLOKKA AS in july 2022"""
    invoiced_fixed_price_large = [
        FixedTariff(
            distributor_name="test",
            price_NOK_per_year=12 * 340,
            start_time=datetime.datetime(2022, 7, 1),
            end_time=datetime.datetime(2022, 7, 31),
        )
    ]
    return invoiced_fixed_price_large


@pytest.fixture
def invoiced_el_fee():
    """Invoiced el-fee for large consumer BI-BYGGET D-BLOKKA AS in july 2022"""
    invoiced_el_fee = [
        ElFeeTariff(
            distributor_name="test",
            price_NOK_per_kWh=0.1541,
            start_time=datetime.datetime(2022, 7, 1),
            end_time=datetime.datetime(2022, 7, 31),
        )
    ]
    return invoiced_el_fee


@pytest.fixture
def calculated_grid_rental_large(
    large_consumer_data_july_22,
    invoiced_energy_price_large,
    invoiced_fixed_price_large,
    invoiced_peak_price_large,
    invoiced_el_fee,
):
    """Calculate grid rental for large consumer with meter ID 707057500055374973

    Only tariffs appearing in the invoice are inputed, and the rest are set to empty lists.
    estimated_yearly_cons is set to 100001 kWh/year because it is above the limit for large consumers,
    and is not a real value.
    """
    calculated_grid_rental_large = calculate_grid_rental(
        large_consumer_data_july_22,
        False,
        100001,
        invoiced_energy_price_large,
        [],
        invoiced_fixed_price_large,
        invoiced_peak_price_large,
        [],
        invoiced_el_fee,
    )
    return calculated_grid_rental_large


def test_invoiced_total_consumption_large(calculated_grid_rental_large):
    """Compare the total consumption listed in the invoice for large consumer BI-BYGGET D-BLOKKA AS in july 2022
    with calculated total consumption, and check that it is within 0.5% of the expected value
    """
    # TODO : see if deviation can be reduced, possibly a timezone issue
    invoiced_total_cons = 56928.0

    assert len(calculated_grid_rental_large["total_consumption"]) == 1
    deviation = (
        calculated_grid_rental_large["total_consumption"][0] / invoiced_total_cons - 1
    )
    assert -0.005 < deviation < 0.005


def test_invoiced_peak_large(calculated_grid_rental_large):
    """Compare the peak listed in the invoice for large consumer BI-BYGGET D-BLOKKA AS in july 2022
    with calculated peak, and check that the values are exactly equal"""
    invoiced_peak = 164.80

    assert len(calculated_grid_rental_large["maximum"]) == 1
    assert invoiced_peak == calculated_grid_rental_large["maximum"][0]


def test_invoiced_peak_cost_large(calculated_grid_rental_large):
    """Compare invoiced peak cost for large consumer BI-BYGGET D-BLOKKA AS in july 2022
    with calculated peak cost, and check that the values are exactly equal"""
    invoiced_peak = 164.80
    invoiced_peak_tariff = 40.0
    expected_peak_cost = invoiced_peak * invoiced_peak_tariff

    assert len(calculated_grid_rental_large["peak_cost"]) == 1
    assert expected_peak_cost == calculated_grid_rental_large["peak_cost"][0]


def test_invoiced_energy_cost_large(calculated_grid_rental_large):
    """Compare invoiced energy cost for large consumer BI-BYGGET D-BLOKKA AS in july 2022
    with calculated energy cost, and check that it is within 1% of the expected value
    """
    # TODO : see if deviation can be reduced, possibly by fixing test_invoiced_total_consumption_large()
    invoiced_total_cons = 56928.0
    invoiced_energy_tariff = 0.06
    expected_energy_cost = invoiced_total_cons * invoiced_energy_tariff

    assert len(calculated_grid_rental_large["energy_cost"]) == 1
    deviation = (
        calculated_grid_rental_large["energy_cost"][0] / expected_energy_cost - 1
    )
    assert -0.01 < deviation < 0.01


def test_invoiced_fixed_cost_large(calculated_grid_rental_large):
    """Compare invoiced fixed cost for large consumer BI-BYGGET D-BLOKKA AS in july 2022
    with calculated fixed cost, and check that it is within 2% of the expected value
    
    Some deviation is expected since it's invoiced as a fixed monthly fee, but the calculator
    weights the fixed cost by the number of days in the month."""
    invoiced_fixed_tariff = 340

    assert len(calculated_grid_rental_large["fixed_cost"]) == 1
    deviation = (
        calculated_grid_rental_large["fixed_cost"][0] / invoiced_fixed_tariff
    ) - 1
    assert -0.02 < deviation < 0.02


@pytest.fixture
def invoiced_energy_price_small():
    """Invoiced energy price for small consumer BKOLON AS in july 2022"""
    invoiced_energy_price_small = [
        EnergyTariff(
            distributor_name="test",
            price_NOK_per_kWh=0.2351,
            start_time=datetime.datetime(2022, 7, 1),
            end_time=datetime.datetime(2022, 7, 31),
        )
    ]
    return invoiced_energy_price_small


@pytest.fixture
def invoiced_peak_price_small():
    """Invoiced peak price for small consumer BKOLON AS in july 2022"""
    invoiced_peak_price_small = [
        PeakTariffSmallConsumers(
            distributor_name="test",
            price_NOK=280.0,
            start_time=datetime.datetime(2022, 7, 1),
            end_time=datetime.datetime(2022, 7, 31),
            lower_limit=5,
            upper_limit=10,
        )
    ]
    return invoiced_peak_price_small


@pytest.fixture
def invoiced_enova_fee_small():
    """Invoiced enova fee for small consumer BKOLON AS in july 2022"""
    invoiced_enova_fee_small = [
        EnovaFee(
            price_NOK_per_year=799.976,
            start_time=datetime.datetime(2022, 7, 1),
            end_time=datetime.datetime(2022, 7, 31),
        )
    ]
    return invoiced_enova_fee_small


@pytest.fixture
def invoiced_el_fee_small():
    """Invoiced el-fee for small consumer BKOLON AS in july 2022"""
    invoiced_el_fee_small = [
        ElFeeTariff(
            distributor_name="test",
            price_NOK_per_kWh=0.1541,
            start_time=datetime.datetime(2022, 7, 1),
            end_time=datetime.datetime(2022, 7, 31),
        )
    ]
    return invoiced_el_fee_small


@pytest.fixture
def calculated_grid_rental_small(
    small_consumer_data_july_22,
    invoiced_energy_price_small,
    invoiced_peak_price_small,
    invoiced_enova_fee_small,
    invoiced_el_fee_small,
):
    """Calculate grid rental for small consumer with meter ID 707057500027547039

    Only tariffs appearing in the invoice are inputed, and the rest are set to empty lists.
    estimated_yearly_cons is set to 90000 kWh/year because it is below the limit for large consumers,
    and is not a real value."""
    calculated_grid_rental_small = calculate_grid_rental(
        small_consumer_data_july_22,
        True,
        90000,
        invoiced_energy_price_small,
        invoiced_enova_fee_small,
        [],
        [],
        invoiced_peak_price_small,
        invoiced_el_fee_small,
    )
    return calculated_grid_rental_small


def test_invoiced_total_consumption_small(calculated_grid_rental_small):
    """Compare invoiced total consumption for small consumer BKOLON AS in july 2022
    with calculated total consumption, and check that it is within 0.5% of the expected value
    """
    # TODO : see if deviation can be reduced, possibly a timezone issue
    invoiced_total_cons = 3047.84

    assert len(calculated_grid_rental_small["total_consumption"]) == 1
    deviation = (
        calculated_grid_rental_small["total_consumption"][0] / invoiced_total_cons - 1
    )
    assert -0.005 < deviation < 0.005


def test_invoiced_peak_cost_small(calculated_grid_rental_small):
    """Compare invoiced peak cost for small consumer BKOLON AS in july 2022
    with calculated peak cost, and check that the values are exactly equal"""
    invoiced_peak_tariff = 280.0

    assert len(calculated_grid_rental_small["peak_cost"]) == 1
    assert invoiced_peak_tariff == calculated_grid_rental_small["peak_cost"][0]


def test_invoiced_energy_cost_small(calculated_grid_rental_small):
    """Compare invoiced energy cost for small consumer BKOLON AS in july 2022
    with calculated energy cost, and check that it is within 1% of the expected value.

    Since day/night energy tariff is not implemented yet, the expected energy cost is calculated
    from the invoiced day price and applied to the entire consumption."""
    # TODO : see if deviation can be reduced, possibly by fixing test_invoiced_total_consumption_small()

    invoiced_total_cons = 3047.84
    invoiced_energy_tariff = 0.2351
    expected_energy_cost = invoiced_total_cons * invoiced_energy_tariff

    assert len(calculated_grid_rental_small["energy_cost"]) == 1
    deviation = (
        calculated_grid_rental_small["energy_cost"][0] / expected_energy_cost - 1
    )
    assert -0.01 < deviation < 0.01


def test_invoiced_enova_fee_small(calculated_grid_rental_small):
    """Compare invoiced enova fee for small consumer BKOLON AS in july 2022
    with calculated enova fee, and check that it is within 1% of the expected value"""

    invoiced_enova_fee = 799.976
    invoiced_fraction_of_year = 0.08494
    expected_enova_cost = invoiced_enova_fee * invoiced_fraction_of_year

    assert len(calculated_grid_rental_small["enova_fee"]) == 1
    deviation = calculated_grid_rental_small["enova_fee"][0] / expected_enova_cost - 1
    assert -0.005 < deviation < 0.005


@pytest.fixture
def constant_intra_month():
    dates = [
        datetime.datetime(2021, 12, 18),
        datetime.datetime(2021, 12, 15, 3),
        datetime.datetime(2021, 12, 21, 2),
        datetime.datetime(2020, 3, 12),
        datetime.datetime(2020, 3, 8, 0),
        datetime.datetime(2020, 3, 8, 1),
        datetime.datetime(2020, 3, 7, 0),
        datetime.datetime(2020, 3, 7, 13),
        datetime.datetime(2020, 3, 7, 23),
        datetime.datetime(2020, 3, 7, 20),
    ]
    vals = [
        2,
        4,
        9,
        8,
        9,
        7,
        13,
        11,
        6,
        10,
    ]  # expected peak values: (2+4+9)/3=5.0, (8+9+13)/3=10.0
    curve = list(zip(dates, vals))
    return curve


@pytest.fixture
def simple_price_data_small():
    peak_tariff_small_2020 = PeakTariffSmallConsumers(
        distributor_name="test",
        price_NOK=4,
        start_time=datetime.datetime(2020, 1, 1),
        end_time=datetime.datetime(2020, 12, 31),
        lower_limit=0,
        upper_limit=100,
    )
    peak_tariff_small_2021 = PeakTariffSmallConsumers(
        distributor_name="test",
        price_NOK=10,
        start_time=datetime.datetime(2021, 1, 1),
        end_time=datetime.datetime(2021, 12, 31),
        lower_limit=0,
        upper_limit=100,
    )
    return [peak_tariff_small_2020, peak_tariff_small_2021]


def test_peak_cost_small_consumer(constant_intra_month, simple_price_data_small):
    monthly_max_df = monthly_maximums(
        constant_intra_month, top_n_averaged=3, single_max_per_day=True
    )[["year", "month", "maximum", "total_consumption"]]
    monthly_max_df["peak_cost"] = _get_peak_tariff_small_consumers(
        monthly_max_df, simple_price_data_small
    )

    assert monthly_max_df["peak_cost"].iloc[0] == 4
    assert monthly_max_df["peak_cost"].iloc[1] == 10
