import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import time
import pandas as pd
from random import randrange


def left_callback():
    st.session_state.left_clicked = True


def right_callback():
    st.session_state.right_clicked = True


def up_callback():
    st.session_state.up_clicked = True


def down_callback():
    st.session_state.down_clicked = True


# getting level


@st.cache
def fetch_data():
    df = pd.read_csv("Plansza.csv", sep=",", header=None)
    return df


# level renderer

tileset = {
    "E": "&#xB7;",  # "&#xA0;",
    "W": '<span style="color:White">&#x2593;</span>',
    "C": "&#x2591;",
    "D": '<span style="color:Grey">D</span>',
    "@": '<span style="color:green">@</span>',
    "G": '<span style="color:gold">G</span>',
    "M": '<span style="color:white">M</span>',
    "B": '<span style="color:red">B</span>',
    "N": "&#xA0;",
}
tileset_movable = {
    "E": True,
    "W": False,
    "C": True,
    "D": True,
    "@": False,
    "G": True,
    "M": True,
    "B": True,
    "N": False,
}


move_directions = ["l", "r", "u", "d"]


def level_renderer(df):
    l1 = '<span style="color:Grey">'
    for x in df:  # array from data frame: df.values
        for y in x:
            l1 = l1 + tileset[y]
        l1 = l1 + "<br>"
        # print("this is value", tileset[y], " yes |")
    l1 = l1 + "</span>"
    return l1


# array_mover


def move(inital_array, direction, who):

    # where is the player?
    k = np.where(inital_array == who)

    # check if we have anything to return (important for non-player)
    if any(k[0]):
        from_top = k[0][0]
        from_left = k[1][0]
        # st.write(k)

        # let's copy input array and remove player
        array_temp = inital_array.copy()
        array_temp[from_top, from_left] = "E"

        # let's check where player can move
        movement = {}
        movement["lt"] = inital_array[from_top, from_left - 1]  # left
        movement["rt"] = inital_array[from_top, from_left + 1]  # right
        movement["ut"] = inital_array[from_top - 1, from_left]  # up
        movement["dt"] = inital_array[from_top + 1, from_left]  # down
        st.session_state["previous_movement_state"] = movement

        # st.write(movement)

        if direction == "l":
            if from_left > 0:
                if tileset_movable[movement["lt"]] == True:
                    array_temp[from_top, from_left - 1] = who
                    st.session_state["previous_move"] = "l"
                    return array_temp
                else:
                    return inital_array
            else:
                return inital_array

        if direction == "r":
            if from_left < 48:
                # st.write(from_left)
                if tileset_movable[movement["rt"]] == True:
                    array_temp[from_top, from_left + 1] = who
                    st.session_state["previous_move"] = "r"
                    return array_temp
                else:
                    return inital_array
            else:
                return inital_array
        if direction == "u":
            if from_top > 0:
                if tileset_movable[movement["ut"]] == True:
                    array_temp[from_top - 1, from_left] = who
                    st.session_state["previous_move"] = "u"
                    return array_temp
                else:
                    return inital_array
            else:
                return inital_array

        if direction == "d":
            if from_top < 48:
                if tileset_movable[movement["dt"]] == True:
                    array_temp[from_top + 1, from_left] = who
                    st.session_state["previous_move"] = "d"
                    return array_temp
                else:
                    return inital_array
            else:
                return inital_array
    else:
        return inital_array


# initiate buttons & variables

if "left_clicked" not in st.session_state:
    st.session_state["left_clicked"] = False

if "right_clicked" not in st.session_state:
    st.session_state["right_clicked"] = False

if "up_clicked" not in st.session_state:
    st.session_state["up_clicked"] = False

if "down_clicked" not in st.session_state:
    st.session_state["down_clicked"] = False

if "gold" not in st.session_state:
    st.session_state["gold"] = 0

#################################
#
#       MAIN GAME CODE
#
#################################

df = fetch_data()

if "array" not in st.session_state:
    st.session_state["array"] = df.values

if "array_before_move" not in st.session_state:
    st.session_state["array_before_move"] = df.values

display_html = st.empty()
html = level_renderer(st.session_state["array"])  # chamber_renderer(size)
display_html = st.markdown(html, unsafe_allow_html=True)

#############################
#
#   game objects interactions
#
##########################


def Interaction(game_object):
    # actual position of the player
    k = np.where(st.session_state["array"] == "@")
    # st.write(k)
    from_top = k[0][0]
    from_left = k[1][0]

    # initiate response
    result = False

    # check if actual position of player is equal to position of Door
    for i in range(
        len(np.where(st.session_state["array_before_move"] == game_object)[0])
    ):

        if (
            from_top
            == np.where(st.session_state["array_before_move"] == game_object)[0][i]
            and from_left
            == np.where(st.session_state["array_before_move"] == game_object)[1][i]
        ):
            result = True

    return result


#################################
#
#       REACTIONS TO BUTTONS
#
#################################

