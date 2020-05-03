from string import ascii_uppercase, digits
from random import choices

confusing_chars = ['O', '0', 'I', '1']
viable_chars = [char for char in (ascii_uppercase + digits)
                if char not in confusing_chars]

def random_id(length=5):
    return choices(viable_chars, k=length)
