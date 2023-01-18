import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import random


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.set_page_config(
    page_title="The Shadows’s Den 2", page_icon="🗡️", initial_sidebar_state="collapsed"
)

# @st.cache
def fetch_data(level_name):
    df = pd.read_csv(level_name, sep=",", header=None)
    return df


# ---------------- links ----------------

# wall = "https://thumbs2.imgbox.com/10/db/7zaxbIP8_t.png"
# floor_plain = "https://thumbs2.imgbox.com/29/22/5rTLr6WH_t.png"
# wall_inner = "https://thumbs2.imgbox.com/a9/db/bpGqFg8q_t.png"
# wall_outer_w = "https://oshi.at/ErrD/vUVT.png"
# wall_outer_nw = "https://oshi.at/VhBU/UKur.png"
# wall_outer_sw = "https://oshi.at/mJCY/VIsb.png"
# wall_outer_n = "https://oshi.at/QwVn/Lotr.png"
# floor_stain_1 = "https://thumbs2.imgbox.com/99/26/4m4rKZCS_t.png"
# npc_wizzard = "https://oshi.at/Timp/PgLb.png"
# floor_edge_1 = "https://oshi.at/NPWg/TtAI.png"
# floor_edge_2 = "https://oshi.at/Uips/sZlP.png"
# floor_edge_3 = "https://oshi.at/KrDD/wYos.png"
cat = "https://oshi.at/rSxZ/Znvx.gif"
# cat_down = "https://oshi.at/RrvJ/OaYF.gif"
# cat_jump = "https://oshi.at/qMZe/FhrD.gif"
# merchant = ("https://oshi.at/sgTa/Qpyr.gif",)
# # npc_palladin = "https://oshi.at/nMCh/yKJe.png"
npc_palladin = "https://oshi.at/ZMUu/avRY.gif"
# monster_orc = "https://oshi.at/UCbC/VIJG.png"
# monster_ogre = "https://oshi.at/fqoK/sMTJ.png"
skelet = "https://oshi.at/HXMd/VQUl.gif"
demon = "https://oshi.at/BrFn/dMIx.gif"

# ---------------- callbacks ----------------


def left_callback():
    st.session_state["player_x"] -= 1


def right_callback():
    st.session_state["player_x"] += 1


def up_callback():
    st.session_state["player_y"] -= 1


def down_callback():
    st.session_state["player_y"] += 1


# ---------------- CSS ----------------

local_css("style.css")

if "player_x" not in st.session_state:
    st.session_state["player_x"] = 4

if "player_y" not in st.session_state:
    st.session_state["player_y"] = 5

tileset = {
    "@": "https://oshi.at/ZMUu/avRY.gif",
    "W": "https://thumbs2.imgbox.com/10/db/7zaxbIP8_t.png",  # wall
    "FP": "https://thumbs2.imgbox.com/29/22/5rTLr6WH_t.png",  # floor_plain
    # "FP": "https://oshi.at/PQkn/ExtR.png",  # floor 1 tilset 2
    "CAT": "https://oshi.at/rSxZ/Znvx.gif",  # cat
    "M": "https://oshi.at/HXMd/VQUl.gif",  # monster, skeleton
    "FS": "https://thumbs2.imgbox.com/99/26/4m4rKZCS_t.png",
    "E": "data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==",
    "FE3": "https://oshi.at/KrDD/wYos.png",  # floor_edge_3
    "WON": "https://oshi.at/QwVn/Lotr.png",  # wall outer n
    "WOW": "https://oshi.at/ErrD/vUVT.png",  # wall outer w
    "WONW": "https://oshi.at/VhBU/UKur.png",  # wall_outer_nw
    "DK": "https://oshi.at/GWHj/wtCk.png",  # darkness
    "WMB": "https://oshi.at/GoQE/zfAw.png",  # wall missing brick
}


def level_renderer(df, game_objects):
    i = 0
    j = 0
    level_html = '<div class="container"><div class="gamegrid">'
    for x in df:  # array from data frame: df.values
        # st.write(x)
        j = 0
        for y in x:

            # if y == "FP" and random.uniform(0, 1) > 0.7:
            #     tilset_tile = tileset["DK"]
            # else:
            #     tilset_tile = tileset[y]

            level_html = (
                level_html
                + '<img src="'
                + tileset[y]  # tilset_tile
                + '" style="grid-column-start: '
                + str(j + 1)
                + "; grid-row-start: "
                + str(i + 1)
                + ';">'
            )
            j = j + 1
        i = i + 1
    level_html = level_html + game_objects + "</div></div>"
    return level_html


