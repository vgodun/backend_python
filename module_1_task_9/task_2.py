import random
import string
list_password = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)
password = ''.join(random.choices(list_password, k=8))

print('Generated password: ',password)