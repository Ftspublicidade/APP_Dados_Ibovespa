import numpy as np
import streamlit as st
import pandas as pd
import pandas_datareader.data as web
import plotly.graph_objs as go
import yfinance as yf
from datetime import date
yf.pdr_override()

ibov = web.get_data_yahoo("^BVSP")
ibov = ibov.reset_index()
ibov_2021 = ibov.loc[ibov["Date"].dt.year == 2021]

def main():
    st.title("Análise dos  dados da Ibovespa - Fernanda Santos")
    st.image("dados.jpg")
    #if file is not None:
        #df = pd.read_csv(file)
    st.text('Visualizando os Últimos registros do dataset...')
    slider = st.slider("Valores", 0,100)
    st.dataframe(ibov.tail(slider))
    st.header('Gráfico do fechamento das ações')

    trace1 = go.Scatter(
                x=ibov.Date,
                y=ibov.Close,
                name = "Ibovespa Close",
                line = dict(color = '#17BECF'),
                opacity = 0.8)
    

    data = [trace1]
    layout = go.Layout(dict(
    title = "Ações Ibovespa",
    title_x= 0.5,
    xaxis =dict(
        range = ['2020-01-01',date.today()])),
    )
    fig = go.Figure(data=data, layout=layout)

    st.write(fig)

    st.header("Gráfico com botões onde podemos escolher analisar todos os meses, os 6 últimos meses ou o mês anterior.")

    trace2 = go.Scatter(
        x=ibov.Date,
        y=ibov.Close,
        name = "Ibovespa close",
        line = dict(color = '#17BECF'),
        opacity = 0.8)

    data1 = [trace2]
    layout1 = go.Layout(dict(
        title="Close",
        title_x=0.5,
        xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label='1m',
                     step='month',
                     stepmode='backward'),
                dict(count=6,
                     label='6m',
                     step='month',
                     stepmode='backward'),
                dict(step='all')
            ])
        ),
        rangeslider=dict(
            visible = True
        ),
        type='date'
    ),
    ))

    fig1 = go.Figure(data=data1, layout=layout1)
    st.write(fig1)


    st.header("Gráfico de Candlestick, onde podemos analisar a oscilação entre a abertura e o fechamento, e se a ação fechou maior ou menor que o preço de abertura, para isso só analisar pela cor, os vermelhos fecharam com o preço menor do que o de abertura e os verdes fecharam com o preço maior do que o de abertura.")
    st.header("Candlestick com os dados de 2020")

    #st.dataframe(ibov_2020)

    trace3 = go.Candlestick(x=ibov_2021['Date'],
                open=ibov_2021['Open'],
                high=ibov_2021['High'],
                low=ibov_2021['Low'],
                close=ibov_2021['Close'])

    data2 = [trace3]
    fig2 = go.Figure(data=data2)
    st.write(fig2)

if __name__ == '__main__':
    main()


