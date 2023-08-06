"""Ability and ability type class definitions."""

from typing import Optional
from ..base import Cached
from ..census import Query
from ..models import ZoneEffectData, ZoneEffectTypeData
from .._proxy import InstanceProxy

from ._ability import Ability

__all__ = [
    'ZoneEffect',
    'ZoneEffectType'
]


class ZoneEffectType(Cached, cache_size=20, cache_ttu=60.0):
    """A type of zone effect.

    This class mostly specifies the purpose of any generic parameters.

    .. attribute:: id
       :type: int

       The unique ID of this zone effect type.

    .. attribute:: description
       :type: str

       A description of what this zone effect type is used for.

    .. attribute:: param*
       :type: str | None

       Descriptions of what the corresponding parameter is used for in
       zone effects of this type.
    """

    collection = 'zone_effect_type'
    data: ZoneEffectTypeData
    id_field = 'zone_effect_type_id'
    _model = ZoneEffectTypeData

    # Type hints for data class fallback attributes
    id: int
    description: str
    param1: Optional[str]
    param2: Optional[str]
    param3: Optional[str]
    param4: Optional[str]
    param5: Optional[str]
    param6: Optional[str]


class ZoneEffect(Cached, cache_size=10, cache_ttu=60.0):
    """An effect or buff applied by a zone.

    Access the corresponding
    :class:`auraxium.ps2.ZoneEffectType` instance via the
    :meth:`ZoneEffect.type` method for information on generic
    parameters.

    .. attribute:: id
       :type: int

       The unique ID of this zone effect.

    .. attribute:: zone_effect_type_id
       :type: int

       The ID of the associated :class:`~auraxium.ps2.ZoneEffectType`.

    .. attribute:: ability_id
       :type: int

       The :class:`~auraxium.ps2.Ability` associated with this zone
       effect.

    .. attribute:: param*
       :type: str | None

       Type-specific parameters for this zone effect. Refer to the
       corresponding :class:`~auraxium.ps2.ZoneEffectType` for details.
    """

    collection = 'zone_effect'
    data: ZoneEffectData
    id_field = 'zone_effect_id'
    _model = ZoneEffectData

    # Type hints for data class fallback attributes
    id: int
    zone_effect_type_id: int
    ability_id: int
    param1: Optional[str]
    param2: Optional[str]
    param3: Optional[str]
    param4: Optional[str]
    param5: Optional[str]
    param6: Optional[str]

    def ability(self) -> InstanceProxy[Ability]:
        """Return the ability associated with this zone effect."""
        query = Query(Ability.collection, service_id=self._client.service_id)
        query.add_term(field=Ability.id_field, value=self.data.ability_id)
        return InstanceProxy(Ability, query, client=self._client)

    def type(self) -> InstanceProxy[ZoneEffectType]:
        """Return the type of this zone effect."""
        query = Query(
            ZoneEffectType.collection, service_id=self._client.service_id)
        query.add_term(
            field=ZoneEffectType.id_field, value=self.data.zone_effect_type_id)
        return InstanceProxy(ZoneEffectType, query, client=self._client)
