from streamlit_lottie import st_lottie as stl
import streamlit as st
import requests
st.set_page_config(page_title="North Dream", page_icon="wave", layout= "wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

menu = ("Home", "Products")
lottie_gadgets = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_b5nyw28b.json")


with st.container():
    column1, column2 = st.columns((1, 2))

    choice = st.sidebar.selectbox("Menu:", menu)
    st.sidebar.write("##")
    st.sidebar.write("Located in Athens we started in 2023 and our fist product are the cubik blocks!")
    st.sidebar.write("##")
    st.sidebar.write("Designer: Filippos Tsoukias")
    st.sidebar.write("Social: Nikos Melegovits")
    st.sidebar.write("Finance: Filippos Colagrande")
    st.sidebar.write("Managing: Lakios Padelis")
    for i in range(15):
        st.sidebar.write("##")
    st.sidebar.write("Copyright@2023")

    
    if choice == "Home":
        with column1:
            
            st.title("Welcome to North Dream!")
            st.write("----")
            st.header("About us:")
            st.write("##")
            st.write("""
                    
                    Here at North Dream we develop Gadgets that make our life and yours easier! 
                    Our gadgets not only help you, but make for a great toy for your kids and friends!
                    Our products are made with love and care to be the best for thaire use! 

                    """)


    if choice == "Products":
        with column1:
            st.title("Welcome to North Dream!")
            st.write("----")
            st.header("Products:")
            st.markdown("- The cubik blocks!")


with st.container():
    with column2:
        stl(lottie_gadgets, height = 450)

