import streamlit as st

st.title("🎓 학생 점수 분석기")

if "names" not in st.session_state:
    st.session_state.names=[]
    st.session_state.scores=[]

name=st.text_input("이름입력")
