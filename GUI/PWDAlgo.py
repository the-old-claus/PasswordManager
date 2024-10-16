import secrets
import strings

C1 = string.ascii_letters
C2 = string.digits
C3 = string.punctuation

random_arrange = C1 + C2 + C3 


pwd_length = int(input("User, Kindly enter the desired length of the password :"))

pwd = ''
for i in range(pwd_length):
  pwd += ''.join(secrets.choice(random_arrange))

print(pwd)