# This is lab 3.
# Name : Bhawana Maswa
# Date: July 27, 2023
# App name: Caesar Cipher
# Description: App that encrypt and decrypt secret message

# Import system function
from os import system

# Set the terminal title 
system("title Caesar Cipher - Bhawana Maswa")

# Constants
# Making constant as string
ENCRYPT = '1'
DECRYPT = "2"
QUIT = "3"
ENCRYPTION_KEY = 200
DECRYPTION_KEY = -200

# INTRODUCTION
# Doc string - multiline string 
INTRODUCTION = """
~~~~~~~~~~~~~~~~~~
~ Caesar Cipher ~
~~~~~~~~~~~~~~~~~~

This app will encrypt/decrypt a secret message using the Caesar Cipher.

"""


# Functions
def encrypt(message):
    """
    Encrypt the secret message given by user
    """
    # Starts empty, we will add encrypted letters 1 by 1 in the for loop
    encrypted_message = ""
    for letter in message:
        # Encrypt the letter by getting its numeric value and adding the ENCRYPTION_KEY
        encrypted_message += chr(ord(letter) + ENCRYPTION_KEY)

    # Return the encrypted message
    return encrypted_message

def decrypt(message):
    """
    Decrypt the given message given by user
    """
    # Starts empty, we will add decrypted letters 1 by 1 in the for loop
    decrypted_message = ""
    for letter in message:
       # Decrypt the letter by getting its numeric value and adding the DECRYPTION_KEY
       decrypted_message += chr(ord(letter) + DECRYPTION_KEY)

    # Return the decrypted message
    return decrypted_message


# Validation loop - app will repeat if the input is invalid 
exit = False # Repeat apps atleast once
while exit == False:
    # Clear the terminal everytime new loops starts.
    system("cls")
    # Main Menu
    # Print the banner message and the INTRODUCTION
    print(INTRODUCTION)

    # Prompt the user to choose an option for encrypting decrypting or quitting the app.
    print("Choose an option: ")
    print("1.  Encrypt a message ")
    print("2.  Decrypt a message ")
    print("3.  Quit app ")
    value = input("-> ")

    # Determine what user wants chooses and prompt them on the basis of their choice
    # If the user input 1, prompt the user to enter a secret message
    if value == ENCRYPT:
        message = input("Enter a secret message to encrypt: ")
        message = encrypt(message)
        print("Encrypted code: " + message)

    # If the user input 2, prompt the user to enter a code to decrypt it
    elif value == DECRYPT:
        message = input("Enter a code to decrypt: ")
        message = decrypt(message)
        print("Decrypted message: " + message)

    # If the user input 3 the condition of while loop will be false and the app will resatrt
    elif value == QUIT:
        print("Quit app")
        exit = True

    # Display an error message if the input is invalid (i.e. is not 1, 2, or 3)
    else:
        print("You entered an invalid input")

    

    # Exit Prompt
    input("Press [enter] to return to the main menu: ")



    

    