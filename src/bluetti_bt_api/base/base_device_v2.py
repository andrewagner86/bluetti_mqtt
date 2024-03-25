from typing import List
from ..utils.commands import ReadHoldingRegisters
from .bluetti_device import BluettiDevice
from ..utils.struct import DeviceStruct


class BaseDeviceV2(BluettiDevice):
    def __init__(self, address: str, type: str, sn: str):
        self.struct = DeviceStruct()

        # Device info
        self.struct.add_swap_string_field("device_type", 110, 6)
        self.struct.add_sn_field("serial_number", 116)

        super().__init__(address, type, sn)

    @property
    def polling_commands(self) -> List[ReadHoldingRegisters]:
        return [
            ReadHoldingRegisters(110, 6),
            ReadHoldingRegisters(116, 4),
        ]
