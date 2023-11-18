from dataclasses import dataclass
import datetime

@dataclass
class AmsMeter:
    """Class to create meter objects"""

    identification: str
    distributor_name: str
    estimated_yearly_cons: float


@dataclass
class PeakTariffLargeConsumers:
    """ Class to create peak tariff objects for large consumers (above 100 MWh/year)
    Effektledd in norwegian.
    """

    distributor_name: str
    price_NOK_per_kWh: float
    start_time: datetime.datetime
    end_time: datetime.datetime


@dataclass
class PeakTariffSmallConsumers:
    """ Class to create peak tariff objects for small consumers (below 100 MWh/year)
    Fastledd/kapasitetsledd in norwegian.
    """

    distributor_name: str
    price_NOK: float
    start_time: datetime.datetime
    end_time: datetime.datetime
    lower_limit: float
    upper_limit: float


@dataclass
class EnergyTariff:
    """ Class to create energy tariff objects
    Energiledd in norwegian.
    """

    distributor_name: str
    price_NOK_per_kWh: float
    start_time: datetime.datetime   # TODO: implement day/night tariff
    end_time: datetime.datetime


@dataclass
class ElFeeTariff:
    """ Class to create el-fee tariff objects
    Forbruksavgift/el-avgift in norwegian."""

    distributor_name: str
    price_NOK_per_kWh: float
    start_time: datetime.datetime
    end_time: datetime.datetime


@dataclass
class FixedTariff:
    """ Class to create objects for fixed yearly fees"""

    distributor_name: str
    price_NOK_per_year: float
    start_time: datetime.datetime
    end_time: datetime.datetime


@dataclass
class EnovaFee:
    """ Class to create objects for the Enova fee"""

    price_NOK_per_year: float
    start_time: datetime.datetime
    end_time: datetime.datetime