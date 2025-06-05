# create input
print("I am going to try and guess your current age ")
current_year = input("What year is it currently? ")
birth_year = input("What year were you born? ")
# calculate age
age = int(current_year) - int(birth_year)
birthday_age = age + 1
print("You are either " + str(age) + " years old or if you have already have had your birthday then you are " + str(birthday_age) + " years old.")