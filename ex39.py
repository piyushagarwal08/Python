states = {
  'Oregon': 'OR',
  'Florida': 'FL',
  'California': 'CA',
  'New York': 'NY',
  'Michigan': "MI"
}

cities = { 'CA': 'San Francisco', "MI": "Detroit", "FL" : "jacksonville"}

cities["NY"] = "New York"
if "OR" not in cities: cities["OR"]="Portland"

print("-"*10)

print("NY state has:", cities["NY"])
print("OR State has:", cities["OR"])

print("-"*10)
print("Michigan's abbreviation is:", states['Michigan'])
print(f"Florida's abbreviation is: {states['Florida']}")

print("-"*10)
print("Michigan has:", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

print("-"*10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

print("-"*10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

print("-"*10)
for state,abbrev in list(states.items()):
    print(f"{state} has the abbreviation as {abbrev}")
    print(f"city of abbreviated {abbrev} is {cities[abbrev]}")

print("-"*10)
print(states)
state = states.get("Texas")
if not state:
    print("sorry , no Texas")

city = cities.get("TX","Does not Exist")
print(f"The city for the state 'TX' is : {city}")
