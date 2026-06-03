import streamlit as st
from openai import OpenAI

# Sidebar for API Key
api_key = st.sidebar.text_input("OpenAI API Key", type="password")

st.title("模考智能反馈系统")

# 定义模板
TEMPLATES = {
    "雅思": """雅思模考反馈
总分：
听力：
阅读：
写作：
口语：
【写作】
小作文：
任务回应：
连贯与衔接：
词汇多样性：
语法准确性与多样性：
大作文：
任务回应：
连贯与衔接：
词汇多样性：
语法准确性与多样性：
【口语】
流利度与连贯性：
词汇多样性：
语法准确性与多样性：
发音：""",
    "托福": """托福模考反馈
总分：
阅读：
听力：
写作：
口语：
【写作】
Task 1: /10
Task 2: /5
Task 3: /5
Task 2 Email评价：
Task 3 Discussion评价：
【口语】
Part 1评价：
Part 2评价："""
}

exam_type = st.selectbox("选择考试类型", ["雅思", "托福"])
uploaded_file = st.file_uploader("上传文件", type=['jpg', 'png', 'mp3', 'wav'])

if st.button("开始分析") and api_key and uploaded_file:
    client = OpenAI(api_key=api_key)
    with st.spinner("正在批改中..."):
        # 这里是调用模型的逻辑
        # 简单演示：直接将请求发给 GPT-4o
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": f"你是一个考官，请严格按照以下模板输出反馈: {TEMPLATES[exam_type]}"},
                {"role": "user", "content": "请分析这个学生的文件。"}
            ]
        )
        st.markdown(response.choices[0].message.content)
