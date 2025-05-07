"""
Data Structures
Student Project
Project Title:
"""
import requests

BASE_URL = "https://randomuser.me/api/"

# Initial request test with basic error handling
try:
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        print("Connected successfully to the random user API!")
    else:
        print("Failed to connect. Status code:", response.status_code)
except:
    print("Something went wrong while trying to connect to the API.")

## -- LIST OF GAMES -- ##
games = ["Red dead redemption 2", "Elden ring", "Spider-man: miles morales", "Cyberpunk 2077", "Hollow knight", "Cuphead", "Sea of Thieves"]

## -- USERNAMES LIST -- ##
usernames = []
## -- PASSWORD LIST -- ##
passwords = []

##-- USER INTRO --##
print("You like free stuff? OFC YOU DO!!\
 Yara's Games is a website that gives you FREE games that would usually cost money.\
 Just make an account to join the rest of us swimming in FREE games.\n")

###--GET USERNAME--###
username = input("Type a username here: ")
password = input("\nType a password here: ")

##-- APPEND INTO LISTS --##
usernames.append(username)
passwords.append(password)

while True:
    # Ask user if they want to see a fake user
    fake_person = input("\nWould you like to see a random person using Yara's website? (y or n): ").lower()

    if fake_person == "y":
        print("\nFetching random fake user information...")

        gender_choice = input("Would you like to fetch a male (m), female (f), or random user? (Press Enter for random): ").lower()

        # Prepare parameters
        params = {}
        if gender_choice == 'm':
            params['gender'] = 'male'
        elif gender_choice == 'f':
            params['gender'] = 'female'

        # Make the API call with basic error handling
        try:
            response = requests.get(BASE_URL, params=params)
            if response.status_code == 200:
                body = response.json()
                user = body["results"][0]

                # Display the user info
                print("\nPotential Friend:")
                print("------------------------------")
                print("Name: " + user['name']['first'] + " " + user['name']['last'])
                print("Gender: " + user['gender'])
                print("Location: " + user['location']['city'] + ", " + user['location']['country'])
                print("Username: " + user['login']['username'])

                input("\nPress Enter to continue to your list of games: ")
                print("\nIf you add them, you have a friend to play these games with: ")
                print(games)
            else:
                print("Couldn't fetch user. Status code:", response.status_code)

        except:
            print("Something went wrong while getting user data.")

    elif fake_person == "n":
        print("\nOkay, have fun playing these games alone :/ ")
        print(games)

    else:
        print("\nPlease pick y or n")