if st.session_state.left_clicked:
    # status = st.write(move(df.values, "left"))  # st.write("left")

    st.session_state["array"] = move(st.session_state["array"], "l", "@").copy()
    # move boss
    st.session_state["array"] = move(
        st.session_state["array"], move_directions[randrange(4)], "B"
    ).copy()
    # move monster
    st.session_state["array"] = move(
        st.session_state["array"], move_directions[randrange(4)], "M"
    ).copy()

    html = level_renderer(st.session_state["array"])
    st.session_state.left_clicked = False
    display_html.empty()
    display_html = st.markdown(html, unsafe_allow_html=True)

    #
    # WRAP THIS PART LATER
    #

    if Interaction("D") == True:
        # st.write(Door())
        st.write("door opened")

    if Interaction("G") == True:
        # st.write(Door())
        st.write("gold acquired")
        st.session_state["gold"] = st.session_state["gold"] + 10

    # update map
    st.session_state["array_before_move"] = st.session_state["array"]

if st.session_state.right_clicked:
    # status = st.write(move(df.values, "left"))  # st.write("left")
    st.session_state["array"] = move(st.session_state["array"], "r", "@").copy()
    # move boss
    st.session_state["array"] = move(
        st.session_state["array"], move_directions[randrange(4)], "B"
    ).copy()
    # move monster
    st.session_state["array"] = move(
        st.session_state["array"], move_directions[randrange(4)], "M"
    ).copy()
    html = level_renderer(st.session_state["array"])
    st.session_state.right_clicked = False
    display_html.empty()
    display_html = st.markdown(html, unsafe_allow_html=True)

    #
    # WRAP THIS PART LATER
    #

    if Interaction("D") == True:
        # st.write(Door())
        st.write("door opened")

    if Interaction("G") == True:
        # st.write(Door())
        st.write("gold acquired")
        st.session_state["gold"] = st.session_state["gold"] + 10

    # update map
    st.session_state["array_before_move"] = st.session_state["array"]

if st.session_state.up_clicked:
    # status = st.write(move(df.values, "left"))  # st.write("left")
    st.session_state["array"] = move(st.session_state["array"], "u", "@").copy()
    # move boss
    st.session_state["array"] = move(
        st.session_state["array"], move_directions[randrange(4)], "B"
    ).copy()
    # move monster
    st.session_state["array"] = move(
        st.session_state["array"], move_directions[randrange(4)], "M"
    ).copy()
    html = level_renderer(st.session_state["array"])
    st.session_state.up_clicked = False
    display_html.empty()
    display_html = st.markdown(html, unsafe_allow_html=True)

    #
    # WRAP THIS PART LATER
    #

    if Interaction("D") == True:
        # st.write(Door())
        st.write("door opened")

    if Interaction("G") == True:
        # st.write(Door())
        st.write("gold acquired")
        st.session_state["gold"] = st.session_state["gold"] + 10

    # update map
    st.session_state["array_before_move"] = st.session_state["array"]

if st.session_state.down_clicked:
    # status = st.write(move(df.values, "left"))  # st.write("left")

    # move player
    st.session_state["array"] = move(st.session_state["array"], "d", "@").copy()

    # move boss
    st.session_state["array"] = move(
        st.session_state["array"], move_directions[randrange(4)], "B"
    ).copy()
    # move monster
    st.session_state["array"] = move(
        st.session_state["array"], move_directions[randrange(4)], "M"
    ).copy()
    html = level_renderer(st.session_state["array"])
    st.session_state.down_clicked = False
    display_html.empty()
    display_html = st.markdown(html, unsafe_allow_html=True)

    #
    # WRAP THIS PART LATER
    #

    if Interaction("D") == True:
        # st.write(Door())
        st.write("door opened")

    if Interaction("G") == True:
        # st.write(Door())
        st.write("gold acquired")
        st.session_state["gold"] = st.session_state["gold"] + 10

    # update map
    st.session_state["array_before_move"] = st.session_state["array"]

st.caption(
    "Level: 1" + " Gold: " + str(st.session_state["gold"]) + " Hp: 11(20) Exp: 2/14"
)


st.markdown(
    """
<style>
/*center metric label*/
div[data-testid="stVerticalBlock"] {
    gap: 0px;
}


p {
 font-size: 14px;
 line-height: 16px;
 font-family: "Courier New", Courier, monospace;
}
</style>
""",
    unsafe_allow_html=True,
)


# https://www.ee.ucl.ac.uk/~mflanaga/java/HTMLandASCIItableC1.html

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
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        '<br> <span style="color:green">@</span> - player', unsafe_allow_html=True
    )
    st.markdown('<br> <span style="color:red">B</span> - boss', unsafe_allow_html=True)
    st.markdown(
        '<br> <span style="color:white">M</span> - monster', unsafe_allow_html=True
    )
    st.markdown('<br> <span style="color:gold">G</span> - gold', unsafe_allow_html=True)
    st.markdown(
        '<br> <span style="color:grey">D</span> - door',
        unsafe_allow_html=True,
    )
    st.markdown("<br>", unsafe_allow_html=True)
    st.caption(
        "Streamlit Rogue v0.1- inspired by Rogue (also known as Rogue: Exploring the Dungeons of Doom) a dungeon crawling video game by Michael Toy and Glenn Wichman with later contributions by Ken Arnold. Rogue was originally developed around 1980 for Unix-based mainframe systems as a freely distributed executable. It was later included in the official Berkeley Software Distribution 4.2 operating system (4.2BSD)."
    )

    # "C": "&#x2591;",
    # "D": "D",
    # "@": '<span style="color:green">@</span>',
    # "G": '<span style="color:gold">G</span>',
    # "M": "M",
    # "B": '<span style="color:red">B</span>',

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
