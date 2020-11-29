import streamlit as st
import pandas as pd
import numpy as np

st.title("API アプリ")

st.write(
    pd.DataFrame([[1,2,3],[4,5,6]], columns=["a","b","c"])
)

"""
# データ



"""

if st.checkbox("Show DataFrame"):
    chart_df = pd.DataFrame(
        np.random.randn(14, 3),
        columns=["M", "S", "T"]
    )
    st.line_chart(chart_df)

"""

# AI予測
### おすすめ

"""