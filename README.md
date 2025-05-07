--🎮 YaraFreeGames--
A simulated gaming website experience where users can create accounts, log in, and "connect" with a friend.

## Overview ##
-Purpose / Problem Statement-
YaraFreeGames mimics a gaming platform's interface, guiding users through account creation, login, and friend-connecting features. While no real games are included, it demonstrates how user-based systems work.

-Target Audience-
This project is for students and young learners interested in web development and gaming platforms. It serves as an educational tool to understand the logic behind user systems.

## The Solution ##
-What It Does-
Simulates account creation and login

Lets users "find" a friend using a fake user from an API

Mimics the layout and flow of a real gaming site

-Limitations-
No real games

No live or real-time multiplayer features

Primarily focused on user interface and system flow

## Key Features ##
Integration with Random User API

Homepage and simulated friend connection

Use of try/except blocks for error handling

Clean structure for educational clarity

-Example Code Snippet-
python
Copy
Edit
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
    
## Technical Process ##
-Challenges-
Simulating realistic user interaction without live data

Structuring the project in manageable steps

Development Steps
Built static layout

Added account and login system

Implemented friend-finding with API

-Future Improvements-
Add game sprites or basic playable elements

Expand user interaction and interface polish

Explore real-time multiplayer using WebSockets

## Tools & Resources Used ##
TechSmart (development platform)

Random User API

Google Docs (for planning and outlining)

Inline code comments (for clarity and documentation)
