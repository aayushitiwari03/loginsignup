import json
import os
print("WELCOME IN LOGIN AND SIGNUP PAGE!")
def signup(p):
    if len(p)>=6 and len(p)<=16:
        if p>="a" or p<="z":
            if "@" in p or "#" in p:
                if "1"in p or "2"in p or "3" in p or "4" in p or "5" in p or "6" in p or "7" in p or "8" in p or "9" in p or "0" in p:
                    print("strong passward")
                else:
                    print("week passward")
                    p=input("Enter your passward:")
                    signup(p)
            else:
                print("add special character.")
                p=input("Enter your paasward:")
                signup(p)
        else:
            print("add alphabets")
            p=input("Enter your paasward:")
            signup(p)
    else:
        print("please check the lenght of passward, atleast 6 and maximum 16.")
        p=input("ENter your passward:")
        signup(p)
def cp(p,p1):
    if p==p1:
        print("correct")
    else: 
        print("your confirm passward is not match with passward.")
        p1=input("Enter your confirm passward:")
user=input("what you want to do login or signup:")
file=os.path.exists("signup.json")
if file ==False:
    if user=="signup":
        n=input("Enter your name:")
        g=input("enter gmail : ")
        p=input("Enter your passward:")
        signup(p)
        p1=input("Enter your confim passward:")
        cp(p,p1)
        print("congrats",n,"you signed up successfully")
        dob=input("Enter your dob")
        ge=input("Enter your gender male or female:")
        l=[]
        dic={}
        n1=["name","gmail","passward","dob","gender"]
        info=[n,g,p,dob,ge]
        for i in range(len(n1)):
            dic.update({n1[i]:info[i]})
        l.append(dic)
        with open("signup.json","a") as f:
            json.dump(l,f,indent=2)
elif file==True:
   if user=="signup":
        n=input("Enter your name:")
        gm=input("enter you gmail : ")
        p=input("Enter your passward:")
        signup(p)
        p1=input("Enter your confirm passward:")
        cp(p,p1)
        r=open("signup.json","r")
        n2=r.read()
        if n in n2:
            print("name is already exists")
        else:
            print("congrates",n,"you are signed up successfully")
            dob=input("Enter your dob:")
            g=input("Enter your gender:")
            dic={}
            n1=["name","gmail","passward","dob","gender"]
            info=[n,gm,p,dob,g,]
            for i in range(len(n1)):
                dic.update({n1[i]:info[i]})
            with open("signup.json","r") as f:
                data=json.load(f)
            data.append(dic)
            with open("signup.json","w") as f:
                json.dump(data,f,indent=2)
   elif user=="login":
            user_gmail=input("Enter your gmail :")
            u1=input("Enter your passward:")
            with open("signup.json","r") as f:
                da=json.load(f)
                for i in range(len(da)): 
                    if da[i]["gmail"]==user_gmail:
                        if da[i]["passward"]==u1:
                            print("login successfully")
                            print("your name is",da[i]["gmail"],"\n")
                            print("and your data is :-\n")
                            for x,y in da[i].items():
                                print(x,'=',y)                          
                        else:
                            print("this name is not exist in this file.")
                            break

