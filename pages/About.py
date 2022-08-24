import streamlit as st
st.title('AWS Korea CSAT Calculator')

st.header('Introduction')

st.write('Hi, my name is Nick Park from AWS Korea Traing & Certification team.\
    I am a technical trainer who made this demo web page for technical trainers checking their csat in AWS Korea\
        more quickly and accurately.')

st.header('How to use')

st.subheader('First')
st.write('Go to **Upload** menu on the left side-bar. Then write your alias(such as seonggyu)\
    and attach your csv file downloaded from kiku.aws.training. After that, click **Upload** button below.\
    Once you check **Success** sign, it is done.')

st.subheader('Second')
st.write('Write your alias. and click **Confirm** button. You can go through two types of data.\
    The chart above is all about your recent CSAT data. The graph chart below is historical data \
        in terms of your total CSAT scores that you have uploaded through this site.')

st.header('How it works')
st.write('This page is made up of Streamlit. Streamlit is an open-source app framework written in Python. \
    Stream application is on to EC2 server through github and it runs in background. \
    If you upload your file, it is loaded in S3 which triggers Lambda to calculate your CSAT. \
        After it finishes your scores, the data are saved in DynamoDB.')
