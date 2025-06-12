import streamlit as st

# ---------- Page Config ----------
st.set_page_config(page_title="BudMenu", layout="centered")

# ---------- Title & Store Selector ----------
st.markdown("<h1 style='text-align: center;'>🌿 Store Bud Menu🌿</h1>", unsafe_allow_html=True)
st.markdown("### Select your store location")

store = st.selectbox("Choose a location:", ["Melville", "Linden", "Fourways"])

# ---------- Category Navigation ----------
st.markdown("---")
st.markdown("### Browse Our Categories")

col1, col2 = st.columns(2)

with col1:
    if st.button("🌸 Flower", use_container_width=True):
        st.session_state["category"] = "flower"
        st.session_state["subcategory"] = None  # Reset subcategory if changing main category

    if st.button("🍭 Edibles", use_container_width=True):
        st.session_state["category"] = "edibles"
        st.session_state["subcategory"] = None

with col2:
    if st.button("💨 Vapes", use_container_width=True):
        st.session_state["category"] = "vapes"
        st.session_state["subcategory"] = None

    if st.button("🎒 Accessories", use_container_width=True):
        st.session_state["category"] = "accessories"
        st.session_state["subcategory"] = None

# ---------- Conditional Navigation ----------
if "category" in st.session_state:
    category = st.session_state["category"]
    st.markdown(f"### Showing items in **{category.capitalize()}** for **{store}**")

    # 🌸 If category is "flower", show flower subcategories
    if category == "flower":
        subcategories = [
            "Outdoor",
            "Greenhouse",
            "Premium Greenhouse",
            "Aeroponics",
            "Indoor",
            "Hydroponics"
        ]
        subcat = st.radio("Choose a flower type:", subcategories, horizontal=True)
        st.session_state["subcategory"] = subcat

        # Show placeholder for menu items in this subcategory
        st.info(f"Menu items for **{subcat}** flower will appear here.")
    else:
        # Placeholder for other categories
        st.info("Item list will go here based on your category/store data.")
