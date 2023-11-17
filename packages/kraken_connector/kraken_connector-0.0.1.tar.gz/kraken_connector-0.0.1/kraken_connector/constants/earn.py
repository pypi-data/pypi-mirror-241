"""Constants related to the Earn endpoints on Kraken API."""
from enum import Enum


class AllocationRestrictionInfo(str, Enum):
    """Alleged 'Items value' value in Kraken Docs.

    This is found in the `/private/Earn/Strategies/` documentation
    and is alleged to be the "items value" value on the `allocation_restriction_info`
    key; however, the key's description also states that it is an array of strings,
    that comprise the "Reason list why user is not eligible for allocating to the
    strategey".  In other words, there appears to be inconsistency in this
    endpoints documentation and descriptions.

    Warning:
        This class is dubious as the docs for the section appear to be inconsistent.
    """

    TIER = "tier"

    def __str__(self) -> str:
        return str(self.value)


class AutoCompoundType(str, Enum):
    """Options for Earn strategies.

    Names:
        DISABLED: "disabled"
        ENABLED: "enabled"
        OPTIONAL: "optional"
    """

    DISABLED = "disabled"
    ENABLED = "enabled"
    OPTIONAL = "optional"

    def __str__(self) -> str:
        return str(self.value)


class StrategyLockType(str, Enum):
    """Lock types for strategies that can be used to filter."""

    BONDED = "bonded"
    FLEX = "flex"
    INSTANT = "instant"
    TIMED = "timed"

    def __str__(self) -> str:
        return str(self.value)


class YieldSourceType(str, Enum):
    """Type of yield source for an Earn strategy."""

    OFF_CHAIN = "off_chain"
    STAKING = "staking"

    def __str__(self) -> str:
        return str(self.value)
