import pandas as pd
import os as os
file="/database/db.csv"
class Users:
    username = ""
    password = ""
    FirstName = ""
    LastName = ""
    profilePic = ""
    description = ""

    def __init__(self):
        # print "test"
        self.username="username"
        #self.username = username
        #self.password = password #sha256_crypt.encrypt(password)
        #self.FirstName = FirstName
        #self.LastName = LastName
        #self.description = description

    def getUsername(self):
        return self.username

    def getPasswordVerified(self, username):
        pass
        #sha256_crypt.verify(self.password, password)
    def insertData(self,path,username,password,description,profilePic,firstName,LastName):
        file=path+"/database/db.csv"
        df=pd.read_csv(file)
        columns=['username','password','description','profilePic','firstName','lastName']
        df2 = pd.DataFrame([[username,password,description,profilePic,firstName,LastName]], columns=columns)
        df=df.append(df2, ignore_index=True)
        df.to_csv(file,index=False)
        print ("Data inserted")
    def validateUsername(self,path,username):
        file = path + "/database/db.csv"
        df=pd.read_csv(file)
        #print (df)
        newdf=(df.loc[df['username'] == username])
        if(len(newdf)>0):
            return True
        else:
            return False
    def validatePassword(self,path,username,password):
        file = path + "/database/db.csv"
        df = pd.read_csv(file)
        #print (df)
        newdf = (df.loc[df['username'] == username])
        if len(newdf)>0:
            print (newdf['password'].tolist()[0])
            print (password)
            if (str(newdf['password'].tolist()[0])==password):
                return True
            else:
                return False
        else:
            return False


    def getUserProfile(self,path,username):
        file = path + "/database/db.csv"
        df = pd.read_csv(file)
        # print (df)
        newdf = (df.loc[df['username'] == username])
        userlist = [newdf['username'].tolist()[0],
                    newdf['password'].tolist()[0],
                    newdf['firstName'].tolist()[0],
                    newdf['lastName'].tolist()[0],
                    newdf['description'].tolist()[0],
                    newdf['profilePic'].tolist()[0],
                    ]
        return userlist
