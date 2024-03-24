from typing import List
from ..commands import ReadHoldingRegisters
from .base.bluetti_device import BluettiDevice
from .base.struct import DeviceStruct


class PBOX(BluettiDevice):
    def __init__(self, address: str, sn: str):
        self.struct = DeviceStruct()

        # overview
        self.struct.add_uint_field('total_battery_soc', 102, (0,100))
        self.struct.add_swap_string_field('device_type', 110, 6)
        self.struct.add_uint_field('uint_142', 142)
        self.struct.add_uint_field('uint_144', 144)
        self.struct.add_uint_field('uint_146', 146)
        self.struct.add_uint_field('uint_148', 148)
        self.struct.add_decimal_field('total_consumption', 152, 1)
        self.struct.add_decimal_field('total_feed', 154, 1)
        self.struct.add_decimal_field('total_grid_consumption', 156, 1)
        self.struct.add_decimal_field('total_grid_feed', 158, 1)

        # device specific things
        self.struct.add_swap_string_field('device_type', 1101, 6)
        self.struct.add_version_field('system_arm_version', 1114)
        self.struct.add_version_field('system_dsp_version', 1117)

        # feed
        self.struct.add_uint_field('dc_input_1_power', 1212)
        self.struct.add_decimal_field('dc_input_1_voltage', 1213, 1)
        self.struct.add_decimal_field('dc_input_1_current', 1214, 1)
        self.struct.add_uint_field('dc_input_2_power', 1220)
        self.struct.add_decimal_field('dc_input_2_voltage', 1221, 1)
        self.struct.add_decimal_field('dc_input_2_current', 1222, 1)
        self.struct.add_uint_field('ac_input_phase1_power', 1228)
        self.struct.add_decimal_field('ac_input_phase1_voltage', 1229, 1)
        self.struct.add_decimal_field('ac_input_phase1_current', 1230, 1)
        self.struct.add_uint_field('ac_input_phase2_power', 1236)
        self.struct.add_decimal_field('ac_input_phase2_voltage', 1237, 1)
        self.struct.add_decimal_field('ac_input_phase2_current', 1238, 1)
        self.struct.add_uint_field('ac_input_phase3_power', 1244)
        self.struct.add_decimal_field('ac_input_phase3_voltage', 1245, 1)
        self.struct.add_decimal_field('ac_input_phase3_current', 1246, 1)

        # grid
        self.struct.add_decimal_field('grid_frequency', 1300, 1)
        self.struct.add_uint_field('uint_1301', 1301)
        self.struct.add_uint_field('uint_1302', 1302)
        self.struct.add_uint_field('uint_1303', 1303)
        self.struct.add_uint_field('uint_1304', 1304)
        self.struct.add_uint_field('uint_1305', 1305)
        self.struct.add_uint_field('uint_1306', 1306)
        self.struct.add_uint_field('uint_1307', 1307)
        self.struct.add_uint_field('uint_1308', 1308)
        self.struct.add_uint_field('uint_1309', 1309)
        self.struct.add_uint_field('uint_1310', 1310)
        self.struct.add_uint_field('uint_1311', 1311)
        self.struct.add_uint_field('uint_1312', 1312)
        self.struct.add_bool_field('bool_1301', 1301)
        self.struct.add_bool_field('bool_1302', 1302)
        self.struct.add_bool_field('bool_1303', 1303)
        self.struct.add_bool_field('bool_1304', 1304)
        self.struct.add_bool_field('bool_1305', 1305)
        self.struct.add_bool_field('bool_1306', 1306)
        self.struct.add_bool_field('bool_1307', 1307)
        self.struct.add_bool_field('bool_1308', 1308)
        self.struct.add_bool_field('bool_1309', 1309)
        self.struct.add_bool_field('bool_1310', 1310)
        self.struct.add_bool_field('bool_1311', 1311)
        self.struct.add_bool_field('bool_1312', 1312)
        self.struct.add_uint_field('grid_phase1_power', 1313)
        self.struct.add_decimal_field('grid_phase1_voltage', 1314, 1)
        self.struct.add_decimal_field('grid_phase1_current', 1315, 1)
        self.struct.add_uint_field('uint_1316', 1316)
        self.struct.add_uint_field('uint_1317', 1317)
        self.struct.add_uint_field('uint_1318', 1318)
        self.struct.add_bool_field('bool_1316', 1316)
        self.struct.add_bool_field('bool_1317', 1317)
        self.struct.add_bool_field('bool_1318', 1318)
        self.struct.add_uint_field('grid_phase2_power', 1319)
        self.struct.add_decimal_field('grid_phase2_voltage', 1320, 1)
        self.struct.add_decimal_field('grid_phase2_current', 1321, 1)
        self.struct.add_uint_field('uint_1322', 1322)
        self.struct.add_uint_field('uint_1323', 1323)
        self.struct.add_uint_field('uint_1324', 1323)
        self.struct.add_bool_field('bool_1322', 1322)
        self.struct.add_bool_field('bool_1323', 1323)
        self.struct.add_bool_field('bool_1324', 1324)
        self.struct.add_uint_field('grid_phase3_power', 1325)
        self.struct.add_decimal_field('grid_phase3_voltage', 1326, 1)
        self.struct.add_decimal_field('grid_phase3_current', 1327, 1)
        self.struct.add_uint_field('uint_1328', 1328)
        self.struct.add_uint_field('uint_1329', 1329)
        self.struct.add_uint_field('uint_1330', 1330)
        self.struct.add_bool_field('bool_1328', 1328)
        self.struct.add_bool_field('bool_1329', 1329)
        self.struct.add_bool_field('bool_1330', 1330)

        # consumption
        self.struct.add_uint_field('ac_output_phase1_power', 1430)
        self.struct.add_decimal_field('ac_output_phase1_voltage', 1431, 1)
        self.struct.add_decimal_field('ac_output_phase1_current', 1432, 1)
        self.struct.add_uint_field('ac_output_phase2_power', 1436)
        self.struct.add_decimal_field('ac_output_phase2_voltage', 1437, 1)
        self.struct.add_decimal_field('ac_output_phase2_current', 1438, 1)
        self.struct.add_uint_field('ac_output_phase3_power', 1442)
        self.struct.add_decimal_field('ac_output_phase3_voltage', 1443, 1)
        self.struct.add_decimal_field('ac_output_phase3_current', 1444, 1)
        
        # unknown
        self.struct.add_decimal_field('unknown_frequency', 1500, 1)
        self.struct.add_uint_field('unknown_phase1_power', 1510)
        self.struct.add_decimal_field('unknown_phase1_voltage', 1511, 1)
        self.struct.add_decimal_field('unknown_phase1_current', 1512, 1)
        self.struct.add_uint_field('unknown_phase2_power', 1517)
        self.struct.add_decimal_field('unknown_phase2_voltage', 1518, 1)
        self.struct.add_decimal_field('unknown_phase2_current', 1519, 1)
        self.struct.add_uint_field('unknown_phase3_power', 1524)
        self.struct.add_decimal_field('unknown_phase3_voltage', 1524, 1)
        self.struct.add_decimal_field('unknown_phase3_current', 1526, 1)

        # battery
        self.struct.add_uint_field('uint_2001', 2001)
        self.struct.add_uint_field('uint_2002', 2002)
        self.struct.add_uint_field('uint_2003', 2003)
        self.struct.add_uint_field('min_battery_soc', 2022)
        self.struct.add_uint_field('max_battery_soc', 2023)
        self.struct.add_uint_field('uint_2032', 2032)
        
        # advanced
        self.struct.add_uint_field('uint_2200', 2200)
        self.struct.add_uint_field('uint_2201', 2201)
        self.struct.add_uint_field('uint_2202', 2202)
        self.struct.add_uint_field('uint_2203', 2203)
        self.struct.add_uint_field('max_input_per_phase_power', 2213)
        self.struct.add_uint_field('max_input_per_phase_current', 2214)
        self.struct.add_uint_field('max_output_per_phase_power', 2215)
        self.struct.add_uint_field('max_output_per_phase_current', 2216)

        # iot
        self.struct.add_version_field('iot_version', 11014)

        # wifi
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
