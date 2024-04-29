from src.password_parser import parse_string
import streamlit as st
import numpy as np
import joblib
from Home import main_web

main_web()
def label_strength(num:int) -> str:
    if num == 0:
        return 'Low strength'
    elif num == 1:
        return 'Medium strength'
    else:
        return 'High strength'
    
model = joblib.load("Jupyter_notebooks\params\password_strength_predictor_rf.pkl")
st.sidebar.subheader("Check here", divider='rainbow')
password = st.sidebar.text_input("Enter your password here: ", type="password")
if len (password) >= 1:
    temp = parse_string(password=password)
    temp_list = list(temp.values())
    temp = np.array(temp_list).reshape((1,-1))
    
    if st.sidebar.expander(label="Prediction"):
        res = model.predict(temp)
        res = label_strength(num=res[0])
        st.sidebar.success(res)
        if res == 'Low strength' or res == 'Medium strength':
            st.sidebar.info("""
                - Length: Make it long, ideally 12+ characters.
                - Complexity: Mix uppercase, lowercase, numbers, symbols.
                - Avoid common words: No "password123" or "qwerty."
                - No personal info: Not your name, birthdate, etc.
                - Passphrase: Use a sentence or sequence of words.
                - Randomness: Generate randomly, no patterns.
                - Variation: Different passwords for each account.
                - No dictionary words: Avoid common words.
                - Update regularly: Change passwords often.
                - Use a manager: Consider a password manager.""")
else:
    if st.sidebar.expander(label="Prediction"):
        st.sidebar.success('Type your password')


