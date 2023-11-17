"""Constant values related to Kraken API Funding endpoints."""
from enum import Enum


class DepositStatus(str, Enum):
    """Additional status properties of a deposit."""

    ONHOLD = "onhold"
    RETURN = "return"

    def __str__(self) -> str:
        return str(self.value)


class TypeWallet(str, Enum):
    """Type of Kraken Wallet."""

    FUTURES_WALLET = "Futures Wallet"
    SPOT_WALLET = "Spot Wallet"

    def __str__(self) -> str:
        return str(self.value)
