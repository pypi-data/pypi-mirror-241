from typing import overload
import typing

import QuantConnect
import QuantConnect.Data
import QuantConnect.Data.Serialization
import QuantConnect.Util
import System
import System.Collections.Generic


class SerializedSubscriptionDataConfig(System.Object):
    """Data transfer object used for serializing a SubscriptionDataConfig"""

    @property
    def Symbol(self) -> QuantConnect.Symbol:
        """Easy access to the order symbol associated with this event."""
        ...

    @property
    def SecurityType(self) -> int:
        """
        Security type
        
        This property contains the int value of a member of the QuantConnect.SecurityType enum.
        """
        ...

    @property
    def Resolution(self) -> int:
        """
        Subscription resolution
        
        This property contains the int value of a member of the QuantConnect.Resolution enum.
        """
        ...

    @property
    def ExtendedMarketHours(self) -> bool:
        """Extended market hours"""
        ...

    @property
    def DataNormalizationMode(self) -> int:
        """
        Data normalization mode
        
        This property contains the int value of a member of the QuantConnect.DataNormalizationMode enum.
        """
        ...

    @property
    def DataMappingMode(self) -> int:
        """
        Data mapping mode
        
        This property contains the int value of a member of the QuantConnect.DataMappingMode enum.
        """
        ...

    @property
    def ContractDepthOffset(self) -> int:
        """Contract depth offset"""
        ...

    @property
    def IsCustomData(self) -> bool:
        """Whether the subscription configuration is for a custom data type"""
        ...

    @property
    def TickTypes(self) -> System.Collections.Generic.List[QuantConnect.TickType]:
        """The subscription data configuration tick type"""
        ...

    @property
    def Type(self) -> str:
        """The data type"""
        ...

    @overload
    def __init__(self) -> None:
        """
        Empty constructor required for JSON converter.
        
        This method is protected.
        """
        ...

    @overload
    def __init__(self, config: QuantConnect.Data.SubscriptionDataConfig) -> None:
        """Creates a new instance based on the provided config"""
        ...

    @overload
    def __init__(self, configs: System.Collections.Generic.IEnumerable[QuantConnect.Data.SubscriptionDataConfig]) -> None:
        """Creates a new instance based on the provided configs for the same symbol"""
        ...


class SubscriptionDataConfigJsonConverter(QuantConnect.Util.TypeChangeJsonConverter[QuantConnect.Data.SubscriptionDataConfig, QuantConnect.Data.Serialization.SerializedSubscriptionDataConfig]):
    """Defines how subscription data configurations should be serialized to json"""

    @overload
    def Convert(self, value: QuantConnect.Data.SubscriptionDataConfig) -> QuantConnect.Data.Serialization.SerializedSubscriptionDataConfig:
        """
        Convert the input value to a value to be serialzied
        
        This method is protected.
        
        :param value: The input value to be converted before serialziation
        :returns: A new instance of TResult that is to be serialzied.
        """
        ...

    @overload
    def Convert(self, value: QuantConnect.Data.Serialization.SerializedSubscriptionDataConfig) -> QuantConnect.Data.SubscriptionDataConfig:
        """
        Converts the input value to be deserialized
        
        This method is protected.
        
        :param value: The deserialized value that needs to be converted to SubscriptionDataConfig
        :returns: The converted value.
        """
        ...


