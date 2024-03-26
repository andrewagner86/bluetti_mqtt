from typing import List
from ..commands import ReadHoldingRegisters
from .bluetti_device import BluettiDevice
from .struct import DeviceStruct


class PBOX(BluettiDevice):
    def __init__(self, address: str, sn: str):
        self.struct = DeviceStruct()

        self.struct.add_uint_field('uint-field-100', 100) # 6003
        self.struct.add_uint_field('uint-field-101', 101) # 6004
        self.struct.add_uint_field('uint-field-103', 103) # 6009
        self.struct.add_uint_field('uint-field-123', 123) # 1131
        self.struct.add_uint_field('uint-field-125', 125) # 6005
        self.struct.add_uint_field('uint-field-148', 148)
        self.struct.add_uint_field('uint-field-162', 162)
        self.struct.add_uint_field('uint-field-1131', 1131) # 123
        self.struct.add_uint_field('uint-field-1200', 1200)
        self.struct.add_uint_field('uint-field-1202', 1202)
        self.struct.add_uint_field('uint-field-1301', 1301)
        self.struct.add_uint_field('uint-field-1303', 1303)
        self.struct.add_uint_field('uint-field-1305', 1305)
        self.struct.add_uint_field('uint-field-1420', 1420)
        self.struct.add_uint_field('uint-field-1422', 1422)
        self.struct.add_uint_field('uint-field-1509', 1509)
        self.struct.add_uint_field('uint-field-1516', 1516)
        self.struct.add_uint_field('uint-field-1523', 1523)
        self.struct.add_uint_field('uint-field-6003', 6003) # 100
        self.struct.add_uint_field('uint-field-6004', 6004) # 101
        self.struct.add_uint_field('uint-field-6005', 6005) # 125
        # self.struct.add_uint_field('uint-field-6006', 6006)
        self.struct.add_uint_field('uint-field-6007', 6007)
        # self.struct.add_uint_field('uint-field-6008', 6008)
        self.struct.add_uint_field('uint-field-6009', 6009) # 103
        self.struct.add_uint_field('uint-field-6010', 6010)
        self.struct.add_uint_field('uint-field-6011', 6011)
        self.struct.add_uint_field('uint-field-6012', 6012)
        self.struct.add_uint_field('uint-field-6019', 6019) # 6133
        self.struct.add_uint_field('uint-field-6111', 6111)
        self.struct.add_uint_field('uint-field-6112', 6112)
        self.struct.add_uint_field('uint-field-6113', 6113)
        self.struct.add_uint_field('uint-field-6116', 6116)
        self.struct.add_uint_field('uint-field-6117', 6117)
        self.struct.add_uint_field('uint-field-6118', 6118)
        self.struct.add_uint_field('uint-field-6119', 6119)
        # self.struct.add_uint_field('uint-field-6120', 6120)
        self.struct.add_uint_field('uint-field-6121', 6121)
        # self.struct.add_uint_field('uint-field-6122', 6122)
        self.struct.add_uint_field('uint-field-6123', 6123)
        # self.struct.add_uint_field('uint-field-6124', 6124)
        self.struct.add_uint_field('uint-field-6125', 6125)
        self.struct.add_uint_field('uint-field-6133', 6133) # 6019
        self.struct.add_uint_field('uint-field-6137', 6137)
        self.struct.add_uint_field('uint-field-6139', 6139)
        self.struct.add_uint_field('uint-field-11026', 11026)

        # # overview
        # # self.struct.add_uint_field('total_battery_soc', 102, (0,100))
        # # self.struct.add_swap_string_field('device_type', 110, 6)
        # self.struct.add_int_field('output_power', 142)
        # self.struct.add_int_field('input_power', 144)
        # self.struct.add_int_field('grid_power', 146)
        # # self.struct.add_uint_field('uint_148', 148)
        # # self.struct.add_decimal_field('total_consumption', 152, 1)
        # # self.struct.add_decimal_field('total_feed', 154, 1)
        # # self.struct.add_decimal_field('total_grid_consumption', 156, 1)
        # # self.struct.add_decimal_field('total_grid_feed', 158, 1)

        # # device specific things
        # # self.struct.add_swap_string_field('device_type', 1101, 6)
        # # self.struct.add_version_field('system_arm_version', 1114)
        # # self.struct.add_version_field('system_dsp_version', 1117)

        # # feed
        # self.struct.add_int_field('dc_input_1_power', 1212)
        # # self.struct.add_decimal_field('dc_input_1_voltage', 1213, 1)
        # # self.struct.add_decimal_field('dc_input_1_current', 1214, 1)
        # self.struct.add_int_field('dc_input_2_power', 1220)
        # # self.struct.add_decimal_field('dc_input_2_voltage', 1221, 1)
        # # self.struct.add_decimal_field('dc_input_2_current', 1222, 1)
        # self.struct.add_int_field('ac_input_phase1_power', 1228)
        # # self.struct.add_decimal_field('ac_input_phase1_voltage', 1229, 1)
        # # self.struct.add_decimal_field('ac_input_phase1_current', 1230, 1)
        # self.struct.add_int_field('ac_input_phase2_power', 1236)
        # # self.struct.add_decimal_field('ac_input_phase2_voltage', 1237, 1)
        # # self.struct.add_decimal_field('ac_input_phase2_current', 1238, 1)
        # self.struct.add_int_field('ac_input_phase3_power', 1244)
        # # self.struct.add_decimal_field('ac_input_phase3_voltage', 1245, 1)
        # # self.struct.add_decimal_field('ac_input_phase3_current', 1246, 1)

        # # grid
        # # self.struct.add_decimal_field('grid_frequency', 1300, 1)
        # self.struct.add_int_field('grid_phase1_power', 1313)
        # # self.struct.add_decimal_field('grid_phase1_voltage', 1314, 1)
        # # self.struct.add_decimal_field('grid_phase1_current', 1315, 1)
        # self.struct.add_int_field('grid_phase2_power', 1319)
        # # self.struct.add_decimal_field('grid_phase2_voltage', 1320, 1)
        # # self.struct.add_decimal_field('grid_phase2_current', 1321, 1)
        # self.struct.add_int_field('grid_phase3_power', 1325)
        # # self.struct.add_decimal_field('grid_phase3_voltage', 1326, 1)
        # # self.struct.add_decimal_field('grid_phase3_current', 1327, 1)

        # # consumption
        # self.struct.add_int_field('ac_output_phase1_power', 1430)
        # # self.struct.add_decimal_field('ac_output_phase1_voltage', 1431, 1)
        # # self.struct.add_decimal_field('ac_output_phase1_current', 1432, 1)
        # self.struct.add_int_field('ac_output_phase2_power', 1436)
        # # self.struct.add_decimal_field('ac_output_phase2_voltage', 1437, 1)
        # # self.struct.add_decimal_field('ac_output_phase2_current', 1438, 1)
        # self.struct.add_int_field('ac_output_phase3_power', 1442)
        # # self.struct.add_decimal_field('ac_output_phase3_voltage', 1443, 1)
        # # self.struct.add_decimal_field('ac_output_phase3_current', 1444, 1)
        
        # # unknown
        # # self.struct.add_decimal_field('unknown_frequency', 1500, 1)
        # self.struct.add_int_field('unknown_phase1_power', 1510)
        # # self.struct.add_decimal_field('unknown_phase1_voltage', 1511, 1)
        # # self.struct.add_decimal_field('unknown_phase1_current', 1512, 1)
        # self.struct.add_int_field('unknown_phase2_power', 1517)
        # # self.struct.add_decimal_field('unknown_phase2_voltage', 1518, 1)
        # # self.struct.add_decimal_field('unknown_phase2_current', 1519, 1)
        # self.struct.add_int_field('unknown_phase3_power', 1524)
        # # self.struct.add_decimal_field('unknown_phase3_voltage', 1524, 1)
        # # self.struct.add_decimal_field('unknown_phase3_current', 1526, 1)

        # # battery
        # # self.struct.add_uint_field('uint_2001', 2001)
        # # self.struct.add_uint_field('uint_2002', 2002)
        # # self.struct.add_uint_field('uint_2003', 2003)
        # # self.struct.add_uint_field('min_battery_soc', 2022)
        # # self.struct.add_uint_field('max_battery_soc', 2023)
        # # self.struct.add_uint_field('uint_2032', 2032)
        
        # # advanced
        # # self.struct.add_uint_field('uint_2200', 2200)
        # # self.struct.add_uint_field('uint_2201', 2201)
        # # self.struct.add_uint_field('uint_2202', 2202)
        # # self.struct.add_uint_field('uint_2203', 2203)
        # # self.struct.add_uint_field('max_input_per_phase_power', 2213)
        # # self.struct.add_uint_field('max_input_per_phase_current', 2214)
        # # self.struct.add_uint_field('max_output_per_phase_power', 2215)
        # # self.struct.add_uint_field('max_output_per_phase_current', 2216)

        # # iot
        # # self.struct.add_version_field('iot_version', 11014)

        # # wifi
        # # self.struct.add_swap_string_field('wifi_name', 12002, 16)
        # # self.struct.add_swap_string_field('wifi_password', 12018, 48)

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
