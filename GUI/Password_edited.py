#EDITED ONLY FOR THE PURPOSE TO MAKE ADD IN STORAGE RUN

from cryptography.fernet import Fernet
import maskpass
import pyperclip

key = Fernet.generate_key()
fernet = Fernet(key)


def encrypt(message):
  #message = maskpass.advpass()
  encMessage = fernet.encrypt(message.encode())
  return encMessage


#a = encrypt()
#print("encrypted string: ", a)
def decrypt(encMessage):
  decMessage = fernet.decrypt(encMessage.decode())
  return decMessage
  pyperclip.copy(str(decMessage)[2:-1])


#b = decrypt(a)
#print("decrypted string: ", b )
