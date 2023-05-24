import streamlit as st
import base64
import os

st.set_page_config(
    page_title='Solucionario',
    page_icon="🧊",
    layout='wide')
st.sidebar.title('Solucionario')

# listdir=[filename for filename in os.listdir(file_to_search) if os.path.isdir(os.path.join(file_to_search,filename))]
dirlist = [d for d in next(os.walk("."))[1]][2:]
st.sidebar.write(dirlist)

# Filtro Curso
lc=[d for d in next(os.walk("."))[1]][2:]
curso = st.sidebar.selectbox('Curso:',lc,0)

# # Filtro Bloque
# lb=[b for b in next(os.walk(curso))[1]]
# curso = st.sidebar.selectbox('Bloque:',lb,0)

def show_pdf(file_path):
    with open(file_path,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
#     pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)



st.title('Ejercicios de Matemáticas')

# files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.pdf')]
files = [f for f in os.listdir('.') if f.endswith('.pdf')]
st.write(files)

for f in files :
    st.header(f.split(".pdf")[0])
    show_pdf(f)
    st.download_button(label="Descargar fichero",
        data=open(f, "rb").read(),
        file_name=f,
        mime='application/octet-stream')
