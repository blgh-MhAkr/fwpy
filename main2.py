from unicodedata import name
import streamlit as st
import time

st.write("""
# Speech to text
test program video dalam betuk web
""")
st.write("(F:-> New folder (6)-> web-> streamlit-> firstpyw)")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    


    st.write("hasil : ", uploaded_file)
    print("hasil : ", uploaded_file)
    vide=uploaded_file
    
    st.write(vide)
    
    st.video(vide)
    # is_mp4 = uploaded_file.endswith(".mp4")
    # st.video(is_mp4)

    # ------------------------------
    # import moviepy.editor as mp
    # print('.')

    # def extract_audio(video_path, savename):
    #     clip = mp.VideoFileClip(video_path)
    #     clip.audio.write_audiofile(savename)
    # print('..')
    
    # video_path = vide
    # savename = 'extracted.wav'
    # extract_audio(video_path, savename)
    # print('done')

    # st.write(savename)
    # st.audio(savename)
    # st.video(savename)