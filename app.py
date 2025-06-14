import streamlit as st
from components.landing import show_landing
from admin.portal import show_admin_portal

# Sidebar mode switch
mode = st.sidebar.selectbox("Select Mode:", ["Customer", "Admin"])

if mode == "Customer":
    show_landing()
elif mode == "Admin":
    show_admin_portal()
