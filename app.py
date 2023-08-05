from connection import KaggleDatasetConnection
import streamlit as st

st.title("Connect to Kaggle")

st.subheader("Singapore Lottery Numbers")

# load data
conn = st.experimental_connection("kaggle_datasets", type=KaggleDatasetConnection)
df = conn.get(path='calven22/singapore-lottery-numbers', filename='Toto Winning Numbers.csv', ttl=3600)

st.write('The dataset has {} rows and {} columns'.format(df.shape[0], df.shape[1]))

st.write('The columns are: {}'.format(', '.join(df.columns)))
st.write('Data Preview:')
st.dataframe(df.head(100))




