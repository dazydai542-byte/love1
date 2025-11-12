import streamlit as st
import random

st.set_page_config(page_title="宝宝温馨提示💖", page_icon="💌", layout="centered")

tips = [
    '今天天气怎么样','今天过得开心嘛','最近幸福吗','顺顺利利','平平安安','早点休息',
    '天冷了，多穿衣服','我不想看你伤心','我喜欢你','你真的很勇敢','今天也辛苦啦',
    '吃饭了嘛','每天都要加油哦','心情好吗','有好好休息吗','平淡就好了，不要再受伤','去健身了吗'
    '健康好不好', '往前看','昨晚有做噩梦吗，抱抱', '到这就可以了，你很棒，剩下的交给我', '我不想看到你的眼泪，我会心痛'
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
    st.rerun()
