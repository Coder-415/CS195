#State population source is is http://worldpopulationreview.com/states/

Population_of_Idaho_in_2020 = 1826156

Population_of_Florida_in_2020 = 21646155

Senators_per_person_in_Idaho = Population_of_Idaho_in_2020/2

Senators_per_person_in_Florida  = Population_of_Florida_in_2020/2

print ("Idaho gets 1 senator per {:,} people".format(Senators_per_person_in_Idaho),
       "while Florida gets 1 senator per {:,} people".format(Senators_per_person_in_Florida))
