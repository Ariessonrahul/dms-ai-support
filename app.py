
import streamlit as st
import json
from PIL import Image

st.set_page_config(page_title="RSPL DMS AI Assistant", page_icon="🤖", layout="wide")

@st.cache_data
def load_data():
    try:
        with open("issues.json","r",encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []

issues=load_data()

st.markdown("<h1 style='text-align:center;color:#6A1B9A'>🤖 RSPL DMS AI Assistant</h1>",unsafe_allow_html=True)
st.caption("Upload Screenshot → Get Instant Solution")

page=st.sidebar.radio("Menu",["🏠 Home","🔍 Search Issue","📷 Upload Screenshot","📚 All Issues","ℹ About"])

if page=="🏠 Home":
    c1,c2,c3=st.columns(3)
    c1.metric("Supported Issues",len(issues))
    c2.metric("Version","2.0")
    c3.metric("Status","Online")
    st.subheader("Supported Error Types")
    for item in issues:
        st.write("✅",item.get("error","Unknown Error"))
elif page=="🔍 Search Issue":
    q=st.text_input("Search")
    if q:
        ok=False
        for item in issues:
            if q.lower() in item.get("error","").lower() or q.lower() in " ".join(item.get("keywords",[])).lower():
                ok=True
                st.success(item.get("error","Unknown Error"))
                for s in item.get("solution",[]):
                    st.write("✔",s)
        if not ok:
            st.error("No matching issue found.")
elif page=="📷 Upload Screenshot":
    f=st.file_uploader("Upload Screenshot",type=["png","jpg","jpeg"])
    if f:
        st.image(Image.open(f),use_container_width=True)
        st.info("OCR feature coming soon.")
elif page=="📚 All Issues":
    for item in issues:
        with st.expander(item.get("error","Unknown Error")):
            for s in item.get("solution",[]):
                st.write("✔",s)
else:
    st.write("RSPL DMS AI Assistant v2.0")

