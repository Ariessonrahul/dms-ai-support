import streamlit as st
import json
from PIL import Image
 
from utils import search_issue
from detector import detect_error, format_solution
from ocr import extract_text
from pdf_generator import generate_pdf
 
st.set_page_config(
    page_title="RSPL DMS AI Assistant",
    page_icon="🤖",
    layout="wide"
)
 
@st.cache_data
def load_data():
    try:
        with open("issues.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []
 
issues = load_data()
 
st.markdown("""
<style>
 
.main-title{
font-size:42px;
font-weight:bold;
text-align:center;
color:#5E35B1;
}
 
.sub-title{
text-align:center;
color:gray;
font-size:18px;
}
 
.card{
padding:15px;
background:#F4F4F4;
border-radius:10px;
margin-bottom:10px;
}
 
</style>
""",unsafe_allow_html=True)
 
st.markdown(
'<div class="main-title">🤖 RSPL DMS AI Assistant</div>',
unsafe_allow_html=True
)
 
st.markdown(
'<div class="sub-title">AI Powered DMS Support System</div>',
unsafe_allow_html=True
)
 
st.divider()
 
page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "🔍 Search",
        "🤖 AI Detection",
        "📷 Screenshot",
        "📚 Issues",
        "ℹ About"
    ]
)
# =========================
# HOME PAGE
# =========================
 
if page == "🏠 Home":
 
    st.success("Welcome to RSPL DMS AI Assistant")
 
    col1, col2, col3 = st.columns(3)
 
    with col1:
        st.metric("Supported Issues", len(issues))
 
    with col2:
        st.metric("Version", "3.0")
 
    with col3:
        st.metric("Status", "🟢 Online")
 
    st.divider()
 
    st.subheader("📌 Supported Error Types")
 
    if len(issues) == 0:
        st.warning("No issues found in issues.json")
    else:
        for item in issues:
            st.write("✅", item.get("error", "Unknown Error"))
 
    st.divider()
 
    st.subheader("🚀 Quick Actions")
 
    c1, c2, c3 = st.columns(3)
 
    with c1:
        st.info("🔍 Search any DMS issue")
 
    with c2:
        st.info("📷 Upload screenshot for
# =========================
# SEARCH PAGE
# =========================
 
elif page == "🔍 Search":
 
    st.header("🔍 Search DMS Issue")
 
    query = st.text_input(
        "Enter Error Code, Error Name or Keyword"
    )
 
    if st.button("Search"):
 
        if query.strip() == "":
            st.warning("Please enter a keyword.")
        else:
 
            results = search_issue(query, issues)
 
            if len(results) == 0:
 
                st.error("❌ No matching issue found.")
 
            else:
 
                st.success(f"{len(results)} matching issue(s) found.")
 
                for item in results:
 
                    st.subheader(item.get("error", "Unknown Error"))
 
                    st.write("### Recommended Solution")
 
                    for step in item.get("solution", []):
                        st.write(f"
# =========================
# SCREENSHOT OCR
# =========================
 
elif page == "📷 Screenshot":
 
    st.header("📷 Screenshot Analysis")
 
    uploaded_file = st.file_uploader(
        "Upload DMS Screenshot",
        type=["png", "jpg", "jpeg"]
    )
 
    if uploaded_file is not None:
 
        image = Image.open(uploaded_file)
 
        st.image(image, use_container_width=True)
 
        with st.spinner("Reading screenshot..."):
 
            extracted_text = extract_text(uploaded_file)
 
        st.subheader("📄 Extracted Text")
 
        st.code(extracted_text)
 
        result = detect_error(extracted_text, issues)
 
        if result["found"]:
 
            issue = result["issue"]
 
            st.success(
                f"✅ Error Detected ({result['confidence']}% Match)"
            )
 
            st.subheader(issue.get("error"))
 
            st.write("### Recommended Solution")
 
            for step in issue.get("solution", []):
                st.write("✔", step)
 
            pdf = generate_pdf(issue)
 
            st.download_button(
                "📄 Download Solution PDF",
                pdf,
                file_name="solution.pdf",
                mime="application/pdf"
            )
 
        else:
 
            st.error("No matching issue found.")
has context menu
