import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา")


if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""

if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""


def reset_game():
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.start = time.time()
    st.session_state.is_ended = False


@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2):
    st.balloons()
    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()

    # ข้อ 1
    if u_ans1 == "banana":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")

    # ข้อ 2
    if u_ans2 == "ruler":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")

    st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")

    if score == 2:
        st.success("🎉 You win!")
    else:
        st.error("💀 You lose!")


# ปุ่มเริ่มเกม
st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)


# แสดงเวลา
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(30 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()


st.divider()


# ข้อ 1
ans1 = st.text_input(
    "ข้อ 1: A `B _ n _ n _` . 🍌 = กล้วย",
    value=st.session_state.ans1_val,
)

# ข้อ 2
ans2 = st.text_input(
    "ข้อ 2: study use `Ru _ _ r`. 📏",
    value=st.session_state.ans2_val,
)


st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2


# ปุ่มส่งคำตอบ
if "start" in st.session_state and not st.session_state.get("is_ended", False):

    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

    time.sleep(1)
    st.rerun()


# แสดงผล
if st.session_state.get("is_ended", False):
    show_result_dialog(ans1, ans2)


st.divider()
st.write("ณฐพัฒน์ ไชยพานิชย์ เลขที่ 34 ม.4/3")
