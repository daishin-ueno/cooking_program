import streamlit as st
import pandas as pd
import numpy as np
import random
import datetime



HEADER_COLOR_CYCLE = itertools.cycle(
    [
        "#00c0f2",  # light-blue-70",
        "#ffbd45",  # "orange-70",
        "#00d4b1",  # "blue-green-70",
        "#1c83e1",  # "blue-70",
        "#803df5",  # "violet-70",
        "#ff4b4b",  # "red-70",
        "#21c354",  # "green-70",
        "#faca2b",  # "yellow-80",
    ]
)
    
def colored_header(label, description=None, color=None):
    """Shows a header with a colored underline and an optional description."""
    st.write("")
    if color is None:
        color = next(HEADER_COLOR_CYCLE)
    st.subheader(label)
    st.write(
        f'<hr style="background-color: {color}; margin-top: 0; margin-bottom: 0; height: 3px; border: none; border-radius: 3px;">',
        unsafe_allow_html=True,
    )
    if description:
        st.caption(description)



def main ():
    #DATE_COLUMN = 'date/time'
    st.title('お疲れ様です！！！')
    dt = datetime.datetime.today()  # ローカルな現在の日付と時刻を取得
    st.title(f"今日は {dt.year}年 {dt.month}月 {dt.day}日です!!!")
    path = r'C:\Users\PC_User\da-ueno\streamlit\Menu\menu.xlsx'
    df = pd.read_excel(path,sheet_name='Menu',index_col=0)

    #path = r'menu.csv'
    #df = pd.read_csv(path)

    df = df.dropna(axis = 1)

    #st.table(df)
    col_len = len(df.columns)
    randnum = random.randint(1,col_len)
    menu = df.loc["Name",randnum]
    material = df.loc["Material",randnum]
    method = df.loc["Method",randnum]
    

    #print(selected)
    #st.write("今日のメニューは" + menu+ "です！！！")
    #st.markdown("材料は \n" + material+ "です！！！")
    #st.markdown("調理方法は \n" + method+ "")
    #st.write("材料は" + list(selected)[1] + "です！！！")
    #st.write("方法は" + list(selected)[2] + "です！！！")



    btn = st.button("ボタン")
    if btn:
        st.write("今日のメニューは" + menu+ "です！！！")
        st.markdown("材料は \n" + material+ "です！！！")
        st.markdown("調理方法は \n" + method+ "")

if __name__ == "__main__":
    main()








