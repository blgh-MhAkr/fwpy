import streamlit as st
import time
# import speech_recognition as sr

st.write("""
# Speech to text
test program dalam betuk web
""")
st.write("(F:-> New folder (6)-> web-> streamlit-> firstpyw)")
st.write("tes apk")

# 3
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events

stt_button = Button(label="Speak", width=100)

stt_button.js_on_event("button_click", CustomJS(code="""
    var recognition = new webkitSpeechRecognition();
    recognition.continuous = true;
    recognition.interimResults = true;
 
    recognition.onresult = function (e) {
        var value = "";
        for (var i = e.resultIndex; i < e.results.length; ++i) {
            if (e.results[i].isFinal) {
                value += e.results[i][0].transcript;
            }
        }
        if ( value != "") {
            document.dispatchEvent(new CustomEvent("GET_TEXT", {detail: value}));
        }
    }
    recognition.start();
    """))

result = streamlit_bokeh_events(
    stt_button,
    events="GET_TEXT",
    key="listen",
    refresh_on_update=False,
    override_height=75,
    debounce_time=0)

if result:
    if "GET_TEXT" in result:
        st.write(result.get("GET_TEXT"))


# --------------------------------------------#
# # 2
# hitung = st.button("rekam")

# if hitung:
#     # st.spinner(text="In progress...")
#     # -------------------------------
#     # import speech_recognition as sr

#     engine = sr.Recognizer()
#     mic = sr.Microphone()
#     hasil = ""
#     engine.pause_treshold = 4

#     with mic as source:
#         st.write("~~ mulai deteksi suara ~~")
#         print("~~ mulai deteksi ~~")
#         rekaman = engine.listen(source)
#         print("~~ deteksi suara ditutup ~~")
#         st.write("~~ deteksi suara ditutup ~~")

#     try:
#         print(".")
#         st.warning('Warning message')
#         with st.spinner('Wait for it...'):
#             hasil = engine.recognize_google(rekaman, language = "id")
#         print("..")
#         st.success('success')
#         print(hasil)
#         st.write("rec = ")
#         print(". . .")
#     # except engine.UnknownValueError:
#     #     st.warning('Warning message')
#     #     print("google tidak mendeteksi")
#     except Exception as e:
#         st.exception(e)
#         print(e)

#     # -------------------------------
#     # st.write("luas segitiganya adalah = ", luas)
#     st.info(f"... {hasil} ")
#     st.balloons()

