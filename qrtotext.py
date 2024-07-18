import cv2
import numpy as np
import streamlit as st

st.title("Streamlit QR Code Reader")
st.header("Try holding a QR code in front of your webcam or upload a QR code file")

if "found_qr" not in st.session_state:
    st.session_state.found_qr = False

if "qr_code_image" not in st.session_state:
    st.session_state.qr_code_image = None

tab1, tab2 = st.tabs(["Camera", "Upload File"])

with tab1:
    img = st.camera_input("Take a picture")

    if img is not None:
        bytes_data = img.getvalue()
        cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

        detector = cv2.QRCodeDetector()

        data, bbox, straight_qrcode = detector.detectAndDecode(cv2_img)

        if data:
            st.session_state["found_qr"] = True
            st.session_state["qr_code_image"] = img
            st.write("QR Code Text:", data)

with tab2:
    uploaded_file = st.file_uploader("Upload QR Code File", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        image = uploaded_file
        cv2_img = cv2.imdecode(np.frombuffer(image.getvalue(), np.uint8), cv2.IMREAD_COLOR)

        detector = cv2.QRCodeDetector()

        data, bbox, straight_qrcode = detector.detectAndDecode(cv2_img)

        if data:
            st.write("QR Code Text:", data)