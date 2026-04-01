def cartoon_effect():
    import streamlit as st
    import cv2
    from PIL import Image
    import numpy as np
    st.markdown("""
    <h1 style='text-align:center; color:#3B82F6;'>
    Cartoon Effect
    </h1>
    """, unsafe_allow_html=True)
    st.write("Cartoon Effect")
    uploaded_file = st.file_uploader("Upload your image",type=["jpeg","png","jpg"])
    col1,col2 = st.columns(2)
    with col1:
        if(uploaded_file is not None):
            # Convert to Opencv format
            image = Image.open(uploaded_file)
            img = np.array(image)
            st.image(img,caption="Original Image",use_container_width=True)
            output = img.copy()
    
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            gray_blur = cv2.medianBlur(gray, 5)

            edges = cv2.adaptiveThreshold(
                gray_blur, 255,
                cv2.ADAPTIVE_THRESH_MEAN_C,
                cv2.THRESH_BINARY,
                9, 9
            )

            color = cv2.bilateralFilter(img, 9, 300, 300)

            cartoon = cv2.bitwise_and(color, color, mask=edges)
            with col2:
                st.image(cartoon,caption="After Cartoon Effect",use_container_width=True)