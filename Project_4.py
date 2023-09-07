import random

states_of_america = ["Delaware","Pennsylvania", "New Jersey", "Georgia", "Connecticut","Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "New Hampshire", "Virginia", "New York", "North Carolina",
                     "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi",
                     "Illinois", "Alabama", "Maine", "Missouri", "Arkansas","Michigan", "Florida","Texas", "Iowa",
                     "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia" ,"Nevada","Nebraska",
                     "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah",
                     "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
# print(states_of_america[1])  # Element using Index
# print(states_of_america[-2])   # Element using Index
# states_of_america[2] = "Nu Jersey" # Element Updation.
# states_of_america.append("Naman's Kingdom")
# print(states_of_america[2])
# print(states_of_america[-1])


# BANKER ROULETTE - Who Will Pay The Bill.
# names_string = input("Give me everybody's name, separated by a comma. ")
# names = names_string.split(", ")
# payer = random.randint(0, len(names)-1)
# print(f"{names[payer]} will pay the bill.")

# Other way - Using the choice function
# payer = random.choice(names)
# print(f"{payer} will pay the bill.")

# DIRTY DOZEN
# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches"
# "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits,vegetables]
print(dirty_dozen)

row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}\n")
position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])  # Gets hold of the first integer input, specifies the column.
vertical = int(position[1])  # Gets hold of the first integer input, specifies the row.

selected_row = map[vertical - 1]
selected_row[horizontal - 1] = 'X'
#OR
map[vertical - 1][horizontal - 1] = 'X'

print(f"{row1}\n{row2}\n{row3}\n")





