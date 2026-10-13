import streamlit as st
import plotly.express as px
from src.data import generate_dei_data
from src.representation import representation, by_level, leadership_representation
from src.equity import median_by_group, pay_gap
from src.inclusion import inclusion_index, inclusion_by_group, flag_low_inclusion

st.title("🌈 DEI Analytics")

@st.cache_data
def load():
    return generate_dei_data()

df = load()

st.subheader("Representation — Gender")
st.plotly_chart(px.pie(values=list(representation(df, "gender").values()),
                        names=list(representation(df, "gender").keys())),
                use_container_width=True)

st.subheader("Leadership Representation")
st.json(leadership_representation(df, "gender"))

st.subheader("Representation по уровням")
st.dataframe(by_level(df, "gender"))

c1, c2 = st.columns(2)
with c1:
    st.metric("Inclusion Index", inclusion_index(df))
with c2:
    st.metric("Pay Gap M vs F", f"{pay_gap(df, 'gender', 'M', 'F')}%")

st.subheader("Inclusion по группам")
st.bar_chart(inclusion_by_group(df, "department"))

st.subheader("⚠️ Low Inclusion Flags")
st.json(flag_low_inclusion(df, "department"))

st.subheader("Median Salary по уровню и полу")
st.dataframe(df.pivot_table(index="level", columns="gender", values="salary", aggfunc="median").round(0))
