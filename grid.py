import streamlit as st


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# ---------------- CSS ----------------

local_css("style.css")


wall = "https://thumbs2.imgbox.com/10/db/7zaxbIP8_t.png"
floor = "https://thumbs2.imgbox.com/fa/32/02bMMt5S_t.png"
wall_inner = "https://thumbs2.imgbox.com/a9/db/bpGqFg8q_t.png"
wall_outer = "https://thumbs2.imgbox.com/ec/19/GL9KbbPq_t.png"
wall_dot = "https://thumbs2.imgbox.com/fc/b5/y7nSLPhM_t.png"
st.markdown(
    f"""
        <div class="gamegrid">
        <div><img src="{wall_outer}" class="image"></div>
        <div><img src="{wall}" class="image"></div>
        <div><img src="{wall}" class="image"></div>
        <div><img src="{wall}" class="image"></div>
        <div><img src="{wall}" class="image"></div>
        <div><img src="{wall}" class="image"></div>
        <div><img src="{wall}" class="image"></div>
        <div><img src="{wall}" class="image"></div>
        <div><img src="{wall}" class="image"></div>
        <div><img src="{wall}" class="image" id="last10"></div>
        <div><img src="{wall_outer}" class="image"></div>
        <div><img src="{floor}" class="image"></div>
        <div><img src="{floor}" class="image"></div>
        <div><img src="{floor}" class="image"></div>
        <div><img src="{floor}" class="image"></div>
        <div><img src="{floor}" class="image"></div>
        <div><img src="{floor}" class="image"></div>
        <div><img src="{floor}" class="image"></div>
        <div><img src="{floor}" class="image"></div>
        <div><img src="{floor}" class="image"></div>
        </div>
    """,
    unsafe_allow_html=True,
)
