import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title='Reefer Dashboard 2026', page_icon='📊', layout='wide')

@st.cache_data
def read_sheet(path, sheet, header=None):
    return pd.read_excel(path, sheet_name=sheet, header=header, engine='openpyxl')

st.title('📊 Reefer Dashboard 2026')
st.caption('Dashboard exploratorio basado en Control reefer.xlsx')

workbook = Path(__file__).with_name('Control reefer.xlsx')
if not workbook.exists():
    st.error('No se encontró Control reefer.xlsx. Mantén el Excel que ya subiste en GitHub.')
    st.stop()

raw = read_sheet(workbook, 'RESUMEN', header=None).dropna(how='all').dropna(axis=1, how='all')
with st.sidebar:
    st.header('Navegación')
    page = st.radio('Vista', ['Resumen ejecutivo','Budget vs FCST','Naves','Conexiones','Flujo diario','PPK','Combustible'])

if page == 'Resumen ejecutivo':
    st.subheader('Resumen ejecutivo')
    st.dataframe(raw, use_container_width=True, hide_index=True)
else:
    maps={'Budget vs FCST':'BUDGET vs FCST','Naves':'NAVES','Conexiones':'CONEXIONES','Flujo diario':'FLUJO DIARIO','PPK':'PPK','Combustible':'COMBUSTIBLE'}
    data=read_sheet(workbook,maps[page],header=None).dropna(how='all').dropna(axis=1,how='all')
    st.subheader(page)
    st.dataframe(data,use_container_width=True,hide_index=True)
    numeric=data.apply(lambda c:pd.to_numeric(c,errors='coerce'))
    cols=numeric.notna().sum(); cols=cols[cols>=3].index.tolist()
    if cols:
        c=numeric[cols].copy(); c.index=range(1,len(c)+1)
        use=st.multiselect('Columnas numéricas para graficar',cols,default=cols[:min(3,len(cols))])
        if use:
            long=c[use].reset_index(names='Fila').melt('Fila',var_name='Serie',value_name='Valor').dropna()
            st.plotly_chart(px.line(long,x='Fila',y='Valor',color='Serie',markers=True),use_container_width=True)
