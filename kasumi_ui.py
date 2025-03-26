import streamlit as st
from simulator.kasumi import Kasumi_sim


    
def kasumi_ui():
    # アプリのタイトル
    st.title("カスミ")
    ks = Kasumi_sim()

    if st.button("カードを使う"):
        num_energy = ks.use_card()
        st.write(f"エネルギー数: {num_energy}")
        
    st.write("履歴")
    # st.write(ks.history)
    str_hist = ["o" * i + "x" for i in ks.history]
    st.write(str_hist)




    

    