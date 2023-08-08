import random
import string

available_chars = list(string.ascii_letters + string.digits)

pass_list = random.choices(available_chars, k=16)

password = ''.join(pass_list)

print(f'Random Password: {password}')