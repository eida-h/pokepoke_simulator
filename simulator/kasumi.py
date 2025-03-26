
import numpy as np
import streamlit as st

class Kasumi_sim:
    def __init__(self):
        if "ksm_history" not in st.session_state:
            st.session_state.ksm_history = []
        self.history = st.session_state.ksm_history

    def use_card(self):
        is_omote = True
        num_energy = 0
        while is_omote:
            if np.random.rand() < 0.5:
                is_omote = False
            else:
                num_energy += 1
        st.session_state.ksm_history.append(num_energy)
        self.history = st.session_state.ksm_history
        return num_energy



