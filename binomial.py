import streamlit as st
import numpy as np
from scipy.stats import binom
import plotly.graph_objects as go
with st.sidebar:
    st.header("Parameters")
    n = st.number_input("Number of trials (n)", min_value=1, max_value=500, value=20)
    p = st.slider("Probability of success (p)", min_value=0.0, max_value=1.0, value=0.90, step=0.01)
if p == 0.5:
    color = "green"
    dist_type = "Symmetric"
elif p < 0.5:
    color = "blue"
    dist_type = "Positively Skewed"
else:
    color = "red"
    dist_type = "Negatively Skewed"
x = np.arange(0, n + 1)
pmf = binom.pmf(x, n, p)
mean = n * p
variance = n * p * (1 - p)
fig = go.Figure(data=[
    go.Bar(
        x=x, 
        y=pmf, 
        marker_color=color,
        hovertemplate='x: %{x}<br>P(X=x): %{y:.3f}<extra></extra>')])

fig.update_layout(
    title=f"Binomial distribution PMF ({dist_type})",
    xaxis_title="Number of Successes (x)",
    yaxis_title="distribution",
    template="plotly_white",
    bargap=0.1)
st.plotly_chart(fig, use_container_width=True)
col1, col2, col3 = st.columns(3)
col1.metric("Mean (μ)", round(mean, 3))
col2.metric("Variance (σ²)", round(variance, 3))
st.info(f"The distribution is **{dist_type}** because p is {'equal to' if p==0.5 else 'less than' if p<0.5 else 'greater than'} 0.5.")