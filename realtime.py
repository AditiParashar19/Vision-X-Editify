import cv2
import streamlit as st

def realtime_page():
    st.markdown("""
    <h1 style='text-align:center; color:#3B82F6;'>
    🎥 Real-Time Camera
    </h1>
    """, unsafe_allow_html=True)

    st.write("Apply filters in real-time using your webcam")

    run = st.checkbox("Start Camera")
    filter_option=st.selectbox("Select Filter ",["None",
                                                 "Grayscale",
                                                 "Blur",
                                                 "Edges",
                                                 "Mirror Effect",
                                                 "Contrast and Brightness"])
    Frames = st.image([])
    cap = cv2.VideoCapture(0)

    if(filter_option=="Contrast and Brightness"):
        alpha = st.slider("Select Contrast",0.5,3.0,1.0)
        beta = st.slider("Select Brightness",-100,100,0)
    else:
        alpha,beta = 1.0,0
    while(run):
        success,img = cap.read()
        if(not success):
            st.write("Failed to access Webcam")
            break
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        if(filter_option=="Grayscale"):
            img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        elif(filter_option=="Blur"):
            img = cv2.GaussianBlur(img,(15,15),0)
        elif(filter_option=="Edges"):
            #gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
            img = cv2.Canny(img,100,100)
        elif(filter_option=="Mirror Effect"):
            img = cv2.flip(img,1)
        elif(filter_option=="Contrast and Brightness"):
            img = cv2.convertScaleAbs(img,alpha=alpha,beta=beta)
            #img[:,:,2] = cv2.add(img[:,:,2], 50)  # Red boost
        Frames.image(img)
    cap.release()
    cv2.destroyAllWindows()