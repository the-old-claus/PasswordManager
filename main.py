#Hash Code

from csv import writer
import hashlib
import maskpass

def hash_pass():
    service=str(input("Enter Service:"))
    usrname=str(input("Enter Username:"))
    passwd=maskpass.askpass(prompt="Enter Password:", mask="#")
    global hashtype
    hashtype=str(input("Enter what type of hash sha256|md5|sha1:"))

    global hashpass

    if hashtype=="md5":
        hash_obj_1=hashlib.md5()
        hash_obj_1.update(passwd.encode())
        hashpass=hash_obj_1.hexdigest()
        print('md5: ',hashpass)

    elif hashtype=="sha1":
        hash_obj_2=hashlib.sha1()
        hash_obj_2.update(passwd.encode())
        hashpass=hash_obj_2.hexdigest()
        print('sha1: ',hashpass)

    elif hashtype=="sha256":
        hash_obj_3=hashlib.sha256()
        hash_obj_3.update(passwd.encode())
        hashpass=hash_obj_3.hexdigest()
        print('sha256: ',hashpass)



    lis1=[service,usrname,hashpass,passwd]

    print("Do you want to save this hash in your inventory?")
    choose=input("Y/N?")

    if choose=="Y":
        with open('user_hass_pass.csv','a') as f_obj:
            writer_obj=writer(f_obj)
            writer_obj.writerow(lis1)

            f_obj.close()


    else:
        ask=input("Do you wanna see your hashed password? Y/N")
        if ask=="Y":
            print("Password:",passwd)
            print("Hashed:",hashpass)
        print("Thank you! Proceed to Menu :)")
        #menu2()


hash_pass()





'''Functions used:
    exit_func
    login
    register





'''
'''
def exit_func():
  print('Thank you for paying a visit to us! Have a fulfilling day! :)')
  wait = input('\n\n\n Press any key to exit...')

#Password Input with conditions for registration modules
condition="Primary conditions for password validation: \n1. Minimum 8 characters \n2. The alphabet must be between [a-z] \n3. At least one alphabet should be of Upper Case [A-Z] \n4. At least 1 number or digit between [0-9] \n5. At least 1 character from [ ! , @ , $ , % , & , * , - , _]."
inp=str(input("Password:"))

cha=['!','@','$','%','&','*','-','_']
l=0
u=0
d=0
p=0
k=False

while k==False:
  if (len(inp) >= 8):
      for i in inp:

          if (i.islower()):
              l+=1           

          elif (i.isupper()):
              u+=1           

          elif (i.isdigit()):
              d+=1           

          elif(i in cha == True):
              p+=1          


  if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(s)):
      print("Valid Password")

  else:
      print("Invalid Password")
      ask=input("Wish to see the conditions again? Type - A")
      if ask=="A":
          print(condition)


'''


