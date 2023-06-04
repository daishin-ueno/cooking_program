import streamlit as st
import pandas as pd
import numpy as np
import random
import datetime
import os

def main ():
    #DATE_COLUMN = 'date/time'
    st.title('お疲れ様です！！！')
    dt = datetime.datetime.today()  # ローカルな現在の日付と時刻を取得
    st.title(f"今日は {dt.year}年 {dt.month}月 {dt.day}日です!!!")
    #path = r'C:\Users\PC_User\da-ueno\streamlit\Menu\menu.xlsx'
    #path = os.path('./data/menu.xlsx')
    #print(path)
    #path = 'menu.xlsx'
    #df = pd.read_excel(path,sheet_name='Menu',index_col=0)

    path = r'menu.csv'
    df = pd.read_csv(path,sep=',',header=0,index_col=0,encoding="shift_jis")

    df = df.dropna(axis = 1)
    #print(df)
    #st.table(df)

    col_len = len(df.columns)
    randnum = str(random.randint(1,col_len))
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
        st.write("今日のメニューは **" + menu+ "** です！！！")
        st.markdown("**材料**は \n" + material+ "です！！！")
        st.markdown("**調理方法**は \n" + method+ "")

if __name__ == "__main__":
    main()








