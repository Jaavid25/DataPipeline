import pandas as pd
import streamlit as st
a = range(0,10)
index = list("abcdefghij")
s = pd.Series(a,index=index,name = "x")
y = pd.Series(a,index=index,name = "y")
df = pd.DataFrame({"duration":s,"number of words":y})
print(df)
st.write("# Global Statistics")
st.write(df)
st.write("# Histograms")
st.write("## Duration per lecture")

st.bar_chart(df["duration"])
st.bar_chart(df["number of words"])