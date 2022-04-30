# import module
import streamlit as st
 
# Title
st.title("Proyecto Flujo Maltifasico")
st.text('Por: Daniela Camacho')

# success
st.success("Success")
 
# success
st.info("Information")
 
# success
st.warning("Warning")
 
# success
st.error("Error")

# first argument takes the titleof the selectionbox
# second argument takes options
hobby = st.selectbox("Hobbies: ",
                     ['Dancing', 'Reading', 'Sports'])