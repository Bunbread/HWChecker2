import streamlit as st
from tabs import *

st.header("MathHWChecker")
st.caption("เฉลยการบ้านคณิต")

user = st.selectbox("เลือกเนื้อหา", ["ค.ร.น.", "ห.ร.ม."])
st.divider()

if user == "ค.ร.น.":
    lcm()

if user == "ห.ร.ม.":
    gcd()
