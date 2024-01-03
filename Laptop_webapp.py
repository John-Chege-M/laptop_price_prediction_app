import streamlit as st 
import joblib
import pandas 
import numpy

model = joblib.load("D:\MACHINE LEARNING PROJECTS\Laptop price prediction\laptop_price_prediction.pkl")
st.header("Laptop Price Prediction App")

st.write("You want to buy a laptop?")
st.write()
st.write("Lets try to predict the cost in reference to specifications that you choose.")
st.write()
st.write()
col1,col2 = st.columns(2)

with col1:
    s1 = st.selectbox("Laptop Brand",('Apple','Hp','Acer','Asus','Dell','Lenovo','Chuwi','MSI',
               'Microsoft','Toshiba','Huawei','Xioami','Vero','Razer',
               'Mediacom','Samsung','Google','Fujitsu','LG'))
    if s1 == 'Apple':
        p1 = 0
    elif s1 == 'Hp':
        p1 = 1
    elif s1 == 'Acer':
        p1 = 2
    elif s1 == 'Asus':
        p1 = 3
    elif s1 == 'Dell':
        p1 = 4
    elif s1 == 'Lenovo':
        p1 = 5
    elif s1 == 'Chuwi':
        p1 = 6
    elif s1 == 'MSI':
        p1 =7
    elif s1 == 'Microsoft':
        p1 = 8
    elif s1 == 'Toshiba':
        p1 = 9
    elif s1 == 'Huawei':
        p1 = 10
    elif s1 == 'Xioami':
        p1 = 11
    elif s1 == 'Vero':
        p1 = 12
    elif s1 == 'Razer':
        p1=13
    elif s1 == 'Mediacom':
        p1=14
    elif s1 == 'Samsung':
        p1 = 15
    elif s1 == 'Google':
        p1 = 16
    elif s1 == 'Fujitsu':
        p1 = 17
    elif s1 == 'LG':
        p1 = 18    

with col2:
    s2 = st.selectbox("Type Name",('Ultrabook','Notebook','Netbook','Gaming','2 in 1 convertible','Workstation'))
    if s2 == 'Ultrabook':
        p2 = 0
    elif s2 == 'Notebook':
        p2 = 1
    elif s2 == 'Netbook':
        p2 = 2
    elif s2 == 'Gaming':
        p2 = 3
    elif s2 == '2 in 1 convertible':
        p2 = 4
    elif s2 == 'Workstation':
        p2 = 5

with col1:
    p3 = st.slider("Laptop size (Inches)",10.1,18.4,step=0.1)

with col2:
    s3 = st.selectbox("Screen Resolution",('2560x1600', '1440x900', '1920x1080', '2880x1800', '1366x768',
       '2304x1440', '3200x1800', '1920x1200', '2256x1504', '3840x2160',
       '2160x1440', '2560x1440', '1600x900', '2736x1824', '2400x1600'))
    if s3 == '2560x1600':
        p4 = 0
    elif s3 == '2304x1440':
        p4 = 1
    elif s3 == '2160x1440':
        p4 = 2
    elif s3 == '1440x900':
        p4 = 3
    elif s3 == '200x1800':
        p4 = 4
    elif s3 == '2560x1440':
        p4 = 5
    elif s3 == '1920x1080':
        p4 = 6
    elif s3 == '920x1200':
        p4 =7
    elif s3 == '1600x900':
        p4 = 8
    elif s3 == '2880x1800':
        p3 = 9
    elif s3 == '2256x1504':
        p4 = 10
    elif s3 == '2736x1824':
        p4 = 11
    elif s3 == '1366x768':
        p4 = 12
    elif s3 == '3840x2160':
        p4=13
    elif s3 == '2400x1600':
        p4=14
with col1:
    p5 = st.slider("Ram in GB",2,64,step=2)
with col2:
    s4 = st.selectbox(" Operating System",('macOS', 'No OS', 'Windows 10', 'Mac OS X', 'Linux', 'Android',
       'Windows 10 S', 'Chrome OS', 'Windows 7'))
    if s4 == 'macOS':
        p6 = 0
    elif s4 == 'No OS':
        p6 = 1
    elif s4 == 'Windows 10':
        p6 = 2
    elif s4 == 'Mac OS X':
        p6 = 3
    elif s4 == 'Linux':
        p6 = 4
    elif s4 == 'Android':
        p6 = 5
    elif s4 == 'Windows 10 S':
        p6 = 6
    elif s4 == 'Chrome OS':
        p6 =7
    elif s4 == 'Windows 7':
        p6 = 8

with col1:
    p7 = st.slider("Weight in Kg",0.69,4.6, step=0.1)

    
with col2:
    s5 = st.selectbox("Cpu type",('Intel', 'AMD', 'Samsung'))
    if s5 == 'Intel':
        p8 = 0
    elif s5 == 'AMD':
        p8 = 1
    elif s5 == 'Samsung':
        p8 = 2
with col1:
    p9 = st.slider("Frequency Ghz",0.9,3.6 ,step=0.1)

with col2:
    s6 = st.selectbox("Gpu type",('Intel', 'AMD', 'Nvidia', 'ARM'))
    if s6 == 'Intel':
        p10 = 0
    elif s6 == 'AMD':
        p10 = 1
    elif s6 == 'Nvidia':
        p10 = 2
    elif s6 == 'ARM':
        p10 = 3
    
with col1:
    p11 = st.slider("Memory Capacity",8,2000, step=2)
with col2:
    s7 = st.selectbox("Memory type",('SSD','HDD','Flash','Hybrid'))
    if s7 == 'SSD':
        p12 = 0
    elif s7 == 'HDD':
        p12 = 1
    elif s7 == 'Flash':
        p12 = 2
    elif s7 == 'Hybrid':
        p12 = 3


if st.button("Predict Price"):
    result = model.predict([[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12]])
    st.success("The price of the laptop is {:.0f} shillings.".format(result[0]))
