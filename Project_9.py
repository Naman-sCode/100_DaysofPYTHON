programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call."
}

# Retrieving information from a dictionary.
print(programming_dictionary["Bug"])

# Adding new item to dictionary
programming_dictionary["Loop"] = " The action of doing something over and over again."
print(programming_dictionary)

# Create an empty dictionary.
empty_dictionary = {}

# Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

# Editing an item in the dictionary
programming_dictionary["Bug"] = "A moth"

# Loop though a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Nesting Dictionary in a Dictionary

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12}
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
}

# Nesting Dictionary in a list.

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visited":12},
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visited":5}
]


def add_new_country(county_visited, times_visited, cities_visited):
     new_country = {}
     new_country["country"] = county_visited
     new_country["visits"] = times_visited
     new_country["cities"] = cities_visited
     travel_log.append(new_country)


add_new_country("Russia",2, ["MOscpw", "Saint Petersburg"])
print(travel_log)


