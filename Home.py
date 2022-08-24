import streamlit as st
import boto3
from boto3.dynamodb.conditions import Key
import pandas as pd
import numpy as np

TABLE_NAME = 'csat-table4'
REGION_NAME = 'ap-northeast-2'

dynamodb = boto3.resource('dynamodb', region_name = REGION_NAME)
table = dynamodb.Table(TABLE_NAME)

st.title("AWS Korea CSAT Calculator")
alias = st.text_input(label = "Alias", value = "seonggyu")

print(alias)
if st.button("Confirm"):
    # response = table.get_item(
    # TableName = TABLE_NAME,
    #     Key = {

    #         'alias-index' : alias
    #     }
    # )
    response = table.query(KeyConditionExpression=Key('Alias').eq(alias))
    # response = table.query(
    #     IndexName = "alias-inedx"
    # )
    if len(response['Items']) == 0:
        st.write('no data')
    else:
        print(response)
        # print(response['Item'][0])
        # print(type(3.14))
        # print((response['Item'][0]['job_impact_score']))
        job_impact_score = float(response['Items'][0]['job_impact_score'])
        courseware_score = float(response['Items'][0]['courseware_score'])
        environment_score = float(response['Items'][0]['environment_score'])
        instructor_score = float(response['Items'][0]['instructor_score'])
        overall_score = float(response['Items'][0]['overall_score'])

        con = st.container()
        con.caption("Result")
        con.write(f"Hello! {str(alias)}. This score is the most recent you've got from customers.")
        view = pd.DataFrame(
            [[job_impact_score], [courseware_score], [environment_score], [instructor_score], [overall_score]],
            index=['job_impact', 'courseware', 'environment', 'instructor', 'overall']
        )

        # view
        st.bar_chart(view)

        historical = []
        job_impact_scores = []
        courseware_scores = []
        environment_scores = []
        instructor_scores = []
        overall_scores = []

        for item in response['Items']:
            for key, value in item.items():
                if key == 'job_impact_score':
                    job_impact_scores.append(float(value))
                elif key == 'overall_score':
                    overall_scores.append(float(value))
                elif key == 'courseware_score':
                    courseware_scores.append(float(value))
                elif key == 'instructor_score':
                    instructor_scores.append(float(value))
                elif key == 'environment_score':
                    environment_scores.append(float(value))
                else:
                    continue
        historical.append(job_impact_scores)
        historical.append(courseware_scores)
        historical.append(environment_scores)
        historical.append(instructor_scores)
        historical.append(overall_scores)

        st.write('## Historical Csat Data')
        st.write('The chart below shows your historical data for CSAT.')
        print('test')
        print(np.random.randn(len(historical[0]), 5))
        print('---')
        print(historical)
        # chart_data = pd.DataFrame(
        #     np.random.randn(20, 5),
        #     columns=['job_impact', 'courseware', 'environment', 'instructor', 'overall'])
        chart_data = pd.DataFrame(
            historical,
            columns=['job_impact', 'courseware', 'environment', 'instructor', 'overall'])

        st.line_chart(chart_data)

# st.write('Hi my name is Nick Park. This site is made up of Streamlit written by')
# st.write('## The most recent lecture score')

# view

# st.bar_chart(view)
