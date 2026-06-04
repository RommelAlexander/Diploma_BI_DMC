import streamlit as st
st.title("Proyecto fina de Diploma BI")
st.ssidebar.title("Parametros")





st.write("Elaborado por: Rommel Picon")

archivo = st.file_uploader("Cargue el archivo excel o csv")
if archivo is not None:
  
  if archivo.nameednswith(".csv"):
    data= pd.read_csv(archivo)
    st.writre(data)
  elif archivo.nameednswith(".xlsx"):
    data= pd.read_excel(archivo)
    st.writre(data)
  else
  st.write("Formato no valido")
  
  else:
  st.write("Por favor cargue su archivo")
