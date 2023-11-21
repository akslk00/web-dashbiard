import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb



def main():
    st.title('차트 그리기 1')
    df=pd.read_csv('./data/iris.csv')
    st.dataframe(df)

    #petal_length와 petal_width의 관게를 차트로 그리시오
    #matplotalib이나 seaborn인 경우
    
    fig1=plt.figure()
    plt.scatter(data= df, x='petal_length',y='petal_width')
    plt.title('Petal length VS width')
    plt.xlabel('petal length')
    plt.ylabel('petal width')
    st.pyplot(fig1)

    fig2=plt.figure()
    sb.regplot(data= df, x='petal_length',y='petal_width')
    st.pyplot(fig2)


    #petal_length로 히스토그램그리기

    fig3=plt.figure()
    plt.hist(data=df, x='petal_length',rwidth=0.8,bins=20)
    st.pyplot(fig3)

    #하나의 영역에 2개의 차트를 그려라
    fig4=plt.figure()
    plt.subplot(1,2,1)
    plt.hist(data=df, x='petal_length',rwidth=0.8,bins=10)

    plt.subplot(1,2,2)
    plt.hist(data=df, x='petal_length',rwidth=0.8,bins=20)

    st.pyplot(fig4)

    #판다스의 차트를 이용하는 방법
    fig5=plt.figure()
    df['petal_length'].hist()
    st.pyplot(fig5)

    
    fig6=plt.figure()
    df['species'].value_counts().plot(kind='barh')
    st.pyplot(fig6)

    fig7=plt.figure()
    sb.countplot(data=df, x= 'species')
    st.pyplot(fig7)

    #plt,seaborn, 판다스의 차트는
    #차트영역을 plt.figure를 이용하여 변수저장하고
    #st.pyplot을 이욜해서 차트를 그리면 된다

if __name__ == '__main__':
    main()