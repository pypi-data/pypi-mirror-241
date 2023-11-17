from typing import TYPE_CHECKING, Any, Dict, List, Self, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..constants.earn import (
    AllocationRestrictionInfo,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..schemas.list_strategies_response_200_result_items_item_apr_estimate import (
        ListStrategiesResponse200ResultItemsItemAprEstimate,
    )
    from ..schemas.list_strategies_response_200_result_items_item_auto_compound_type_0 import (
        ListStrategiesResponse200ResultItemsItemAutoCompoundType0,
    )
    from ..schemas.list_strategies_response_200_result_items_item_auto_compound_type_1 import (
        ListStrategiesResponse200ResultItemsItemAutoCompoundType1,
    )
    from ..schemas.list_strategies_response_200_result_items_item_auto_compound_type_2 import (
        ListStrategiesResponse200ResultItemsItemAutoCompoundType2,
    )
    from ..schemas.list_strategies_response_200_result_items_item_lock_type_type_0 import (
        ListStrategiesResponse200ResultItemsItemLockTypeType0,
    )
    from ..schemas.list_strategies_response_200_result_items_item_lock_type_type_1 import (
        ListStrategiesResponse200ResultItemsItemLockTypeType1,
    )
    from ..schemas.list_strategies_response_200_result_items_item_lock_type_type_2 import (
        ListStrategiesResponse200ResultItemsItemLockTypeType2,
    )
    from ..schemas.list_strategies_response_200_result_items_item_lock_type_type_3 import (
        ListStrategiesResponse200ResultItemsItemLockTypeType3,
    )
    from ..schemas.list_strategies_response_200_result_items_item_yield_source_type_0 import (
        ListStrategiesResponse200ResultItemsItemYieldSourceType0,
    )
    from ..schemas.list_strategies_response_200_result_items_item_yield_source_type_1 import (
        ListStrategiesResponse200ResultItemsItemYieldSourceType1,
    )


@_attrs_define
class ListStrategiesResponse200ResultItemsItem:
    """Parameters for a single strategy

    Attributes:
        allocation_fee (Union[float, int, str]): Fee applied when allocating to this strategy
        allocation_restriction_info (List[AllocationRestrictionInfo]):
            Reason list why user is not eligible for allocating to the strategy
        asset (str): The asset to invest for this earn strategy
        auto_compound (Union['ListStrategiesResponse200ResultItemsItemAutoCompoundType0',
            'ListStrategiesResponse200ResultItemsItemAutoCompoundType1',
            'ListStrategiesResponse200ResultItemsItemAutoCompoundType2']): Auto compound choices for the earn strategy
        can_allocate (bool): Is allocation available for this strategy
        can_deallocate (bool): Is deallocation available for this strategy
        deallocation_fee (Union[float, int, str]): Fee applied when deallocating from this strategy
        id (str): The unique identifier for this strategy
        lock_type (Union['ListStrategiesResponse200ResultItemsItemLockTypeType0',
            'ListStrategiesResponse200ResultItemsItemLockTypeType1',
            'ListStrategiesResponse200ResultItemsItemLockTypeType2',
            'ListStrategiesResponse200ResultItemsItemLockTypeType3']): Type of the strategy
        yield_source (Union['ListStrategiesResponse200ResultItemsItemYieldSourceType0',
            'ListStrategiesResponse200ResultItemsItemYieldSourceType1']): Yield generation mechanism of this strategy
        apr_estimate (Union[Unset, None, ListStrategiesResponse200ResultItemsItemAprEstimate]): The estimate is based on
            previous revenues from the strategy.
        user_cap (Union[Unset, None, str]): The maximum amount of funds that any given user may allocate to an account.
            Absence of value means there is no limit. Zero means that all new allocations will return an error (though auto-
            compound is unaffected).
        user_min_allocation (Union[Unset, None, str]): Minimum amount (in USD) for an allocation or deallocation
    """

    allocation_fee: Union[float, int, str]
    allocation_restriction_info: List[AllocationRestrictionInfo]
    asset: str
    auto_compound: Union[
        "ListStrategiesResponse200ResultItemsItemAutoCompoundType0",
        "ListStrategiesResponse200ResultItemsItemAutoCompoundType1",
        "ListStrategiesResponse200ResultItemsItemAutoCompoundType2",
    ]
    can_allocate: bool
    can_deallocate: bool
    deallocation_fee: Union[float, int, str]
    id: str
    lock_type: Union[
        "ListStrategiesResponse200ResultItemsItemLockTypeType0",
        "ListStrategiesResponse200ResultItemsItemLockTypeType1",
        "ListStrategiesResponse200ResultItemsItemLockTypeType2",
        "ListStrategiesResponse200ResultItemsItemLockTypeType3",
    ]
    yield_source: Union[
        "ListStrategiesResponse200ResultItemsItemYieldSourceType0",
        "ListStrategiesResponse200ResultItemsItemYieldSourceType1",
    ]
    apr_estimate: Union[
        Unset, None, "ListStrategiesResponse200ResultItemsItemAprEstimate"
    ] = UNSET
    user_cap: Union[Unset, None, str] = UNSET
    user_min_allocation: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..schemas.list_strategies_response_200_result_items_item_auto_compound_type_0 import (
            ListStrategiesResponse200ResultItemsItemAutoCompoundType0,
        )
        from ..schemas.list_strategies_response_200_result_items_item_auto_compound_type_1 import (
            ListStrategiesResponse200ResultItemsItemAutoCompoundType1,
        )
        from ..schemas.list_strategies_response_200_result_items_item_lock_type_type_0 import (
            ListStrategiesResponse200ResultItemsItemLockTypeType0,
        )
        from ..schemas.list_strategies_response_200_result_items_item_lock_type_type_1 import (
            ListStrategiesResponse200ResultItemsItemLockTypeType1,
        )
        from ..schemas.list_strategies_response_200_result_items_item_lock_type_type_2 import (
            ListStrategiesResponse200ResultItemsItemLockTypeType2,
        )
        from ..schemas.list_strategies_response_200_result_items_item_yield_source_type_0 import (
            ListStrategiesResponse200ResultItemsItemYieldSourceType0,
        )

        allocation_fee: Union[float, int, str]

        allocation_fee = self.allocation_fee

        allocation_restriction_info = []
        for allocation_restriction_info_item_data in self.allocation_restriction_info:
            allocation_restriction_info_item = (
                allocation_restriction_info_item_data.value
            )

            allocation_restriction_info.append(allocation_restriction_info_item)

        asset = self.asset
        auto_compound: Dict[str, Any]

        if isinstance(
            self.auto_compound,
            ListStrategiesResponse200ResultItemsItemAutoCompoundType0,
        ):
            auto_compound = self.auto_compound.to_dict()

        elif isinstance(
            self.auto_compound,
            ListStrategiesResponse200ResultItemsItemAutoCompoundType1,
        ):
            auto_compound = self.auto_compound.to_dict()

        else:
            auto_compound = self.auto_compound.to_dict()

        can_allocate = self.can_allocate
        can_deallocate = self.can_deallocate
        deallocation_fee: Union[float, int, str]

        deallocation_fee = self.deallocation_fee

        id = self.id
        lock_type: Dict[str, Any]

        if isinstance(
            self.lock_type, ListStrategiesResponse200ResultItemsItemLockTypeType0
        ):
            lock_type = self.lock_type.to_dict()

        elif isinstance(
            self.lock_type, ListStrategiesResponse200ResultItemsItemLockTypeType1
        ):
            lock_type = self.lock_type.to_dict()

        elif isinstance(
            self.lock_type, ListStrategiesResponse200ResultItemsItemLockTypeType2
        ):
            lock_type = self.lock_type.to_dict()

        else:
            lock_type = self.lock_type.to_dict()

        yield_source: Dict[str, Any]

        if isinstance(
            self.yield_source, ListStrategiesResponse200ResultItemsItemYieldSourceType0
        ):
            yield_source = self.yield_source.to_dict()

        else:
            yield_source = self.yield_source.to_dict()

        apr_estimate: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.apr_estimate, Unset):
            apr_estimate = self.apr_estimate.to_dict() if self.apr_estimate else None

        user_cap = self.user_cap
        user_min_allocation = self.user_min_allocation

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allocation_fee": allocation_fee,
                "allocation_restriction_info": allocation_restriction_info,
                "asset": asset,
                "auto_compound": auto_compound,
                "can_allocate": can_allocate,
                "can_deallocate": can_deallocate,
                "deallocation_fee": deallocation_fee,
                "id": id,
                "lock_type": lock_type,
                "yield_source": yield_source,
            }
        )
        if apr_estimate is not UNSET:
            field_dict["apr_estimate"] = apr_estimate
        if user_cap is not UNSET:
            field_dict["user_cap"] = user_cap
        if user_min_allocation is not UNSET:
            field_dict["user_min_allocation"] = user_min_allocation

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        from ..schemas.list_strategies_response_200_result_items_item_apr_estimate import (
            ListStrategiesResponse200ResultItemsItemAprEstimate,
        )
        from ..schemas.list_strategies_response_200_result_items_item_auto_compound_type_0 import (
            ListStrategiesResponse200ResultItemsItemAutoCompoundType0,
        )
        from ..schemas.list_strategies_response_200_result_items_item_auto_compound_type_1 import (
            ListStrategiesResponse200ResultItemsItemAutoCompoundType1,
        )
        from ..schemas.list_strategies_response_200_result_items_item_auto_compound_type_2 import (
            ListStrategiesResponse200ResultItemsItemAutoCompoundType2,
        )
        from ..schemas.list_strategies_response_200_result_items_item_lock_type_type_0 import (
            ListStrategiesResponse200ResultItemsItemLockTypeType0,
        )
        from ..schemas.list_strategies_response_200_result_items_item_lock_type_type_1 import (
            ListStrategiesResponse200ResultItemsItemLockTypeType1,
        )
        from ..schemas.list_strategies_response_200_result_items_item_lock_type_type_2 import (
            ListStrategiesResponse200ResultItemsItemLockTypeType2,
        )
        from ..schemas.list_strategies_response_200_result_items_item_lock_type_type_3 import (
            ListStrategiesResponse200ResultItemsItemLockTypeType3,
        )
        from ..schemas.list_strategies_response_200_result_items_item_yield_source_type_0 import (
            ListStrategiesResponse200ResultItemsItemYieldSourceType0,
        )
        from ..schemas.list_strategies_response_200_result_items_item_yield_source_type_1 import (
            ListStrategiesResponse200ResultItemsItemYieldSourceType1,
        )

        d = src_dict.copy()

        def _parse_allocation_fee(data: object) -> Union[float, int, str]:
            return cast(Union[float, int, str], data)

        allocation_fee = _parse_allocation_fee(d.pop("allocation_fee"))

        allocation_restriction_info = []
        _allocation_restriction_info = d.pop("allocation_restriction_info")
        for allocation_restriction_info_item_data in _allocation_restriction_info:
            allocation_restriction_info_item = AllocationRestrictionInfo(
                allocation_restriction_info_item_data
            )

            allocation_restriction_info.append(allocation_restriction_info_item)

        asset = d.pop("asset")

        def _parse_auto_compound(
            data: object,
        ) -> Union[
            "ListStrategiesResponse200ResultItemsItemAutoCompoundType0",
            "ListStrategiesResponse200ResultItemsItemAutoCompoundType1",
            "ListStrategiesResponse200ResultItemsItemAutoCompoundType2",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                auto_compound_type_0 = (
                    ListStrategiesResponse200ResultItemsItemAutoCompoundType0.from_dict(
                        data
                    )
                )

                return auto_compound_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                auto_compound_type_1 = (
                    ListStrategiesResponse200ResultItemsItemAutoCompoundType1.from_dict(
                        data
                    )
                )

                return auto_compound_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            auto_compound_type_2 = (
                ListStrategiesResponse200ResultItemsItemAutoCompoundType2.from_dict(
                    data
                )
            )

            return auto_compound_type_2

        auto_compound = _parse_auto_compound(d.pop("auto_compound"))

        can_allocate = d.pop("can_allocate")

        can_deallocate = d.pop("can_deallocate")

        def _parse_deallocation_fee(data: object) -> Union[float, int, str]:
            return cast(Union[float, int, str], data)

        deallocation_fee = _parse_deallocation_fee(d.pop("deallocation_fee"))

        id = d.pop("id")

        def _parse_lock_type(
            data: object,
        ) -> Union[
            "ListStrategiesResponse200ResultItemsItemLockTypeType0",
            "ListStrategiesResponse200ResultItemsItemLockTypeType1",
            "ListStrategiesResponse200ResultItemsItemLockTypeType2",
            "ListStrategiesResponse200ResultItemsItemLockTypeType3",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                lock_type_type_0 = (
                    ListStrategiesResponse200ResultItemsItemLockTypeType0.from_dict(
                        data
                    )
                )

                return lock_type_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                lock_type_type_1 = (
                    ListStrategiesResponse200ResultItemsItemLockTypeType1.from_dict(
                        data
                    )
                )

                return lock_type_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                lock_type_type_2 = (
                    ListStrategiesResponse200ResultItemsItemLockTypeType2.from_dict(
                        data
                    )
                )

                return lock_type_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            lock_type_type_3 = (
                ListStrategiesResponse200ResultItemsItemLockTypeType3.from_dict(data)
            )

            return lock_type_type_3

        lock_type = _parse_lock_type(d.pop("lock_type"))

        def _parse_yield_source(
            data: object,
        ) -> Union[
            "ListStrategiesResponse200ResultItemsItemYieldSourceType0",
            "ListStrategiesResponse200ResultItemsItemYieldSourceType1",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                yield_source_type_0 = (
                    ListStrategiesResponse200ResultItemsItemYieldSourceType0.from_dict(
                        data
                    )
                )

                return yield_source_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            yield_source_type_1 = (
                ListStrategiesResponse200ResultItemsItemYieldSourceType1.from_dict(data)
            )

            return yield_source_type_1

        yield_source = _parse_yield_source(d.pop("yield_source"))

        _apr_estimate = d.pop("apr_estimate", UNSET)
        apr_estimate: Union[
            Unset, None, ListStrategiesResponse200ResultItemsItemAprEstimate
        ]
        if _apr_estimate is None:
            apr_estimate = None
        elif isinstance(_apr_estimate, Unset):
            apr_estimate = UNSET
        else:
            apr_estimate = (
                ListStrategiesResponse200ResultItemsItemAprEstimate.from_dict(
                    _apr_estimate
                )
            )

        user_cap = d.pop("user_cap", UNSET)

        user_min_allocation = d.pop("user_min_allocation", UNSET)

        list_strategies_response_200_result_items_item = cls(
            allocation_fee=allocation_fee,
            allocation_restriction_info=allocation_restriction_info,
            asset=asset,
            auto_compound=auto_compound,
            can_allocate=can_allocate,
            can_deallocate=can_deallocate,
            deallocation_fee=deallocation_fee,
            id=id,
            lock_type=lock_type,
            yield_source=yield_source,
            apr_estimate=apr_estimate,
            user_cap=user_cap,
            user_min_allocation=user_min_allocation,
        )

        list_strategies_response_200_result_items_item.additional_properties = d
        return list_strategies_response_200_result_items_item

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
