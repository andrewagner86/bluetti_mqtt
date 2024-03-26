# Bluetti Bluetooth Protocol V2

These tables contains the currently known adresses, type, name and data length in bytes of the protocol. It also contains information about which Powerstation supports this field.

## Devices

These devices currently use the V2 Protocol:

- AC60
- EP600

## Readable Fields

| Address | Length | Type    | S/P | Range   | Name                         | [AC60] | [EP600] |
| ------- | ------ | ------- | --- | ------- | ---------------------------- | ------ | ------- |
| 102     | 1      | uint    |     | 0/100   | total_battery_soc            | y      | y       |
| 110     | 6      | string  |     |         | device_type                  | y      | y       |
| 116     | 4      | int     |     |         | device_serial_number         | y      | y       |
| 142     | 1      | int     |     |         | output_power                 | ?      | y       |
| 144     | 1      | int     |     |         | input_power                  | ?      | y       |
| 146     | 1      | int     |     |         | grid_power                   | ?      | y       |
| 148     | 1      | int     |     |         | ?                            | ?      | y       |
| 152     | 1      | decimal | 1   |         | total_consumption            | ?      | y       |
| 154     | 1      | decimal | 1   |         | total_feed                   | ?      | y       |
| 156     | 1      | decimal | 1   |         | total_grid_consumption       | ?      | y       |
| 158     | 1      | decimal | 1   |         | total_grid_feed              | ?      | y       |
| 1101    | 6      | string  |     |         | device_type                  | y      | y       |
| 1107    | 4      | int     |     |         | device_serial_number         | y      | y       |
| 1114    | 2      | int     |     |         | system_arm_version           | ?      | y       |
| 1117    | 2      | int     |     |         | system_dsp_version           | ?      | y       |
| 1212    | 1      | int     |     |         | dc_input1_power              | ?      | y       |
| 1213    | 1      | decimal | 1   |         | dc_input1_voltage            | ?      | y       |
| 1214    | 1      | decimal | 1   |         | dc_input1_current            | ?      | y       |
| 1220    | 1      | int     |     |         | dc_input2_power              | ?      | y       |
| 1221    | 1      | decimal | 1   |         | dc_input2_voltage            | ?      | y       |
| 1222    | 1      | decimal | 1   |         | dc_input2_current            | ?      | y       |
| 1228    | 1      | int     |     |         | ac_input_phase1_power        | ?      | y       |
| 1229    | 1      | decimal | 1   |         | ac_input_phase1_voltage      | ?      | y       |
| 1230    | 1      | decimal | 1   |         | ac_input_phase1_current      | ?      | y       |
| 1236    | 1      | int     |     |         | ac_input_phase2_power        | ?      | y       |
| 1237    | 1      | decimal | 1   |         | ac_input_phase2_voltage      | ?      | y       |
| 1238    | 1      | decimal | 1   |         | ac_input_phase2_current      | ?      | y       |
| 1244    | 1      | int     | 1   |         | ac_input_phase3_power        | ?      | y       |
| 1245    | 1      | decimal | 1   |         | ac_input_phase3_voltage      | ?      | y       |
| 1246    | 1      | decimal | 1   |         | ac_input_phase3_current      | ?      | y       |
| 1300    | 1      | decimal | 1   |         | grid_frequency               | ?      | y       |
| 1313    | 1      | int     |     |         | grid_phase1_power            | ?      | y       |
| 1314    | 1      | decimal | 1   |         | grid_phase1_voltage          | ?      | y       |
| 1315    | 1      | decimal | 1   |         | grid_phase1_current          | ?      | y       |
| 1319    | 1      | int     |     |         | grid_phase2_power            | ?      | y       |
| 1320    | 1      | decimal | 1   |         | grid_phase2_voltage          | ?      | y       |
| 1321    | 1      | decimal | 1   |         | grid_phase2_current          | ?      | y       |
| 1325    | 1      | int     |     |         | grid_phase3_power            | ?      | y       |
| 1326    | 1      | decimal | 1   |         | grid_phase3_voltage          | ?      | y       |
| 1327    | 1      | decimal | 1   |         | grid_phase3_current          | ?      | y       |
| 1430    | 1      | int     |     |         | ac_output_phase1_power       | ?      | y       |
| 1431    | 1      | decimal | 1   |         | ac_output_phase1_voltage     | ?      | y       |
| 1432    | 1      | decimal | 1   |         | ac_output_phase1_current     | ?      | y       |
| 1436    | 1      | int     |     |         | ac_output_phase2_power       | ?      | y       |
| 1437    | 1      | decimal | 1   |         | ac_output_phase2_voltage     | ?      | y       |
| 1438    | 1      | decimal | 1   |         | ac_output_phase2_current     | ?      | y       |
| 1442    | 1      | int     |     |         | ac_output_phase3_power       | ?      | y       |
| 1443    | 1      | decimal | 1   |         | ac_output_phase3_voltage     | ?      | y       |
| 1444    | 1      | decimal | 1   |         | ac_output_phase3_current     | ?      | y       |
| 1500    | 1      | decimal | 1   |         | ?_frequency                  | ?      | y       |
| 1510    | 1      | int     |     |         | ?_phase1_power               | ?      | y       |
| 1511    | 1      | decimal | 1   |         | ?_phase1_voltage             | ?      | y       |
| 1512    | 1      | decimal | 1   |         | ?_phase1_current             | ?      | y       |
| 1517    | 1      | int     |     |         | ?_phase2_power               | ?      | y       |
| 1518    | 1      | decimal | 1   |         | ?_phase2_voltage             | ?      | y       |
| 1519    | 1      | decimal | 1   |         | ?_phase2_current             | ?      | y       |
| 1524    | 1      | int     |     |         | ?_phase3_power               | ?      | y       |
| 1525    | 1      | decimal | 1   |         | ?_phase3_voltage             | ?      | y       |
| 1526    | 1      | decimal | 1   |         | ?_phase3_current             | ?      | y       |
| 2001    | 1      | utint   | 0   |         | datetime_year                | ?      | y       |
| 2001    | 1      | utint   | 1   |         | datetime_month               | ?      | y       |
| 2002    | 1      | utint   | 0   |         | datetime_day                 | ?      | y       |
| 2002    | 1      | utint   | 1   |         | datetime_hour                | ?      | y       |
| 2003    | 1      | utint   | 0   |         | datetime_minute              | ?      | y       |
| 2003    | 1      | utint   | 1   |         | datetime_second              | ?      | y       |
| 2011    | 1      | bool    |     |         | main_switch                  | ?      | y       |
| 2022    | 1      | uint    |     | 0/100   | min_battery_soc              | ?      | y       |
| 2023    | 1      | uint    |     | 0/100   | max_battery_soc              | ?      | y       |
| 2029    | 1      | bool    |     |         | time_control_switch          | ?      | y       |
| 2030    | 1      | enum    |     | 1/3     | time_schedule1_mode          | ?      | y       |
| 2031    | 1      | utint   | 0   |         | time_schedule1_start_hour    | ?      | y       |
| 2031    | 1      | utint   | 1   |         | time_schedule1_start_minute  | ?      | y       |
| 2032    | 1      | utint   | 0   |         | time_schedule1_end_hour      | ?      | y       |
| 2032    | 1      | utint   | 1   |         | time_schedule1_end_minute    | ?      | y       |
| 2033    | 1      | enum    |     | 1/3     | time_schedule2_mode          | ?      | y       |
| 2034    | 1      | utint   | 0   |         | time_schedule2_start_hour    | ?      | y       |
| 2034    | 1      | utint   | 1   |         | time_schedule2_start_minute  | ?      | y       |
| 2035    | 1      | utint   | 0   |         | time_schedule2_end_hour      | ?      | y       |
| 2035    | 1      | utint   | 1   |         | time_schedule2_end_minute    | ?      | y       |
| 2036    | 1      | enum    |     | 1/3     | time_schedule3_mode          | ?      | y       |
| 2037    | 1      | utint   | 0   |         | time_schedule3_start_hour    | ?      | y       |
| 2037    | 1      | utint   | 1   |         | time_schedule3_start_minute  | ?      | y       |
| 2038    | 1      | utint   | 0   |         | time_schedule3_end_hour      | ?      | y       |
| 2038    | 1      | utint   | 1   |         | time_schedule3_end_minute    | ?      | y       |
| 2039    | 1      | enum    |     | 1/3     | time_schedule4_mode          | ?      | y       |
| 2040    | 1      | utint   | 0   |         | time_schedule4_start_hour    | ?      | y       |
| 2040    | 1      | utint   | 1   |         | time_schedule4_start_minute  | ?      | y       |
| 2041    | 1      | utint   | 0   |         | time_schedule4_end_hour      | ?      | y       |
| 2041    | 1      | utint   | 1   |         | time_schedule4_end_minute    | ?      | y       |
| 2042    | 1      | enum    |     | 1/3     | time_schedule5_mode          | ?      | y       |
| 2043    | 1      | utint   | 0   |         | time_schedule5_start_hour    | ?      | y       |
| 2043    | 1      | utint   | 1   |         | time_schedule5_start_minute  | ?      | y       |
| 2044    | 1      | utint   | 0   |         | time_schedule5_end_hour      | ?      | y       |
| 2044    | 1      | utint   | 1   |         | time_schedule5_end_minute    | ?      | y       |
| 2045    | 1      | enum    |     | 1/3     | time_schedule6_mode          | ?      | y       |
| 2046    | 1      | utint   | 0   |         | time_schedule6_start_hour    | ?      | y       |
| 2046    | 1      | utint   | 1   |         | time_schedule6_start_minute  | ?      | y       |
| 2047    | 1      | utint   | 0   |         | time_schedule6_end_hour      | ?      | y       |
| 2047    | 1      | utint   | 1   |         | time_schedule6_end_minute    | ?      | y       |
| 2066    | 1      | bool    |     |         | buzzer_switch                | ?      | y       |
| 2207    | 1      | bool    |     |         | charge_from_grid             | ?      | y       |
| 2208    | 1      | bool    |     |         | feed_to_grid                 | ?      | y       |
| 2213    | 1      | uint    |     | 0/15000 | max_input_power_per_phase    | ?      | y       |
| 2214    | 1      | uint    |     | 0/65    | max_input_current_per_phase  | ?      | y       |
| 2215    | 1      | uint    |     | 0/15000 | max_output_power_per_phase   | ?      | y       |
| 2216    | 1      | uint    |     | 0/65    | max_output_current_per_phase | ?      | y       |
| 2225    | 1      | bool    |     |         | grid_self_adjustment         | ?      | y       |
| 2226    | 1      | bool    |     |         | restore_system_switch        | ?      | y       |
| 7002    | 1      | bool    |     |         | battery_heater               | ?      | y       |
| 11014   | 2      | int     |     |         | iot_version                  | ?      | y       |
| 12002   | 16     | string  |     |         | wifi_name                    | ?      | y       |
| 12018   | 48     | string  |     |         | wifi_password                | ?      | y       |

