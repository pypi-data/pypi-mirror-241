from typing import Any, Dict, List, Self, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


@_attrs_define
class AssetTickerInfo:
    """Asset Ticker Info

    Attributes:
        a (Union[Unset, List[str]]): Ask `[<price>, <whole lot volume>, <lot volume>]`
        b (Union[Unset, List[str]]): Bid `[<price>, <whole lot volume>, <lot volume>]`
        c (Union[Unset, List[str]]): Last trade closed `[<price>, <lot volume>]`
        v (Union[Unset, List[str]]): Volume `[<today>, <last 24 hours>]`
        p (Union[Unset, List[str]]): Volume weighted average price `[<today>, <last 24 hours>]`
        t (Union[Unset, List[int]]): Number of trades `[<today>, <last 24 hours>]`
        l (Union[Unset, List[str]]): Low `[<today>, <last 24 hours>]`
        h (Union[Unset, List[str]]): High `[<today>, <last 24 hours>]`
        o (Union[Unset, str]): Today's opening price
    """

    a: Union[Unset, List[str]] = UNSET
    b: Union[Unset, List[str]] = UNSET
    c: Union[Unset, List[str]] = UNSET
    v: Union[Unset, List[str]] = UNSET
    p: Union[Unset, List[str]] = UNSET
    t: Union[Unset, List[int]] = UNSET
    l: Union[Unset, List[str]] = UNSET
    h: Union[Unset, List[str]] = UNSET
    o: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        a: Union[Unset, List[str]] = UNSET
        if not isinstance(self.a, Unset):
            a = self.a

        b: Union[Unset, List[str]] = UNSET
        if not isinstance(self.b, Unset):
            b = self.b

        c: Union[Unset, List[str]] = UNSET
        if not isinstance(self.c, Unset):
            c = self.c

        v: Union[Unset, List[str]] = UNSET
        if not isinstance(self.v, Unset):
            v = self.v

        p: Union[Unset, List[str]] = UNSET
        if not isinstance(self.p, Unset):
            p = self.p

        t: Union[Unset, List[int]] = UNSET
        if not isinstance(self.t, Unset):
            t = self.t

        l: Union[Unset, List[str]] = UNSET
        if not isinstance(self.l, Unset):
            l = self.l

        h: Union[Unset, List[str]] = UNSET
        if not isinstance(self.h, Unset):
            h = self.h

        o = self.o

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if a is not UNSET:
            field_dict["a"] = a
        if b is not UNSET:
            field_dict["b"] = b
        if c is not UNSET:
            field_dict["c"] = c
        if v is not UNSET:
            field_dict["v"] = v
        if p is not UNSET:
            field_dict["p"] = p
        if t is not UNSET:
            field_dict["t"] = t
        if l is not UNSET:
            field_dict["l"] = l
        if h is not UNSET:
            field_dict["h"] = h
        if o is not UNSET:
            field_dict["o"] = o

        return field_dict

    @classmethod
    def from_dict(cls: Self, src_dict: Dict[str, Any]) -> Self:
        d = src_dict.copy()
        a = cast(List[str], d.pop("a", UNSET))

        b = cast(List[str], d.pop("b", UNSET))

        c = cast(List[str], d.pop("c", UNSET))

        v = cast(List[str], d.pop("v", UNSET))

        p = cast(List[str], d.pop("p", UNSET))

        t = cast(List[int], d.pop("t", UNSET))

        l = cast(List[str], d.pop("l", UNSET))

        h = cast(List[str], d.pop("h", UNSET))

        o = d.pop("o", UNSET)

        asset_ticker_info = cls(
            a=a,
            b=b,
            c=c,
            v=v,
            p=p,
            t=t,
            l=l,
            h=h,
            o=o,
        )

        asset_ticker_info.additional_properties = d
        return asset_ticker_info

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
