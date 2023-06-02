import streamlit as st
import os
import requests
import json

def max_width():
    max_width_str = f"max-width: 1200px;"
    st.markdown(
        f"""
        <style>
        .reportview-container .main .block-container{{{max_width_str}}}
        </style>
        """,
            unsafe_allow_html=True,
    )

def query(data):
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))

st.set_page_config(
    page_title = "Speech-To-Text By NOOBPOOK",
    page_icon = "🎶",
    layout = "wide"
)

st.image("logo.png", width=200)
max_width()
f = st.file_uploader("", type=[".wav"])
st.info(f"""Upload a .wav file for speech to text work!""")

if f is not None:
    path_in = f.name
    old_file_position = f.tell()
    f.seek(0, os.SEEK_END)
    getsize = f.tell()
    f.seek(old_file_position, os.SEEK_SET)
    getsize = round((getsize/1000000),1)
    st.caption(f"The size of this file is {getsize}")

    headers = {"Authorization": f"Bearer {api_token}"}
    API_URL = "https://api-inference.huggingface.co/models/facebook/wav2vec2-base-960h"
    data = query(f)

    values_view = data.values()
    value_iterator = iter(values_view)
    text_value = next(value_iterator)

    text_value = text_value.lower()

    st.success(text_value)

    st.download_button(
        "Download the transcription",
        text_value,
        file_name= None,
        mime=None,
        key = None,
        help=None,
        on_click=None,
        args=None,
        kwargs=None,
    )

