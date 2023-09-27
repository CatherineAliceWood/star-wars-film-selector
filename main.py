# import requests library - used for API requests. To install use the command <pip install requests>
import requests

# Swapi Star Wars API - open API - no key needed. Used to collect Star Wars data.
# test API
# API_response = requests.get('https://swapi.dev/api')
# print(API_response.status_code)

# create empty list of characters
characters = []

# create empty list and set for film names
film_names_list = []
film_names_set = set()


# create function to get the character data from API, targeting the dictionary entry
def get_character(name):
    character = requests.get(f'https://swapi.dev/api/people/?search={name}').json()
    return character['results'][0]


# create function to get correct name of character entered on input
def get_correct_name(name):
    return name.get("name")


# create function to print and append to file: correct name is in following films
def print_correct_name_in_following_films(name):
    print(f"\n{name} is in the following films: ")
# create file to write results into
    with open("star_wars_film_selection.txt", "a") as star_wars_file:
        star_wars_file.write(f"\n\n{name} is in the following films: ")


# create function for getting film names
def get_film_names(name):
    for film in name['films']:
        film = requests.get(film).json()
        # add film title to list
        film_names_list.append(film['title'])
        # print and append to file: film title and slice of release date to include only the year
        print(f"{film['title']} ({film['release_date'][:4]})")
        with open("star_wars_film_selection.txt", "a") as star_wars_file:
            star_wars_file.write(f"\n{film['title']} ({film['release_date'][:4]})")


# create a function to add a new character to the user's list of choices
def add_new_character():
    # select a character
    new_character = input("\nChoose a Star Wars character: ")
    # get this character's data as json from the API
    new_character_parsed = get_character(new_character)
    # get correct name of character
    new_character_correct_name = get_correct_name(new_character_parsed)
    # add the character to the characters list
    characters.append(new_character_correct_name)
    # print that the character is in the following list of films
    print_correct_name_in_following_films(new_character_correct_name)
    # get the names of the films that the new character is in
    get_film_names(new_character_parsed)


# print and append to file: title of app
print("Star Wars Film Selector")
with open("star_wars_film_selection.txt", "a") as star_wars_file:
    star_wars_file.write("Star Wars Film Selection")

# print app info
print("\nWe're going to help you choose which Star Wars film to watch based on which characters you want to see!")

# call the add_new_character function to start the programme
add_new_character()

# create loop to continue to ask the user if they want to add another character, until they say no
add_character_question = input("\nWould you like to add another Star Wars character? y/n: ")
while add_character_question == "y":
    add_new_character()
    add_character_question = input("\nWould you like to add another Star Wars character? y/n: ")

'''create if statement to ask the user if they want to add Luke Skywalker to their list of characters
if they have not already added him'''
if "Luke Skywalker" not in characters:
    add_luke = input("\nWould you like to add Luke Skywalker to your list? y/n: ")
    # if they answer to yes to adding Luke, add him to their list of characters
    if add_luke == "y":
        luke = get_character("luke")
        luke_correct_name = get_correct_name(luke)
        characters.append(luke_correct_name)
        print_correct_name_in_following_films(luke_correct_name)
        get_film_names(luke)
    # otherwise, print the following
    else:
        print("\nOk, you're sure of your choices. That's good!")

# create if statement to create a printable set of films if the user has selected more than one character
if len(characters) > 1:
    print(f"\nYour list of characters is: {', '.join(characters)}")
    with open("star_wars_film_selection.txt", "a") as star_wars_file:
        star_wars_file.write(f"\n\nYour list of characters is: {', '.join(characters)}")
    # create for loop to check the list of films for duplicates
    for film_ in film_names_list:
        '''where the number of duplicates of each film is the same as the number of characters selected, add that film
        set of film names so that the films all selected characters are in can be printed each once'''
        if film_names_list.count(film_) == len(characters):
            film_names_set.add(film_)
    ''' create if statement to print statements and append to file if the user's list of characters are in at least 1 
    film together'''
    if len(film_names_set) > 0:
        print("\nThey are in the following films: ")
        with open("star_wars_film_selection.txt", "a") as star_wars_file:
            star_wars_file.write("\n\nThey are in the following films: ")
            print(f"{', '.join(film_names_set)}")
            star_wars_file.write(f"\n{', '.join(film_names_set)}")
            print("\nGreat character choices! Enjoy the films!")
            star_wars_file.write("\nGreat character choices! Enjoy the films!")
    # otherwise print the following
    else:
        print("\nThey aren't in any films together. You'll have to watch them individually!")
else:
    # if the user has only selected one character, print the following
    print(f"\nYou chose: {''.join(characters)} \nGreat character choice! Enjoy the films!")
    # and append the following to the file
    with open("star_wars_film_selection.txt", "a") as star_wars_file:
        star_wars_file.write(f"\n\nGreat character choice! Enjoy the films!")