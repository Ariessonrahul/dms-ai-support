import streamlit as st
import json
from PIL import Image
 
st.set_page_config(
    page_title="RSPL DMS AI Assistant",
    page_icon="🤖",
    layout="wide"
)
 
# ---------------- CSS ----------------
 
st.markdown("""
<style>
 
.main-title{
text-align:center;
font-size:42px;
font-weight:bold;
color:#6A1B9A;
}
 
.sub-title{
text-align:center;
font-size:22px;
color:gray;
margin-bottom:20px;
}
 
.card{
background:#F8F9FA;
padding:15px;
border-radius:12px;
border:1px solid #E5E5E5;
}
 
</style>
""", unsafe_allow_html=True)
 
# ---------------- LOAD JSON ----------------
 
@st.cache_data
def load_data():
    try:
        with open("issues.json","r",encoding="utf-8") as f:
            return json.load(f)
    except:
        return []
 
issues = load_data()
 
# ---------------- HEADER ----------------
 
st.markdown(
'<div class="main-title">🤖 RSPL DMS AI Assistant</div>',
unsafe_allow_html=True
)
 
st.markdown(
'<div class="sub-title">Upload Screenshot → Get Instant Solution</div>',
unsafe_allow_html=True
)
 
st.divider()
 
# ---------------- SIDEBAR ----------------
 
page = st.sidebar.radio(
"📌 Menu",
[
"🏠 Home",
"🔍 Search Issue",
"📷 Upload Screenshot",
"📚 All Issues",
"ℹ About"
]
)
 
# ---------------- HOME ----------------
 
if page=="🏠 Home":
 
    st.success("Welcome to RSPL DMS AI Assistant")
 
    c1,c2,c3=st.columns(3)
 
    c1.metric("Supported Issues",len(issues))
    c2.metric("Version","2.0")
    c3.metric("Status","🟢 Online")
 
    st.divider()
 
    st.subheader("Supported Error Types")
 
    for item in issues:
        st.write("✅", item.get("error","Unknown Error"))
