import streamlit as st
import json
from PIL import Image
 
# ------------------------
# PAGE CONFIG
# ------------------------
st.set_page_config(
    page_title="RSPL DMS AI Assistant",
    page_icon="🤖",
    layout="wide"
)
 
# ------------------------
# LOAD ISSUES
# ------------------------
def load_issues():
    try:
        with open("issues.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return []
 
issues = load_issues()
 
# ------------------------
# HEADER
# ------------------------
st.markdown("""
# 🤖 RSPL DMS AI Assistant
### Upload Screenshot → Get Instant Solution
---
""")
 
# ------------------------
# SIDEBAR
# ------------------------
st.sidebar.title("📌 Menu")
 
page = st.sidebar.radio(
    "Select",
    [
        "🏠 Home",
        "🔍 Search Issue",
        "📷 Upload Screenshot",
        "ℹ️ About"
    ]
)
 
# ------------------------
# HOME
# ------------------------
if page == "🏠 Home":
 
    st.success("Welcome to RSPL DMS AI Assistant")
 
    st.info("Supported Issues")
 
    col1, col2 = st.columns(2)
 
    with col1:
        st.write("✅ Employee ID Missing")
        st.write("✅ Preparing App")
        st.write("✅ Internet Error")
        st.write("✅ Payment Status None")
 
    with col2:
        st.write("✅ Portal Error")
        st.write("✅ No BP Showing")
        st.write("✅ Loading Issue")
        st.write("✅ Synchronization")
 
# ------------------------
# SEARCH
# ------------------------
elif page == "🔍 Search Issue":
 
    search = st.text_input("Enter Error")
 
    if search:
 
        found = False
 
        for issue in issues:
 
            if search.lower() in issue["title"].lower():
 
                found = True
 
                st.success(issue["title"])
 
                st.subheader("Solution")
 
                for step in issue["solution"]:
                    st.write("✅", step)
 
        if not found:
            st.error("No Matching Issue Found")
 
# ------------------------
# UPLOAD
# ------------------------
elif page == "📷 Upload Screenshot":
 
    image = st.file_uploader(
        "Upload Screenshot",
        type=["png","jpg","jpeg"]
    )
 
    if image:
 
        img = Image.open(image)
 
        st.image(img, use_container_width=True)
 
        st.info("OCR + AI Detection coming in next version")
 
# ------------------------
# ABOUT
# ------------------------
else:
 
    st.title("About")
 
    st.write("RSPL DMS AI Assistant")
 
    st.write("Version 1.0")
 
    st.write("Developed for DMS Support Team")
has context menu

