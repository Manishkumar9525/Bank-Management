import random
import string
import json
from pathlib import Path




class BankAccount:
  database='data.json'
  data=[]

  try:
    if Path(database).exists():
      with open(database)as fs:
        data=json.loads(fs.read())
    else:
      print("no such file exist ")
  except Exception as err:
    print(f"an exception occured as {err}")



  @classmethod
  def __update(cls):
    with open(cls.database,'w') as fs:
      fs.write(json.dumps(BankAccount.data))
    
  @classmethod
  def __accountNumgenerate(cls):
    alph=random.choices(string.ascii_letters,k=3)
    num=random.choices(string.digits,k=3)
    id=alph + num 
    random.shuffle(id)
    return"".join(id)

  def createAccount(self):
    info={
      "name":input("enter your name :- "),
      "age":int(input("enter your age :- ")),
      "email":input("enter your email :- "),
      "pin":int(input("enter your 4 digit pin :- ")),
      "accountNo":self.__accountNumgenerate(),
      "balance":0
    }
    if info['age']<18 and len(str(info['pin'])) !=4:
      print("Sorry you cannot create your account ")
    else:
      print("you account is successfully created")
      for i in info:
        print(f"{i}:{info[i]}")

      print("Notedown your Account Number ")
      BankAccount.data.append(info)
      self.__update()

  def depositMoney(self):
    acountNUmber=input("enter your account number :- ")
    pin=int(input("enter your pin :- "))

    userdata=[i for i in BankAccount.data if i['accountNo']== acountNUmber and i['pin']==pin]

    if not userdata :
      print("Sorry no data found")
    else:
      amount=int(input("enter your deposite amount :- "))
      if amount>10000 and amount<=0:
        print("sorry the amount to much you can deposite below 10000 and above 1")
      else:
        # print(userdata)
        userdata[0]['balance'] += amount
        self.__update()
        print("Amount is deposite Successffuly")



  def Withdraw(self):
    accountNO=input("Enter your account number :- ")
    pin=int(input("enter your 4 digit pin :- "))

    userData=[i for i in BankAccount.data if i['accountNo']== accountNO and i['pin']==pin]

    if not userData :
      print("sorry no data found")
    else:
      amount=int(input("enter your Amount :- "))
      if amount > userData[0]['balance'] :
        print("you account have not much amount ...")
      else:
        userData[0]['balance'] -=amount
        self.__update()
        print(f"Withdrawal successful!")
        print(f"Amount withdrawn: ₹{amount}")
        print(f"Remaining balance: ₹{userData[0]['balance']}") 




  def showDetails(self):
    accountNO=input("Enter your account number :- ")
    pin=int(input("enter your 4 digit pin :- "))
    userData=[i for i in BankAccount.data if i['accountNo']== accountNO and i['pin']==pin]
    print(userData)
    if not userData:
     print("Sorry, no account found.")
    else:
      print("your Information are \n\n")
      for key, value in userData[0].items():
        if key != "pin":
          print(f"{key} : {value}")
    


  def updateDeatils(self):
     accnumber = input("Please tell your account number: ")
     pin = int(input("Please tell your pin as well: "))

     userdata=[i for i in BankAccount.data if i['accountNo']==accnumber and i['pin']==pin]

     if not userdata:
        print("No such user found")

     else:
       print("\nYou cannot change age, account number, or balance.")
       print("Fill the details you want to change.")
       print("Leave it empty if you don't want to change it.\n")

       newdata={
         "name": input("Please tell new name or press Enter to skip: "),
            "email": input("Please tell your new email or press Enter to skip: "),
            "pin": input("Enter new PIN or press Enter to skip: ")
       }

       if newdata['name']=="":
         newdata["name"]=userdata[0]['name']
       if newdata['email']=="":
         newdata["email"]=userdata[0]['email']
       if newdata['pin']=="":
         newdata["pin"]=userdata[0]['pin']
       else:
         newdata['pin']=int(newdata['pin'])

       newdata["age"] = userdata[0]["age"]
       newdata["accountNo"] = userdata[0]["accountNo"]
       newdata["balance"] = userdata[0]["balance"]

       for i in newdata:
         if newdata[i] == userdata[0][i]:
            continue
         else:
            userdata[0][i] = newdata[i]

       BankAccount.__update()
       print("\nDetails updated successfully!")

         
  def Delete_account(self):
    accnumber = input("Please tell your account number: ")
    pin = int(input("Please tell your pin as well: "))

    userData=[i for i in BankAccount.data if i['accountNo']==accnumber and i['pin']==pin]

    if not userData:
      print("no such user found")
    else:
      print("\n Account found ")
      print(f"Name : {userData[0]['name']}")
      print(f"Account Number: {userData[0]['accountNo']}")
      print(f"Balance: {userData[0]['balance']}")

    confirm=input("\n are you sure you want to delete this account ? (yes / no)")
    if confirm.lower()=="yes":
      BankAccount.data.remove(userData[0])
      self.__update()
      print("Account delete successfully ✅✅")
    else:
      print("\nAccount deletion cancelled.❌❌")


      
    
    

        



  







user = BankAccount()




print("press 1 for create an Account")
print("press 2 for Deposititing the money in the bank ")
print("press 3 for withDraw the money ")
print("press 4 for details")
print("press 5 for update the details")
print("press 6 for deleting you bank account ")

check=int(input(" tell your response :- "))
if check==1:
  user.createAccount()
if check==2:
  user.depositMoney()
if check==3:
  user.Withdraw()
if check==4:
  user.showDetails()
if check==5:
  user.updateDeatils()
if check==6:
  user.Delete_account()