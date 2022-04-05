import streamlit as st
import time

st.write("""
# Speech to text
test program dalam betuk web
""")
st.write("(F:-> New folder (6)-> web-> streamlit-> firstpyw)")

# 3

# 2
hitung = st.button("rekam")

if hitung:
    # st.spinner(text="In progress...")
    # -------------------------------
    import speech_recognition as sr

    engine = sr.Recognizer()
    mic = sr.Microphone()
    hasil = ""
    engine.pause_treshold = 4

    with mic as source:
        st.write("~~ mulai deteksi suara ~~")
        print("~~ mulai deteksi ~~")
        rekaman = engine.listen(source)
        print("~~ deteksi suara ditutup ~~")
        st.write("~~ deteksi suara ditutup ~~")

    try:
        print(".")
        st.warning('Warning message')
        with st.spinner('Wait for it...'):
            hasil = engine.recognize_google(rekaman, language = "id")
        print("..")
        st.success('success')
        print(hasil)
        st.write("rec = ")
        print(". . .")
    # except engine.UnknownValueError:
    #     st.warning('Warning message')
    #     print("google tidak mendeteksi")
    except Exception as e:
        st.exception(e)
        print(e)

    # -------------------------------
    # st.write("luas segitiganya adalah = ", luas)
    st.info(f"... {hasil} ")
    st.balloons()