## Readable Battery Fields

| Address | Length | Type    | Name                                 | [AC60] | [EP600] |
| ------- | ------ | ------- | ------------------------------------ | ------ | ------- |
| 6101    | 6      | string  | battery1_type                        | y      | y       |
| 6107    | 4      | int     | battery1_serial_number               | y      | y       |
| 6175    | 2      | int     | battery1_bcu_version                 | y      | y       |
| 6178    | 2      | int     | battery1_bmu_version                 | ?      | y       |
| 6181    | 2      | int     | battery1_safety_module_version       | ?      | y       |
| 6184    | 2      | int     | battery1_high_voltage_module_version | ?      | y       |

## Writeable Fields

| Address | Length | Type    | S/P | Range   | Name                         | [AC60] | [EP600] |
| ------- | ------ | ------- | --- | ------- | ---------------------------- | ------ | ------- |
| 2011    | 1      | bool    |     |         | main_switch                  | ?      | y       |
| 2022    | 1      | uint    |     | 0/100   | min_battery_soc              | ?      | y       |
| 2023    | 1      | uint    |     | 0/100   | max_battery_soc              | ?      | y       |
| 2029    | 1      | bool    |     |         | time_control_switch          | ?      | y       |
| 2030    | 1      | enum    |     | 1/3     | time_schedule1_mode          | ?      | y       |
| 2031    | 1      | utint   | 0   |         | time_schedule1_start_hour    | ?      | y       |
| 2031    | 1      | utint   | 1   |         | time_schedule1_start_minute  | ?      | y       |
| 2032    | 1      | utint   | 0   |         | time_schedule1_end_hour      | ?      | y       |
| 2032    | 1      | utint   | 1   |         | time_schedule1_end_minute    | ?      | y       |
| 2033    | 1      | enum    |     | 1/3     | time_schedule2_mode          | ?      | y       |
| 2034    | 1      | utint   | 0   |         | time_schedule2_start_hour    | ?      | y       |
| 2034    | 1      | utint   | 1   |         | time_schedule2_start_minute  | ?      | y       |
| 2035    | 1      | utint   | 0   |         | time_schedule2_end_hour      | ?      | y       |
| 2035    | 1      | utint   | 1   |         | time_schedule2_end_minute    | ?      | y       |
| 2036    | 1      | enum    |     | 1/3     | time_schedule3_mode          | ?      | y       |
| 2037    | 1      | utint   | 0   |         | time_schedule3_start_hour    | ?      | y       |
| 2037    | 1      | utint   | 1   |         | time_schedule3_start_minute  | ?      | y       |
| 2038    | 1      | utint   | 0   |         | time_schedule3_end_hour      | ?      | y       |
| 2038    | 1      | utint   | 1   |         | time_schedule3_end_minute    | ?      | y       |
| 2039    | 1      | enum    |     | 1/3     | time_schedule4_mode          | ?      | y       |
| 2040    | 1      | utint   | 0   |         | time_schedule4_start_hour    | ?      | y       |
| 2040    | 1      | utint   | 1   |         | time_schedule4_start_minute  | ?      | y       |
| 2041    | 1      | utint   | 0   |         | time_schedule4_end_hour      | ?      | y       |
| 2041    | 1      | utint   | 1   |         | time_schedule4_end_minute    | ?      | y       |
| 2042    | 1      | enum    |     | 1/3     | time_schedule5_mode          | ?      | y       |
| 2043    | 1      | utint   | 0   |         | time_schedule5_start_hour    | ?      | y       |
| 2043    | 1      | utint   | 1   |         | time_schedule5_start_minute  | ?      | y       |
| 2044    | 1      | utint   | 0   |         | time_schedule5_end_hour      | ?      | y       |
| 2044    | 1      | utint   | 1   |         | time_schedule5_end_minute    | ?      | y       |
| 2045    | 1      | enum    |     | 1/3     | time_schedule6_mode          | ?      | y       |
| 2046    | 1      | utint   | 0   |         | time_schedule6_start_hour    | ?      | y       |
| 2046    | 1      | utint   | 1   |         | time_schedule6_start_minute  | ?      | y       |
| 2047    | 1      | utint   | 0   |         | time_schedule6_end_hour      | ?      | y       |
| 2047    | 1      | utint   | 1   |         | time_schedule6_end_minute    | ?      | y       |
| 2066    | 1      | bool    |     |         | buzzer_switch                | ?      | y       |
| 2207    | 1      | bool    |     |         | charge_from_grid             | ?      | y       |
| 2208    | 1      | bool    |     |         | feed_to_grid                 | ?      | y       |
| 2213    | 1      | uint    |     | 0/15000 | max_input_power_per_phase    | ?      | y       |
| 2214    | 1      | uint    |     | 0/65    | max_input_current_per_phase  | ?      | y       |
| 2215    | 1      | uint    |     | 0/15000 | max_output_power_per_phase   | ?      | y       |
| 2216    | 1      | uint    |     | 0/65    | max_output_current_per_phase | ?      | y       |
| 2225    | 1      | bool    |     |         | grid_self_adjustment         | ?      | y       |
| 2226    | 1      | bool    |     |         | restore_system_switch        | ?      | y       |
| 7002    | 1      | bool    |     |         | battery_heater               | ?      | y       |

## data fields

### time_schedule_mode

- 1 - charge
- 2 - discharge
- 3 - unset
  