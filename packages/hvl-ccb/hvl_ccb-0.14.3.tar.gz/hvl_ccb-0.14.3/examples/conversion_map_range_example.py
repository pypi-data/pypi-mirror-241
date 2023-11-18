#  Copyright (c) ETH Zurich, SIS ID and HVL D-ITET
#
from hvl_ccb.utils.conversion import MapBitAsymRange, MapBitSymRange, MapRanges

# conversion between 4-20 mA and 0-10 V
signal_conv = MapRanges((4, 20), (0, 10), float, float)
value_1 = 4
print(f"{value_1} mA is converted to {signal_conv.convert_to_range2(value_1)} V")
value_2 = 5
print(f"{value_2} V is converted to {signal_conv.convert_to_range1(value_2)} mA")


# conversion between asym-bit-range and float
bit = 10
signal_conv = MapBitAsymRange(10, bit)
value_1 = 3.2
print(f"{value_1} is {signal_conv.convert_to_bits(value_1)} as {bit} bit value")
value_2 = 987
print(f"{value_2} ({bit} bit value) is {signal_conv.convert_to_number(value_2)}")
value_3 = 0
print(f"{value_3} is {signal_conv.convert_to_bits(value_3)} as {bit} bit value")

# conversion between sym-bit-range and float
signal_conv = MapBitSymRange(5, bit)
value_1 = 3.2
print(f"{value_1} is {signal_conv.convert_to_bits(value_1)} as {bit} bit value")
value_2 = 245
print(f"{value_2} ({bit} bit value) is {signal_conv.convert_to_number(value_2)}")
value_3 = 0
print(f"{value_3} is {signal_conv.convert_to_bits(value_3)} as {bit} bit value")
