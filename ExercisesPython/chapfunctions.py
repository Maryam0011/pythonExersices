'''8-1. Message: Write a function called display_message() that prints one sen￾tence telling everyone what you are learning about in this chapter. Call the 
function, and make sure the message displays correctly.'''

def display_message():
    '''Display a custom message'''
    print('I am learning how functions work in Python in this exciting chapter of this most helpful book')

display_message()

'''8-2. Favorite Book: Write a function called favorite_book() that accepts one 
parameter, title. The function should print a message, such as One of my 
favorite books is Alice in Wonderland. Call the function, making sure to 
include a book title as an argument in the function call.'''

def favorite_book(title):
    '''Describe favourite book'''
    print(f'One of the most impactful books I have read in recent years is {title}')
favorite_book('Sapiens')


'''8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the 
text of a message that should be printed on the shirt. The function should print 
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the 
function a second time using keyword arguments.'''

def make_shirt(size,message):

    print(f'{size} shirt, {message}')

make_shirt('Medium','Go get it man')
make_shirt(size='Medium',message='Go get it man')

'''8-4. Large Shirts: Modify the make_shirt() function so that shirts are large 
by default with a message that reads I love Python. Make a large shirt and a 
medium shirt with the default message, and a shirt of any size with a different 
message.'''
def make_shirt_v2(size='large',message='I love Python'):
    '''Summarising shirt details'''
    print(f'{size} shirt, {message}')

make_shirt_v2('large')
make_shirt_v2('medium')
make_shirt_v2('small','Coding rocks')

'''8-5. Cities: Write a function called describe_city() that accepts the name of 
a city and its country. The function should print a simple sentence, such as 
Reykjavik is in Iceland. Give the parameter for the country a default value. 
Call your function for three different cities, at least one of which is not in the 
default country.'''
def describe_city(city,country='Nigeria'):
    '''Describe a city'''
    print(f'{city} is an important city in {country}')
describe_city('Kano')
describe_city('Kaduna')
describe_city('Paris','France')

''' 8-6. City Names: Write a function called city_country() that takes in the name 
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile" 
Call your function with at least three city-country pairs and print the values that are returned.'''
def city_country(city,country):
    '''Returns the formatted name of a city and its country'''
    full = f'{city}, {country}'
    return full.title()

kd = city_country('kaduna','nigeria')
print(kd)
par = city_country('paris','france')
print(par)
la = city_country('los angeles','USA')
print(la)