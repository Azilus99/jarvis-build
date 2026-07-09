import streamlit as st
from streamlit_mic_recorder import mic_recorder
import os
import time

st.set_page_config(page_title="JARVIS OS - Android Game Dev", layout="wide", initial_sidebar_state="expanded")

# --- СТИЛИЗАЦИЯ ИНТЕРФЕЙСА ПОД CHATGPT ---
st.markdown("""
<style>
    .stApp { background-color: #212121; color: #ececec; font-family: 'Inter', sans-serif; }
    [data-testid="stSidebar"] { background-color: #171717 !important; border-right: 1px solid #2f2f2f; }
    .studio-card { background-color: #171717; border: 1px solid #2f2f2f; border-radius: 12px; padding: 20px; margin-bottom: 15px; }
    div[data-testid="stChatInput"] { background-color: #2f2f2f !important; border: 1px solid #424242 !important; border-radius: 16px !important; }
</style>
""", unsafe_allow_html=True)

# Инициализация статуса серверов в ОЗУ
if "active_server" not in st.session_state:
    st.session_state.active_server = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Функция умного поочередного переключения мобильных серверов
def switch_android_server(target_server):
    if st.session_state.active_server != target_server:
        if st.session_state.active_server:
            with st.spinner(f"🔋 Выгрузка сервера [{st.session_state.active_server}] для экономии батареи..."):
                time.sleep(0.5)
        if target_server:
            with st.spinner(f"🚀 Запуск ИИ-модуля [{target_server}] внутри памяти..."):
                time.sleep(0.8)
        st.session_state.active_server = target_server

# ================= 🧭 ВЫДВИЖНАЯ ЛЕВАЯ ШТОРКА (36 ИИ-ЦЕХОВ) =================
with st.sidebar:
    st.markdown("<h2 style='color: #00c853; font-weight: 700;'>🤖 JARVIS OS v2026</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #8e8e93; font-size: 12px;'>ЭКОСИСТЕМА АВТОНОМНЫХ ИИ-АГЕНТОВ:</p>", unsafe_allow_html=True)
    
    current_studio = st.radio(
        "Выберите ИИ-цех разработки:",
        [
            "💬 Главный Чат Оркестратор", 
            "🧠 Память Мира & Живые NPC",
            "🏠 Архитектор Локаций & Дизайн",
            "🖼️ Мобильная Графика (Midjourney)", 
            "📦 3D-Скульптор & Авто-Риггинг", 
            "🎭 Мастер Эмоций & Липсинк",
            "💻 Написание и Оптимизация Кода", 
            "🎵 Сжатые Звуки и Музыка (Suno)",
            "🧪 Тестировщик & Балансировщик",
            "📦 Сборщик APK & Защита Ключей"
        ],
        label_visibility="collapsed"
    )
    st.write("---")
    st.markdown(f"📱 **Активен процесс в ОЗУ:**\n`{st.session_state.active_server if st.session_state.active_server else 'Все спят'}`")

# ================= 📜 ВЫВОД СОДЕРЖИМОГО КАТЕГОРИЙ =================

# 1. ГЛАВНЫЙ ЧАТ
if current_studio == "💬 Главный Чат Оркестратор":
    switch_android_server("Текст и Логика (Mobile Llama)")
    st.write("<h3 style='text-align: center;'>Центральный Контроллер Джарвиса</h3>", unsafe_allow_html=True)
    
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Панель инструментов внизу экрана
    st.write("---")
    col_file, col_text, col_mic = st.columns([1, 4, 0.5])
    with col_file:
        uploaded_file = st.file_uploader("📎", type=["py", "cs", "mp3", "wav", "mp4", "png", "jpg", "txt"], label_visibility="collapsed")
    with col_text:
        user_input = st.chat_input("Прикажите Джарвису продумать хоррор-механики или собрать APK...")
    with col_mic:
        mic_recorder(start_prompt="🎤", stop_prompt="🛑", key='main_mic', just_once=True)

    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        st.session_state.chat_history.append({"role": "assistant", "content": f"Джарвис принял задачу: `{user_input}`. Все 36 скрытых серверов подключены. Результаты распределяются по вкладкам в левой шторке."})
        st.rerun()

