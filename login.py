import streamlit as st


st.set_page_config(initial_sidebar_state="collapsed")
unamelist = ['admin', 'suneesh']
passwlist = ['123','345']

uname = st.text_input(label="User name")
passw = st.text_input(label="Password")
login = st.button("Login")
if login:
    if uname in unamelist:
        if passw == passwlist[unamelist.index(uname)]:
            st.switch_page("pages/Aidetecter.py")
        else:
            st.subheader("User name or password is wrong", divider="red")
    else:
        st.subheader("User name or password is wrong", divider="red")

