#1 - Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
        'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
        'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x = [1][0] = 15
print(x)

# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'
print(students)

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'])

# Change the value 20 in z to 30
z[0]['y'] = 30
print(z)

#2 - Iterate Through a List of Dictionaries
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(dictionary):
    for i in dictionary:
        string = ''
        for (k, v) in i.items():
            string += f'{k}: - {v}, '
        print(string)
        string = ''
iterateDictionary(students)

#3 - Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for i in some_list:
        for (k, v) in i.items():
            if k == key_name:
                print(v)
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

#4 - Iterate Through a Dictionary with List Values
# This creates a dictionary named 'dojo' with two keys: 'locations' and 'instructors', 
# and each key has a list of values associated with it.
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

# This defines a function named 'printInfo' that takes a single argument named 'dictionary'.
def printInfo(dictionary):
    # This line starts a for loop that iterates over key-value pairs in the given 'dictionary'.
    for (key, value) in dictionary.items():
        # This calculates the number of items in the 'value' (which is a list) and assigns it to 'count'.
        count = len(value)
        # This prints the number of items and the key (converted to uppercase) from the dictionary.
        print(f'{count} {(key).upper()}')
        # This nested for loop iterates over each individual item in the 'value' list.
        for ruben in value:
            # This prints the current item from the 'value' list.
            print(ruben)

# This calls the 'printInfo' function and provides the 'dojo' dictionary as an argument.
printInfo(dojo)
