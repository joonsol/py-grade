import streamlit as st

st.title("🎓 학생 점수 분석기")

if "names" not in st.session_state:
    st.session_state.names=[]
    st.session_state.scores=[]

name=st.text_input("이름입력")

score=st.number_input("점수 입력",min_value=0,max_value=100)
# push

if st.button("입력"):
    if name:
        st.session_state.names.append(name)
        st.session_state.scores.append(score)
        st.success(f"{name}학생 -{score}점 등록 완료")

    else:
        st.warning("이름을 입력하세요")

if st.session_state.names:
    avg= sum(st.session_state.scores)/len(st.session_state.scores)
    max_score = max(st.session_state.scores)
    min_score = min(st.session_state.scores)


    max_name =st.session_state.names[st.session_state.scores.index(max_score)]
    min_name =st.session_state.names[st.session_state.scores.index(min_score)]

    st.subheader("결과")
    st.write(f"학생수 :{len(st.session_state.names)}명")
    st.write(f"평균 점수 :{avg:.2f}점")
    st.write(f"최고 점수 :{max_name} ({max_score}점)")
    st.write(f"최저 점수 :{min_name} ({min_score}점)")
