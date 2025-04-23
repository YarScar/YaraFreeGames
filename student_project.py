"""
Data Structures
Student Project
Project Title:
"""
import requests

BASE_URL = "https://randomuser.me/api/"

## -- LIST OF GAMES -- ##
games = ["Red dead redemption 2", "Elden ring", "Spider-man: miles morales", "Cyberpunk 2077", "Hollow knight", "Cuphead", "Sea of Thieves"]

## -- USERNAMES LIST --##
usernames = []
## -- PASSWORD LIST --##
passwords = []
##-- GET USERNAME --##

print("You like free stuff? OFC YOU DO!!\
Yara's Games is a website that gives you FREE games that would usually cost money.\
Just make an account to join the rest of us swimming in FREE games.")
print("")

###--GET USERNAME--###
username = input("type a username here: ") #putting user input into a variable so I can use the info

##-- GET PASSWORD --##
print("")
password = input("type a password here: ")

##-- APPEND INTO LISTS --##
usernames.append(username) #I appended the username and password into the lsits of usernames and passwords
passwords.append(password)

while True:
#getting random user info that uses the website
    fake_person = input("would you like to see a random person using yara's website? y or n: ")
    if fake_person == "y":
        print("\nFetching random fake user information...")
    
    
        gender_choice = input("Would you like to fetch a male (m), female (f), or random user? (Press Enter for random): ").lower()
    
     # Prepare parameters for the request
        params = {}
        if gender_choice == 'm':
            params['gender'] = 'male'
        elif gender_choice == 'f':
            params['gender'] = 'female'
            
    # Make the GET request to fetch user data
        response = requests.get(BASE_URL, params=params)
        
    # Check if the request was successful
        if response.status_code == 200:
        
    #JSON data from the response
            body = response.json()
        
     # Extract user data
        user = body.get("results", [])[0]
        
     # Display the user information in a readable format
        print("\nPotential Friend:")
        print("------------------------------")
        print("Name: " + user['name']['first'] + " " + user['name']['last'])
        print("Gender: " + user['gender'])
        print("Location: " + user['location']['city'] + ", " + user['location']['country'])
        print("Username: " + user['login']['username'])
        input("\npress enter to continue to your list of games: ")
        print("\nIf you add them you have a friend to play these games with: ")
        print(games)
    
    elif fake_person == "n":
        print("\nokay have fun playing these games alone :/ ")
        print("")
        print(games)
    else:
        print("\nPlease pick y or n")
        continue
