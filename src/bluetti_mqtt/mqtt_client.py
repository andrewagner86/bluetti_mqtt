import asyncio
from dataclasses import dataclass
from enum import auto, Enum, unique
import json
import logging
import re
from typing import List, Optional
from aiomqtt import Client, MqttError
from paho.mqtt.client import MQTTMessage
from bluetti_mqtt.bus import CommandMessage, EventBus, ParserMessage
from bluetti_mqtt.core import BluettiDevice, DeviceCommand


@unique
class MqttFieldType(Enum):
    NUMERIC = auto()
    BOOL = auto()
    ENUM = auto()
    BUTTON = auto()


@dataclass(frozen=True)
class MqttFieldConfig:
    type: MqttFieldType
    setter: bool
    advanced: bool  # Do not export by default to Home Assistant
    home_assistant_extra: dict
    id_override: Optional[str] = None  # Used to override Home Assistant field id


COMMAND_TOPIC_RE = re.compile(r'^bluetti/command/(\w+)-(\d+)/([a-z_]+)$')
NORMAL_DEVICE_FIELDS = {
    'dc_input_power': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'DC Input Power',
            'unit_of_measurement': 'W',
            'device_class': 'power',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'ac_input_power': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'AC Input Power',
            'unit_of_measurement': 'W',
            'device_class': 'power',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'ac_output_power': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'AC Output Power',
            'unit_of_measurement': 'W',
            'device_class': 'power',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'dc_output_power': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'DC Output Power',
            'unit_of_measurement': 'W',
            'device_class': 'power',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'power_generation': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'Total Power Generation',
            'unit_of_measurement': 'kWh',
            'device_class': 'energy',
            'state_class': 'total_increasing',
        }
    ),
    'total_battery_soc': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'Total Battery SoC',
            'unit_of_measurement': '%',
            'device_class': 'battery',
            'state_class': 'measurement',
        }
    ),
    'ac_output_on': MqttFieldConfig(
        type=MqttFieldType.BOOL,
        setter=True,
        advanced=False,
        home_assistant_extra={
            'name': 'AC Output',
            'device_class': 'outlet',
        }
    ),
    'dc_output_on': MqttFieldConfig(
        type=MqttFieldType.BOOL,
        setter=True,
        advanced=False,
        home_assistant_extra={
            'name': 'DC Output',
            'device_class': 'outlet',
        }
    ),
    'ac_output_mode': MqttFieldConfig(
        type=MqttFieldType.ENUM,
        setter=False,
        advanced=True,
        home_assistant_extra={
            'name': 'AC Output Mode',
        }
    ),
    'internal_ac_voltage': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=True,
        home_assistant_extra={
            'name': 'Internal AC Voltage',
            'unit_of_measurement': 'V',
            'device_class': 'voltage',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'internal_current_one': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=True,
        home_assistant_extra={
            'name': 'Internal Current Sensor 1',
            'unit_of_measurement': 'A',
            'device_class': 'current',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'internal_power_one': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=True,
        home_assistant_extra={
            'name': 'Internal Power Sensor 1',
            'unit_of_measurement': 'W',
            'device_class': 'power',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'internal_ac_frequency': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=True,
        home_assistant_extra={
            'name': 'Internal AC Frequency',
            'unit_of_measurement': 'Hz',
            'device_class': 'frequency',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'internal_current_two': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=True,
        home_assistant_extra={
            'name': 'Internal Current Sensor 2',
            'unit_of_measurement': 'A',
            'device_class': 'current',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'internal_power_two': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=True,
        home_assistant_extra={
            'name': 'Internal Power Sensor 2',
            'unit_of_measurement': 'W',
            'device_class': 'power',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'ac_input_voltage': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=True,
        home_assistant_extra={
            'name': 'AC Input Voltage',
            'unit_of_measurement': 'V',
            'device_class': 'voltage',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'internal_current_three': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=True,
        home_assistant_extra={
            'name': 'Internal Current Sensor 3',
            'unit_of_measurement': 'A',
            'device_class': 'current',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'internal_power_three': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=True,
        home_assistant_extra={
            'name': 'Internal Power Sensor 3',
            'unit_of_measurement': 'W',
            'device_class': 'power',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'ac_input_frequency': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=True,
        home_assistant_extra={
            'name': 'AC Input Frequency',
            'unit_of_measurement': 'Hz',
            'device_class': 'frequency',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'total_battery_voltage': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=True,
        home_assistant_extra={
            'name': 'Total Battery Voltage',
            'unit_of_measurement': 'V',
            'device_class': 'voltage',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'total_battery_current': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=True,
        home_assistant_extra={
            'name': 'Total Battery Current',
            'unit_of_measurement': 'A',
            'device_class': 'current',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'ups_mode': MqttFieldConfig(
        type=MqttFieldType.ENUM,
        setter=True,
        advanced=False,
        home_assistant_extra={
            'name': 'UPS Working Mode',
            'options': ['CUSTOMIZED', 'PV_PRIORITY', 'STANDARD', 'TIME_CONTROL'],
        }
    ),
    'split_phase_on': MqttFieldConfig(
        type=MqttFieldType.BOOL,
        setter=False,  # For safety purposes, I'm not exposing this as a setter
        advanced=False,
        home_assistant_extra={
            'name': 'Split Phase',
        }
    ),
    'split_phase_machine_mode': MqttFieldConfig(
        type=MqttFieldType.ENUM,
        setter=False,  # For safety purposes, I'm not exposing this as a setter
        advanced=False,
        home_assistant_extra={
            'name': 'Split Phase Machine',
        }
    ),
    'grid_charge_on': MqttFieldConfig(
        type=MqttFieldType.BOOL,
        setter=True,
        advanced=False,
        home_assistant_extra={
            'name': 'Grid Charge',
        }
    ),
    'time_control_on': MqttFieldConfig(
        type=MqttFieldType.BOOL,
        setter=True,
        advanced=False,
        home_assistant_extra={
            'name': 'Time Control',
        }
    ),
    'battery_range_start': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=True,
        advanced=False,
        home_assistant_extra={
            'name': 'Battery Range Start',
            'step': 1,
            'min': 0,
            'max': 100,
            'unit_of_measurement': '%',
        }
    ),
    'battery_range_end': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=True,
        advanced=False,
        home_assistant_extra={
            'name': 'Battery Range End',
            'step': 1,
            'min': 0,
            'max': 100,
            'unit_of_measurement': '%',
        }
    ),
    'led_mode': MqttFieldConfig(
        type=MqttFieldType.ENUM,
        setter=True,
        advanced=False,
        home_assistant_extra={
            'name': 'LED Mode',
            'icon': 'mdi:lightbulb',
            'options': ['LOW', 'HIGH', 'SOS', 'OFF'],
        }
    ),
    'power_off': MqttFieldConfig(
        type=MqttFieldType.BUTTON,
        setter=True,
        advanced=False,
        home_assistant_extra={
            'name': 'Power Off',
            'payload_press': 'ON',
        }
    ),
    'auto_sleep_mode': MqttFieldConfig(
        type=MqttFieldType.ENUM,
        setter=True,
        advanced=False,
        home_assistant_extra={
            'name': 'Screen Auto Sleep Mode',
            'icon': 'mdi:sleep',
            'options': ['THIRTY_SECONDS', 'ONE_MINUTE', 'FIVE_MINUTES', 'NEVER'],
        }
    ),
    'eco_on': MqttFieldConfig(
        type=MqttFieldType.BOOL,
        setter=True,
        advanced=False,
        home_assistant_extra={
            'name': 'ECO',
            'icon': 'mdi:sprout',
        }
    ),
    'eco_shutdown': MqttFieldConfig(
        type=MqttFieldType.ENUM,
        setter=True,
        advanced=False,
        home_assistant_extra={
            'name': 'ECO Shutdown',
            'icon': 'mdi:sprout',
            'options': ['ONE_HOUR', 'TWO_HOURS', 'THREE_HOURS', 'FOUR_HOURS'],
        }
    ),
    'charging_mode': MqttFieldConfig(
        type=MqttFieldType.ENUM,
        setter=True,
        advanced=False,
        home_assistant_extra={
            'name': 'Charging Mode',
            'icon': 'mdi:battery-charging',
            'options': ['STANDARD', 'SILENT', 'TURBO'],
        }
    ),
    'power_lifting_on': MqttFieldConfig(
        type=MqttFieldType.BOOL,
        setter=True,
        advanced=False,
        home_assistant_extra={
            'name': 'Power Lifting',
            'icon': 'mdi:arm-flex',
        }
    ),
    'total_battery_soc': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'total_battery_soc',
            'unit_of_measurement': '%',
            'device_class': 'battery',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'output_power': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'output_power',
            'unit_of_measurement': 'W',
            'device_class': 'power',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'input_power': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'input_power',
            'unit_of_measurement': 'W',
            'device_class': 'power',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'grid_power': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'grid_power',
            'unit_of_measurement': 'W',
            'device_class': 'power',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'uint_148': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'uint_148',
            'unit_of_measurement': '?',
            'device_class': 'None',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'total_consumption': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'total_consumption',
            'unit_of_measurement': 'kWh',
            'device_class': 'energy',
            'state_class': 'total_increasing',
            'force_update': True,
        }
    ),
    'total_feed': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'total_feed',
            'unit_of_measurement': 'kWh',
            'device_class': 'energy',
            'state_class': 'total_increasing',
            'force_update': True,
        }
    ),
    'total_feed': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'total_feed',
            'unit_of_measurement': 'kWh',
            'device_class': 'energy',
            'state_class': 'total_increasing',
            'force_update': True,
        }
    ),
    'total_grid_consumption': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'total_grid_consumption',
            'unit_of_measurement': 'kWh',
            'device_class': 'energy',
            'state_class': 'total_increasing',
            'force_update': True,
        }
    ),
    'total_grid_feed': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'total_grid_feed',
            'unit_of_measurement': 'kWh',
            'device_class': 'energy',
            'state_class': 'total_increasing',
            'force_update': True,
        }
    ),
    'dc_input_1_power': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'dc_input_1_power',
            'unit_of_measurement': 'W',
            'device_class': 'power',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'dc_input_1_voltage': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'dc_input_1_voltage',
            'unit_of_measurement': 'V',
            'device_class': 'voltage',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'dc_input_1_current': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'dc_input_1_current',
            'unit_of_measurement': 'A',
            'device_class': 'current',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'dc_input_2_power': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'dc_input_2_power',
            'unit_of_measurement': 'W',
            'device_class': 'power',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'dc_input_2_voltage': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'dc_input_2_voltage',
            'unit_of_measurement': 'V',
            'device_class': 'voltage',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'dc_input_2_current': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'dc_input_2_current',
            'unit_of_measurement': 'A',
            'device_class': 'current',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'ac_input_phase1_power': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'ac_input_phase1_power',
            'unit_of_measurement': 'W',
            'device_class': 'power',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'ac_input_phase1_voltage': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'ac_input_phase1_voltage',
            'unit_of_measurement': 'V',
            'device_class': 'voltage',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'ac_input_phase1_current': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'ac_input_phase1_current',
            'unit_of_measurement': 'A',
            'device_class': 'current',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'ac_input_phase2_power': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'ac_input_phase2_power',
            'unit_of_measurement': 'W',
            'device_class': 'power',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'ac_input_phase2_voltage': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'ac_input_phase2_voltage',
            'unit_of_measurement': 'V',
            'device_class': 'voltage',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'ac_input_phase2_current': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'ac_input_phase2_current',
            'unit_of_measurement': 'A',
            'device_class': 'current',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'ac_input_phase3_power': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'ac_input_phase3_power',
            'unit_of_measurement': 'W',
            'device_class': 'power',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'ac_input_phase3_voltage': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'ac_input_phase3_voltage',
            'unit_of_measurement': 'V',
            'device_class': 'voltage',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'ac_input_phase3_current': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'ac_input_phase3_current',
            'unit_of_measurement': 'A',
            'device_class': 'current',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'grid_frequency': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'grid_frequency',
            'unit_of_measurement': 'Hz',
            'device_class': 'frequency',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'grid_frequency': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'grid_frequency',
            'unit_of_measurement': 'Hz',
            'device_class': 'frequency',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'grid_frequency': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'grid_frequency',
            'unit_of_measurement': 'Hz',
            'device_class': 'frequency',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'uint_1301': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'uint_1301',
            'unit_of_measurement': '?',
            'device_class': 'None',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'uint_1302': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'uint_1302',
            'unit_of_measurement': '?',
            'device_class': 'None',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'uint_1303': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'uint_1303',
            'unit_of_measurement': '?',
            'device_class': 'None',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'uint_1304': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'uint_1304',
            'unit_of_measurement': '?',
            'device_class': 'None',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'uint_1305': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'uint_1305',
            'unit_of_measurement': '?',
            'device_class': 'None',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'uint_1306': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'uint_1306',
            'unit_of_measurement': '?',
            'device_class': 'None',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'uint_1307': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'uint_1307',
            'unit_of_measurement': '?',
            'device_class': 'None',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'uint_1308': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'uint_1308',
            'unit_of_measurement': '?',
            'device_class': 'None',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'uint_1309': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'uint_1309',
            'unit_of_measurement': '?',
            'device_class': 'None',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'uint_1310': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'uint_1310',
            'unit_of_measurement': '?',
            'device_class': 'None',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'uint_1311': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'uint_1311',
            'unit_of_measurement': '?',
            'device_class': 'None',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'uint_1312': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'uint_1312',
            'unit_of_measurement': '?',
            'device_class': 'None',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'grid_phase1_power': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'grid_phase1_power',
            'unit_of_measurement': 'W',
            'device_class': 'power',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'grid_phase1_voltage': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'grid_phase1_voltage',
            'unit_of_measurement': 'V',
            'device_class': 'voltage',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'grid_phase1_current': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'grid_phase1_current',
            'unit_of_measurement': 'A',
            'device_class': 'current',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'uint_1316': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'uint_1316',
            'unit_of_measurement': '?',
            'device_class': 'None',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'uint_1317': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'uint_1317',
            'unit_of_measurement': '?',
            'device_class': 'None',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'uint_1318': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'uint_1318',
            'unit_of_measurement': '?',
            'device_class': 'None',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'grid_phase2_power': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'grid_phase2_power',
            'unit_of_measurement': 'W',
            'device_class': 'power',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'grid_phase2_voltage': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'grid_phase2_voltage',
            'unit_of_measurement': 'V',
            'device_class': 'voltage',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'grid_phase2_current': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'grid_phase2_current',
            'unit_of_measurement': 'A',
            'device_class': 'current',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'uint_1322': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'uint_1322',
            'unit_of_measurement': '?',
            'device_class': 'None',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'uint_1323': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'uint_1323',
            'unit_of_measurement': '?',
            'device_class': 'None',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'uint_1324': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'uint_1324',
            'unit_of_measurement': '?',
            'device_class': 'None',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'grid_phase3_power': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'grid_phase3_power',
            'unit_of_measurement': 'W',
            'device_class': 'power',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'grid_phase3_voltage': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'grid_phase3_voltage',
            'unit_of_measurement': 'V',
            'device_class': 'voltage',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'grid_phase3_current': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'grid_phase3_current',
            'unit_of_measurement': 'A',
            'device_class': 'current',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'uint_1328': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'uint_1328',
            'unit_of_measurement': '?',
            'device_class': 'None',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'uint_1329': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'uint_1329',
            'unit_of_measurement': '?',
            'device_class': 'None',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'uint_1330': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'uint_1330',
            'unit_of_measurement': '?',
            'device_class': 'None',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'ac_output_phase1_power': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'ac_output_phase1_power',
            'unit_of_measurement': 'W',
            'device_class': 'power',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'ac_output_phase1_voltage': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'ac_output_phase1_voltage',
            'unit_of_measurement': 'V',
            'device_class': 'voltage',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'ac_output_phase1_current': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'ac_output_phase1_current',
            'unit_of_measurement': 'A',
            'device_class': 'current',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'ac_output_phase2_power': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'ac_output_phase2_power',
            'unit_of_measurement': 'W',
            'device_class': 'power',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'ac_output_phase2_voltage': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'ac_output_phase2_voltage',
            'unit_of_measurement': 'V',
            'device_class': 'voltage',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'ac_output_phase2_current': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'ac_output_phase2_current',
            'unit_of_measurement': 'A',
            'device_class': 'current',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'ac_output_phase3_power': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'ac_output_phase3_power',
            'unit_of_measurement': 'W',
            'device_class': 'power',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'ac_output_phase3_voltage': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'ac_output_phase3_voltage',
            'unit_of_measurement': 'V',
            'device_class': 'voltage',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'ac_output_phase3_current': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'ac_output_phase3_current',
            'unit_of_measurement': 'A',
            'device_class': 'current',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'unknown_frequency': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'unknown_frequency',
            'unit_of_measurement': 'Hz',
            'device_class': 'frequency',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'unknown_frequency': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'unknown_frequency',
            'unit_of_measurement': 'Hz',
            'device_class': 'frequency',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'unknown_frequency': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'unknown_frequency',
            'unit_of_measurement': 'Hz',
            'device_class': 'frequency',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'unknown_phase1_power': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'unknown_phase1_power',
            'unit_of_measurement': 'W',
            'device_class': 'power',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'unknown_phase1_voltage': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'unknown_phase1_voltage',
            'unit_of_measurement': 'V',
            'device_class': 'voltage',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'unknown_phase1_current': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'unknown_phase1_current',
            'unit_of_measurement': 'A',
            'device_class': 'current',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'unknown_phase2_power': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'unknown_phase2_power',
            'unit_of_measurement': 'W',
            'device_class': 'power',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'unknown_phase2_voltage': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'unknown_phase2_voltage',
            'unit_of_measurement': 'V',
            'device_class': 'voltage',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'unknown_phase2_current': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'unknown_phase2_current',
            'unit_of_measurement': 'A',
            'device_class': 'current',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'unknown_phase3_power': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'unknown_phase3_power',
            'unit_of_measurement': 'W',
            'device_class': 'power',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'unknown_phase3_voltage': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'unknown_phase3_voltage',
            'unit_of_measurement': 'V',
            'device_class': 'voltage',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'unknown_phase3_current': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'unknown_phase3_current',
            'unit_of_measurement': 'A',
            'device_class': 'current',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'uint_2001': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'uint_2001',
            'unit_of_measurement': '?',
            'device_class': 'None',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'uint_2002': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'uint_2002',
            'unit_of_measurement': '?',
            'device_class': 'None',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'uint_2003': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'uint_2003',
            'unit_of_measurement': '?',
            'device_class': 'None',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'min_battery_soc': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=True,
        advanced=False,
        home_assistant_extra={
            'name': 'min_battery_soc',
            'unit_of_measurement': '%',
            'device_class': 'None',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'max_battery_soc': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=True,
        advanced=False,
        home_assistant_extra={
            'name': 'max_battery_soc',
            'unit_of_measurement': '%',
            'device_class': 'None',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'uint_2032': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'uint_2032',
            'unit_of_measurement': '?',
            'device_class': 'None',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'uint_2200': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'uint_2200',
            'unit_of_measurement': '?',
            'device_class': 'None',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'uint_2201': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'uint_2201',
            'unit_of_measurement': '?',
            'device_class': 'None',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'uint_2202': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'uint_2202',
            'unit_of_measurement': '?',
            'device_class': 'None',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'uint_2203': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'uint_2203',
            'unit_of_measurement': '?',
            'device_class': 'None',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'max_input_power_per_phase': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=True,
        advanced=False,
        home_assistant_extra={
            'name': 'max_input_power_per_phase',
            'unit_of_measurement': 'W',
            'device_class': 'power',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'max_input_current_per_phase': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=True,
        advanced=False,
        home_assistant_extra={
            'name': 'max_input_current_per_phase',
            'unit_of_measurement': 'A',
            'device_class': 'current',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'max_output_power_per_phase': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=True,
        advanced=False,
        home_assistant_extra={
            'name': 'max_output_power_per_phase',
            'unit_of_measurement': 'W',
            'device_class': 'power',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'max_output_current_per_phase': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=True,
        advanced=False,
        home_assistant_extra={
            'name': 'max_output_current_per_phase',
            'unit_of_measurement': 'A',
            'device_class': 'current',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
}
DC_INPUT_FIELDS = {
    'dc_input_voltage1': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'DC Input Voltage 1',
            'unit_of_measurement': 'V',
            'device_class': 'voltage',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'dc_input_power1': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'DC Input Power 1',
            'unit_of_measurement': 'W',
            'device_class': 'power',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
    'dc_input_current1': MqttFieldConfig(
        type=MqttFieldType.NUMERIC,
        setter=False,
        advanced=False,
        home_assistant_extra={
            'name': 'DC Input Current 1',
            'unit_of_measurement': 'A',
            'device_class': 'current',
            'state_class': 'measurement',
            'force_update': True,
        }
    ),
}


def battery_pack_fields(pack: int):
    return {
        'pack_status': MqttFieldConfig(
            type=MqttFieldType.ENUM,
            setter=False,
            advanced=True,
            home_assistant_extra={
                'name': f'Battery Pack {pack} Status',
                'value_template': '{{ value_json.status }}'
            },
            id_override=f'pack_status{pack}'
        ),
        'pack_voltage': MqttFieldConfig(
            type=MqttFieldType.NUMERIC,
            setter=False,
            advanced=True,
            home_assistant_extra={
                'name': f'Battery Pack {pack} Voltage',
                'unit_of_measurement': 'V',
                'device_class': 'voltage',
                'state_class': 'measurement',
                'force_update': True,
                'value_template': '{{ value_json.voltage }}'
            },
            id_override=f'pack_voltage{pack}'
        ),
        'pack_battery_percent': MqttFieldConfig(
            type=MqttFieldType.NUMERIC,
            setter=False,
            advanced=False,
            home_assistant_extra={
                'name': f'Battery Pack {pack} Percent',
                'unit_of_measurement': '%',
                'device_class': 'battery',
                'state_class': 'measurement',
                'value_template': '{{ value_json.percent }}'
            },
            id_override=f'pack_percent{pack}'
        ),
    }


class MQTTClient:
    devices: List[BluettiDevice]
    message_queue: asyncio.Queue

    def __init__(
        self,
        bus: EventBus,
        hostname: str,
        home_assistant_mode: str,
        port: int = 1883,
        username: Optional[str] = None,
        password: Optional[str] = None,
    ):
        self.bus = bus
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.home_assistant_mode = home_assistant_mode
        self.devices = []

    async def run(self):
        while True:
            logging.info('Connecting to MQTT broker...')
            try:
                async with Client(
                    hostname=self.hostname,
                    port=self.port,
                    username=self.username,
                    password=self.password
                ) as client:
                    logging.info('Connected to MQTT broker')

                    # Connect to event bus
                    self.message_queue = asyncio.Queue()
                    self.bus.add_parser_listener(self.handle_message)

                    # Handle pub/sub
                    await asyncio.gather(
                        self._handle_commands(client),
                        self._handle_messages(client)
                    )
            except MqttError:
                logging.exception('MQTT error:')
                await asyncio.sleep(5)

    async def handle_message(self, msg: ParserMessage):
        await self.message_queue.put(msg)

    async def _handle_commands(self, client: Client):
        await client.subscribe('bluetti/command/#')
        async for mqtt_message in client.messages:
            await self._handle_command(mqtt_message)

    async def _handle_messages(self, client: Client):
        while True:
            msg: ParserMessage = await self.message_queue.get()
            if msg.device not in self.devices:
                await self._init_device(msg.device, client)
            await self._handle_message(client, msg)
            self.message_queue.task_done()

    async def _init_device(self, device: BluettiDevice, client: Client):
        # Register device
        self.devices.append(device)

        # Skip announcing device to Home Assistant if disabled
        if self.home_assistant_mode == 'none':
            return

        def payload(id: str, device: BluettiDevice, field: MqttFieldConfig) -> str:
            ha_id = id if not field.id_override else field.id_override
            payload_dict = {
                'state_topic': f'bluetti/state/{device.type}-{device.sn}/{id}',
                'device': {
                    'identifiers': [
                        f'{device.sn}'
                    ],
                    'manufacturer': 'Bluetti',
                    'name': f'{device.type} {device.sn}',
                    'model': device.type
                },
                'unique_id': f'{device.sn}_{ha_id}',
                'object_id': f'{device.type}_{ha_id}',
            }
            if field.setter:
                payload_dict['command_topic'] = f'bluetti/command/{device.type}-{device.sn}/{id}'
            payload_dict.update(field.home_assistant_extra)

            return json.dumps(payload_dict, separators=(',', ':'))

        # Publish normal fields
        for name, field in NORMAL_DEVICE_FIELDS.items():
            # Skip fields not supported by the device
            if not device.has_field(name):
                continue

            # Skip advanced fields if not enabled
            if field.advanced and self.home_assistant_mode != 'advanced':
                continue

            # Figure out Home Assistant type
            if field.type == MqttFieldType.NUMERIC:
                type = 'number' if field.setter else 'sensor'
            elif field.type == MqttFieldType.BOOL:
                type = 'switch' if field.setter else 'binary_sensor'
            elif field.type == MqttFieldType.ENUM:
                type = 'select' if field.setter else 'sensor'
            elif field.type == MqttFieldType.BUTTON:
                type = 'button'

            # Publish config
            await client.publish(
                f'homeassistant/{type}/{device.sn}_{name}/config',
                payload=payload(name, device, field).encode(),
                retain=True
            )

        # Publish battery pack configs
        for pack in range(1, device.pack_num_max + 1):
            fields = battery_pack_fields(pack)
            for name, field in fields.items():
                # Skip fields not supported by the device
                if not device.has_field(name):
                    continue

                # Publish config
                await client.publish(
                    f'homeassistant/sensor/{device.sn}_{field.id_override}/config',
                    payload=payload(f'pack_details{pack}', device, field).encode(),
                    retain=True
                )

        # Publish DC input config
        if device.has_field('internal_dc_input_voltage'):
            for name, field in DC_INPUT_FIELDS.items():
                await client.publish(
                    f'homeassistant/sensor/{device.sn}_{name}/config',
                    payload=payload(name, device, field).encode(),
                    retain=True
                )

        logging.info(f'Sent discovery message of {device.type}-{device.sn} to Home Assistant')

    async def _handle_command(self, mqtt_message: MQTTMessage):
        # Parse the mqtt_message.topic
        m = COMMAND_TOPIC_RE.match(str(mqtt_message.topic))
        if not m:
            logging.warn(f'unknown command topic: {mqtt_message.topic}')
            return

        # Find the matching device for the command
        device = next((d for d in self.devices if d.type == m[1] and d.sn == m[2]), None)
        if not device:
            logging.warn(f'unknown device: {m[1]} {m[2]}')
            return

        # Check if the device supports setting this field
        if not device.has_field_setter(m[3]):
            logging.warn(f'Received command for unknown topic: {m[3]} - {mqtt_message.topic}')
            return

        cmd: DeviceCommand = None
        if m[3] in NORMAL_DEVICE_FIELDS:
            field = NORMAL_DEVICE_FIELDS[m[3]]
            if field.type == MqttFieldType.ENUM:
                value = mqtt_message.payload.decode('ascii')
                cmd = device.build_setter_command(m[3], value)
            elif field.type == MqttFieldType.BOOL or field.type == MqttFieldType.BUTTON:
                value = mqtt_message.payload == b'ON'
                cmd = device.build_setter_command(m[3], value)
            elif field.type == MqttFieldType.NUMERIC:
                value = int(mqtt_message.payload.decode('ascii'))
                cmd = device.build_setter_command(m[3], value)
            else:
                raise AssertionError(f'unexpected enum type: {field.type}')
        else:
            logging.warn(f'Received command for unhandled topic: {m[3]} - {mqtt_message.topic}')
            return

        await self.bus.put(CommandMessage(device, cmd))

    async def _handle_message(self, client: Client, msg: ParserMessage):
        logging.debug(f'Got a message from {msg.device}: {msg.parsed}')
        topic_prefix = f'bluetti/state/{msg.device.type}-{msg.device.sn}/'

        # Publish normal fields
        for name, value in msg.parsed.items():
            # Skip unconfigured fields
            if name not in NORMAL_DEVICE_FIELDS:
                continue

            # Build payload string
            field = NORMAL_DEVICE_FIELDS[name]
            if field.type == MqttFieldType.NUMERIC:
                payload = str(value)
            elif field.type == MqttFieldType.BOOL or field.type == MqttFieldType.BUTTON:
                payload = 'ON' if value else 'OFF'
            elif field.type == MqttFieldType.ENUM:
                payload = value.name
            else:
                assert False, f'Unhandled field type: {field.type.name}'

            await client.publish(topic_prefix + name, payload=payload.encode())

        # Publish battery pack data
        pack_details = self._build_pack_details(msg.parsed)
        if 'pack_num' in msg.parsed and len(pack_details) > 0:
            await client.publish(
                topic_prefix + f'pack_details{msg.parsed["pack_num"]}',
                payload=json.dumps(pack_details, separators=(',', ':')).encode()
            )

        # Publish DC input data
        if 'internal_dc_input_voltage' in msg.parsed:
            await client.publish(
                topic_prefix + 'dc_input_voltage1',
                payload=str(msg.parsed['internal_dc_input_voltage']).encode()
            )
        if 'internal_dc_input_power' in msg.parsed:
            await client.publish(
                topic_prefix + 'dc_input_power1',
                payload=str(msg.parsed['internal_dc_input_power']).encode()
            )
        if 'internal_dc_input_current' in msg.parsed:
            await client.publish(
                topic_prefix + 'dc_input_current1',
                payload=str(msg.parsed['internal_dc_input_current']).encode()
            )

    def _build_pack_details(self, parsed: dict):
        details = {}
        if 'pack_status' in parsed:
            details['status'] = parsed['pack_status'].name
        if 'pack_battery_percent' in parsed:
            details['percent'] = parsed['pack_battery_percent']
        if 'pack_voltage' in parsed:
            details['voltage'] = float(parsed['pack_voltage'])
        if 'cell_voltages' in parsed:
            details['voltages'] = [float(d) for d in parsed['cell_voltages']]
        return details
