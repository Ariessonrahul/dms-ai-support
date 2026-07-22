import streamlit as st
import json
from PIL import Image
 
# ---------------- PAGE ----------------
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
    color:#6A1B9A;
    font-weight:bold;
}
.sub-title{
    text-align:center;
    font-size:20px;
    color:#555;
}
.card{
    background:#f5f5f5;
    padding:15px;
    border-radius:12px;
    margin-bottom:10px;
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
st.markdown('<div class="main-title">🤖 RSPL DMS AI Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Upload Screenshot → Get Instant Solution</div>', unsafe_allow_html=True)
 
st.divider()
 
# ---------------- SIDEBAR ----------------
page = st.sidebar.selectbox(
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
    c2.metric("Version","1.0")
    c3.metric("Status","Online")
 
    st.divider()
 
    st.subheader("Supported Error Types")
 
    for item in issues:
 st.write("✅", item.get("error"
item.get("title", "Unknown Error")))
 
# ---------------- SEARCH ----------------
elif page=="🔍 Search Issue":
 
    search=st.text_input("Search by Error Code / Name / Keyword")
 
    if search:
 
        found=False
 
        for item in issues:
 
            keywords=" ".join(item.get("keywords",[]))
 
            if (
                search.lower() in item["error"].lower()
                or search.lower() in keywords.lower()
            ):
 
                found=True
 
                st.success(item["error"])
 
                st.write("### Solution")
 
                for step in item["solution"]:
                    st.write("✔",step)
 
        if not found:
            st.error("No matching issue found.")
 
# ---------------- UPLOAD ----------------
elif page=="📷 Upload Screenshot":
 
    img=st.file_uploader(
        "Upload Screenshot",
        type=["png","jpg","jpeg"]
    )
 
    if img:
 
        image=Image.open(img)
 
        st.image(image,use_container_width=True)
 
        st.info("OCR + AI Detection will be added in Part 2")
 
# ---------------- ALL ISSUES ----------------
elif page=="📚 All Issues":
 
    for item in issues:
 
        with st.expander(item["error"]):
 
            for s in item["solution"]:
                st.write("✔",s)
 
# ---------------- ABOUT ----------------
else:
 
    st.header("About")
 
    st.write("RSPL DMS AI Assistant")
 
    st.write("Developed for DMS Support Team")
 
    st.write("Future Features")
 
    st.write("• OCR Detection")
    st.write("• AI Matching")
    st.write("• Auto Screenshot Analysis")
    st.write("• PDF Export")
