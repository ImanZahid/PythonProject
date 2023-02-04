from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie

#https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title='My Webpage',page_icon="tada:" ,layout="wide")

def load_lottieURL(url):
	r= requests.get(url)
	if r.status_code !=200:
		return None

	return r.json()

def local_css(file_name):
	with open(file_name) as f:
		st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
local_css("style/style.css")


lottie_coding =load_lottieURL("https://assets8.lottiefiles.com/packages/lf20_tfb3estd.json")
img1=Image.open("images/pic2.png")
img2=Image.open("images/pic3.png")
img3=Image.open("images/pic1.png")

with st.container():
	st.subheader("Hi, I am Iman :wave:")
st.title("CTIS student at Bilkent University")
st.write("Meticulous web developer with over 2 years of front end experience and passion for responsive website design.")
st.write("[Llinkedin >](https://www.linkedin.com/in/iman-zahid/)")


with st.container():
	st.write("---")
	left_column,right_column=st.columns(2)
	with left_column:
		st.header("What I do")
		st.write("##")
		st.write("""
			I am currently a Front-end developer intern at Inovako and 
			a sophomore student aiming to become a professional software 
			engineer. My inquisitive nature pushes me to learn new technologies
			 to enhance my skill and gain maximum knowledge.""")
		st.header("Skills")
		st.write("LANGUAGES")
		st.write("""
			- JavaScript(ES6)
			- C/C++
			- Java
			- Python
			""")
		st.write("[GitHub >](https://github.com/ImanZahid)")
	with right_column:
		st_lottie(lottie_coding, height=300, key="coding")

with st.container():
	st.write("---")
	st.header("My Projects")
	st.write("##")
	image_column, text_column=st.columns((1,2))
	with image_column:
		st.image(img1)
		st.image(img2)

	with text_column:
		st.subheader("Garden of Eden")
		st.write("""
			🌼🌹 Garden of Eden is a flower shop app with some management features. Garden of Eden was built using Java and MySQL
			- Users can purchase flowers and flower jewelry.
			- Create their own bouquets.
			- Add/Delete from cart.
			- Manager can keep track of inventory.
			- Add/Delete from inventory.
			- Delete all expired products.
			- Keep track of statistics""")
with st.container():
	image_column,text_column=st.columns((1,2))
	with image_column:
		st.image(img3)
	with text_column:
		st.subheader("Word Puzzle")
		st.write("The game is a version of “Words of Wonders” mobile game made using HTML, CSS, Javascript and jQuery. With the given letters, you will find words that exist in the puzzle.")
with st.container():
	st.write("---")
	st.header("Get In Touch With Me!")
	st.write("##")

	contact_form="""
	<form action="https://formsubmit.co/imanzahidzahid3@gmail.com" method="POST">
	<input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
	</form>
	"""
left_column,right_column=st.columns(2)
with left_column:
	st.markdown(contact_form, unsafe_allow_html=True)
	with right_column:
		st.empty()









	
		

