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

print("Table status:"