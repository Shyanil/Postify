import json
import streamlit as st
from few_short import FewShortPosts
from post_generator import generate_post
from post_generator import generate_image_ideas

length_options = ["Short", "Medium", "Long"]



def unique_languages(json_path):
    with open(json_path , 'r' , encoding='utf-8') as f:
        posts = json.load(f)
    language = set()
    for post in posts:
        lang = post.get('language')
        if lang:
            language.add(lang)
    return list(language)


language_options = unique_languages('data/preprocess_post.json')

def add_custom_fonts():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto&family=Open+Sans&display=swap');

        html, body, [class*="css"]  {
            font-family: 'Roboto', 'Open Sans', sans-serif;
        }

        /* You can also customize font weights, sizes here */
        </style>
        """,
        unsafe_allow_html=True
    )

def main():
    st.set_page_config(page_title="LinkedIn Post Generator", layout="centered")

    add_custom_fonts()

    st.title("💡 LinkedIn Post Generator")
    st.markdown("Create engaging LinkedIn posts efficiently.")

    fs = FewShortPosts()
    tags = fs.get_tags()

    with st.form("post_form"):
        col1, col2, col3 = st.columns([4, 2, 2])
        with col1:
            selected_tag = st.selectbox("Select Topic", options=tags, help="Choose the topic of your LinkedIn post")
        with col2:
            selected_length = st.selectbox("Select Length", options=length_options, help="Choose the post length")
        with col3:
            selected_language = st.selectbox("Select Language", options=language_options, help="Choose the post language")

        st.markdown("")

        generate_clicked = st.form_submit_button("🚀 Generate Post")

    st.markdown("---")

    if generate_clicked:
        with st.spinner("Generating your post..."):
            post = generate_post(selected_length, selected_language, selected_tag)
            image_ideas = generate_image_ideas(post)
        st.success("Here is your LinkedIn post:")
        st.text_area("Generated Post", post, height=200)

        st.markdown("## 🖼️ Image Idea")
        st.info("Add ideas here for what kind of image could visually complement the post. For now, this is just a placeholder box.")
        st.text_area("Suggested Image Concepts", f"{image_ideas}", height=200)

    st.markdown("---")
    st.caption("Powered by Shyanil | Created for efficient LinkedIn content creation")

if __name__ == "__main__":
    main()
