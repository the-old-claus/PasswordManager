from csv import writer
import hashlib
import maskpass


def hash_pass():
  service = str(input("Enter Service:"))
  usrname = str(input("Enter Username:"))
  passwd = maskpass.askpass(prompt="Enter Password:", mask="#")
  global hashtype
  hashtype = str(input("Enter what type of hash sha256|md5|sha1:"))

  global hashpass

  if hashtype == "md5":
    hash_obj_1 = hashlib.md5()
    hash_obj_1.update(passwd.encode())
    hashpass = hash_obj_1.hexdigest()
    print('md5: ', hashpass)

  elif hashtype == "sha1":
    hash_obj_2 = hashlib.sha1()
    hash_obj_2.update(passwd.encode())
    hashpass = hash_obj_2.hexdigest()
    print('sha1: ', hashpass)

  elif hashtype == "sha256":
    hash_obj_3 = hashlib.sha256()
    hash_obj_3.update(passwd.encode())
    hashpass = hash_obj_3.hexdigest()
    print('sha256: ', hashpass)
    
  ask = input("Do you wanna see your hashed password? Y/N")
  if ask == "Y":
    print("Password:", passwd)
    print("Hashed:", hashpass)
    
  else:
    
    print("Thank you! Proceed to Menu :)")
    #menu2()

  '''
  #Code to save hashed password to a file
  #Confused if it should be saved or not
  lis1 = [service, usrname, hashpass, passwd]

  print("Do you want to save this hash in your inventory?")
  choose = input("Y/N?")

  if choose == "Y":
    with open('user_pass.csv', 'a') as f_obj:
      writer_obj = writer(f_obj)
      writer_obj.writerow(lis1)

      f_obj.close()

  else:
    ask = input("Do you wanna see your hashed password? Y/N")
    if ask == "Y":
      print("Password:", passwd)
      print("Hashed:", hashpass)
    print("Thank you! Proceed to Menu :)")
    #menu2()
  '''
  
hash_pass()
