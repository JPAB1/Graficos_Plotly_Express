import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html


df = pd.read_csv('projeto_3\ecommerce_estatistica.csv')
df.dropna()


def grafico_histogr(df):
    # Gráfico de  Histograma
    # Ver como estão distribuídas as avaliações dos produtos
    
    fig1 = px.histogram(df, x='Nota', nbins=10, title='Histograma teste', opacity=1)
    
    return fig1

def grafico_dispersao(df):
    #Gráfico de Dispersão
    # Ajudar a entender se produtos com mais avaliações apresentam notas mais altas (ou vice-versa).

    fig2 = px.scatter(df, x='Nota', y='N_Avaliações', color_discrete_sequence=px.colors.qualitative.Bold, opacity=1)
    fig2.update_layout(
        title='Disperção - Nota e Quantidade de Avaliações',
        xaxis_title='Nota',
        yaxis_title='Qtd. Avaliações'
    )
    return fig2
    
def grafico_calor(df):
    # Mapa de Calor
    # Poderá detectar padrões ou relações importantes que podem embasar decisões estratégicas.

    corr = df[['Nota', 'N_Avaliações', 'Desconto', 'Qtd_Vendidos_Cod']].corr()
    fig3 = px.imshow(corr, text_auto=True, aspect='auto', color_continuous_scale='Viridis', title='Mapa de Calor de Correlação')
    return fig3


def grafico_barra(df):

    # Gráfico de barra
    # Visualizar as 10 Marcas com mais frequência
    
    df_marca = df['Marca'].value_counts().head(10)
    fig4 = px.bar(df.head(10), x=df_marca.index, y=df_marca.values, color=df_marca.index, barmode='group',color_discrete_sequence=px.colors.qualitative.Bold, opacity=1)
    fig4.update_layout(
        title='Gráfico de Barra - Frequência de Produtos por Marca',
        xaxis_title='Marcas',
        yaxis_title='Quantidade de Produtos',
        legend_title='Frequência Marcas',
        plot_bgcolor='rgba(222, 255, 253, 1)', # Fundo interno
        paper_bgcolor='rgba(186, 245, 241, 1)' # Fundo externo
    )
    return fig4


def grafico_pizza(df):
    # Gráfico de Pizza
    # OS 5 Gêneros mas usados
    
    y = df['Gênero'].value_counts().head(5).values
    x = df['Gênero'].value_counts().head(5).index
    fig5 = px.pie(y, names=x, values=y,  hole= 0.2, color_discrete_sequence=px.colors.sequential.RdBu)
    fig5.update_layout(
        title='Gráfico de Pizza - Os 5 Gênero Mas Usados'
    )
    return fig5


def grafico_densidade(df):
    # Gráfico de Densidade
    # Útil para identificar a “forma” da distribuição – por exemplo, se os preços se concentram em determinada faixa
    
    fig6 = px.density_contour(df, x='Preço', y=df['Preço'].index)
    fig6.update_layout(
        title='Gráfico de Densidade'
    )
    return fig6


def grafico_regressao(df):
    # Gráfico de Regressão
    # É ideal para visualizar a tendência linear (ou ajustar uma reta de regressão)

    fig7 = px.scatter(df, x='Preço', y='Qtd_Vendidos_Cod', trendline='ols', trendline_color_override='blue')
    fig7.update_layout(title='Gráfico De Regressão')

    return fig7


def cria_app(df):

    app = Dash(__name__)

    fig1 = grafico_histogr(df)
    fig2 = grafico_dispersao(df)
    fig3 = grafico_calor(df)
    fig4 = grafico_barra(df)
    fig5 = grafico_pizza(df)
    fig6 = grafico_densidade(df)
    fig7 = grafico_regressao(df)

    app.layout = html.Div([
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2),
        dcc.Graph(figure=fig3),
        dcc.Graph(figure=fig4),
        dcc.Graph(figure=fig5),
        dcc.Graph(figure=fig6),
        dcc.Graph(figure=fig7)
    ])
    return app



if __name__=='__main__':

    app = cria_app(df)
    app.run(debug=True, port=8050)