# fetch level with certain number
df = fetch_data("test.csv")
if "level" not in st.session_state:  # or st.session_state["level_change"]:
    st.session_state["level"] = df.values


game_objects = f"""<img src="{npc_palladin}" class="player" style="grid-column-start: {st.session_state["player_x"]}; grid-row-start: {st.session_state["player_y"]};"><img src="{skelet}" style="grid-column-start: 42; grid-row-start: 30;"><img src="{cat}" style="grid-column-start: 33; grid-row-start: 3;">"""


html = level_renderer(st.session_state["level"], game_objects)

display_html = st.empty()
display_html = st.markdown(html, unsafe_allow_html=True)

# st.markdown(
#     f"""
#         <div class="container">
#         <div class="gamegrid">
#         <img src="{wall_outer_nw}" style="grid-column-start: 1; grid-row-start: 1;">
#         <img src="{wall_outer_n}" style="grid-column-start: 2; grid-row-start: 1;">
#         <img src="{wall_outer_n}" style="grid-column-start: 3; grid-row-start: 1;">
#         <img src="{wall_outer_n}" style="grid-column-start: 4; grid-row-start: 1;">
#         <img src="{wall_outer_n}" style="grid-column-start: 5; grid-row-start: 1;">
#         <img src="{wall_outer_n}" style="grid-column-start: 5; grid-row-start: 1;">
#         <img src="{wall_outer_n}" style="grid-column-start: 6; grid-row-start: 1;">
#         <img src="{wall_outer_n}" style="grid-column-start: 7; grid-row-start: 1;">
#         <img src="{wall_outer_n}" style="grid-column-start: 8; grid-row-start: 1;">
#         <img src="{wall_outer_n}" style="grid-column-start: 9; grid-row-start: 1;">
#         <img src="{wall_outer_n}" style="grid-column-start: 10; grid-row-start: 1;">
#         <img src="{wall_outer_w}" style="grid-column-start: 1; grid-row-start: 2;">
#         <img src="{wall}" style="grid-column-start: 2; grid-row-start: 2;">
#         <img src="{wall}" style="grid-column-start: 3; grid-row-start: 2;">
#         <img src="{wall}" style="grid-column-start: 4; grid-row-start: 2;">
#         <img src="{wall}" style="grid-column-start: 5; grid-row-start: 2;">
#         <img src="{wall}" style="grid-column-start: 6; grid-row-start: 2;">
#         <img src="{wall}" style="grid-column-start: 7; grid-row-start: 2;">
#         <img src="{wall}" style="grid-column-start: 8; grid-row-start: 2;">
#         <img src="{wall}" style="grid-column-start: 9; grid-row-start: 2;">
#         <img src="{wall}" style="grid-column-start: 10; grid-row-start: 2;">
#         <img src="{wall_outer_w}" style="grid-column-start: 1; grid-row-start: 3;">
#         <img src="{floor_stain_1}" style="grid-column-start: 2; grid-row-start: 3;">
#         <img src="{floor_stain_1}" style="grid-column-start: 3; grid-row-start: 3;">
#         <img src="{floor_stain_1}" style="grid-column-start: 4; grid-row-start: 3;">
#         <img src="{floor_stain_1}" style="grid-column-start: 5; grid-row-start: 3;">
#         <img src="{floor_stain_1}" style="grid-column-start: 6; grid-row-start: 3;">
#         <img src="{floor_stain_1}" style="grid-column-start: 7; grid-row-start: 3;">
#         <img src="{floor_stain_1}" style="grid-column-start: 8; grid-row-start: 3;">
#         <img src="{floor_stain_1}" style="grid-column-start: 9; grid-row-start: 3;">
#         <img src="{floor_stain_1}" style="grid-column-start: 10; grid-row-start: 3;">
#         <img src="{wall_outer_sw}" style="grid-column-start: 1; grid-row-start: 4;">
#         <img src="{floor_plain}" style="grid-column-start: 2; grid-row-start: 4;">
#         <img src="{floor_plain}" style="grid-column-start: 3; grid-row-start: 4;">
#         <img src="{floor_plain}" style="grid-column-start: 4; grid-row-start: 4;">
#         <img src="{floor_plain}" style="grid-column-start: 5; grid-row-start: 4;">
#         <img src="{floor_plain}" style="grid-column-start: 6; grid-row-start: 4;">
#         <img src="{floor_plain}" style="grid-column-start: 7; grid-row-start: 4;">
#         <img src="{floor_plain}" style="grid-column-start: 8; grid-row-start: 4;">
#         <img src="{floor_plain}" style="grid-column-start: 9; grid-row-start: 4;">
#         <img src="{floor_plain}" style="grid-column-start: 10; grid-row-start: 4;">

