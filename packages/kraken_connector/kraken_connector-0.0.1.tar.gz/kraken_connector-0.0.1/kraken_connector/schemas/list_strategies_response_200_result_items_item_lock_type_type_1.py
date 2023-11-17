from typing import Any, Dict, List, Self, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..constants.earn import (
    StrategyLockType,
)
from ..types import UNSET, Unset


@_attrs_define
class ListStrategiesResponse200ResultItemsItemLockTypeType1:
    """Explicit allocate and deallocate action by user is required and bonding/unbonding parameters apply.

    Attributes:
        bonding_period (int): Duration of the bonding period, in seconds
        bonding_rewards (bool): Whether rewards are earned during the bonding period (payouts occur after bonding is
            complete)
        exit_queue_period (int): In order to remove funds, if this value is greater than 0, funds will first have to
            enter an exit queue and will have to wait for the exit queue period to end. Once ended, her funds will then
            follow and respect the `unbonding_period`.

            If the value of the exit queue period is 0, then no waiting will have to occur and the exit queue will be
            skipped

            Rewards are always paid out for the exit queue
        payout_frequency (int): At what intervals are rewards distributed and credited to the user`s ledger, in seconds
        type (StrategyLockType.BONDED):
        unbonding_period (int): Duration of the unbonding period in seconds. In order to remove funds, you must wait for
            the unbonding period to pass after requesting removal before funds become available in her spot wallet
        unbonding_rewards (bool): Whether rewards are earned and payouts are done during the unbonding period
        bonding_period_variable (Union[Unset, bool]): Is the bonding period length variable (`true`) or static (`false`;
            default)
        unbonding_period_variable (Union[Unset, bool]): Is the unbonding period length variable (`true`) or static
            (`false`; default)
    """

    bonding_period: int
    bonding_rewards: bool
    exit_queue_period: int
    payout_frequency: int
    type: StrategyLockType.BONDED
    unbonding_period: int
    unbonding_rewards: bool
    bonding_period_variable: Union[Unset, bool] = False
    unbonding_period_variable: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bonding_period = self.bonding_period
        bonding_rewards = self.bonding_rewards
        exit_queue_period = self.exit_queue_period
        payout_frequency = self.payout_frequency
        type = self.type.value

        unbonding_period = self.unbonding_period
        unbonding_rewards = self.unbonding_rewards
        bonding_period_variable = self.bonding_period_variable
        unbonding_period_variable = self.unbonding_period_variable

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bonding_period": bonding_period,
                "bonding_rewards": bonding_rewards,
                "exit_queue_period": exit_queue_period,
                "payout_frequency": payout_frequency,
                "type": type,
                "unbonding_period": unbonding_period,
                "unbonding_rewards": unbonding_rewards,
            }
        )
        if bonding_period_variable is not UNSET:
            field_dict["bonding_period_variable"] = bonding_period_variable
        if unbonding_period_variable is not UNSET:
            field_dict["unbonding_period_variable"] = unbonding_period_variable

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        d = src_dict.copy()
        bonding_period = d.pop("bonding_period")

        bonding_rewards = d.pop("bonding_rewards")

        exit_queue_period = d.pop("exit_queue_period")

        payout_frequency = d.pop("payout_frequency")

        type = StrategyLockType(d.pop("type"))

        unbonding_period = d.pop("unbonding_period")

        unbonding_rewards = d.pop("unbonding_rewards")

        bonding_period_variable = d.pop("bonding_period_variable", UNSET)

        unbonding_period_variable = d.pop("unbonding_period_variable", UNSET)

        list_strategies_response_200_result_items_item_lock_type_type_1 = cls(
            bonding_period=bonding_period,
            bonding_rewards=bonding_rewards,
            exit_queue_period=exit_queue_period,
            payout_frequency=payout_frequency,
            type=type,
            unbonding_period=unbonding_period,
            unbonding_rewards=unbonding_rewards,
            bonding_period_variable=bonding_period_variable,
            unbonding_period_variable=unbonding_period_variable,
        )

        list_strategies_response_200_result_items_item_lock_type_type_1.additional_properties = (
            d
        )
        return list_strategies_response_200_result_items_item_lock_type_type_1

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
