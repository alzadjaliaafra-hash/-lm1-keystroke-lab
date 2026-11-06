from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="LM1 Keystroke Lab", page_icon="🧮", layout="wide")
st.markdown(
    "<style>.block-container{padding-top:0.5rem;padding-bottom:0;max-width:1180px}"
    "header[data-testid='stHeader']{display:none}</style>",
    unsafe_allow_html=True,
)

html = (Path(__file__).parent / "lm1_keystroke_lab.html").read_text(encoding="utf-8")
height = st.sidebar.slider("Page height (px)", 1200, 3200, 1900, 100,
                           help="Raise this on a phone, where the page stacks into one column.")
components.html(html, height=height, scrolling=True)
