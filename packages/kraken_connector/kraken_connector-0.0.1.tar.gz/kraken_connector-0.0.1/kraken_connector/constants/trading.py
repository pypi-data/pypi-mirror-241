"""Constants related to Orders on the Kraken exchange."""
from enum import Enum


class ConditionalCloseOrderType(str, Enum):
    """Type of Order to place upon execution of the primary Order.

    Note:
        Conditional Close Orders are triggered by execution of the
        primary order in the same quantity and opposite direction,
        but once triggered are independent orders.
    """

    LIMIT = "limit"
    STOP_LOSS = "stop-loss"
    STOP_LOSS_LIMIT = "stop-loss-limit"
    TAKE_PROFIT = "take-profit"
    TAKE_PROFIT_LIMIT = "take-profit-limit"


class OrderStatus(str, Enum):
    """Status of an Order.

    Names:
        CANCELED: order canceled
        CLOSED: closed order
        EXPIRED: order expired
        OPEN: open order
        PENDING: order is pending book entry
    """

    CANCELED = "canceled"
    CLOSED = "closed"
    EXPIRED = "expired"
    OPEN = "open"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)


class OrderTrigger(str, Enum):
    """Price signal used to trigger conditional orders."""

    INDEX = "index"
    LAST = "last"

    def __str__(self) -> str:
        return str(self.value)


class OrderType(str, Enum):
    "Order type used to open a position."
    LIMIT = "limit"
    MARKET = "market"
    SETTLE_POSITION = "settle-position"
    STOP_LOSS = "stop-loss"
    STOP_LOSS_LIMIT = "stop-loss-limit"
    TAKE_PROFIT = "take-profit"
    TAKE_PROFIT_LIMIT = "take-profit-limit"

    def __str__(self) -> str:
        return str(self.value)


class SelfTradePreventionStrategy(str, Enum):
    """Strategy to apply to an Order to prevent self-trading.

    Self Trade Prevention (STP) is a mechanism employed by trading
    platforms to prevent users from inadvertently trading against
    themselves. This situation, known as self-trading, occurs when
    a user's own orders match each other on the order book.
    """

    CANCEL_BOTH = "cancel-both"
    CANCEL_NEWEST = "cancel-newest"
    CANCEL_OLDEST = "cancel-oldest"

    def __str__(self) -> str:
        return str(self.value)


class TimeInForce(str, Enum):
    """Time-in-force of the order.

    Specifies how long it should remain in the order book before being
    cancelled.

    Names:
        GTC: Good-'til-cancelled
        IOC: Immediate-or-cancel
        GTD: Good-'til-date.

    Note:
        If GTD is specified, must coincide with a desired `expiretm`.
    """

    GTC = "GTC"
    GTD = "GTD"
    IOC = "IOC"

    def __str__(self) -> str:
        return str(self.value)


class Trigger(str, Enum):
    """The price signal used to trigger a conditional order."""

    INDEX = "index"
    LAST = "last"

    def __str__(self) -> str:
        return str(self.value)


class TypeOrder(str, Enum):
    """The type of Order.

    This can also be thought of as the direction of the Order.
    """

    BUY = "buy"
    SELL = "sell"

    def __str__(self) -> str:
        return str(self.value)
