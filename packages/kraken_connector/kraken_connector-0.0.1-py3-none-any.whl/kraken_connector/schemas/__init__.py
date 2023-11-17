"""Contains all the data schemas used in requests and responses."""

from .account_balance import AccountBalance
from .account_transfer import (
    AccountTransferRequest,
    AccountTransferResponse,
    AccountTransferResult,
)
from .add_2 import Add2
from .add_2_order_added import Add2OrderAdded
from .add_2_order_added_descr import Add2OrderAddedDescr
from .add_export_data import AddExportData
from .add_export_response_200 import AddExportResponse200
from .add_export_response_200_result import AddExportResponse200Result
from .add_standard_order_request_body import AddStandardOrderRequestBody
from .addresses import Addresses
from .addresses_2 import Addresses2
from .allocate_strategy_json_body import AllocateStrategyJsonBody
from .allocate_strategy_json_body_nonce import AllocateStrategyJsonBodyNonce
from .allocate_strategy_response_200 import AllocateStrategyResponse200
from .asset_info import AssetInfo
from .asset_pair import AssetPair
from .asset_ticker_info import AssetTickerInfo
from .balance_2 import Balance2
from .balanceex_2 import Balanceex2
from .balanceex_2_extended_balance import Balanceex2ExtendedBalance
from .batch_cancel_open_orders_request_body import BatchCancelOpenOrdersRequestBody
from .batch_cancel_open_orders_request_body_orders_item import (
    BatchCancelOpenOrdersRequestBodyOrdersItem,
)
from .batchadd_2 import Batchadd2
from .batchadd_2_result import Batchadd2Result
from .batchadd_2_result_orders_item import Batchadd2ResultOrdersItem
from .batchadd_2_result_orders_item_descr import Batchadd2ResultOrdersItemDescr
from .cancel_all_orders_after_data import CancelAllOrdersAfterData
from .cancel_all_orders_after_response_200 import CancelAllOrdersAfterResponse200
from .cancel_all_orders_after_response_200_result import (
    CancelAllOrdersAfterResponse200Result,
)
from .cancel_all_orders_response_200 import CancelAllOrdersResponse200
from .cancel_all_orders_response_200_result import CancelAllOrdersResponse200Result
from .cancel_open_order_request_body import CancelOpenOrderRequestBody
from .cancel_withdrawal_response_200 import CancelWithdrawalResponse200
from .closed_2 import Closed2
from .closed_2_closed_orders import Closed2ClosedOrders
from .closed_2_closed_orders_closed import Closed2ClosedOrdersClosed
from .closed_order import ClosedOrder
from .create_subaccount_data import CreateSubaccountData
from .create_subaccount_response_200 import CreateSubaccountResponse200
from .deallocate_strategy_json_body import DeallocateStrategyJsonBody
from .deallocate_strategy_json_body_nonce import DeallocateStrategyJsonBodyNonce
from .deallocate_strategy_response_200 import DeallocateStrategyResponse200
from .deposit import Deposit
from .deposit_address import DepositAddress
from .deposit_method import DepositMethod
from .depth import Depth
from .depth_result import DepthResult
from .edit_2 import Edit2
from .edit_2_order_edited import Edit2OrderEdited
from .edit_2_order_edited_descr import Edit2OrderEditedDescr
from .edit_standard_order_request_body import EditStandardOrderRequestBody
from .export_status_data import ExportStatusData
from .export_status_response_200 import ExportStatusResponse200
from .export_status_response_200_result_item import ExportStatusResponse200ResultItem
from .extended_balance import ExtendedBalance
from .fee_tier_info import FeeTierInfo
from .get_allocate_strategy_status_json_body import GetAllocateStrategyStatusJsonBody
from .get_allocate_strategy_status_json_body_nonce import (
    GetAllocateStrategyStatusJsonBodyNonce,
)
from .get_allocate_strategy_status_response_200 import (
    GetAllocateStrategyStatusResponse200,
)
from .get_allocate_strategy_status_response_200_result import (
    GetAllocateStrategyStatusResponse200Result,
)
from .get_deallocate_strategy_status_json_body import (
    GetDeallocateStrategyStatusJsonBody,
)
from .get_deallocate_strategy_status_json_body_nonce import (
    GetDeallocateStrategyStatusJsonBodyNonce,
)
from .get_deallocate_strategy_status_response_200 import (
    GetDeallocateStrategyStatusResponse200,
)
from .get_deallocate_strategy_status_response_200_result import (
    GetDeallocateStrategyStatusResponse200Result,
)
from .get_desposit_methods_request_body import GetDespositMethodsRequestBody
from .get_open_positions_data import GetOpenPositionsData
from .get_open_positions_response_200 import GetOpenPositionsResponse200
from .get_open_positions_response_200_result import GetOpenPositionsResponse200Result
from .get_open_positions_response_200_result_additional_property import (
    GetOpenPositionsResponse200ResultAdditionalProperty,
)
from .get_status_of_recent_deposits_request_body import (
    GetStatusOfRecentDepositsRequestBody,
)
from .get_status_of_recent_withdrawals_request_body import (
    GetStatusOfRecentWithdrawalsRequestBody,
)
from .get_system_status_response_200 import GetSystemStatusResponse200
from .get_system_status_response_200_result import GetSystemStatusResponse200Result
from .get_tradable_asset_pairs_response_200 import GetTradableAssetPairsResponse200
from .get_tradable_asset_pairs_response_200_result import (
    GetTradableAssetPairsResponse200Result,
)
from .get_trades_info_response_200 import GetTradesInfoResponse200
from .get_trades_info_response_200_result import GetTradesInfoResponse200Result
from .get_websockets_token_response_200 import GetWebsocketsTokenResponse200
from .get_websockets_token_response_200_result import (
    GetWebsocketsTokenResponse200Result,
)
from .history_2 import History2
from .info_2 import Info2
from .info_2_result import Info2Result
from .info_3 import Info3
from .info_3_ledgers_info import Info3LedgersInfo
from .info_3_ledgers_info_ledger import Info3LedgersInfoLedger
from .info_4 import Info4
from .info_5 import Info5
from .info_5_withdrawal_info import Info5WithdrawalInfo
from .ledger_entry import LedgerEntry
from .list_allocations_json_body import ListAllocationsJsonBody
from .list_allocations_json_body_nonce import ListAllocationsJsonBodyNonce
from .list_allocations_response_200 import ListAllocationsResponse200
from .list_allocations_response_200_result import ListAllocationsResponse200Result
from .list_allocations_response_200_result_items_item import (
    ListAllocationsResponse200ResultItemsItem,
)
from .list_allocations_response_200_result_items_item_amount_allocated import (
    ListAllocationsResponse200ResultItemsItemAmountAllocated,
)
from .list_allocations_response_200_result_items_item_amount_allocated_bonding import (
    ListAllocationsResponse200ResultItemsItemAmountAllocatedBonding,
)
from .list_allocations_response_200_result_items_item_amount_allocated_bonding_allocations_item import (
    ListAllocationsResponse200ResultItemsItemAmountAllocatedBondingAllocationsItem,
)
from .list_allocations_response_200_result_items_item_amount_allocated_exit_queue import (
    ListAllocationsResponse200ResultItemsItemAmountAllocatedExitQueue,
)
from .list_allocations_response_200_result_items_item_amount_allocated_exit_queue_allocations_item import (
    ListAllocationsResponse200ResultItemsItemAmountAllocatedExitQueueAllocationsItem,
)
from .list_allocations_response_200_result_items_item_amount_allocated_pending import (
    ListAllocationsResponse200ResultItemsItemAmountAllocatedPending,
)
from .list_allocations_response_200_result_items_item_amount_allocated_total import (
    ListAllocationsResponse200ResultItemsItemAmountAllocatedTotal,
)
from .list_allocations_response_200_result_items_item_amount_allocated_unbonding import (
    ListAllocationsResponse200ResultItemsItemAmountAllocatedUnbonding,
)
from .list_allocations_response_200_result_items_item_amount_allocated_unbonding_allocations_item import (
    ListAllocationsResponse200ResultItemsItemAmountAllocatedUnbondingAllocationsItem,
)
from .list_allocations_response_200_result_items_item_payout import (
    ListAllocationsResponse200ResultItemsItemPayout,
)
from .list_allocations_response_200_result_items_item_payout_accumulated_reward import (
    ListAllocationsResponse200ResultItemsItemPayoutAccumulatedReward,
)
from .list_allocations_response_200_result_items_item_payout_estimated_reward import (
    ListAllocationsResponse200ResultItemsItemPayoutEstimatedReward,
)
from .list_allocations_response_200_result_items_item_total_rewarded import (
    ListAllocationsResponse200ResultItemsItemTotalRewarded,
)
from .list_strategies_json_body import ListStrategiesJsonBody
from .list_strategies_json_body_nonce import ListStrategiesJsonBodyNonce
from .list_strategies_response_200 import ListStrategiesResponse200
from .list_strategies_response_200_result import ListStrategiesResponse200Result
from .list_strategies_response_200_result_items_item import (
    ListStrategiesResponse200ResultItemsItem,
)
from .list_strategies_response_200_result_items_item_apr_estimate import (
    ListStrategiesResponse200ResultItemsItemAprEstimate,
)
from .list_strategies_response_200_result_items_item_auto_compound_type_0 import (
    ListStrategiesResponse200ResultItemsItemAutoCompoundType0,
)
from .list_strategies_response_200_result_items_item_auto_compound_type_1 import (
    ListStrategiesResponse200ResultItemsItemAutoCompoundType1,
)
from .list_strategies_response_200_result_items_item_auto_compound_type_2 import (
    ListStrategiesResponse200ResultItemsItemAutoCompoundType2,
)
from .list_strategies_response_200_result_items_item_lock_type_type_0 import (
    ListStrategiesResponse200ResultItemsItemLockTypeType0,
)
from .list_strategies_response_200_result_items_item_lock_type_type_1 import (
    ListStrategiesResponse200ResultItemsItemLockTypeType1,
)
from .list_strategies_response_200_result_items_item_lock_type_type_2 import (
    ListStrategiesResponse200ResultItemsItemLockTypeType2,
)
from .list_strategies_response_200_result_items_item_lock_type_type_3 import (
    ListStrategiesResponse200ResultItemsItemLockTypeType3,
)
from .list_strategies_response_200_result_items_item_yield_source_type_0 import (
    ListStrategiesResponse200ResultItemsItemYieldSourceType0,
)
from .list_strategies_response_200_result_items_item_yield_source_type_1 import (
    ListStrategiesResponse200ResultItemsItemYieldSourceType1,
)
from .lock import Lock
from .methods_2 import Methods2
from .ohlc import Ohlc
from .ohlc_result import OhlcResult
from .open_2 import Open2
from .open_2_open_orders import Open2OpenOrders
from .open_2_open_orders_open import Open2OpenOrdersOpen
from .open_order import OpenOrder
from .open_order_order_description import OpenOrderOrderDescription
from .order_book import OrderBook
from .query_2 import Query2
from .query_2_result import Query2Result
from .query_3 import Query3
from .query_3_result import Query3Result
from .query_orders_info_request_body import QueryOrdersInfoRequestBody
from .recent_2 import Recent2
from .recent_2_result_type_1 import Recent2ResultType1
from .remove_export_data import RemoveExportData
from .remove_export_response_200 import RemoveExportResponse200
from .remove_export_response_200_result import RemoveExportResponse200Result
from .request_withdrawal_cancelation_request_body import (
    RequestWithdrawalCancelationRequestBody,
)
from .retrieve_export_data import RetrieveExportData
from .retrieve_export_response_200 import RetrieveExportResponse200
from .spread_2 import Spread2
from .spread_2_result import Spread2Result
from .ticker_2 import Ticker2
from .ticker_2_result import Ticker2Result
from .time import Time
from .time_server_time import TimeServerTime
from .trade import Trade
from .trade_history import TradeHistory
from .trade_history_trades import TradeHistoryTrades
from .trades import Trades
from .trades_result import TradesResult
from .volume import Volume
from .volume_trade_volume import VolumeTradeVolume
from .volume_trade_volume_fees import VolumeTradeVolumeFees
from .volume_trade_volume_fees_maker import VolumeTradeVolumeFeesMaker
from .wallet_transfer_data import WalletTransferData
from .wallet_transfer_response_200 import WalletTransferResponse200
from .wallet_transfer_response_200_result import WalletTransferResponse200Result
from .withdrawal import Withdrawal
from .withdrawal_2 import Withdrawal2
from .withdrawal_2_result import Withdrawal2Result

