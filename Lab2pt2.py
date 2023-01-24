# Estimate population

# Constants
birth_rate = 1/7  # birth every 7 seconds
death_rate = 1/13  # death every 13 seconds
immigrant_rate = 1/35  # new immigrant every 35 seconds

# Initial population
population = 334205119

# Time elapsed
days = 19  # January 20th - January 1st
hours = 23  # 12:15:20 PM - 01:00:00 AM
minutes = 15
seconds = 20

# Calculate population growth
population += days * ((birth_rate - death_rate + immigrant_rate) * 24 * 60 * 60)
population += hours * ((birth_rate - death_rate + immigrant_rate) * 60 * 60)
population += minutes * ((birth_rate - death_rate + immigrant_rate) * 60)
population += seconds * (birth_rate - death_rate + immigrant_rate)

# Print estimated population
print(f'Estimated population on January 20, 2022 at 12:15:20: {population}')
