import streamlit as st
import plotly.express as px
from roadmap import load, to_gantt

st.title("🗺️ Product Roadmap Planner")
data = load()
gantt = to_gantt(data)
fig = px.timeline(gantt, x_start="Start", x_end="Finish", y="Task", color="Status")
fig.update_yaxes(autorange="reversed")
st.plotly_chart(fig, use_container_width=True)
st.dataframe(gantt)
