deadCounter.lua

The deadCounter.lua script is designed to create a death counter GUI in a Roblox game. Here are its key functionalities:
1. It creates a ScreenGui named "DeathCounterGui" and attaches it to the player's PlayerGui.
2. A Frame is created within the ScreenGui to hold the death counter display.
3. A TextLabel is created within the Frame to display the number of deaths.
The script updates the death count display whenever the player's death count changes by connecting to the Changed event of the "Deaths" value in the player's leaderstats.

emailChecker.py

emailChecker checks if an email is valid or invalid.

messages.py

The messages.py script is designed to send a POST request to a specified Discord channel URL. Here's a breakdown of its functionality:

1. It imports necessary libraries: requests, json, random, os, and dotenv.
2. Loads environment variables from a .env file using load_dotenv().
3. Retrieves the AUTHORIZATION, COOKIE, and URL from the environment variables.
4. Sets up the request URL and headers, including authorization and cookie information.
5. Constructs a JSON payload with a content field containing a message and a few other fields.
6. Sends a POST request to the Discord channel URL with the constructed payload.
7. Prints the status code and response body of the request.

routlete.py

The routlete.py script simulates a game of Russian Roulette. Here's a breakdown of its functionality:

1. Imports the random library.
2. Prompts the user to input the number of charged bullets.
3. Initializes a list carga representing the chambers of the revolver, with one "cooked" (bullet) and the rest "saved" (empty).
4. Shuffles the list carga.
5. Prompts the user to shuffle the chambers multiple times based on user input.
6. Defines a shoot function that prompts the user to "Shoot".
7. Iterates through the carga list, calling the shoot function and printing whether the user is "alive" or "YOU LOST" based on the chamber status.
