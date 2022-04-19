import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np
import plost
from PIL import Image
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode

# Page setting
# st.set_page_config(layout="wide")

st.set_page_config(
    page_title="Brazilian stocks",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# from Data
seattle_weather = pd.read_csv(
    'https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv', parse_dates=['date'])
stocks = pd.read_csv(
    'https://raw.githubusercontent.com/dataprofessor/data/master/stocks_toy.csv')


detail_joel = pd.read_csv(
    'https://github.com/jonavicius-marcio/stocks/blob/main/detail_joel.csv?raw=true', sep=',')

joel_performance = pd.read_csv(
    'https://github.com/jonavicius-marcio/stocks/blob/main/joel_performance.csv?raw=true', sep=',')

grahan_performance = pd.read_csv(
    'https://github.com/jonavicius-marcio/stocks/blob/main/grahan_performance.csv?raw=true', sep=',')


detail_grahan = pd.read_csv(
    'https://github.com/jonavicius-marcio/stocks/blob/main/detail_grahan.csv?raw=true', sep=',')


DATA_URL = (
    'https://github.com/jonavicius-marcio/stocks/blob/main/joel_performance.csv?raw=true')


def load_data():
    data = pd.read_csv(DATA_URL, sep=',')
    return data


stocks_2 = load_data()
stocks_2['date'] = stocks_2['date'].astype('str')
stocks_2 = stocks_2.set_index('date')


st.write("""
# Compare stock selection performance  
Comparation of **Joel** and **Grahan** methods fos stock selecion.
""")


############################### Function ####################################################

def line_chart(x, y1, y2, title, y1_name, y2_name):
    fig = plt.figure()

    ax1 = fig.add_subplot(111)
    ax1.plot(x, y1,  linestyle='dotted')
    ax1.tick_params(axis='x', labelrotation=90)

    ax1.set_ylabel(y1_name)
    ax1.set_title(title)
    ax1.legend([y1_name], bbox_to_anchor=(1.07, 0.9), loc="upper left")

    ax2 = ax1.twinx()  # this is the important function
    ax2.plot(x, y2, 'r', label='Inline label')
    # ax2.set_xlim([0, np.e])
    ax2.set_ylabel(y2_name)

    ax2.legend([y2_name], bbox_to_anchor=(1.07, 1), loc="upper left")

    return st.pyplot(plt)


################################ Joel ###################################################

joel_performance['date'] = joel_performance['date'].astype('str')

x = joel_performance['date'].to_numpy()
y1 = joel_performance['percent'].to_numpy()
y2 = joel_performance['profit_total'].to_numpy()


joel1, joel2 = st.columns(2)
joel1.header("Joel formula")


with joel1:
    line_chart(x, y1, y2, 'Joel Performance',  'pnl Percentage', 'pnl amount')

joel2.header(" Joel Stocks detail")
with joel2:
    AgGrid(
        detail_joel,
        data_return_mode='AS_INPUT',
        update_mode='MODEL_CHANGED',
        fit_columns_on_grid_load=False,
        theme='blue',  # Add theme color to the table
        enable_enterprise_modules=True,
        height=750,
        width='20%',
        reload_data=True
    )

############################### Grahan ####################################################

grahan_performance['date'] = grahan_performance['date'].astype('str')

gr_x = grahan_performance['date'].to_numpy()
gr_y1 = grahan_performance['percent'].to_numpy()
gr_y2 = grahan_performance['profit_total'].to_numpy()


grahan1, grahan2 = st.columns(2)
grahan1.header("Grahan formula")


with grahan1:
    line_chart(gr_x, gr_y1, gr_y2, 'Grahan Performance',
               'pnl Percentage', 'pnl amount')

grahan2.header(" Grahan Stocks detail")
with grahan2:
    AgGrid(
        detail_grahan,
        data_return_mode='AS_INPUT',
        update_mode='MODEL_CHANGED',
        fit_columns_on_grid_load=False,
        theme='blue',  # Add theme color to the table
        enable_enterprise_modules=True,
        height=750,
        width='20%',
        reload_data=True
    )


# show data on streamlit
st.line_chart(stocks_2.profit_total, width=20,
              height=400, use_container_width=True)

# show data on streamlit
st.line_chart(stocks_2.percent, width=20,
              height=400, use_container_width=True)


st.write(stocks_2)


###################################################################################

# Row A
#a1, a2, a3 = st.columns(3)
# a1.image(Image.open('streamlit-logo-secondary-colormark-darktext.png'))
#a2.metric("Wind", "9 mph", "-8%")
#a3.metric("Humidity", "86%", "4%")

# Row B
#b1, b2, b3, b4 = st.columns(4)
#b1.metric("Temperature", "70 °F", "1.2 °F")
#b2.metric("Wind", "9 mph", "-8%")
#b3.metric("Humidity", "86%", "4%")
#b4.metric("Humidity", "86%", "4%")

# Row C
#c1, c2 = st.columns((7, 3))
# with c1:
#    st.markdown('### Heatmap')
#    plost.time_hist(
#        data=seattle_weather,
#        date='date',
#        x_unit='week',
#        y_unit='day',
#        color='temp_max',
#        aggregate='median',
#        legend=None)
# with c2:
#    st.markdown('### Bar chart')
#    plost.donut_chart(
#        data=stocks,
#        theta='q2',
#        color='company')
