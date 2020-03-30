import decimal
import json
import time

import boto3

dynamodb = boto3.resource('dynamodb', region_name='ca-central-1')
wod_log = dynamodb.Table('wod_log')

print(wod_log.item_count)
print(wod_log.key_schema)