import streamlit as st
import random

st.set_page_config(page_title="🎮 Game Hub", layout="centered")

st.title("🎮 Play Store Game Hub")

# Score system
if "score" not in st.session_state:
    st.session_state.score = 0

tab1, tab2, tab3, tab4 = st.tabs(["🎯 Guess", "✊ RPS", "🔤 Word", "🤖 AI TicTacToe"])

# ------------------ GUESS GAME ------------------
with tab1:
    st.subheader("🎯 Guess the Number")

    if "number" not in st.session_state:
        st.session_state.number = random.randint(1, 10)

    guess = st.number_input("Enter number", 1, 10)

    if st.button("Check Guess"):
        if guess == st.session_state.number:
            st.success("Correct 🎉")
            st.session_state.score += 1
        else:
            st.error("Wrong ❌")

# ------------------ RPS ------------------
with tab2:
    st.subheader("✊ Rock Paper Scissors")

    choices = ["Rock", "Paper", "Scissors"]
    user = st.selectbox("Choose", choices)

    if st.button("Play RPS"):
        comp = random.choice(choices)
        st.write("Computer:", comp)

        if user == comp:
            st.info("Draw 😐")
        elif (user=="Rock" and comp=="Scissors") or \
             (user=="Paper" and comp=="Rock") or \
             (user=="Scissors" and comp=="Paper"):
            st.success("You Win 🎉")
            st.session_state.score += 1
        else:
            st.error("You Lose 😢")

# ------------------ WORD GAME ------------------
with tab3:
    st.subheader("🔤 Word Scramble")

    words = ["python", "streamlit", "hackathon"]
    
    if "word" not in st.session_state:
        st.session_state.word = random.choice(words)

    scrambled = ''.join(random.sample(st.session_state.word, len(st.session_state.word)))
    st.write("Scrambled:", scrambled)

    guess_word = st.text_input("Your guess")

    if st.button("Check Word"):
        if guess_word == st.session_state.word:
            st.success("Correct 🎉")
            st.session_state.score += 1
        else:
            st.error("Wrong ❌")

# ------------------ AI TIC TAC TOE ------------------
with tab4:
    st.subheader("🤖 AI Tic Tac Toe")

    if "board" not in st.session_state:
        st.session_state.board = [""] * 9

    def ai_move():
        empty = [i for i,v in enumerate(st.session_state.board) if v==""]
        if empty:
            move = random.choice(empty)
            st.session_state.board[move] = "O"

    cols = st.columns(3)

    for i in range(9):
        if cols[i%3].button(st.session_state.board[i] or " ", key=i):
            if st.session_state.board[i] == "":
                st.session_state.board[i] = "X"
                ai_move()

    if st.button("Reset Board"):
        st.session_state.board = [""] * 9

# ------------------ SCORE ------------------
st.markdown("---")
st.subheader(f"🏆 Total Score: {st.session_state.score}")
