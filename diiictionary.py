dicti = {'Matt': 20, 'Sally': 30, 'Billy': 20, 'Ben': 80, 'Alex': 50} #Create a dictionary to store the names and ages of 5 people.

def add(key, value): #Add a new person to the dictionary.
    dicti[key] = value

def remove(name): #Remove a person from the dictionary by name.
    del dicti[name]

def average(dicti):
    print(sum(dicti.values()) / len(dicti)) #Print the average age of the people in the dictionary. To do this, 
    #get the sum of all the values, then divide it by the size of the dictionary.

def highest(dicti): #Print the name of the student with the highest score.
    print(max(dicti, key = dicti.get)) #You look through the dictionary and find the maximum value. Then, you return the key of where that value is stored.

def score80(dicti): #Print the names of all students who scored above 80.
    above = [name for name, score in dicti.items() if score > 80] #We are creating a list 
    #that will create a list of names when the value in the dictionary is greater than 80.
    print(above)

print(dicti)
add('Bill', 45)
print(dicti)
remove('Matt')
print(dicti)
average(dicti)

dict2 = {'Bill': 85, 'John': 100, 'Gabe': 80, 'Jack': 0}
highest(dict2)
score80(dict2)