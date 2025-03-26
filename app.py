import streamlit as st
from celebi_ui import celebi
from kasumi_ui import kasumi_ui

with st.sidebar:
    selected_tab = st.radio(
        "機能を選択:",
        ["セレビィex", "カスミ"]
    )

if selected_tab == "セレビィex":
    celebi()
elif selected_tab == "カスミ":
    kasumi_ui()
