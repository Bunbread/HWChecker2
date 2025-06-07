import streamlit as st
from tabs import *

st.header("MathHWChecker")
st.caption("เฉลยการบ้านคณิต")

tab1, tab2 = st.tabs(["คณิตศาสตร์", "อื่นๆ"])

with tab1:
    user = st.selectbox("เลือกเนื้อหา", ["ค.ร.น.", "ห.ร.ม."])
    st.divider()

    if user == "ค.ร.น.":
        lcm()

    if user == "ห.ร.ม.":
        gcd()

with tab2:
    "ยังไม่เสร็จ"
