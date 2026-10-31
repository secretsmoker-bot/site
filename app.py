import streamlit as st

st.set_page_config(page_title="Веб-приложение", layout="wide")

st.title("Веб-приложение")

tab1, tab2, tab3 = st.tabs(["Главная", "Тест", "🔗 Полезные ссылки"])

with tab1:
    st.header("О проекте")
    st.write("Учебное приложение на базе фреймворка Streamlit.")

with tab2:
    st.header("Вопрос")
    answer = st.radio(
        "Какой язык используется для Streamlit?",
        ["C++", "Python", "JavaScript"]
    )
    if st.button("Проверить"):
        if answer == "Python":
            st.success("Верно!")
        else:
            st.error("Неверно, попробуйте еще раз.")

with tab3:
    st.header("Полезные ссылки")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Обучение")
        st.markdown("""
- 🐍 [Python Docs](https://docs.python.org/3/) — документация Python
- ⚡ [Streamlit Docs](https://docs.streamlit.io/) — документация фреймворка
        """)
        
    with col2:
        st.subheader("Игры")
        st.markdown("""
- 🎮 [CheckiO](https://checkio.org/) — игра-тренажер для Python
- ⚔️ [CodeCombat](https://codecombat.com/) — обучение через RPG
        """)
