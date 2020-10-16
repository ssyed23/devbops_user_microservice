import boto3
from boto3.dynamodb.conditions import Attr
import bcrypt


class Users:
    def __init__(self):
        # connecting to the dynamdo db 
        self.__Tablename__ = "user_devbops"
        self.client = boto3.client('dynamodb')
        self.DB = boto3.resource('dynamodb')
        self.Primary_Column_Name = "username"
        # self.Primary_key = 1
        # providing values for the colmuns
        self.columns = ["current city", "current country", "email", "first name", "last name", "password"]
        self.table = self.DB.Table(self.__Tablename__)

    def put(self, user, currentcity, currentcountry, email, firstname, lastname, password):

        response = self.table.put_item(
            Item={
                self.Primary_Column_Name: user,
                self.columns[0]: currentcity,
                self.columns[1]: currentcountry,
                self.columns[2]: email,
                self.columns[3]: firstname,
                self.columns[4]: lastname,
                self.columns[5]: self.hash_pw(password)

            }
        )

        print(response["ResponseMetadata"]["HTTPStatusCode"])

    def verifying_email_and_user_are_available(self, user, currentcity, currentcountry, email, firstname, lastname,
                                               password):
        # this function first verfiys that the username and email are available to use
        # if one or the other is not available we return false
        # if available we call our put function that pushes items to db
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
            return username

    def check_if_user_exists_email(self, email):
        response = self.table.scan(
            FilterExpression=Attr("email").eq(email)
        )
        if response["Items"] == []:
            return email

    def hash_pw(self, password):
        hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        """
        above hased is a byte stream; below we decode back into a striing and save pw as string
        """

        return hashed.decode("utf-8")

    def de_hash(self, password, hashed):
        if bcrypt.checkpw(password, hashed):
            
            return True
        else:
            
            return False


    def verify_that_user_exists(self, user, password):
        response = self.table.scan(
            FilterExpression=Attr("username").eq(user)
        )
        print (response)








    def authincate_user(self, user, password):
        response = self.table.scan(
            FilterExpression=Attr("username").eq(user)
        )

        ## check if list is emtpy
        if (len(response["Items"]) > 0):
            # we have find the user
            # perform verification
            hased = response['Items'][0]["password"].encode("utf-8")

            self.de_hash(password.encode("utf-8"), hased)

            verification = self.de_hash(password.encode("utf-8"), hased)

            if (verification):
                print("it matches")
                return {
                    "Result": True,
                    "Error": None,
                    "City": response['Items'][0]["current city"],
                    "Country": response['Items'][0]["current country"]
                }
            else:
                print("password inncorrect")
                return {
                    "Result": False,
                    "Error": "Password incorrect",
                    "City": None,
                    "Country": None
                }

        else:
            # that means cant find anythign
            print("no such user")
            return {
                "Result": False,
                "Error": "Username not found",
                "City": None,
                "Country": None
            }

    def delete_user(self, user):
        # checking if user exists
        response = self.table.scan(
            FilterExpression=Attr("username").eq(user)
        )
        print(response)
        print(len(response["Items"]))



test = Users()
# test.verifying_email_and_user_are_available(user="abdul", currentcity="NY", currentcountry="USA", email="dev", firstname="abdul", lastname="syed",
#                                                password="password")
# test.authincate_user(user="abdul", password="password")
# test.authincate_user(user="abdul", password="password123")
# test.authincate_user(user="abdulsx", password="password123")
test.delete_user("abdulty")