# 2. ЖИВЫЕ NPC И ПАМЯТЬ
elif current_studio == "🧠 Память Мира & Живые NPC":
    switch_android_server("NLP Диалоги & Векторная Память")
    st.header("🧠 Модуль Живых NPC (Векторная память)")
    st.markdown('<div class="studio-card"><b>Система Radiant AI 2.0</b><br>Здесь настраивается независимая жизнь ботов, их репутация и квесты. Персонажи будут помнить ваши слова неделями.</div>', unsafe_allow_html=True)

# 3. АРХИТЕКТОР ЛОКАЦИЙ И ФИЗИКА FALLOUT
elif current_studio == "🏠 Архитектор Локаций & Дизайн":
    switch_android_server("Genesis Physics & Spatial AI")
    st.header("🏠 Архитектор особняка (Стиль Promethean AI)")
    st.markdown('<div class="studio-card"><b>Авто-дизайн комнат и падение предметов Fallout-style</b><br>ИИ процедурно строит дома, расставляет мебель, книги и утварь по полкам, просчитывая физику столкновений.</div>', unsafe_allow_html=True)

# 4. МОБИЛЬНАЯ ГРАФИКА
elif current_studio == "🖼️ Мобильная Графика (Midjourney)":
    switch_android_server("Генератор Интерфейсов & Текстур")
    st.header("🖼️ Цех мобильной графики (Сетка Midjourney)")
    st.markdown('<div class="studio-card">Генерация бесшовных текстур стен, паков кнопок интерфейса и иконок способностей под экраны смартфонов.</div>', unsafe_allow_html=True)

# 5. 3D И АВТО-СКЕЛЕТЫ
elif current_studio == "📦 3D-Скульптор & Авто-Риггинг":
    switch_android_server("Мобильный 3D Просчет & Риггинг")
    st.header("📦 Low-Poly 3D и Скелеты")
    st.markdown('<div class="studio-card"><b>Tripo3D & Mixamo Коннектор</b><br>ИИ создает 3D-модель из текста и автоматически зашивает внутрь нее костный каркас (скелет) для анимаций.</div>', unsafe_allow_html=True)

# 6. ЭМОЦИИ И ЛИПСИНК
elif current_studio == "🎭 Мастер Эмоций & Липсинк":
    switch_android_server("Face AudioSync Engine")
    st.header("🎭 Мимика и Озвучка NPC")
    st.markdown('<div class="studio-card">Синхронизация мимики лица 3D-персонажа с речью из микрофона. Лицо монстра или продавца будет реалистично искажаться от эмоций.</div>', unsafe_allow_html=True)

# 7. АНДРОИД КОДЕР
elif current_studio == "💻 Написание и Оптимизация Кода":
    switch_android_server("Компилятор C# / Touch Input")
    st.header("💻 Оптимизатор Скриптов (Стиль Claude Artifacts)")
    st.markdown('<div class="studio-card">Написание кода под Unity/Unreal с автоматической оптимизацией RAM и поддержкой мобильных нажатий (Input.GetTouch).</div>', unsafe_allow_html=True)

# 8. СТУДИЯ ЗВУКА
elif current_studio == "🎵 Сжатые Звуки и Музыка (Suno)":
    switch_android_server("Синтезатор Волн AudioCraft")
    st.header("🎵 Аудио-студия (Интерфейс Suno)")
    st.markdown('<div class="studio-card">Создание легких фоновых музыкальных лупов и SFX звуков (клики кнопок, скрипы дверей), сжатых под формат мобильной игры.</div>', unsafe_allow_html=True)

# 9. ТЕСТЕР И БАЛАНСИРОВЩИК
elif current_studio == "🧪 Тестировщик & Балансировщик":
    switch_android_server("Авто-тесты QA & Бюджет Сложности")
    st.header("🧪 Автоматический поиск багов и Адаптивная сложность")
    st.markdown('<div class="studio-card">ИИ-агент сам запускает игру и ищет застревания в текстурах. Модуль сложности подстраивает силу монстров под навыки игрока.</div>', unsafe_allow_html=True)

# 10. СБОРКА И ЗАЩИТА КЛЮЧЕЙ
elif current_studio == "📦 Сборщик APK & Защита Ключей":
    switch_android_server("Build Master & DRM Security")
    st.header("📦 Финальная сборка APK и Защита")
    st.markdown('<div class="studio-card">Компиляция всего проекта в один установочный файл .apk с вшитым античитом и уникальной системой ключей активации.</div>', unsafe_allow_html=True)

