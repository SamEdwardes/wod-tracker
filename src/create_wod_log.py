import decimal
import json
import time

import boto3

from helpers import print_break

dynamodb = boto3.resource('dynamodb', region_name='ca-central-1')

##############################################
# Step 1: create table
##############################################

print_break("Checking if table exists:")

try:
    table = dynamodb.Table('wod_log')
    table.delete()
    print("Deleting table.")
    table.wait_until_not_exists()
    print("Table deleted.")
    
except:
    print("Table not yet created. Creating table...")

print_break("Creating a new table")

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
table = dynamodb.Table('wod_log')
table.wait_until_exists()
print("Table status:", table.table_status)

##############################################
# Step 2: create table
##############################################

print_break("Adding data to table")

with open("data/wod_log.json") as json_file:
    wod_log = json.load(json_file, parse_float = decimal.Decimal)
    for movement in wod_log:
        name = movement['name']
        date = movement['date']
        sets = int(movement['sets'])
        reps = int(movement['reps'])
        weight = movement['weight']
        user = movement['user']

        print("Adding movement:", name, date)

        table.put_item(
           Item={
               'name': name,
               'date': date,
               'sets': sets,
               'reps': reps,
               'weight': weight,
               'user': user
            }
        )

print("Complete!")