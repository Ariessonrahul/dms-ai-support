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
     # ---------------- SEARCH ----------------
 
elif page=="🔍 Search Issue":
 
    search = st.text_input("🔍 Search Error Code / Name / Keyword")
 
    if search:
 
        found = False
 
        for item in issues:
 
            keywords = " ".join(item.get("keywords", []))
 
            if (
                search.lower() in item.get("error", "").lower()
                or search.lower() in keywords.lower()
            ):
 
                found = True
 
                st.success("✅ " + item.get("error", "Unknown Error"))
 
                st.subheader("Solution")
 
                for step in item.get("solution", []):
                    st.write("✔", step)
 
        if not found:
            st.error("❌ No matching issue found")
 
# ---------------- SCREENSHOT ----------------
 
elif page=="📷 Upload Screenshot":
 
    uploaded = st.file_uploader(
        "Upload Screenshot",
        type=["png","jpg","jpeg"]
    )
 
    if uploaded:
 
        image = Image.open(uploaded)
 
        st.image(image, use_container_width=True)
 
        st.info("🤖 AI Detection module coming in next update.")
 
# ---------------- ALL ISSUES ----------------
 
elif page=="📚 All Issues":
 
    for item in issues:
 
        with st.expander(item.get("error","Unknown Error")):
 
            for step in item.get("solution",[]):
 
                st.write("✔",step)
 
# ---------------- ABOUT ----------------
 
else:
 
    st.header("About")
 
    st.write("RSPL DMS AI Assistant")
 
    st.write("Version 2.0")
 
    st.write("Developed by Rahul Maurya ❤️")
 
    st.write("Upcoming Features")
 
    st.write("• OCR Detection")
    st.write("• AI Screenshot Matching")
    st.write("• PDF Download")
    st.write("• Admin Panel")
# ---------------- EXTRA DASHBOARD ----------------
 
if page == "🏠 Home":
 
    st.divider()
    st.subheader("📊 Dashboard Overview")
 
    col1, col2 = st.columns(2)
 
    with col1:
        st.info(f"📌 Total Supported Issues : {len(issues)}")
        st.success("🟢 System Status : Online")
 
    with col2:
        st.warning("📷 OCR Status : Coming Soon")
        st.info("🤖 AI Engine : Ready")
 
    st.divider()
 
    st.subheader("🚀 Quick Actions")
 
    a1, a2, a3 = st.columns(3)
 
    with a1:
        if st.button("🔍 Search Issue"):
            st.info("Open the 'Search Issue' menu from the sidebar.")
 
    with a2:
        if st.button("📷 Upload Screenshot"):
            st.info("Open the 'Upload Screenshot' menu from the sidebar.")
 
    with a3:
        if st.button("📚 View All Issues"):
            st.info("Open the 'All Issues' menu from the sidebar.")
 
    st.divider()
 
    st.subheader("📞 Need Help?")
 
    st.success(
        """
        If your issue is not listed:
 
        ✅ Contact DMS Support Team
 
        📧 Email: dms.support@company.com
 
        ☎️ Extension: XXXX
        """
    )
