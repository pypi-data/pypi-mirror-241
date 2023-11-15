
'''
    In this file we will create a function that will generate a password
'''

# Importing the random module
import random

# Importing the string module
import string

# Creating a function that will generate a password

# def generate_password(length):
#     behavior = string.ascii_letters + string.digits + string.punctuation
#     password = [random.choice(behavior) for i in range(length)]
#     return ''.join(password)


def generate_password(length=8, uppercase=False, digits=False, special_chars=False):
    characters = string.ascii_lowercase  # Caractères minuscules par défaut
    
    if uppercase:
        characters += string.ascii_uppercase  # Ajouter les majuscules
    
    if digits:
        characters += string.digits  # Ajouter les chiffres
    
    if special_chars:
        characters += string.punctuation  # Ajouter les caractères spéciaux
    
    password = ''.join(random.choice(characters) for i in range(length))
    return password

