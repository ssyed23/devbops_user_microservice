import boto3


class users:
    def __init__(self):
        self.__Tablename__ = "User_devbops"
        self.client = boto3.client('dynamodb')
        self.DB = boto3.resource('dynamodb')
        self.Primary_Column_Name = "ID"
        self.Primary_key = 1
        self.columns = ["Username", "current city", "current country", "email", "first name", "last name", "password"]
        self.table = self.DB.Table(self.__Tablename__)

    def put(self, name, password, email, firstname, lastname, currentcity, currentcountry):

        response = self.table.put_item(
            Item = {
                self.Primary_Column_Name:3,
                self.columns[0]: name,
                self.columns[1] : password,
                self.columns[2] : email,
                self.columns[3] : firstname,
                self.columns[4] : lastname,
                self.columns[5] : currentcity,
                self.columns[6] : currentcountry


            }
        )

        print(response["ResponseMetadata"]["HTTPStatusCode"])
        all_items = self.table.scan()
        print(len(all_items))
        print("Asas")

    def hash_pw(self, password):
        pass


      
        
              
        
          
