import math
import streamlit as st
from functions import *

def lcm():
    st.header("ค.ร.น.")
    st.caption("คูณร่วมน้อย")
    with st.form(key="lcm"):
        st.caption("วิธีใช้: ใส่ข้อคณิตศาสตร์ (แยกข้อด้วยเว้นวรรค) เช่น 1,2,3 4,5,6 3,6,7 ถ้าใส่ผิดพลาดอาจเกิดข้อผิดพลาดได้")
        user_lcm = st.text_input("ใส่ข้อคณิตศาสตร์ (แยกข้อด้วยเว้นวรรค): ")
        submit = st.form_submit_button("ยืนยัน")

        if submit:
            if user_lcm != "":  
                parts = user_lcm.split()
                nested_list = [[int(x) for x in part.split(',')] for part in parts]

                for i in nested_list:
                    result = math.lcm(*i)

                    prime_factors = get_prime_factors(result)
                    formula_display = " x ".join(str(factor) for factor in prime_factors) if result > 1 else str(result)
                    
                    formatted_list = ", ".join(str(num) for num in i)
                    
                    st.success(f"ค.ร.น. ของ {formatted_list} คือ {formula_display} = **{result:,}**")
                    
                    # --- Display "วิธีทำ" ---
                    st.subheader(f"วิธีทำ: ค.ร.น. ของ {formatted_list}")
                    st.markdown(generate_lcm_steps(i))
                    st.markdown("---")
            else:
                st.warning("โปรดใส่โจทย์คณิตศาสตร์")
        elif user_lcm == "": # This ensures the warning shows initially or after clearing
            st.warning("โปรดใส่โจทย์คณิตศาสตร์")

def gcd():
    st.header("ห.ร.ม.")
    st.caption("หารร่วมมาก")
    with st.form(key="gcd"):
            st.caption("วิธีใช้: ใส่ข้อคณิตศาสตร์ (แยกข้อด้วยเว้นวรรค) เช่น 1,2,3 4,5,6 3,6,7 ถ้าใส่ผิดพลาดอาจเกิดข้อผิดพลาดได้")
            user_gcd = st.text_input("ใส่ข้อคณิตศาสตร์ (แยกข้อด้วยเว้นวรรค): ")
            submit = st.form_submit_button("ยืนยัน")
            if submit:
                if user_gcd != "":  
                    parts = user_gcd.split()
                    nested_list = [[int(x) for x in part.split(',')] for part in parts]

                    for i in nested_list:
                        result = math.gcd(*i)

                        if result > 1:
                            prime_factors = get_prime_factors(result)
                            formula_display = " x ".join(str(factor) for factor in prime_factors)
                        else:
                            formula_display = str(result)

                        formatted_list = ", ".join(str(num) for num in i)
                        if is_prime(result) or result == 1:
                            st.success(f"ห.ร.ม. ของ {formatted_list} คือ {result:,}")
                        else:
                            st.success(f"ห.ร.ม. ของ {formatted_list} คือ {formula_display} = {result:,}")
            if user_gcd == "":
                    st.warning("โปรดใส่โจทย์คณิตศาสตร์")
