import streamlit as st
from functions import *
import math
from tabs import *

st.header("HWChecker")
st.caption("ตรวจการบ้าน")

tab1, tab2 = st.tabs(["งานคณิตศาสตร์", "อื่นๆ"])

with tab1:
    user = st.selectbox("เลือกเนื้อหา", ["ค.ร.น.", "ห.ร.ม."])
    st.divider()

    if user == "ค.ร.น.":
        gcd()

    if user == "ห.ร.ม.":
        lcm()

with tab2:
    st.header("อื่นๆ")
    user2 = st.selectbox("เลือกเนื้อหา", ["เครื่องคิดเลข", "เกี่ยวกับ"])
    st.divider()
    
    if user2 == "เครื่องคิดเลข":
        with st.form(key="eval"):
            equation_input = st.text_input("ใส่โจทย์คณิตศาสตร์ (เช่น '2*3 + 4')")
            submit = st.form_submit_button()
            if submit:
                if equation_input:
                        try:
                            allowed_builtins = {
                                '__builtins__': {
                                    'int': int, 'float': float, 'complex': complex,
                                    'round': round, 'abs': abs, 'min': min, 'max': max,
                                    'sum': sum, 'len': len,
                                    'pow': pow
                                }
                            }

                            result = eval(equation_input, {"__builtins__": allowed_builtins}) 

                            st.success(f"ผลลัพธ์ของ {equation_input} = {result}")
                        except SyntaxError:
                            st.error("ข้อผิดพลาดทางไวยากรณ์: โปรดตรวจสอบรูปแบบโจทย์ของคุณ")
                        except NameError as e:
                            st.error(f"ข้อผิดพลาด: ตัวแปรหรือฟังก์ชันที่ไม่รู้จัก. {e}")
                            st.info("โปรดใช้เฉพาะตัวเลขและตัวดำเนินการพื้นฐาน เช่น +, -, *, /, **")
                        except Exception as e:
                            st.error(f"เกิดข้อผิดพลาด: {e}")
    if user2 == "เกี่ยวกับ":
        st.markdown("__เว็บไซต์นี้สร้างขึ้นเพื่อหาคำตอบของการบ้านและไม่ได้เฉลยทั้งหมด 👍__")
        st.caption("สร้างโดย wasin")
