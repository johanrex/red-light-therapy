# Dose calculator for for photobiomodulation
import os
import math

print("Photobiomodulation (Red Light Therapy) Dose Calculator")
print("  - Instructions: https://github.com/sharpe5/red-light-therapy/")
print("")
print("User set variables:")

watts_per_meter = 160
# Note: This is 10x the value in mW/cm2 (milliwatts to watts is 1000, and 10000 square centimetres in a in metre.
print("  - What does our TES-1333 light meter read in W/m2? " + str(watts_per_meter))

# How many seconds we spend at each 45 degree angle. This is the *only* variable we have to manually change.
total_seconds_per_eighth = 60
print("  - Total seconds spent standing at each 45 degree angle: " + str(total_seconds_per_eighth))

print("")
print("Calculated (intermediate):")
total_seconds = total_seconds_per_eighth * 8
print("  - Total number of 45 degree angles in 360 degreese: 8")

print("  - Total seconds to rotate 360 degrees: " + str(total_seconds))
print("  - Total minutes to rotate 360 degrees: " + str(total_seconds/60))

milliwatts_per_centimeter = watts_per_meter / 10
# each square centimetre of skin gets three exposures: facing panel, previous (45 degrees less), next (45 degrees more)
# first position, facing straight at the panel
total_joules_position_1 = total_seconds_per_eighth  *milliwatts_per_centimeter / 1000
# next position, rotated 45 more degrees facing the panel
total_joules_position_2 = total_joules_position_1 * math.cos(math.radians(45))
# previous position, rotated 45 less degrees facing the panel
total_joules_position_3 = total_joules_position_1 * math.cos(math.radians(45))
total_joules_this = total_joules_position_1 + total_joules_position_2 + total_joules_position_3

print("  - Total joules/centimetre2 this: " + str(total_joules_this))

# What we would get from a full body light pod from www.NovoThor.com in N minutes.
time_minutes = 12
print("  - Total minutes in NovoThor: " + str(time_minutes/60))
time_seconds = 60*time_minutes
millijoules_per_centimetre = 16.666
print("  - Light intensity in NovoThor [mW/cm2]: " + str(millijoules_per_centimetre))
total_joules_novothor = time_seconds * millijoules_per_centimetre / 1000
print("  - Total joules/centimetre2 NovoThor: " + str(total_joules_novothor))

percent_this_of_novothor = total_joules_this / total_joules_novothor * 100

print("")
print("Calculated (final value):")
print("  - Percent dose compared to one full-body NovoThor session of " + str(time_minutes) + " minutes @ "
      + str(millijoules_per_centimetre) + " mW/cm2: " + str(round(percent_this_of_novothor, 1)) + "%")