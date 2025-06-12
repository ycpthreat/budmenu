import streamlit as st
import pandas as pd

st.title("Bud Box Melville")
st.subheader("*last stock update: 12:00")

# Dummy inventory
data = {
    "Store": ["Pretoria", "Johannesburg", "Cape Town"],
    "Item": ["PS5 Controller", "Xbox Console", "PS5 Controller"],
    "Quantity": [5, 3, 0]
}

df = pd.DataFrame(data)

store = st.selectbox("Choose a store:", df["Store"].unique())
filtered = df[df["Store"] == store]

st.write("Items available:")
st.table(filtered)
