import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Spotify Data Analysis")

df = pd.read_csv("Spotify.csv")

st.write(df.head())
st.header("Dataset Information")

st.write("Total Rows:", df.shape[0])
st.write("Total Columns:", df.shape[1])

st.subheader("Column Names")
st.write(df.columns.tolist())
st.header("Energy Distribution")

fig = px.histogram(df, x="energy")
st.plotly_chart(fig)
st.header("Danceability Distribution")

fig = px.histogram(df, x="danceability")
st.plotly_chart(fig)
st.header("Top 10 Artists")

top_artists = df["artist"].value_counts().head(10)
fig = px.bar(x=top_artists.index, y=top_artists.values)
st.plotly_chart(fig)
st.header("Song Duration")

df["duration"] = df["duration_ms"] / 60000
fig = px.histogram(df, x="duration")
st.plotly_chart(fig)
st.header("Energy vs Danceability")

fig = px.scatter(df, x="energy", y="danceability")
st.plotly_chart(fig)
st.header("Tempo vs Danceability")

fig = px.scatter(df, x="tempo", y="danceability")
st.plotly_chart(fig)
st.header("Loudness vs Energy")

fig = px.scatter(df, x="energy", y="loudness")
st.plotly_chart(fig)
st.header("Danceability by Target")

fig = px.box(df, x="target", y="danceability")
st.plotly_chart(fig)
