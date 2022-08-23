import boto3
from decimal import *
from datetime import datetime
import random

TABLE_NAME = 'csat-table4'
REGION_NAME = 'ap-northeast-2'

dynamodb = boto3.resource('dynamodb', region_name = REGION_NAME)
table = dynamodb.Table(TABLE_NAME)

for idx in range(5):
    
    now = str(datetime.now())
    job_impact_score = random.uniform(0, 5)
    courseware_score = random.uniform(0, 5)
    environment_score = random.uniform(0, 5)
    instructor_score = random.uniform(0, 5)
    overall_score = random.uniform(0, 5)

    table.put_item(
        Item={
            'Alias': 'seonggyu',
            'CreatedAt': now,
            'job_impact_score': round(Decimal(job_impact_score), 2),
            'courseware_score': round(Decimal(courseware_score), 2),
            'environment_score': round(Decimal(environment_score), 2),
            'instructor_score': round(Decimal(instructor_score), 2),
            'overall_score': round(Decimal(overall_score), 2),
        }
    )

print("Done!")