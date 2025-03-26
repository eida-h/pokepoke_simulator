import streamlit as st
from simulator.kasumi import kasumi

history = []

def kasumi_ui():
    # アプリのタイトル
    st.title("カスミ")

    if st.button("カードを使う"):
        num_energy = kasumi()
        st.write(f"エネルギー数: {num_energy}")
        history.append(num_energy)
    
    st.write("履歴")
    st.write(history)
    return history



    

    