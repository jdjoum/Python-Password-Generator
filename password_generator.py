import random
import string

# generate_password - Generates a password based on the input params
def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation