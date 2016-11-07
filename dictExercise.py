#Collects input for a list of people and populates a dictionary with name and age
#Creates an empty list named people
people = []

#Function for inputting person's information and adds to dictionary
def get_person():
	person_name = input("Enter a name: ")
	person_age = input("Enter age: ")

	person = {
		"name" : person_name,
		"age" : person_age
	}
	
	return person

person_count = int(input("How many people will be added? "))

#Loop for person input 
for count in range(person_count):
	people.append(get_person())
	print("You've added " + str(count + 1) + " people.")
	print("Here they are: " + str(people))
