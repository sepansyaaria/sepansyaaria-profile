import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config (
    page_title= "My Profile",
    page_icon=":boy:",
    layout="wide")

def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
                return None
        return r.json()


#header

lottie_coding = load_lottieurl("https://lottie.host/d27b9c3e-dc7e-4dd2-802b-ca09ed1c0a78/wafqChnm2E.json")

st.subheader("hi, i am Sepansya Aria Muhammad Asfian :wave:")
st.title("Student of Science Institute and National Technology")
st.write("I am passionate to learn something new and also looking for new experience.")
st.write("This is my social media:")
st.write("[My Instagram >](https://www.instagram.com/sepansyaas/)")
st.write("[My Twitter >](https://twitter.com/expelliarmusl)")


st.write("---")
left_column,right_column = st.columns(2)
with left_column:
        st.header("What i do")
        st.write("##")
        st.write(
            """ 
            On my Youtube channel i make toturials for people who:
            - are looking for a structure of network thopology and security network
            - are looking for explaination of basic python
            - are looking fot how to create a basic animation with Macroflash 8

            """
        )
        st.write("[My Youtube Channel >](https://www.youtube.com/channel/UCaU3BKuo5n1svJdFMZn-ahQ)")

with right_column:
        st_lottie(lottie_coding, height = 300, key="coding")

st.write("---")
st.header(":mailbox: Get In Touch With Me!")
st.write("##")

contact_form = """
<form action="https://formsubmit.co/abangepan18@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="message" placeholder="Your Massage here" ></textarea>
     <button type="submit">Send</button>
</form>
"""
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form,unsafe_allow_html=True)
with right_column:
       st.empty()

def local_css(file_name):
       with open(file_name) as f:
              st.markdown(f"<style>{f.read()}<style/>",unsafe_allow_html=True)

local_css("style/style.css")