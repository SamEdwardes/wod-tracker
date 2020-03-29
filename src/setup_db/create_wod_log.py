import decimal
import json
import time

import boto3

dynamodb = boto3.resource('dynamodb', region_name='ca-central-1')

##############################################
# Step 1: create table
##############################################

try:
    table = dynamodb.Table('wod_log')
    table.delete()
    table.wait_until_not_exists()
    print("Table deleted.")
    
except:
    print("Table not yet created. Creating table...")


table = dynamodb.create_table(
    TableName='wod_log',
    KeySchema=[
        {
            'AttributeName': 'date',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'name',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'date',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'name',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status)

##############################################
# Step 2: create table
##############################################

table = dynamodb.Table('wod_log')
table.wait_until_exists()

with open("data/wod_log.json") as json_file:
    wod_log = json.load(json_file, parse_float = decimal.Decimal)
    for movement in wod_log:
        name = movement['name']
        date = movement['date']
        sets = int(movement['sets'])
        weight = movement['weight']

        print("Adding movement:", name, date)

        table.put_item(
           Item={
               'name': name,
               'date': date,
               'sets': sets,
               'weight': weight
            }
        )
