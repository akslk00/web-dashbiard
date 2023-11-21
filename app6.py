import streamlit as st

def main():
    #텍스트를 입력받는 방법
    name = st.text_input('이름을 입력하세요')

    st.subheader('제이름은 '+ name +'입니다.')

    #st.text_input('이름 입력',value='홍길동')

    st.text_input('이름 입력해',value='홍길동', max_chars= 5, placeholder= '홍길동')
    
    text=st.text_area('메세지를 입력하세요')

    st.text(text)

    #숫자 입력 방법
    birth_year=st.number_input('출생년도를 입력하세요', 1900, 2023,)
    st.text('제 출생년도는 '+ str(birth_year) + '입니다')

    st.number_input('실수를 입력하세요',-2.0,100.0,step=0.001)

    #날짜 입력 받는법
    my_date=st.date_input('약속날짜 입력')

    print(my_date)
    st.warning(my_date)

    print(type(my_date))
    st.text(type(my_date))

    #'2023년11월11일 월요일 입니다.'라고 웹화면에 표시
    
    st.text(my_date.strftime('%y년 %m월 %d일 %A 입니다'))

    #식간 입력방법

    my_time=st.time_input('약속시간 선택')

    print(type(my_time))

    st.text(my_time.strftime('%H:%M에 약속시간을 잡앗습니다'))

    #비밀번호 입력방법
    password=st.text_input('비밀번호 입력',type='password')

    print(password)

    #색깔 입력

    color=st.color_picker('색을 선택')
    st.text(color)
if __name__ == '__main__':
    main()