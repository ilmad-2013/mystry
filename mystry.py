import streamlit as st

st.set_page_config(
    page_title="Mystery Mansion",
    page_icon="🔎"
)

st.title("🔎 Mystery Mansion")
st.write("A strange mansion. A missing treasure. Three suspects.")
st.write("Can you solve the mystery?")

# Starting the game
if "started" not in st.session_state:
    st.session_state.started = False

if "clues" not in st.session_state:
    st.session_state.clues = []

if "rooms" not in st.session_state:
    st.session_state.rooms = []

if not st.session_state.started:

    st.subheader("Welcome, Detective")

    name = st.text_input("Enter your detective name:")

    if st.button("Enter Mansion"):
        if name:
            st.session_state.started = True
            st.session_state.name = name
            st.rerun()
        else:
            st.warning("Please enter your name.")

else:

    st.success("Detective " + st.session_state.name + ", the investigation begins.")

    st.sidebar.header("Investigation")

    st.sidebar.write("Rooms searched:")
    st.sidebar.write(len(st.session_state.rooms))

    st.sidebar.write("Clues found:")
    st.sidebar.write(len(st.session_state.clues))

    room = st.selectbox(
        "Which room do you want to investigate?",
        [
            "Library",
            "Kitchen",
            "Study",
            "Bedroom"
        ]
    )

    if st.button("Search Room"):

        if room not in st.session_state.rooms:

            st.session_state.rooms.append(room)

            if room == "Library":
                clue = "You found a torn piece of a black glove."

            elif room == "Kitchen":
                clue = "You discovered muddy footprints near the back door."

            elif room == "Study":
                clue = "You found a note saying: 'Meet me at midnight.'"

            else:
                clue = "You found a silver key hidden under the pillow."

            st.session_state.clues.append(clue)

            st.success("You searched the " + room + ".")
            st.info("CLUE: " + clue)

        else:
            st.warning("You already searched this room.")

    st.divider()

    st.subheader("Your Clues")

    if st.session_state.clues:
        for number, clue in enumerate(
            st.session_state.clues, 1
        ):
            st.write(str(number) + ". " + clue)

    else:
        st.write("You haven't found any clues yet.")

    st.divider()

    st.subheader("Who stole the treasure?")

    suspect = st.radio(
        "Choose a suspect:",
        [
            "The Butler",
            "The Gardener",
            "The Owner"
        ]
    )

    if st.button("Make Accusation"):

        if len(st.session_state.clues) < 3:
            st.warning(
                "You need at least 3 clues before making an accusation!"
            )

        elif suspect == "The Gardener":
            st.success(
                "CASE SOLVED! The Gardener was the thief!"
            )
            st.balloons()

        else:
            st.error(
                "Wrong suspect! The mystery continues..."
            )

    if st.button("Restart Game"):
        st.session_state.clear()
        st.rerun()