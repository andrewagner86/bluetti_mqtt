from typing import List
from ..commands import ReadHoldingRegisters
from .bluetti_device import BluettiDevice
from .struct import DeviceStruct


class PBOX(BluettiDevice):
    def __init__(self, address: str, sn: str):
        self.struct = DeviceStruct()

        self.struct.add_bool_field('bool-field-2000', 2000)
        self.struct.add_bool_field('bool-field-2001', 2001)
        self.struct.add_bool_field('bool-field-2002', 2002)
        self.struct.add_bool_field('bool-field-2003', 2003)
        self.struct.add_bool_field('bool-field-2004', 2004)
        self.struct.add_bool_field('bool-field-2005', 2005)
        self.struct.add_bool_field('bool-field-2006', 2006)
        self.struct.add_bool_field('bool-field-2007', 2007)
        self.struct.add_bool_field('bool-field-2008', 2008)
        self.struct.add_bool_field('bool-field-2009', 2009)
        self.struct.add_bool_field('bool-field-2010', 2010)
        self.struct.add_bool_field('bool-field-2011', 2011)
        self.struct.add_bool_field('bool-field-2012', 2012)
        self.struct.add_bool_field('bool-field-2013', 2013)
        self.struct.add_bool_field('bool-field-2014', 2014)
        self.struct.add_bool_field('bool-field-2015', 2015)
        self.struct.add_bool_field('bool-field-2016', 2016)
        self.struct.add_bool_field('bool-field-2017', 2017)
        self.struct.add_bool_field('bool-field-2018', 2018)
        self.struct.add_bool_field('bool-field-2019', 2019)
        self.struct.add_bool_field('bool-field-2020', 2020)
        self.struct.add_bool_field('bool-field-2021', 2021)

        self.struct.add_bool_field('bool-field-2024', 2024)
        self.struct.add_bool_field('bool-field-2025', 2025)
        self.struct.add_bool_field('bool-field-2026', 2026)
        self.struct.add_bool_field('bool-field-2027', 2027)
        self.struct.add_bool_field('bool-field-2028', 2028)
        self.struct.add_bool_field('bool-field-2029', 2029)
        self.struct.add_bool_field('bool-field-2030', 2030)
        self.struct.add_bool_field('bool-field-2031', 2031)
        self.struct.add_bool_field('bool-field-2032', 2032)
        self.struct.add_bool_field('bool-field-2033', 2033)
        self.struct.add_bool_field('bool-field-2034', 2034)
        self.struct.add_bool_field('bool-field-2035', 2035)
        self.struct.add_bool_field('bool-field-2036', 2036)
        self.struct.add_bool_field('bool-field-2037', 2037)
        self.struct.add_bool_field('bool-field-2038', 2038)
        self.struct.add_bool_field('bool-field-2039', 2039)
        self.struct.add_bool_field('bool-field-2040', 2040)
        self.struct.add_bool_field('bool-field-2041', 2041)
        self.struct.add_bool_field('bool-field-2042', 2042)
        self.struct.add_bool_field('bool-field-2043', 2043)
        self.struct.add_bool_field('bool-field-2044', 2044)
        self.struct.add_bool_field('bool-field-2045', 2045)
        self.struct.add_bool_field('bool-field-2046', 2046)
        self.struct.add_bool_field('bool-field-2047', 2047)
        self.struct.add_bool_field('bool-field-2048', 2048)
        self.struct.add_bool_field('bool-field-2049', 2049)
        self.struct.add_bool_field('bool-field-2050', 2050)
        self.struct.add_bool_field('bool-field-2051', 2051)
        self.struct.add_bool_field('bool-field-2052', 2052)
        self.struct.add_bool_field('bool-field-2053', 2053)
        self.struct.add_bool_field('bool-field-2054', 2054)
        self.struct.add_bool_field('bool-field-2055', 2055)
        self.struct.add_bool_field('bool-field-2056', 2056)
        self.struct.add_bool_field('bool-field-2057', 2057)
        self.struct.add_bool_field('bool-field-2058', 2058)
        self.struct.add_bool_field('bool-field-2059', 2059)
        self.struct.add_bool_field('bool-field-2060', 2060)
        self.struct.add_bool_field('bool-field-2061', 2061)
        self.struct.add_bool_field('bool-field-2062', 2062)
        self.struct.add_bool_field('bool-field-2063', 2063)
        self.struct.add_bool_field('bool-field-2064', 2064)
        self.struct.add_bool_field('bool-field-2065', 2065)
        self.struct.add_bool_field('bool-field-2066', 2066)
        self.struct.add_bool_field('bool-field-2067', 2067)
        self.struct.add_bool_field('bool-field-2068', 2068)
        self.struct.add_bool_field('bool-field-2069', 2069)
        self.struct.add_bool_field('bool-field-2070', 2070)
        self.struct.add_bool_field('bool-field-2071', 2071)
        self.struct.add_bool_field('bool-field-2072', 2072)
        self.struct.add_bool_field('bool-field-2073', 2073)
        self.struct.add_bool_field('bool-field-2074', 2074)
        self.struct.add_bool_field('bool-field-2075', 2075)
        self.struct.add_bool_field('bool-field-2076', 2076)
        self.struct.add_bool_field('bool-field-2077', 2077)
        self.struct.add_bool_field('bool-field-2078', 2078)
        self.struct.add_bool_field('bool-field-2079', 2079)
        self.struct.add_bool_field('bool-field-2080', 2080)
        self.struct.add_bool_field('bool-field-2081', 2081)
        self.struct.add_bool_field('bool-field-2082', 2082)
        self.struct.add_bool_field('bool-field-2083', 2083)
        self.struct.add_bool_field('bool-field-2084', 2084)
        self.struct.add_bool_field('bool-field-2085', 2085)
        self.struct.add_bool_field('bool-field-2086', 2086)
        self.struct.add_bool_field('bool-field-2087', 2087)
        self.struct.add_bool_field('bool-field-2088', 2088)

        self.struct.add_bool_field('bool-field-2200', 2200)
        self.struct.add_bool_field('bool-field-2201', 2201)
        self.struct.add_bool_field('bool-field-2202', 2202)
        self.struct.add_bool_field('bool-field-2203', 2203)
        self.struct.add_bool_field('bool-field-2204', 2204)
        self.struct.add_bool_field('bool-field-2205', 2205)
        self.struct.add_bool_field('bool-field-2206', 2206)
        self.struct.add_bool_field('bool-field-2209', 2209)
        self.struct.add_bool_field('bool-field-2210', 2210)
        self.struct.add_bool_field('bool-field-2211', 2211)
        self.struct.add_bool_field('bool-field-2212', 2212)

        self.struct.add_bool_field('bool-field-2217', 2217)
        self.struct.add_bool_field('bool-field-2218', 2218)
        self.struct.add_bool_field('bool-field-2219', 2219)
        self.struct.add_bool_field('bool-field-2220', 2220)
        self.struct.add_bool_field('bool-field-2221', 2221)
        self.struct.add_bool_field('bool-field-2222', 2222)
        self.struct.add_bool_field('bool-field-2223', 2223)
        self.struct.add_bool_field('bool-field-2224', 2224)
        self.struct.add_bool_field('bool-field-2227', 2227)
        self.struct.add_bool_field('bool-field-2228', 2228)
        self.struct.add_bool_field('bool-field-2229', 2229)
        self.struct.add_bool_field('bool-field-2230', 2230)
        self.struct.add_bool_field('bool-field-2231', 2231)
        self.struct.add_bool_field('bool-field-2232', 2232)
        self.struct.add_bool_field('bool-field-2233', 2233)
        self.struct.add_bool_field('bool-field-2234', 2234)
        self.struct.add_bool_field('bool-field-2235', 2235)
        self.struct.add_bool_field('bool-field-2236', 2236)
        self.struct.add_bool_field('bool-field-2237', 2237)
        self.struct.add_bool_field('bool-field-2238', 2238)
        self.struct.add_bool_field('bool-field-2239', 2239)
        self.struct.add_bool_field('bool-field-2240', 2240)
        self.struct.add_bool_field('bool-field-2241', 2241)
        self.struct.add_bool_field('bool-field-2242', 2242)

        # overview
        # self.struct.add_uint_field('total_battery_soc', 102, (0,100))
        # self.struct.add_swap_string_field('device_type', 110, 6)
        self.struct.add_int_field('output_power', 142)
        self.struct.add_int_field('input_power', 144)
        self.struct.add_int_field('grid_power', 146)
        # self.struct.add_uint_field('uint_148', 148)
        # self.struct.add_decimal_field('total_consumption', 152, 1)
        # self.struct.add_decimal_field('total_feed', 154, 1)
        # self.struct.add_decimal_field('total_grid_consumption', 156, 1)
        # self.struct.add_decimal_field('total_grid_feed', 158, 1)

        # device specific things
        # self.struct.add_swap_string_field('device_type', 1101, 6)
        # self.struct.add_version_field('system_arm_version', 1114)
        # self.struct.add_version_field('system_dsp_version', 1117)

        # feed
        self.struct.add_int_field('dc_input_1_power', 1212)
        # self.struct.add_decimal_field('dc_input_1_voltage', 1213, 1)
        # self.struct.add_decimal_field('dc_input_1_current', 1214, 1)
        self.struct.add_int_field('dc_input_2_power', 1220)
        # self.struct.add_decimal_field('dc_input_2_voltage', 1221, 1)
        # self.struct.add_decimal_field('dc_input_2_current', 1222, 1)
        self.struct.add_int_field('ac_input_phase1_power', 1228)
        # self.struct.add_decimal_field('ac_input_phase1_voltage', 1229, 1)
        # self.struct.add_decimal_field('ac_input_phase1_current', 1230, 1)
        self.struct.add_int_field('ac_input_phase2_power', 1236)
        # self.struct.add_decimal_field('ac_input_phase2_voltage', 1237, 1)
        # self.struct.add_decimal_field('ac_input_phase2_current', 1238, 1)
        self.struct.add_int_field('ac_input_phase3_power', 1244)
        # self.struct.add_decimal_field('ac_input_phase3_voltage', 1245, 1)
        # self.struct.add_decimal_field('ac_input_phase3_current', 1246, 1)

        # grid
        # self.struct.add_decimal_field('grid_frequency', 1300, 1)
        self.struct.add_int_field('grid_phase1_power', 1313)
        # self.struct.add_decimal_field('grid_phase1_voltage', 1314, 1)
        # self.struct.add_decimal_field('grid_phase1_current', 1315, 1)
        self.struct.add_int_field('grid_phase2_power', 1319)
        # self.struct.add_decimal_field('grid_phase2_voltage', 1320, 1)
        # self.struct.add_decimal_field('grid_phase2_current', 1321, 1)
        self.struct.add_int_field('grid_phase3_power', 1325)
        # self.struct.add_decimal_field('grid_phase3_voltage', 1326, 1)
        # self.struct.add_decimal_field('grid_phase3_current', 1327, 1)

        # consumption
        self.struct.add_int_field('ac_output_phase1_power', 1430)
        # self.struct.add_decimal_field('ac_output_phase1_voltage', 1431, 1)
        # self.struct.add_decimal_field('ac_output_phase1_current', 1432, 1)
        self.struct.add_int_field('ac_output_phase2_power', 1436)
        # self.struct.add_decimal_field('ac_output_phase2_voltage', 1437, 1)
        # self.struct.add_decimal_field('ac_output_phase2_current', 1438, 1)
        self.struct.add_int_field('ac_output_phase3_power', 1442)
        # self.struct.add_decimal_field('ac_output_phase3_voltage', 1443, 1)
        # self.struct.add_decimal_field('ac_output_phase3_current', 1444, 1)
        
        # unknown
        # self.struct.add_decimal_field('unknown_frequency', 1500, 1)
        self.struct.add_int_field('unknown_phase1_power', 1510)
        # self.struct.add_decimal_field('unknown_phase1_voltage', 1511, 1)
        # self.struct.add_decimal_field('unknown_phase1_current', 1512, 1)
        self.struct.add_int_field('unknown_phase2_power', 1517)
        # self.struct.add_decimal_field('unknown_phase2_voltage', 1518, 1)
        # self.struct.add_decimal_field('unknown_phase2_current', 1519, 1)
        self.struct.add_int_field('unknown_phase3_power', 1524)
        # self.struct.add_decimal_field('unknown_phase3_voltage', 1524, 1)
        # self.struct.add_decimal_field('unknown_phase3_current', 1526, 1)

        # battery
        # self.struct.add_uint_field('uint_2001', 2001)
        # self.struct.add_uint_field('uint_2002', 2002)
        # self.struct.add_uint_field('uint_2003', 2003)
        # self.struct.add_uint_field('min_battery_soc', 2022)
        # self.struct.add_uint_field('max_battery_soc', 2023)
        # self.struct.add_uint_field('uint_2032', 2032)
        
        # advanced
        # self.struct.add_uint_field('uint_2200', 2200)
        # self.struct.add_uint_field('uint_2201', 2201)
        # self.struct.add_uint_field('uint_2202', 2202)
        # self.struct.add_uint_field('uint_2203', 2203)
        # self.struct.add_uint_field('max_input_per_phase_power', 2213)
        # self.struct.add_uint_field('max_input_per_phase_current', 2214)
        # self.struct.add_uint_field('max_output_per_phase_power', 2215)
        # self.struct.add_uint_field('max_output_per_phase_current', 2216)

        # iot
        # self.struct.add_version_field('iot_version', 11014)

        # wifi
        # self.struct.add_swap_string_field('wifi_name', 12002, 16)
        # self.struct.add_swap_string_field('wifi_password', 12018, 48)


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
            # ReadHoldingRegisters(700, 6),
            # ReadHoldingRegisters(720, 49),
            # ReadHoldingRegisters(1100, 54),
            ReadHoldingRegisters(1200, 90),
            ReadHoldingRegisters(1300, 31),
            ReadHoldingRegisters(1400, 48),
            ReadHoldingRegisters(1500, 30),
            # ReadHoldingRegisters(1600, 14),
            # ReadHoldingRegisters(1700, 10),
            # ReadHoldingRegisters(2000, 89),
            # ReadHoldingRegisters(2200, 43),
            # ReadHoldingRegisters(2300, 36),
            # ReadHoldingRegisters(2400, 50),
            # ReadHoldingRegisters(3000, 27),
            # ReadHoldingRegisters(3500, 48),
            # ReadHoldingRegisters(3600, 59),
            # ReadHoldingRegisters(6000, 32),
            # ReadHoldingRegisters(6100, 104),
            # ReadHoldingRegisters(6300, 386),
            # ReadHoldingRegisters(7000, 5),
            # ReadHoldingRegisters(11000, 39),
            # ReadHoldingRegisters(12000, 164),
        ]
