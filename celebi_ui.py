import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from simulator.power_storm import PowerStorm
import pandas as pd

def celebi():
    # アプリのタイトル
    st.title("セレビィex ダメージ計算")

    # 説明文
    st.markdown("""
    ポケポケのセレビィexの技「パワフルブルーム」のダメージを計算するアプリです。
    ### 使い方:
    1. エネルギー数をスライダーで選択
    2. 標準偏差の倍数を選択し、確率とダメージを確認
    """)

    # 自然数の入力（スライダー）
    n = st.slider("エネルギー数", min_value=1, max_value=30, value=2, step=1)


    # シミュレーションの実行
    ps = PowerStorm(n)

    # 棒グラフの描画
    x_label = ps.x_damage
    x = ps.x_coin
    y = ps.y
    data = pd.DataFrame({"x": x_label, "y": y}).set_index("x")
    num_std = st.slider("標準偏差の倍数", min_value=1, max_value=5, value=1, step=1)

    st.write("**Summary**")
    # 追加の説明
    damages, probability = ps.get_damage_in_std(num_std=num_std)


    dam_eval = int(ps.expected_value*ps.damage_unit)
    # 小数点以下2桁まで表示
    dam_std = ps.std*ps.damage_unit
    dam_std = round(dam_std, 2)
    probability = round(probability*100, 1)

    summary_markdown_table = f"""
    | | |
    |-|-|
    | エネルギー数 | {n} |
    | 期待値 | {dam_eval} |
    | 標準偏差 | {dam_std} |
    | {num_std}標準偏差内の確率 | {probability} % |
    | {num_std}標準偏差内のダメージ | {damages[0]} から {damages[-1]} |
    """
    st.markdown(summary_markdown_table)

    # タイトル
    st.write("**横軸:** ダメージ | **縦軸:** 確率")
    st.bar_chart(data)