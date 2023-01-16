import streamlit as st


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# ---------------- CSS ----------------

local_css("style.css")


st.markdown(
    f"""
        <div class="gamegrid">
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat3.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat2.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat3.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat2.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat3.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat2.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat3.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat2.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat3.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat2.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat3.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat2.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat3.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat2.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat3.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat2.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat3.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat2.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat3.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat2.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat3.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat2.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat3.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat2.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat3.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat2.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat3.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat2.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat3.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat2.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat3.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat2.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat3.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat2.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat3.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat2.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat3.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat2.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat3.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat2.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat3.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat2.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat3.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat.png" class="image"></div>
        <div><img src="https://raw.githubusercontent.com/TomJohnH/streamlit-game/main/images/cat2.png" class="image"></div>
        </div>
    """,
    unsafe_allow_html=True,
)
