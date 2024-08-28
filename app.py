import streamlit as st
import pandas as pd

# 기본 설정
st.set_page_config(page_title="Schedule Tracker", layout="centered")

# 일정 데이터를 저장할 딕셔너리 초기화
if 'schedule_data' not in st.session_state:
    st.session_state.schedule_data = {}

# 날짜 선택
selected_date = st.date_input("날짜를 선택하세요")

# 일정 입력
st.write("## 일정 추가하기")
event_name = st.text_input("일정 이름", "")
event_time = st.time_input("시간", value=None)

if st.button("일정 추가"):
    if selected_date and event_name and event_time:
        # 선택한 날짜의 일정 리스트 가져오기
        schedule_list = st.session_state.schedule_data.get(selected_date, [])
        
        # 새로운 일정 추가
        schedule_list.append({
            "event_name": event_name,
            "event_time": event_time.strftime("%H:%M")
        })
        
        # 세션 상태에 저장
        st.session_state.schedule_data[selected_date] = schedule_list
        st.success(f"{event_name} 일정이 추가되었습니다!")
    else:
        st.error("모든 필드를 입력해 주세요.")

# 선택한 날짜의 일정 보기
st.write("## 선택한 날짜의 일정 보기")
if selected_date in st.session_state.schedule_data:
    schedule_list = st.session_state.schedule_data[selected_date]
    if schedule_list:
        df = pd.DataFrame(schedule_list)
        st.table(df)
    else:
        st.write("일정이 없습니다.")
else:
    st.write("일정이 없습니다.")

# 전체 일정 보기
st.write("## 전체 일정 보기")
if st.session_state.schedule_data:
    all_schedules = []
    for date, events in st.session_state.schedule_data.items():
        for event in events:
            all_schedules.append({
                "날짜": date,
                "일정 이름": event["event_name"],
                "시간": event["event_time"]
            })
    df_all = pd.DataFrame(all_schedules)
    st.table(df_all)
else:
    st.write("등록된 일정이 없습니다.")