#         <img src="{floor_edge_2}" style="grid-column-start: 2; grid-row-start: 5;">
#         <img src="{floor_edge_1}" style="grid-column-start: 3; grid-row-start: 5;">
#         <img src="{floor_edge_2}" style="grid-column-start: 4; grid-row-start: 5;">
#         <img src="{floor_edge_1}" style="grid-column-start: 5; grid-row-start: 5;">
#         <img src="{floor_edge_2}" style="grid-column-start: 6; grid-row-start: 5;">
#         <img src="{floor_edge_1}" style="grid-column-start: 7; grid-row-start: 5;">
#         <img src="{floor_edge_2}" style="grid-column-start: 8; grid-row-start: 5;">
#         <img src="{floor_edge_1}" style="grid-column-start: 9; grid-row-start: 5;">


#         <img src="{floor_plain}" style="grid-column-start: 10; grid-row-start: 5;">
#         <img src="{floor_plain}" style="grid-column-start: 10; grid-row-start: 6;">
#         <img src="{floor_plain}" style="grid-column-start: 10; grid-row-start: 7;">
#         <img src="{floor_plain}" style="grid-column-start: 10; grid-row-start: 8;">


#         <img src="{floor_plain}" style="grid-column-start: 11; grid-row-start: 8;">
#         <img src="{floor_plain}" style="grid-column-start: 12; grid-row-start: 8;">
#         <img src="{floor_plain}" style="grid-column-start: 13; grid-row-start: 8;">
#         <img src="{floor_plain}" style="grid-column-start: 14; grid-row-start: 8;">
#         <img src="{floor_plain}" style="grid-column-start: 15; grid-row-start: 8;">

#         <img src="{floor_edge_2}" style="grid-column-start: 10; grid-row-start: 9;">
#         <img src="{floor_edge_3}" style="grid-column-start: 11; grid-row-start: 9;">
#         <img src="{floor_edge_3}" style="grid-column-start: 12; grid-row-start: 9;">
#         <img src="{floor_edge_3}" style="grid-column-start: 13; grid-row-start: 9;">
#         <img src="{floor_edge_3}" style="grid-column-start: 14; grid-row-start: 9;">
#         <img src="{floor_edge_3}" style="grid-column-start: 15; grid-row-start: 9;">


#         <img src="{wall_outer_n}" style="grid-column-start: 15; grid-row-start: 4;">
#         <img src="{wall_outer_n}" style="grid-column-start: 16; grid-row-start: 4;">
#         <img src="{wall_outer_n}" style="grid-column-start: 17; grid-row-start: 4;">
#         <img src="{wall_outer_n}" style="grid-column-start: 18; grid-row-start: 4;">

#         <img src="{wall}" style="grid-column-start: 15; grid-row-start: 5;">
#         <img src="{wall}" style="grid-column-start: 16; grid-row-start: 5;">
#         <img src="{wall}" style="grid-column-start: 17; grid-row-start: 5;">
#         <img src="{wall}" style="grid-column-start: 18; grid-row-start: 5;">


#         <img src="{floor_plain}" style="grid-column-start: 15; grid-row-start: 6;">
#         <img src="{floor_plain}" style="grid-column-start: 15; grid-row-start: 7;">
#         <img src="{floor_plain}" style="grid-column-start: 15; grid-row-start: 8;">
#         <img src="{floor_plain}" style="grid-column-start: 15; grid-row-start: 9;">
#         <img src="{floor_plain}" style="grid-column-start: 15; grid-row-start: 10;">

