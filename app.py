import streamlit as st
 
st.set_page_config(
    page_title="DMS AI Support",
    page_icon="🤖",
    layout="wide"
)
 
st.title("🤖 DMS AI Support Assistant")
st.markdown("### Upload your DMS error screenshot")
 
uploaded_file = st.file_uploader(
    "Choose Screenshot",
    type=["png", "jpg", "jpeg"]
)
 
if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Screenshot", use_container_width=True)
 
    st.success("Screenshot uploaded successfully ✅")
 
    st.info("⚠️ AI Detection module is under development...")
 
st.markdown("---")
st.subheader("Common Issues")
 
st.button("Employee ID Missing")
st.button("Preparing App")
st.button("Internet Error")
st.button("Synchronization Issue")
st.button("Payment Status None")