__all__ = (
    "AccountBalance",
    "AccountTransferRequest",
    "AccountTransferResponse",
    "AccountTransferResult",
    "Add2",
    "Add2OrderAdded",
    "Add2OrderAddedDescr",
    "AddExportData",
    "AddExportResponse200",
    "AddExportResponse200Result",
    "Addresses",
    "Addresses2",
    "AddStandardOrderRequestBody",
    "AllocateStrategyJsonBody",
    "AllocateStrategyJsonBodyNonce",
    "AllocateStrategyResponse200",
    "AssetInfo",
    "AssetPair",
    "AssetTickerInfo",
    "Balance2",
    "Balanceex2",
    "Balanceex2ExtendedBalance",
    "Batchadd2",
    "Batchadd2Result",
    "Batchadd2ResultOrdersItem",
    "Batchadd2ResultOrdersItemDescr",
    "BatchCancelOpenOrdersRequestBody",
    "BatchCancelOpenOrdersRequestBodyOrdersItem",
    "CancelAllOrdersAfterData",
    "CancelAllOrdersAfterResponse200",
    "CancelAllOrdersAfterResponse200Result",
    "CancelAllOrdersResponse200",
    "CancelAllOrdersResponse200Result",
    "CancelOpenOrderRequestBody",
    "CancelWithdrawalResponse200",
    "Closed2",
    "Closed2ClosedOrders",
    "Closed2ClosedOrdersClosed",
    "ClosedOrder",
    "CreateSubaccountData",
    "CreateSubaccountResponse200",
    "DeallocateStrategyJsonBody",
    "DeallocateStrategyJsonBodyNonce",
    "DeallocateStrategyResponse200",
    "Deposit",
    "DepositAddress",
    "DepositMethod",
    "Depth",
    "DepthResult",
    "Edit2",
    "Edit2OrderEdited",
    "Edit2OrderEditedDescr",
    "EditStandardOrderRequestBody",
    "ExportStatusData",
    "ExportStatusResponse200",
    "ExportStatusResponse200ResultItem",
    "ExtendedBalance",
    "FeeTierInfo",
    "GetAllocateStrategyStatusJsonBody",
    "GetAllocateStrategyStatusJsonBodyNonce",
    "GetAllocateStrategyStatusResponse200",
    "GetAllocateStrategyStatusResponse200Result",
    "GetDeallocateStrategyStatusJsonBody",
    "GetDeallocateStrategyStatusJsonBodyNonce",
    "GetDeallocateStrategyStatusResponse200",
    "GetDeallocateStrategyStatusResponse200Result",
    "GetDespositMethodsRequestBody",
    "GetOpenPositionsData",
    "GetOpenPositionsResponse200",
    "GetOpenPositionsResponse200Result",
    "GetOpenPositionsResponse200ResultAdditionalProperty",
    "GetStatusOfRecentDepositsRequestBody",
    "GetStatusOfRecentWithdrawalsRequestBody",
    "GetSystemStatusResponse200",
    "GetSystemStatusResponse200Result",
    "GetTradableAssetPairsResponse200",
    "GetTradableAssetPairsResponse200Result",
    "GetTradesInfoResponse200",
    "GetTradesInfoResponse200Result",
    "GetWebsocketsTokenResponse200",
    "GetWebsocketsTokenResponse200Result",
    "History2",
    "Info2",
    "Info2Result",
    "Info3",
    "Info3LedgersInfo",
    "Info3LedgersInfoLedger",
    "Info4",
    "Info5",
    "Info5WithdrawalInfo",
    "LedgerEntry",
    "ListAllocationsJsonBody",
    "ListAllocationsJsonBodyNonce",
    "ListAllocationsResponse200",
    "ListAllocationsResponse200Result",
    "ListAllocationsResponse200ResultItemsItem",
    "ListAllocationsResponse200ResultItemsItemAmountAllocated",
    "ListAllocationsResponse200ResultItemsItemAmountAllocatedBonding",
    "ListAllocationsResponse200ResultItemsItemAmountAllocatedBondingAllocationsItem",
    "ListAllocationsResponse200ResultItemsItemAmountAllocatedExitQueue",
    "ListAllocationsResponse200ResultItemsItemAmountAllocatedExitQueueAllocationsItem",
    "ListAllocationsResponse200ResultItemsItemAmountAllocatedPending",
    "ListAllocationsResponse200ResultItemsItemAmountAllocatedTotal",
    "ListAllocationsResponse200ResultItemsItemAmountAllocatedUnbonding",
    "ListAllocationsResponse200ResultItemsItemAmountAllocatedUnbondingAllocationsItem",
    "ListAllocationsResponse200ResultItemsItemPayout",
    "ListAllocationsResponse200ResultItemsItemPayoutAccumulatedReward",
    "ListAllocationsResponse200ResultItemsItemPayoutEstimatedReward",
    "ListAllocationsResponse200ResultItemsItemTotalRewarded",
    "ListStrategiesJsonBody",
    "ListStrategiesJsonBodyNonce",
    "ListStrategiesResponse200",
    "ListStrategiesResponse200Result",
    "ListStrategiesResponse200ResultItemsItem",
    "ListStrategiesResponse200ResultItemsItemAprEstimate",
    "ListStrategiesResponse200ResultItemsItemAutoCompoundType0",
    "ListStrategiesResponse200ResultItemsItemAutoCompoundType1",
    "ListStrategiesResponse200ResultItemsItemAutoCompoundType2",
    "ListStrategiesResponse200ResultItemsItemLockTypeType0",
    "ListStrategiesResponse200ResultItemsItemLockTypeType1",
    "ListStrategiesResponse200ResultItemsItemLockTypeType2",
    "ListStrategiesResponse200ResultItemsItemLockTypeType3",
    "ListStrategiesResponse200ResultItemsItemYieldSourceType0",
    "ListStrategiesResponse200ResultItemsItemYieldSourceType1",
    "Lock",
    "Methods2",
    "Ohlc",
    "OhlcResult",
    "Open2",
    "Open2OpenOrders",
    "Open2OpenOrdersOpen",
    "OpenOrder",
    "OpenOrderOrderDescription",
    "OrderBook",
    "Ordertype",
    "Query2",
    "Query2Result",
    "Query3",
    "Query3Result",
    "QueryOrdersInfoRequestBody",
    "Recent2",
    "Recent2ResultType1",
    "RemoveExportData",
    "RemoveExportResponse200",
    "RemoveExportResponse200Result",
    "RequestWithdrawalCancelationRequestBody",
    "RetrieveExportData",
    "RetrieveExportResponse200",
    "Spread2",
    "Spread2Result",
    "Ticker2",
    "Ticker2Result",
    "Time",
    "TimeServerTime",
    "Trade",
    "TradeHistory",
    "TradeHistoryTrades",
    "Trades",
    "TradesResult",
    "Volume",
    "VolumeTradeVolume",
    "VolumeTradeVolumeFees",
    "VolumeTradeVolumeFeesMaker",
    "WalletTransferData",
    "WalletTransferResponse200",
    "WalletTransferResponse200Result",
    "Withdrawal",
    "Withdrawal2",
    "Withdrawal2Result",
)
