import boto3
from boto3.dynamodb.conditions import Attr
import bcrypt


class users:
    def __init__(self):
        self.__Tablename__ = "Users_devbops"
        self.client = boto3.client('dynamodb')
        self.DB = boto3.resource('dynamodb')
        self.Primary_Column_Name = "ID"
        self.Primary_key = 1
        self.columns = ["Username", "current city", "current country", "email", "first name", "last name", "password"]
        self.table = self.DB.Table(self.__Tablename__)



    def put(self, user, currentcity, currentcountry, email, firstname, lastname, password):
        all_items = self.table.scan()
        last_primary_key = len(all_items['Items']) + 1

        response = self.table.put_item(
            Item = {
                self.Primary_Column_Name:last_primary_key,
                self.columns[0]: user,
                self.columns[1] : currentcity,
                self.columns[2] : currentcountry,
                self.columns[3] : email,
                self.columns[4] : firstname,
                self.columns[5] : lastname,
                self.columns[6] : self.hash_pw(password)


            }
        )

        print(response["ResponseMetadata"]["HTTPStatusCode"])
        
        

    def hash_pw(self, password):
        convert_into_byte_stream =  password
        
        converted = bytes(convert_into_byte_stream, 'utf8')
        

        password = converted
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        print(hashed)
        return hashed
    
    



    def verifying_email_and_user_are_available(self, user, currentcity, currentcountry, email, firstname, lastname, password):
        if self.check_if_user_exists(user) and self.check_if_user_exists_email(email):
            self.put(user, currentcity, currentcountry, email, firstname, lastname, password)
            return True
        else:
            return False
            


    def check_if_user_exists(self, username):
        response = self.table.scan(
            FilterExpression=Attr("Username").eq(username)
        )
        if response["Items"] == []:
            # print("name is avaiavible")
            return username
    
    def check_if_user_exists_email(self, email):
        response = self.table.scan(
            FilterExpression=Attr("email").eq(email)
        )
        if response["Items"] == []:
            # print("email is avaiavible")
            return email

        













    def de_hash(self, password, hashed):
        if bcrypt.checkpw(password, hashed):
            print("it matches")
        else:
            print("it didnt match")

    def authincate_user(self, user, password):
        response = self.table.scan(
            FilterExpression=Attr("Username").eq(user)
        )
        print(response['Items'][0])
    

      

 

        
        
 



# t1 = users()
# # t1.put("asas", "test", "asasas", "asasas", "asasasasas", "asasasas", "asasasasas")
# # t1.hash_pw("test")
# # t1.authincate_user(user="summi", password="cats123")    
# t1.check_if_user_exists("summi")
          
