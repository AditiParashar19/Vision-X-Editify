def drawing():
    import streamlit as st
    import cv2
    import numpy as np
    import io
    from PIL import Image
    from utils import hex_to_bgr

    st.markdown("""
    <h1 style='text-align:center; color:#3B82F6;'>
    Drawing Studio
    </h1>
    """, unsafe_allow_html=True)
    st.write("Draw on your image")

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
                                "Draw Line",
                                "Draw Rectangle",
                                "Draw Circle",
        ])
            if(filter=="Draw Line"):
                x1 =st.slider("Select Starting X",0,img.shape[1],0)
                y1 = st.slider("Select Starting Y",0,img.shape[0],0)

                x2 = st.slider("Select Ending X",0,img.shape[1],0)
                y2 = st.slider("Select Ending Y",0,img.shape[0],0)
                color="#0F0E0FFF"
                
                color = st.color_picker("Pick Color", "#ff0000")
                bgr_color = hex_to_bgr(color)
                pt1=(x1,y1)
                pt2 =(x2,y2)
                thickness=st.slider("Select Thickness: ",0,30,2)
                cv2.line(output,pt1,pt2,bgr_color,thickness)
            elif(filter=="Draw Rectangle"):
                x1 = st.slider("Top left X",0,img.shape[1],0)
                y1 = st.slider("Top left Y",0,img.shape[0],0)
                x2 = st.slider("Bottom Right X",0,img.shape[1],img.shape[1]//2)
                y2 = st.slider("Bottom Right Y",0,img.shape[0],img.shape[0]//2)
                color = st.color_picker("Pick Color", "#1aff00")
                bgr_color = hex_to_bgr(color)
                fill = st.checkbox("Fill rectangle")
                if(fill):
                    thickness = -1
                else:
                    thickness = st.slider("Select thickness",0,30,2)
                cv2.rectangle(output,(x1,y1),(x2,y2),bgr_color,thickness)
            elif(filter =="Draw Circle"):
                x1 = st.slider("Center x",0,img.shape[1],img.shape[1]//2)
                y1 = st.slider("Center Y",0,img.shape[0],img.shape[0]//2)
                radius = st.slider("Radius", 0, 300, 50)
                color = st.color_picker("Pick Color", "#e61af5")
                center = (x1,y1)
                bgr_color = hex_to_bgr(color)
                fill = st.checkbox("Fill Circle")
                if(fill):
                    thickness=-1
                else:
                    thickness = st.slider("Select Thickness",0,30,2)

                cv2.circle(output,center,radius,bgr_color,thickness)
            with col2:
                    st.image(output , caption="After drawing ",use_container_width=True)
                    st.success("Image processed successfully! ")
                    result = Image.fromarray(output)
                    buf = io.BytesIO()
                    result.save(buf, format="PNG")
                    st.download_button(
                    "📥 Download Filtered Image",
                    data=buf.getvalue(),
                    file_name="filtered.png",
                    mime="image/png"
                    )
                    #Cartoon Effect = Blur(Smooth colors) +Edge detection(Bold outlines) 

