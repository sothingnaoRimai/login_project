import json
import os
def strong_password():
    global password1
    password1=input("enter password")
    if len(password1)>=8:
        if "a" in password1 or "b" in password1 or "c" in password1 or "d" in password1 or "e" in password1 or "f" in password1 or "g" in password1 or "h" in password1 or "i" in password1  or "j" in password1 or"k" in password1 or "l" in password1 or "m" in password1 or"n" in password1 or "o" in password1 or "p" in password1 or "q" in password1 or"r" in password1 or "s" in password1 or "t" in password1 or "u" in password1 or"v" in password1 or "w" in password1 or "x" in password1 or "y" in password1 or "z" in password1:
            if "A" in password1 or "B" in password1 or "C" in password1 or "D" in password1 or "E" in password1 or "F" in password1 or "G" in password1 or "H" in password1 or "I" in password1  or "J" in password1 or"K" in password1 or "L" in password1 or "M" in password1 or"N" in password1 or "O" in password1 or "P" in password1 or "Q" in password1 or"R" in password1 or "S" in password1 or "T" in password1 or "U" in password1 or"V" in password1 or "W" in password1 or "X" in password1 or "Y" in password1 or "Y" in password1 or "Z" in password1:
                if "1" in password1 or "2" in password1 or "3" in password1 or "4" in password1 or "5" in password1 or "6" in password1 or "7" in password1 or "8" in password1 or "9" in password1:
                    if "$" in password1 or "&" in password1 or "@" in password1 or "*" in password1 or "!" in password1:
                        confirm_pass=input("re enter password")
                        if password1==confirm_pass:
                            print("password confirm")
                        else:
                            print("password not match")
                            strong_password()
                    else:
                        print("should contain atleast 1 special character")
                        strong_password()
                else:
                    print("should contain atleast 1 special character")
                    strong_password()
            else:
                print("should contain atleast 1 upper case")
                strong_password()
        else:
            print("should contain atleast 1 lower case")
            strong_password()
    else:
        print("password is too short")
        strong_password()


def sign_up():
    username=input("enter your name:   ")
    strong_password()
    if(os.path.isfile('login_signup1.json')):
        file_name=open("login_signup1.json","r")
        a=json.load(file_name) # json to python in a file
        for i in a["User"]:
            if i["username"]==username:
                print("This user is already exist")
                break
            else:
                dic,d={},{}
                dic["username"]=username
                dic["password"]=password1
                d["description"]=input("About: ")
                d["Dob"]=input("date of birth: ")
                d["Gender"]=input("gender: ")
                d["Hobbies"]=input("hobbies: ")
                dic["Profile"]=d
                v=a["User"]
                v.append(dic)
                f=open("login_signup1.json","w+")
                json.dump(a,f,indent=4)  
                f.close()
                print("Signup Succesfully....")
                break    

    else:                       
        dic,li,d,di={},[],{},{}
        dic["username"]=username
        dic["password"]=password1
        d["description"]=input("About:- ")
        d["Dob"]=input("Date of birth:- ")
        d["Gender"]=input("gender:- ")
        d["Hobbies"]=input("hobbies:- ")
        dic["Profile"]=d
        li.append(dic)
        di["User"]=li
        f=open("login_signup1.json","w+")
        json.dump(di,f ,indent=4)
        f.close()
        print("Signup Succesfully....")


def log_in(): 
    # global password1
    a=open("login_signup1.json","r")
    f=json.load(a)
    d=input("Enter your user name:- ")
    v=input("Enter your password:-  ")
    for i in f["User"]:
        if d==i["username"]:
            if v==i["password"]:
                print("Login successful :) .......")
                print(i)
                break
            else:
                print("wrong  password :( .....")
                break
    else:
        print("wrong username :( ....")
        


option=input("Login | Signup ")
def home():
    if option =="Signup":
        sign_up()
    elif option=="Login":
        log_in()
    else:
        print("enter a valid option")
home()
