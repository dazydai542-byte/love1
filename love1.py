import streamlit as st
import random

st.set_page_config(page_title="宝宝温馨提示💖", page_icon="💌", layout="centered")

tips = [
    '我想你了','今天过得开心嘛','期待和你见面','顺顺利利','平平安安','早点休息',
    '天冷了，多穿衣服','今天有想我嘛','我喜欢你','要想我哦','今天也辛苦啦',
    '吃饭了嘛','每天都要喜欢我哦', '想你想你想你','开心每一天', '宝贝','想和你在一起','想抱抱你','想亲亲你',
    '你是我的小苹果','遇见你真好','你是最棒的','爱你哟','想你了，快回来','想听你的声音','想见你',
    '想念你的笑容','你是我的唯一','每天都在想你','我们去河边散步好不好','你是我的全世界','想和你手牵手',
    '你世界第一好','想和你一起看星星','你好可爱','想和你一起旅行','好幸运遇见你','想和你一起吃饭','想和你一起看电影',
    '想和你一起做饭','想和你一起睡觉','想和你一起逛街','想和你一起运动','想和你一起学习','想和你一起打游戏',
    '想和你一起听音乐','想和你一起看书','想和你一起做手工','想和你一起养一只小狗','I love you', 'I miss you'
]

bg_colors = ['pink','skyblue','lightgreen','lavender','lightyellow','plum','coral','bisque']

st.markdown(
    f"""
    <div style='background-color:{random.choice(bg_colors)};padding:30px;border-radius:15px;text-align:center;'>
        <h2 style='color:#333;font-family:Microsoft YaHei;'>{random.choice(tips)}</h2>
    </div>
    """,
    unsafe_allow_html=True
)

if st.button("再来一句 💬"):
    st.experimental_rerun()