#         <img src="{floor_plain}" style="grid-column-start: 16; grid-row-start: 6;">
#         <img src="{floor_plain}" style="grid-column-start: 16; grid-row-start: 7;">
#         <img src="{floor_plain}" style="grid-column-start: 16; grid-row-start: 8;">
#         <img src="{floor_plain}" style="grid-column-start: 16; grid-row-start: 9;">
#         <img src="{floor_plain}" style="grid-column-start: 16; grid-row-start: 10;">

#         <img src="{floor_plain}" style="grid-column-start: 17; grid-row-start: 6;">
#         <img src="{floor_plain}" style="grid-column-start: 17; grid-row-start: 7;">
#         <img src="{floor_plain}" style="grid-column-start: 17; grid-row-start: 8;">
#         <img src="{floor_plain}" style="grid-column-start: 17; grid-row-start: 9;">
#         <img src="{floor_plain}" style="grid-column-start: 17; grid-row-start: 10;">

#         <img src="{floor_plain}" style="grid-column-start: 18; grid-row-start: 6;">
#         <img src="{floor_plain}" style="grid-column-start: 18; grid-row-start: 7;">
#         <img src="{floor_plain}" style="grid-column-start: 18; grid-row-start: 8;">
#         <img src="{floor_plain}" style="grid-column-start: 18; grid-row-start: 9;">
#         <img src="{floor_plain}" style="grid-column-start: 18; grid-row-start: 10;">

#         <img src="{floor_edge_3}" style="grid-column-start: 15; grid-row-start: 11;">
#         <img src="{floor_edge_3}" style="grid-column-start: 16; grid-row-start: 11;">
#         <img src="{floor_edge_3}" style="grid-column-start: 17; grid-row-start: 11;">
#         <img src="{floor_edge_3}" style="grid-column-start: 18; grid-row-start: 11;">


#         <img src="{npc_palladin}" class="player" style="grid-column-start: {st.session_state["player_x"]}; grid-row-start: {st.session_state["player_y"]};">

#         <img src="{skelet}" style="grid-column-start: 17; grid-row-start: 8;">

#         <img src="{cat}" style="grid-column-start: 12; grid-row-start: 7;">


#         </div>

#         </div>
#     """,
#     unsafe_allow_html=True,
# )

# st.markdown(
#     f"""
#         <img src="{npc_palladin}" class="player" style="grid-column-start: {st.session_state["player_x"]}; grid-row-start: {st.session_state["player_y"]};">

#         <img src="{skelet}" style="grid-column-start: 17; grid-row-start: 8;">

#         <img src="{cat}" style="grid-column-start: 12; grid-row-start: 7;">
#         </div>

#         </div>
#     """,
#     unsafe_allow_html=True,
# )

with st.sidebar:
    st.write("Use keyboard arrows or buttons below")
    st.markdown("<br>", unsafe_allow_html=True)
    left_col, middle_col, right_col = st.columns([1, 1, 1])
    with middle_col:
        st.button("&nbsp;UP&nbsp;", on_click=up_callback, key="UP")
    st.markdown("<br>", unsafe_allow_html=True)

    left_col, middle_col, right_col = st.columns([1, 1, 1])
    with left_col:
        st.button("LEFT", on_click=left_callback, key="LEFT")

    with right_col:
        st.button("RIGHT", on_click=right_callback, key="RIGHT")
    st.markdown("<br>", unsafe_allow_html=True)
    left_col, middle_col, right_col = st.columns([1, 1, 1])
    with middle_col:
        st.button("DOWN", on_click=down_callback, key="DOWN")


components.html(
    """
<script>
const doc = window.parent.document;
buttons = Array.from(doc.querySelectorAll('button[kind=secondary]'));
const left_button = buttons.find(el => el.innerText === 'LEFT');
const right_button = buttons.find(el => el.innerText === 'RIGHT');
const up_button = buttons.find(el => el.innerText === String.fromCharCode(160)+'UP'+String.fromCharCode(160));
const down_button = buttons.find(el => el.innerText === 'DOWN');
doc.addEventListener('keydown', function(e) {
switch (e.keyCode) {
    case 37: // (37 = left arrow)
        left_button.click();
        break;
    case 39: // (39 = right arrow)
        right_button.click();
        break;
    case 38: // (39 = right arrow)
        up_button.click();
        break;
    case 40: // (39 = right arrow)
        down_button.click();
        break;
}
});
</script>
""",
    height=0,
    width=0,
)
