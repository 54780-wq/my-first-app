import streamlit as st

st.markdown("# :red[🏋️ คํานวนค่าดัชนีมวลกาย BMI]")
st.write("กรอกข้อมูลนํ้าหนักเเละส่วนวูงของคุณ เพื่อเช็กสุขภาพเบื้องต้น")

weight = st.number_input("กรอกนํ้าหนักงของคุณ (กิโลกรัม):",min value=1.0)
height_cm = st.number_input("กรอกส่วนสูงของคุณ (เซ็นติเมตร):",min value=1.0)

if st.button("คํานวนค่า BMI 🎯"):
  height_m = height_cm / 100
  bmi = weight("---")
  st.header(f"ค่า BMI ของคุณคือ: **{bmi:.2f}**")

if bmi < 18.5:
    st.warning("⚠️ คุณมีน้ำหนักน้อยกว่าเกณฑ์ (ผอม)")
elif 18.5 <= bmi < 23.0:
    st.success("🎉 คุณมีน้ำหนักอยู่ในเกณฑ์ปกติ (สุขภาพดี)")
elif 23.0 <= bmi < 25.0:
    st.info("💡 คุณเริ่มมีน้ำหนักเกินเกณฑ์ (ท้วม)")
else:
    st.error("🚨 คุณอยู่ในเกณฑ์อ้วน ควรระวังเรื่องสุขภาพและออกกำลังกาย")

st.divider()
st.write("ณฐพัฒน์ ไชยพานิชย์ เลขที่ 34 ม.4/3")
