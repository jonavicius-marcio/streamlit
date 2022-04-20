import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode

# Page setting
# st.set_page_config(layout="wide")

st.set_page_config(
    page_title="Brazilian stocks",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# from Data

detail_joel = pd.read_csv(
    'https://github.com/jonavicius-marcio/stocks/blob/main/detail_joel.csv?raw=true', sep=',')

joel_performance = pd.read_csv(
    'https://github.com/jonavicius-marcio/stocks/blob/main/joel_performance.csv?raw=true', sep=',')

grahan_performance = pd.read_csv(
    'https://github.com/jonavicius-marcio/stocks/blob/main/grahan_performance.csv?raw=true', sep=',')


detail_grahan = pd.read_csv(
    'https://github.com/jonavicius-marcio/stocks/blob/main/detail_grahan.csv?raw=true', sep=',')

detail_grahan = pd.read_csv(
    'https://github.com/jonavicius-marcio/stocks/blob/main/detail_grahan.csv?raw=true', sep=',')


df_grahan_actual_quote = pd.read_csv(
    'https://github.com/jonavicius-marcio/stocks/blob/main/df_grahan_actual_quote.csv?raw=true', sep=',')


df_joel_actual = pd.read_csv(
    'https://github.com/jonavicius-marcio/stocks/blob/main/df_joel_actual.csv?raw=true', sep=',')

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
        height=400,
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
        height=400,
        width='20%',
        reload_data=True
    )


############################### actual  ####################################################

actual1, actual2 = st.columns(2)


actual1.header("Joel Actual")
with actual1:
    AgGrid(
        df_joel_actual,
        data_return_mode='AS_INPUT',
        update_mode='MODEL_CHANGED',
        fit_columns_on_grid_load=False,
        theme='blue',  # Add theme color to the table
        enable_enterprise_modules=True,
        height=400,
        width='20%',
        reload_data=True
    )

actual2.header("Grahan Actual")
with actual2:
    AgGrid(
        df_grahan_actual_quote,
        data_return_mode='AS_INPUT',
        update_mode='MODEL_CHANGED',
        fit_columns_on_grid_load=False,
        theme='blue',  # Add theme color to the table
        enable_enterprise_modules=True,
        height=400,
        width='20%',
        reload_data=True
    )

###################################################################################

# show data on streamlit
# st.line_chart(stocks_2.profit_total, width=20,
#              height=400, use_container_width=True)

# show data on streamlit
# st.line_chart(stocks_2.percent, width=20,
#              height=400, use_container_width=True)


# st.write(stocks_2)
