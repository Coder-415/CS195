#Sources - https://en.wikipedia.org/wiki/United_Nations_Security_Council; data.worldbank.org

China_Population = 1392730000
US_Population = 327164300
Russia_Population = 144478050
France_Population = 66987240
UK_Population = 66488990

UNPSM_Population = (China_Population+US_Population+Russia_Population+France_Population+UK_Population)
UNPSM_Minus_China = (US_Population+Russia_Population+France_Population+UK_Population)

World_Population = 7594270360


print("Per Wikipedia's page on the United Nations Security Council, the five permanent members of the United Nations Security Council are China, the United States, Russia,\nFrance, and the United Kingdom. These were the principal powers which won World War Two, after which the United Nation Security Council was established. According\nto the World Bank's population data for 2018, these countries had a combined population of {:,}. Given that the world's population was estimated to be\n{:,} in 2018, that represents {:%} of the world's population. The four members not including China only have {:%} of the world' population. India,\nwhich is not a member of the United Nations Security Council, has twice as many people as those four members combined.".format(UNPSM_Population,World_Population,UNPSM_Population/World_Population,UNPSM_Minus_China/World_Population))

