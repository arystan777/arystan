import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="M5cs", page_icon="🥶", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

lottie_coding = load_lottieurl("https://lottie.host/5ddc0ca2-0232-4746-9e5f-abe8129e5230/cqw38AEF9F.json")
img_lottie_animation = ("https://www.aspiringsupercarowners.com/wp-content/uploads/2021/01/bmw_m5_cs_6.jpg")
img_lottie_negr = ("https://i.ytimg.com/vi/5NCR_wWWE2Q/maxresdefault.jpg")
with st.container():
    st.subheader("Sup folks")
    st.title("I am Arystan from 9(G) class")
    st.write("Here you can learn abt me ")
    st.write("BD 11.03.09")   
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Flag_of_Kazakhstan.svg/255px-Flag_of_Kazakhstan.svg.png")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Hobby")
        st.write("##")
        st.write(
            """
            Car spotting

            Car spotting is a thrilling hobby that involves observing and identifying various automobiles in their natural environment.
            It fosters a sense of community among enthusiasts and offers an educational experience in automotive design and history. 
            Through photography, enthusiasts capture the beauty of their sightings, turning their passion into artistic expression. 
            Car spotting is more than just a pastime; it's a way of life for automotive enthusiasts, providing excitement, camaraderie, and appreciation for the craftsmanship behind each vehicle.
            """
        )
        st.write("[You have to see my page >](https://www.instagram.com/qazaqelinecars?igsh=Y2szMHdnc2o1enU2)")
    with right_column:
        st.image("https://media.autoexpress.co.uk/image/private/s--4HN2uUTf--/f_auto,t_content-image-full-desktop@1/v1686238153/autoexpress/2023/06/BMW%20M3%20CS%202023%20UK.jpg")

with st.container():
    st.write("---")
    st.header("Education & skills")
    st.write("##")
    st.subheader("Tamos")
    st.write(
            """
            Since the fourth grade, I started studying at Tamos Education school, and it became an exciting journey of knowledge.
            I really like the whole learning process: interesting lessons, a variety of activities and caring teachers make learning fun and informative. 
            I enjoy every day at school and am happy to study new subjects and learn about the world around me.
            It was a great experience
            """
        )
with st.container():
        st.subheader("Skills")
        st.write(
            """
            As a programmer, I have excellent programming skills, which allows me to create innovative programs and effectively solve complex problems. 
            In addition, I also actively practice calisthenics, which helps me maintain excellent physical fitness, endurance and flexibility. 
            Both of these skills reflect my constant pursuit of self-improvement and achieving high results in various areas of my life.
            """
        )


with st.container():
    st.write("---")
    st.header("Feedback")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/arystan909@yahoo.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="your name" required>
        <input type="email" name="email" placeholder="your email" required>
        <textarea name="message" placeholder="Your message hear" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(contact_form, unsafe_allow_html=True)
    with c2:
        st.empty()
