from enum import Enum, auto, unique

@unique
class FieldType(Enum):
    NUMERIC = auto()
    CHARACTER = auto()
    BOOL = auto()
    ENUM = auto()


class FieldAttributes:
    def __init__(
        self,
        type: FieldType = FieldType.NUMERIC,
        setter: bool = False,
        name: str = "",
        unit_of_measurement: str | None = None,
        device_class: str | None = None,
        state_class: str | None = None,
        options: Enum | None = None,
    ):
        self.type = type
        self.setter = setter
        self.name = name
        self.unit_of_measurement = unit_of_measurement
        self.device_class = device_class
        self.state_class = state_class
        self.options = options


class PowerFieldAttributes(FieldAttributes):
    def __init__(
        self,
        name: str = "",
    ):
        super().__init__(
            name=name,
            unit_of_measurement="W",
            device_class="power",
            state_class="measurement",
        )