import streamlit as st
import logging
import boto3
import os
import pandas as pd
from io import StringIO
from botocore.exceptions import ClientError

FILE_NAME = 'tempDir' + '/'
BUCKET_NAME = 'nick-park-csat-bucket'

def upload_file(alias, file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = alias + '/' + os.path.basename(FILE_NAME)
        print(object_name)
    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(FILE_NAME, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

alias = st.text_input('Insert your Alias', 'seonggyu')
st.write('The current alias is', alias)

uploaded_file = st.file_uploader("Choose a file", type=['csv'])
# print("uploaded_file : ", uploaded_file)

if uploaded_file is not None:
    FILE_NAME += uploaded_file.name
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    # st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    # st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    # st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

    # Save a uploaded file
    with open(os.path.join("tempDir",uploaded_file.name),"wb") as f:
        f.write(uploaded_file.getbuffer())

if st.button("Upload"):
    if upload_file(alias, uploaded_file.name, BUCKET_NAME):
        st.success('This is a success message!')
    else:
        st.error('This is an error', icon="🚨")

else:
    st.write("Please upload your CSAT csv file")