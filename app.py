import streamlit as st
import pandas as pd

df = pd.read_csv("products.csv")

st.title("🛒 AI Shopping Buddy")

query = st.text_input("What are you looking for?")

budget = st.number_input(
    "Enter Budget",
    min_value=0
)

if st.button("Recommend"):

    query = query.lower()

    if "mobile" in query:
        category = "Mobile"

    elif "laptop" in query:
        category = "Laptop"

    elif "headphone" in query:
        category = "Headphones"

    else:
        category = None

    if category:

        result = df[
            (df["Category"] == category)
            &
            (df["Price"] <= budget)
        ]

        if not result.empty:
            st.success("Recommended Products")
            st.dataframe(result)
        else:
            st.warning("No products found")

    else:
        st.error("Please enter Mobile, Laptop or Headphones")