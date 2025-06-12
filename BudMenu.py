import streamlit as st

# ---------- Page Config ----------
st.set_page_config(page_title="BudMenu", layout="centered")

# ---------- Title & Store Selector ----------
st.markdown("<h1 style='text-align: center;'>🌿 Welcome to BudMenu 🌿</h1>", unsafe_allow_html=True)
st.markdown("### Select your store location")

store = st.selectbox("Choose a location:", ["Pretoria", "Johannesburg", "Cape Town"])

# ---------- Category Navigation ----------
st.markdown("---")
st.markdown("### Browse Our Categories")

col1, col2 = st.columns(2)

with col1:
    if st.button("🌸 Flower", use_container_width=True):
        st.session_state["category"] = "flower"

    if st.button("🍭 Edibles", use_container_width=True):
        st.session_state["category"] = "edibles"

with col2:
    if st.button("💨 Vapes", use_container_width=True):
        st.session_state["category"] = "vapes"

    if st.button("🎒 Accessories", use_container_width=True):
        st.session_state["category"] = "accessories"

# ---------- Conditional Navigation ----------
if "category" in st.session_state:
    st.markdown(f"### Showing items in **{st.session_state['category'].capitalize()}** for **{store}**")
    # display the menu items for the selected category + store
    st.info("Item list will go here based on your category/store data.")
