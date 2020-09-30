import boto3

__tablename__ = "users_devbops"


Primary_Column_Name = "ID"
Primary_key = "1"
columns = ["Username", "current city", "current country", "email", "first name", "last name", "password"]





client = boto3.client('dynamodb')
DB = boto3.resource('dynamodb')

table = DB.Table(__tablename__)

"""
get data
"""

response = table.get_item(
    Key={
        Primary_Column_Name:Primary_key
    }
)

print(response["Item"])




"""
put item
"""
Primary_key = "2"

response = table.put_item(
    Item={
        Primary_Column_Name:Primary_key,
        columns[0] : "test",
        columns[1] : "test",
        columns[2] : "test",
        columns[3] : "test",
        columns[4] : "test",
        columns[5] : "test",
        columns[6] : "test"


    }
)

print(response["ResponseMetadata"]["HTTPStatusCode"])


