current_population = 380123456
born = 6
dies = 12
immigrates = 40
seconds_every_year = (365 * 24 * 60 * 60)
three_year_pop = seconds_every_year * 3

estimate_pop = current_population + (three_year_pop/born) + (three_year_pop/immigrates) - (three_year_pop/dies)
print(estimate_pop) 