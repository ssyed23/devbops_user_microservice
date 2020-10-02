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

    def put(self, name):
        response = self.table.put_item(
            Item = {
                self.Primary_Column_Name:self.Primary_key,
                self.columns[0]: name,
                self.columns[1] : "test",
                self.columns[2] : "test",
                self.columns[3] : "test",
                self.columns[4] : "test",
                self.columns[5] : "test",
                self.columns[6] : "test",





            }
        )

        print(response["ResponseMetadata"]["HTTPStatusCode"])
        
              
        
          
