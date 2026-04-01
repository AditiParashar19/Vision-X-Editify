def apply_filter():
    import streamlit as st
    import cv2
    import numpy as np
    from PIL import Image
    from rembg import remove
    import io
    st.markdown("""
    <h1 style='text-align:center; color:#3B82F6;'>
    Image Filters
    </h1>
    """, unsafe_allow_html=True)
    st.markdown("<h3> Image Filter App</h3>",unsafe_allow_html=True)
    st.write("Filter your image...")

    uploaded_file = st.file_uploader("Upload your image",type=["jpeg","png","jpg"])

    col1,col2 = st.columns(2)
    with col1:
        if(uploaded_file is not None):
            # Convert to Opencv format
            image = Image.open(uploaded_file)
            img = np.array(image)
            st.image(img,caption="Original Image",use_container_width=True)
            output = img.copy()
            filter = st.selectbox("Select filter for your image: ",
                                ["None",
                                "Grayscale",
                                "Blur",
                                "Flip Vertical",
                                "Flip Horizontal",
                                "Flip Both",
                                "Negative Image",
                                "Rotate Image",
                                "Resize Image",
                                "Change Brightness"])
            if(filter=="Grayscale"):
                output= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            elif(filter=="Blur"):
                output = cv2.GaussianBlur(img,(15,15),0)
            elif(filter =="Flip Vertical"):
                output = cv2.flip(img,0)
            elif(filter =="Flip Horizontal"):
                output = cv2.flip(img,1)
            elif(filter=="Flip Both"):
                output = cv2.flip(img,-1)
            elif(filter=="Negative Image"):
                output = 255 - img
            elif(filter=="Rotate Image"):
                angle = st.slider("Select angle for Rotation",0,360,0)
                (h,w) = img.shape[:2]
                center = (w//2,h//2)
                M=cv2.getRotationMatrix2D(center,angle,1.0)
                output = cv2.warpAffine(img,M,(w,h))
            elif(filter=="Resize Image"):
                width = int(st.number_input("Enter width for resizing: "))
                height = int(st.number_input("Enter height for resizing: "))
                if(width>0 and height>0):
                    output = cv2.resize(img,(width,height))
            elif(filter=="Change Brightness"):
                brightness = st.slider("Select Brightness",-100,100,0)
                output = cv2.convertScaleAbs(img,alpha=1,beta =brightness)
            with col2:
                st.spinner()
                st.image(output,caption="Processed Image",use_container_width=True)
                st.success("Image processed successfully!")
                st.balloons()
                result = Image.fromarray(output)
                buf = io.BytesIO()
                result.save(buf, format="PNG")
                st.download_button(
                "📥 Download Filtered Image",
                data=buf.getvalue(),
                file_name="filtered.png",
                mime="image/png"
                )




        


