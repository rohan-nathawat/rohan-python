# Takes user input for the number of seconds.
# Converts seconds to days, hours, minutes, and seconds.
# ======================================================

# Specify conversion constants
SECONDS_PER_DAY = 86400
SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60

# Read input from the user
seconds = int(input("Enter the number of seconds:"))

# Compute days
days = seconds / SECONDS_PER_DAY
seconds = seconds % SECONDS_PER_DAY

# Compute hours
hours = seconds / SECONDS_PER_HOUR
seconds = seconds % SECONDS_PER_HOUR

# Compute minutes
minutes = seconds / SECONDS_PER_MINUTE
seconds = seconds % SECONDS_PER_MINUTE

# Print days, hours, minutes, and seconds
# Format output integers with two digits if 
# necessay add a leading zero.
print("The number of days, hours, minutes, and seconds \
are %d:%02d:%02d:%02d " %(days, hours, minutes, seconds))