from typing import List
from ..commands import ReadHoldingRegisters
from .bluetti_device import BluettiDevice
from .struct import DeviceStruct


class PBOX(BluettiDevice):
    def __init__(self, address: str, sn: str):
        self.struct = DeviceStruct()

        self.struct.add_uint_field('unknown-field-100', 100) # 6003
        self.struct.add_uint_field('unknown-field-101', 101) # 6004
        self.struct.add_uint_field('unknown-field-103', 103) # 6009
        self.struct.add_uint_field('unknown-field-123', 123) # 1131
        self.struct.add_uint_field('unknown-field-125', 125) # 6005
        self.struct.add_int_field('unknown-field-148', 148)
        self.struct.add_uint_field('unknown-field-162', 162)
        self.struct.add_uint_field('unknown-field-1131', 1131) # 123
        self.struct.add_uint_field('unknown-field-1200', 1200)
        self.struct.add_uint_field('unknown-field-1202', 1202)
        self.struct.add_uint_field('unknown-field-1301', 1301)
        self.struct.add_uint_field('unknown-field-1303', 1303)
        self.struct.add_uint_field('unknown-field-1305', 1305)
        self.struct.add_uint_field('unknown-field-1420', 1420)
        self.struct.add_uint_field('unknown-field-1422', 1422)
        self.struct.add_uint_field('unknown-field-1509', 1509)
        self.struct.add_uint_field('unknown-field-1516', 1516)
        self.struct.add_uint_field('unknown-field-1523', 1523)
        self.struct.add_uint_field('unknown-field-6003', 6003) # 100
        self.struct.add_uint_field('unknown-field-6004', 6004) # 101
        self.struct.add_uint_field('unknown-field-6005', 6005) # 125
        # self.struct.add_uint_field('unknown-field-6006', 6006)
        self.struct.add_uint_field('unknown-field-6007', 6007)
        # self.struct.add_uint_field('unknown-field-6008', 6008)
        self.struct.add_uint_field('unknown-field-6009', 6009) # 103
        self.struct.add_uint_field('unknown-field-6010', 6010)
        self.struct.add_uint_field('unknown-field-6011', 6011)
        self.struct.add_uint_field('unknown-field-6012', 6012)
        self.struct.add_uint_field('unknown-field-6019', 6019) # 6133
        self.struct.add_uint_field('unknown-field-6111', 6111)
        self.struct.add_uint_field('unknown-field-6112', 6112)
        self.struct.add_uint_field('unknown-field-6113', 6113)
        self.struct.add_uint_field('unknown-field-6116', 6116)
        self.struct.add_uint_field('unknown-field-6117', 6117)
        self.struct.add_uint_field('unknown-field-6118', 6118)
        self.struct.add_uint_field('unknown-field-6119', 6119)
        # self.struct.add_uint_field('unknown-field-6120', 6120)
        self.struct.add_uint_field('unknown-field-6121', 6121)
        # self.struct.add_uint_field('unknown-field-6122', 6122)
        self.struct.add_uint_field('unknown-field-6123', 6123)
        # self.struct.add_uint_field('unknown-field-6124', 6124)
        self.struct.add_uint_field('unknown-field-6125', 6125)
        self.struct.add_uint_field('unknown-field-6133', 6133) # 6019
        self.struct.add_uint_field('unknown-field-6137', 6137)
        self.struct.add_uint_field('unknown-field-6139', 6139)
        self.struct.add_uint_field('unknown-field-11026', 11026)

        self.struct.add_uint_field('total_battery_soc', 102, (0,100))
        self.struct.add_swap_string_field('device_type', 110, 6)
        self.struct.add_sn_field('device_sn', 116)
        self.struct.add_int_field('output_power', 142)
        self.struct.add_int_field('input_power', 144)
        self.struct.add_int_field('grid_power', 146)
        self.struct.add_int_field('?', 148)
        self.struct.add_decimal_field('total_consumption', 152, 1)
        self.struct.add_decimal_field('total_feed', 154, 1)
        self.struct.add_decimal_field('total_grid_consumption', 156, 1)
        self.struct.add_decimal_field('total_grid_feed', 158, 1)
        self.struct.add_swap_string_field('device_type', 1101, 6)
        self.struct.add_sn_field('device_sn', 1107)
        self.struct.add_version_field('system_arm_version', 1114)
        self.struct.add_version_field('system_dsp_version', 1117)
        self.struct.add_int_field('dc_input1_power', 1212)
        self.struct.add_decimal_field('dc_input1_voltage', 1213, 1)
        self.struct.add_decimal_field('dc_input1_current', 1214, 1)
        self.struct.add_int_field('dc_input2_power', 1220)
        self.struct.add_decimal_field('dc_input2_voltage', 1221, 1)
        self.struct.add_decimal_field('dc_input2_current', 1222, 1)
        self.struct.add_int_field('ac_input_phase1_power', 1228)
        self.struct.add_decimal_field('ac_input_phase1_voltage', 1229, 1)
        self.struct.add_decimal_field('ac_input_phase1_current', 1230, 1)
        self.struct.add_int_field('ac_input_phase2_power', 1236)
        self.struct.add_decimal_field('ac_input_phase2_voltage', 1237, 1)
        self.struct.add_decimal_field('ac_input_phase2_current', 1238, 1)
        self.struct.add_int_field('ac_input_phase3_power', 1244)
        self.struct.add_decimal_field('ac_input_phase3_voltage', 1245, 1)
        self.struct.add_decimal_field('ac_input_phase3_current', 1246, 1)
        self.struct.add_decimal_field('grid_frequency', 1300, 1)
        self.struct.add_int_field('grid_phase1_power', 1313)
        self.struct.add_decimal_field('grid_phase1_voltage', 1314, 1)
        self.struct.add_decimal_field('grid_phase1_current', 1315, 1)
        self.struct.add_int_field('grid_phase2_power', 1319)
        self.struct.add_decimal_field('grid_phase2_voltage', 1320, 1)
        self.struct.add_decimal_field('grid_phase2_current', 1321, 1)
        self.struct.add_int_field('grid_phase3_power', 1325)
        self.struct.add_decimal_field('grid_phase3_voltage', 1326, 1)
        self.struct.add_decimal_field('grid_phase3_current', 1327, 1)
        self.struct.add_int_field('ac_output_phase1_power', 1430)
        self.struct.add_decimal_field('ac_output_phase1_voltage', 1431, 1)
        self.struct.add_decimal_field('ac_output_phase1_current', 1432, 1)
        self.struct.add_int_field('ac_output_phase2_power', 1436)
        self.struct.add_decimal_field('ac_output_phase2_voltage', 1437, 1)
        self.struct.add_decimal_field('ac_output_phase2_current', 1438, 1)
        self.struct.add_int_field('ac_output_phase3_power', 1442)
        self.struct.add_decimal_field('ac_output_phase3_voltage', 1443, 1)
        self.struct.add_decimal_field('ac_output_phase3_current', 1444, 1)
        self.struct.add_decimal_field('?_frequency', 1500, 1)
        self.struct.add_int_field('?_phase1_power', 1510)
        self.struct.add_decimal_field('?_phase1_voltage', 1511, 1)
        self.struct.add_decimal_field('?_phase1_current', 1512, 1)
        self.struct.add_int_field('?_phase2_power', 1517)
        self.struct.add_decimal_field('?_phase2_voltage', 1518, 1)
        self.struct.add_decimal_field('?_phase2_current', 1519, 1)
        self.struct.add_int_field('?_phase3_power', 1524)
        self.struct.add_decimal_field('?_phase3_voltage', 1525, 1)
        self.struct.add_decimal_field('?_phase3_current', 1526, 1)
        self.struct.add_utint_field('datetime_year', 2001, 0)
        self.struct.add_utint_field('datetime_month', 2001, 1)
        self.struct.add_utint_field('datetime_day', 2002, 0)
        self.struct.add_utint_field('datetime_hour', 2002, 1)
        self.struct.add_utint_field('datetime_minute', 2003, 0)
        self.struct.add_utint_field('datetime_second', 2003, 1)
        self.struct.add_bool_field('main_switch', 2011)
        self.struct.add_uint_field('min_battery_soc', 2022, (0,100))
        self.struct.add_uint_field('max_battery_soc', 2023, (0,100))
        self.struct.add_bool_field('time_control_switch', 2029)
        # self.struct.add_enum_field('time_schedule1_mode', 2030, TimeScheduleMode)
        self.struct.add_utint_field('time_schedule1_start_hour', 2031, 0)
        self.struct.add_utint_field('time_schedule1_start_minute', 2031, 1)
        self.struct.add_utint_field('time_schedule1_end_hour', 2032, 0)
        self.struct.add_utint_field('time_schedule1_end_minute', 2032, 1)
        # self.struct.add_enum_field('time_schedule2_mode', 2033, TimeScheduleMode)
        self.struct.add_utint_field('time_schedule2_start_hour', 2034, 0)
        self.struct.add_utint_field('time_schedule2_start_minute', 2034, 1)
        self.struct.add_utint_field('time_schedule2_end_hour', 2035, 0)
        self.struct.add_utint_field('time_schedule2_end_minute', 2035, 1)
        # self.struct.add_enum_field('time_schedule3_mode', 2036, TimeScheduleMode)
        self.struct.add_utint_field('time_schedule3_start_hour', 2037, 0)
        self.struct.add_utint_field('time_schedule3_start_minute', 2037, 1)
        self.struct.add_utint_field('time_schedule3_end_hour', 2038, 0)
        self.struct.add_utint_field('time_schedule3_end_minute', 2038, 1)
        # self.struct.add_enum_field('time_schedule4_mode', 2039, TimeScheduleMode)
        self.struct.add_utint_field('time_schedule4_start_hour', 2040, 0)
        self.struct.add_utint_field('time_schedule4_start_minute', 2040, 1)
        self.struct.add_utint_field('time_schedule4_end_hour', 2041, 0)
        self.struct.add_utint_field('time_schedule4_end_minute', 2041, 1)
        # self.struct.add_enum_field('time_schedule5_mode', 2042, TimeScheduleMode)
        self.struct.add_utint_field('time_schedule5_start_hour', 2043, 0)
        self.struct.add_utint_field('time_schedule5_start_minute', 2043, 1)
        self.struct.add_utint_field('time_schedule5_end_hour', 2044, 0)
        self.struct.add_utint_field('time_schedule5_end_minute', 2044, 1)
        # self.struct.add_enum_field('time_schedule6_mode', 2045, TimeScheduleMode)
        self.struct.add_utint_field('time_schedule6_start_hour', 2046, 0)
        self.struct.add_utint_field('time_schedule6_start_minute', 2046, 1)
        self.struct.add_utint_field('time_schedule6_end_hour', 2047, 0)
        self.struct.add_utint_field('time_schedule6_end_minute', 2047, 1)
        self.struct.add_bool_field('buzzer_switch', 2066)
        self.struct.add_bool_field('charge_from_grid', 2207)
        self.struct.add_bool_field('feed_to_grid', 2208)
        self.struct.add_uint_field('max_input_power_per_phase', 2213, (0,15000))
        self.struct.add_uint_field('max_input_current_per_phase', 2214, (0,65))
        self.struct.add_uint_field('max_output_power_per_phase', 2215, (0,15000))
        self.struct.add_uint_field('max_output_current_per_phase', 2216, (0,65))
        self.struct.add_bool_field('grid_self_adjustment', 2225)
        self.struct.add_bool_field('restore_system_switch', 2226)
        self.struct.add_bool_field('battery_heater', 7002)
        self.struct.add_version_field('iot_version', 11014)
        self.struct.add_swap_string_field('wifi_name', 12002, 16)
        self.struct.add_swap_string_field('wifi_password', 12018, 48)


        super().__init__(address, 'PBOX', sn)

    @property
    def pack_num_max(self):
        return 16

    @property
    def polling_commands(self) -> List[ReadHoldingRegisters]:
        return [
            ReadHoldingRegisters(0, 21),
            ReadHoldingRegisters(100, 67),
            ReadHoldingRegisters(700, 6),
            ReadHoldingRegisters(720, 49),
            ReadHoldingRegisters(1100, 54),
            ReadHoldingRegisters(1200, 90),
            ReadHoldingRegisters(1300, 31),
            ReadHoldingRegisters(1400, 48),
            ReadHoldingRegisters(1500, 30),
            ReadHoldingRegisters(1600, 14),
            ReadHoldingRegisters(1700, 10),
            ReadHoldingRegisters(2000, 89),
            ReadHoldingRegisters(2200, 43),
            ReadHoldingRegisters(2300, 36),
            ReadHoldingRegisters(2400, 50),
            ReadHoldingRegisters(3000, 27),
            ReadHoldingRegisters(3500, 48),
            ReadHoldingRegisters(3600, 59),
            ReadHoldingRegisters(6000, 32),
            ReadHoldingRegisters(6100, 104),
            ReadHoldingRegisters(6300, 386),
            ReadHoldingRegisters(7000, 5),
            ReadHoldingRegisters(11000, 39),
            ReadHoldingRegisters(12000, 164),
        ]

    @property
    def logging_commands(self) -> List[ReadHoldingRegisters]:
        return [
            ReadHoldingRegisters(0, 21),
            ReadHoldingRegisters(100, 67),
            ReadHoldingRegisters(700, 6),
            ReadHoldingRegisters(720, 49),
            ReadHoldingRegisters(1100, 54),
            ReadHoldingRegisters(1200, 90),
            ReadHoldingRegisters(1300, 31),
            ReadHoldingRegisters(1400, 48),
            ReadHoldingRegisters(1500, 30),
            ReadHoldingRegisters(1600, 14),
            ReadHoldingRegisters(1700, 10),
            ReadHoldingRegisters(2000, 89),
            ReadHoldingRegisters(2200, 43),
            ReadHoldingRegisters(2300, 36),
            ReadHoldingRegisters(2400, 50),
            ReadHoldingRegisters(3000, 27),
            ReadHoldingRegisters(3500, 48),
            ReadHoldingRegisters(3600, 59),
            ReadHoldingRegisters(6000, 32),
            ReadHoldingRegisters(6100, 104),
            ReadHoldingRegisters(6300, 386),
            ReadHoldingRegisters(7000, 5),
            ReadHoldingRegisters(11000, 39),
            ReadHoldingRegisters(12000, 164),
        ]

    @property
    def writable_ranges(self) -> List[range]:
        return [
            range(2011, 2066),
            range(2207, 2226),
        ]