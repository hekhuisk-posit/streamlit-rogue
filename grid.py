import streamlit as st


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# ---------------- CSS ----------------

local_css("style.css")


wall = "https://thumbs2.imgbox.com/10/db/7zaxbIP8_t.png"
floor = "https://thumbs2.imgbox.com/fa/32/02bMMt5S_t.png"
wall_inner = "https://thumbs2.imgbox.com/a9/db/bpGqFg8q_t.png"
wall_outer_w = "https://thumbs2.imgbox.com/ec/19/GL9KbbPq_t.png"
wall_outer_nw = "https://thumbs2.imgbox.com/fc/b5/y7nSLPhM_t.png"
wall_outer_n = "https://thumbs2.imgbox.com/6d/e2/7n2IlNB9_t.png"
floor_stain_1 = "https://thumbs2.imgbox.com/99/26/4m4rKZCS_t.png"
npc_wizzard = "https://oshi.at/Timp/PgLb.png"
st.markdown(
    f"""
        <div class="container">
        <div class="gamegrid">
        <img src="{wall_outer_nw}" style="grid-column-start: 1; grid-row-start: 1;">
        <img src="{wall_outer_n}" style="grid-column-start: 2; grid-row-start: 1;">
        <img src="{wall_outer_n}" style="grid-column-start: 3; grid-row-start: 1;">
        <img src="{wall_outer_n}" style="grid-column-start: 4; grid-row-start: 1;">
        <img src="{wall_outer_n}" style="grid-column-start: 5; grid-row-start: 1;">
        <img src="{wall_outer_n}" style="grid-column-start: 5; grid-row-start: 1;">
        <img src="{wall_outer_n}" style="grid-column-start: 6; grid-row-start: 1;">
        <img src="{wall_outer_n}" style="grid-column-start: 7; grid-row-start: 1;">
        <img src="{wall_outer_n}" style="grid-column-start: 8; grid-row-start: 1;">
        <img src="{wall_outer_n}" style="grid-column-start: 9; grid-row-start: 1;">
        <img src="{wall_outer_n}" style="grid-column-start: 10; grid-row-start: 1;">
        <img src="{wall_outer_w}" style="grid-column-start: 1; grid-row-start: 2;">
        <img src="{wall}" style="grid-column-start: 2; grid-row-start: 2;">
        <img src="{wall}" style="grid-column-start: 3; grid-row-start: 2;">
        <img src="{wall}" style="grid-column-start: 4; grid-row-start: 2;">
        <img src="{wall}" style="grid-column-start: 5; grid-row-start: 2;">
        <img src="{wall}" style="grid-column-start: 6; grid-row-start: 2;">
        <img src="{wall}" style="grid-column-start: 7; grid-row-start: 2;">
        <img src="{wall}" style="grid-column-start: 8; grid-row-start: 2;">
        <img src="{wall}" style="grid-column-start: 9; grid-row-start: 2;">
        <img src="{wall}" style="grid-column-start: 10; grid-row-start: 2;">
        <img src="{wall_outer_w}" style="grid-column-start: 1; grid-row-start: 3;">
        <img src="{floor_stain_1}" style="grid-column-start: 2; grid-row-start: 3;">
        <img src="{floor_stain_1}" style="grid-column-start: 3; grid-row-start: 3;">
        <img src="{floor_stain_1}" style="grid-column-start: 4; grid-row-start: 3;">
        <img src="{floor_stain_1}" style="grid-column-start: 5; grid-row-start: 3;">
        <img src="{floor_stain_1}" style="grid-column-start: 6; grid-row-start: 3;">
        <img src="{floor_stain_1}" style="grid-column-start: 7; grid-row-start: 3;">
        <img src="{floor_stain_1}" style="grid-column-start: 8; grid-row-start: 3;">
        <img src="{floor_stain_1}" style="grid-column-start: 9; grid-row-start: 3;">
        <img src="{floor_stain_1}" style="grid-column-start: 10; grid-row-start: 5;">
        <img src="{npc_wizzard}" style="grid-column-start: 5; grid-row-start: 3;">
        </div>
        <div class="gamegrid2">
        
        </div>
        </div>
    """,
    unsafe_allow_html=True,
)
