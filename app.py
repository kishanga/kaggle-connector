from connection import KaggleDatasetConnection
import streamlit as st

st.title("Connect to Kaggle")

st.subheader("Loading Netflix Movies and TV Shows dataset")

# load data
conn = st.experimental_connection("kaggle_datasets", type=KaggleDatasetConnection)
df = conn.get(path='shivamb/netflix-shows', filename='netflix_titles.csv', ttl=3600)

st.write('The dataset has {} rows and {} columns'.format(df.shape[0], df.shape[1]))

st.write('The columns are: {}'.format(', '.join(df.columns)))
st.write('Data Preview:')
st.dataframe(df.head(20))




