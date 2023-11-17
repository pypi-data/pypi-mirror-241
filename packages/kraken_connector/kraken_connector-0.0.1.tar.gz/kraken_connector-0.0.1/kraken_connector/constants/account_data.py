"""Constants related to Account Data API endpoints."""

from enum import Enum


class TypeDeleteReportRequest(str, Enum):
    """Type of Request made to delete a Report.

    Note:
        DELETE can only be used for reports that have been processed.
        Use CANCEL for report requests that are queued or processing.
    """

    CANCEL = "cancel"
    DELETE = "delete"

    def __str__(self) -> str:
        return str(self.value)


class LedgerEntryType(str, Enum):
    ADJUSTMENT = "adjustment"
    DEPOSIT = "deposit"
    MARGIN = "margin"
    RECEIVE = "receive"
    ROLLOVER = "rollover"
    SETTLED = "settled"
    SPEND = "spend"
    TRADE = "trade"
    TRANSFER = "transfer"
    WITHDRAWAL = "withdrawal"

    def __str__(self) -> str:
        return str(self.value)


class PositionStatus(str, Enum):
    """The status of a position taken by Trader."""

    OPEN = "open"
    CLOSED = "closed"

    def __str__(self) -> str:
        return str(self.value)


class OpenPositionsDataConsolidation(str, Enum):
    """Indicator to consolidate data by market/pair."""

    MARKET = "market"

    def __str__(self) -> str:
        return str(self.value)


class ReportFileFormat(str, Enum):
    """The file format into which the data will be exported."""

    CSV = "CSV"
    TSV = "TSV"

    def __str__(self) -> str:
        return str(self.value)


class ReportRequestStatus(str, Enum):
    """The status of a requested Report for exporting."""

    PROCESSED = "Processed"
    PROCESSING = "Processing"
    QUEUED = "Queued"

    def __str__(self) -> str:
        return str(self.value)


class ReportType(str, Enum):
    """The type of data to export."""

    LEDGERS = "ledgers"
    TRADES = "trades"

    def __str__(self) -> str:
        return str(self.value)
