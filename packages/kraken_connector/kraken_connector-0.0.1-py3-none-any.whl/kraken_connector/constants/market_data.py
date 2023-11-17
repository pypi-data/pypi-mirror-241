"""Constants related to Market Data public endpoints in Kraken API."""
from enum import Enum, IntEnum


class OHLCDataInterval(IntEnum):
    """The interval at which to compose OHLC data."""

    ONE_MINUTE = 1
    FIVE_MINUTES = 5
    FIFTEEN_MINUTES = 15
    THIRTY_MINUTES = 30
    ONE_HOUR = 60
    FOUR_HOURS = 240
    ONE_DAY = 1440
    SEVEN_DAYS = 10080
    FIFTEEN_DAYS = 21600

    ONE_WEEK = 10080

    def __str__(self) -> str:
        return str(self.value)


class SystemStatus(str, Enum):
    """Status of the Kraken API Exchange."""

    CANCEL_ONLY = "cancel_only"
    MAINTENANCE = "maintenance"
    ONLINE = "online"
    POST_ONLY = "post_only"

    def __str__(self) -> str:
        return str(self.value)


class TradableAssetPairInfo(str, Enum):
    """Type of Information available for a Tradable Asset Pair.

    Names:
        FEES: Fee information related to an asset pair.
        INFO: All available information options related to an
            asset pair.
        LEVERAGE: Leverage information related to an asset pair.
        MARGIN: Margin information related to an asset pair.
    """

    FEES = "fees"
    INFO = "info"
    LEVERAGE = "leverage"
    MARGIN = "margin"

    def __str__(self) -> str:
        return str(self.value)
