import streamlit as st
from streamlit_folium import folium_static
import pandas as pd
import numpy as np
import folium
from folium.plugins import MarkerCluster
import geopandas
import time
import plotly.express as px
from datetime import datetime
import seaborn as sns
from matplotlib import pyplot as plt
from PIL import Image
(pd.set_option('display.float_format', lambda x: '%.3f' % x))
st.set_page_config(layout='wide')

image=Image.open('Assets/HRC.png')
st.sidebar.image(image,use_column_width=True,caption='HRC em breve terrenos  na lua e em Marte.')

options = st.sidebar.radio('Selecione uma seção do Projeto para visitar.',('Home', 'Estatística Descritiva', 'Densidade de Portfólio','Visualização de dados','Insights de Mercado','Avaliação Imobiliária'))
if options == 'Home':
    progress=st.progress(0)
    for i in range(100):
        time.sleep(0.1)
        progress.progress(i+1) 
    
    st.markdown("<h1 style='text-align: center; color: black;'>House Rocket Company</h1>", unsafe_allow_html=True)
    link = '[SejaUmDataScientist](hhttps://sejaumdatascientist.com/os-5-projetos-de-data-science-que-fara-o-recrutador-olhar-para-voce/)'
    st.write('Este é um projeto fictício. A empresa, o contexto e as perguntas de negócios não são reais. Este portfólio está seguindo as recomendações do blog Seja um Data Scientist, para mais informações clique no link a seguir.')
    st.markdown(link, unsafe_allow_html=True)
    st.header('Descrição')
    st.write('House Rocket é uma imobiliaria que procura novos imóveis para seu catalogo, fomentada pela alta e baixa recorrente do mercado imobiliario a empresa busca novas oportunidades de compra de imóveis. A empresa procurou um Cientista de dados para ajudar a encontrar as melhores oportunidades de negócio, ou seja, maximizar a receita. A melhor estratégia é a compra de casas em condições regulares quando estiverem em baixa no mercado e revende-las quando o mercado estiver em alta. Os atributos das casas as tornam mais ou menos atrativas, influenciando a atratividade dos imóveis e, consequentemente, o seu preço. As questões a serem respondidas são:')
    st.write('1. Quais casas a House Rocket deveria comprar e por qual preço de compra?')
    st.write('2. Uma vez a casa em posse da empresa, qual o melhor momento para vendê-las e qual seria o preço da venda?')
    st.header('Premissas do Negócio')
    st.write('As seguintes premissas foram consideradas para esse projeto:')
    st.write('- Os valores iguais a zero em yr_renovated são casas que nunca foram reformadas.')
    st.write('- O valor igual a 33 na coluna bathroom foi considerada um erro e por isso foi delatada das análises.')
    st.write('- Os valores não inteiros nos atributos bathrooms e floors foram arrendados com o intuito de simplificar o projeto.')
    st.write('- A coluna price significa o preço que a casa foi / será comprada pela empresa House Rocket.')
    st.write('- Valores duplicados em ID foram removidos e considerados somente a compra mais recente.')
    st.write('- A localidade e a condição do imóvel foram características decisivas na compra ou não do imóvel.')
    st.write('- A estação do ano foi a característica decisiva para a época da venda do imóvel.')
    st.header('Planejamento do Projeto')
    st.write('1. Coleta de dados via Kaggle')
    st.write('2. Entendimento de negócio')
    st.write('3. Tratamento de dados')
    st.write('3.1. Tranformação de variaveis')
    st.write('3.2. Limpeza')
    st.write('3.3. Entendimento')
    st.write('4. Exploração de dados')
    st.write('5. Responder problemas do negócio')
    st.write('6. Resultados para o negócio')
    st.write('7. Conclusão')
    st.header('Ferramentas utilizadas')
    st.write('- Python 3.8.0')
    st.write('- Jupyter Notebook')
    st.write('- Spyder')
    st.write('- Streamlit')
    st.write('- Heroku') 
    st.header('Conclusão')
    st.write('Os objetivos foram alcançados. Os imóveis foram agrupados por região (zipcode). Considerando o preço do imóvel e a condição minima como regular(3 - 5) foi calculado a mediana do preço. Ao total 10505 imóveis foram declarados como Imóveis com alto potencial de revenda, dentre estes foram sugeridos os 20 mais lucrativos para a empresa comprar. Os imóveis aptos para compra foram agrupados pela localidade e a estação do ano. A mediana foi calculada e imóveis com preço abaixo da mediana teve um acréscimo de 10% em seu valor, enquanto imóveis com preço acima da mediana teve um acréscimo de 30% acima do seu valor.')
    st.header('Proiximos passos')
    st.write('Seria interessante analisar o potencial de lucratividade atraves de reformas para alguns imóveis baseados em sua localização, comprando imoveis em  condições ruins, reformando-os e revendendo-os com finalidade de avaliar qual tipo de reforma retornaria lucro para a empresa. Outra ideia seria a possibilidade de prever a valorização do imóvel, tirando o limitando de 4 estações para os valores dos imóveis, possibilitando uma margem de lucro maior.')
    
    st.markdown("""
    <style>
    .big-font {
        font-size:14px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    
    st.header('Contato')
    st.write('Este Projeto for realizado e revisado por Lujan Rafael Rezende, Engenheiro Ambiental e Sanitarista:')
    link2 = '[Lujanrr - GitHub](https://github.com/lujanrr)'
    link3 = '[Lujanrr - Instagram](https://instagram.com/lujanrr)'
    link4 = '[Lujanrr - LinkedIn](https://www.linkedin.com/in/lujanrr)'
    c1,c2= st.beta_columns(2)
    with c1:
        st.markdown(link2, unsafe_allow_html=True)
        st.markdown(link3, unsafe_allow_html=True)
        st.markdown(link4, unsafe_allow_html=True)
    with c2:
        image2=Image.open('Assets/Jiban.jpg')
        c2.image(image2,caption='Jiban o Policial de Aço', width=130)
    
@st.cache(allow_output_mutation=True)
def get_data(path):
    data = pd.read_csv(path)
    return data
@st.cache(allow_output_mutation=True)
def get_df_buy(path2):
    df_buy= pd.read_csv(path2)
    return df_buy
@st.cache(allow_output_mutation=True)
def get_geofile(url):
    geofile=geopandas.read_file(url)
    return geofile
def set_feature(data):
    data['sqm_lot']= data['sqft_lot']/10.764
    data['sqm_living']=data['sqft_living']/10.764
    data['price_m2']=data['price']/data['sqm_lot']
    data['date']=pd.to_datetime(data['date']).dt.strftime('%Y-%m-%d')
    return data
def overview_data(data):
    if options == 'Estatística Descritiva':
        progress=st.progress(0)
        for i in range(100):
            time.sleep(0.1)
            progress.progress(i+1)
    #====================================
    # Data Overview
    #====================================
        data=data1.copy()
        st.sidebar.title('Filtro de Atributos')
        f_attributes=st.sidebar.multiselect('Selecione os atributos desejados', data.columns)
        f_zipcode=st.sidebar.multiselect('Selecione o zipcode desejado', data['zipcode'].unique())
        st.markdown("<h1 style='text-align: center; color: black;'>House Rocket Company</h1>", unsafe_allow_html=True)
        st.write('Esta seção é destinada para olhar estatisticamente o conjunto de dados, analisando inicialmente algumas métricas para o entendimento do negócio.')
    #attributes+zipcode= selecionar colunas e linhas
    #attributes= selecionar colunas
    #zipcode= selecionar linhas
    #0+0= Retorno o dataset original
    
        if (f_zipcode != []) & (f_attributes != []):
            data= data.loc[data['zipcode'].isin(f_zipcode),f_attributes]
    
        elif (f_zipcode != []) & (f_attributes == []):
            data= data.loc[data['zipcode'].isin(f_zipcode),:]
        if (f_zipcode == []) & (f_attributes != []):
            data= data.loc[:,f_attributes]  
        else:
            data=data.copy()
        if st.checkbox('Mostrar a tabela geral de atributos'):
            st.header('Data Overview')
            st.dataframe(data)
      
        
        c1,c2 = st.beta_columns((1,1))  
      
    #Average metrics
        if 'floors' or 'id' or 'zipcode' or 'price' or 'sqm_lot' or 'price_m2' or 'sqm_living' or 'lat' or 'long' or 'date' or 'bathrooms' or 'yr_built' or 'bedrooms' or 'sqft_living' or 'sqft_lot' or 'waterfront' or 'view' or 'condition' or 'grade' or 'sqft_above' or 'sqft_basement' or 'yr_renovated'or 'sqft_living15' or 'sqft_lot15' not in data:
            data['floors'] = data1['floors']
            data['id'] = data1['id']
            data['zipcode'] = data1['zipcode']
            data['price'] = data1['price']
            data['sqm_lot'] = data1['sqm_lot']
            data['price_m2'] = data1['price_m2'] 
            data['sqm_living'] = data1['sqm_living']
            data['lat'] = data1['lat']
            data['long'] = data1['long']
            data['date'] = pd.to_datetime(data1['date']).dt.strftime('%Y-%m-%d')
            data['bathrooms'] = data1['bathrooms'] 
            data['yr_renovated'] = data1['yr_renovated']
            data['yr_built'] = data1['yr_built'] 
            data['bedrooms'] = data1['bedrooms']
            data['sqft_living'] = data1['sqft_living']
            data['sqft_living15'] = data1['sqft_living15']
            data['sqft_lot'] = data1['sqft_lot']
            data['sqft_lot15'] = data1['sqft_lot15']
            data['waterfront'] = data1['waterfront']
            data['view'] = data1['view']
            data['condition'] = data1['condition']
            data['grade'] = data1['grade']
            data['sqft_above'] = data1['sqft_above']
            data['sqft_basement'] = data1['sqft_basement']
        
        df1= data[['id','zipcode']].groupby('zipcode').count().reset_index()
        df2= data[['price','zipcode']].groupby('zipcode').mean().reset_index()
        df3= data[['sqm_living','zipcode']].groupby('zipcode').mean().reset_index()
        df4= data[['price_m2','zipcode']].groupby('zipcode').mean().reset_index()
    
    #merge
        m1=pd.merge(df1,df2,on ='zipcode', how='inner')
        m2=pd.merge(m1,df3,on ='zipcode', how='inner')
        df=pd.merge(m2,df4,on ='zipcode', how='inner')
        df.columns =['ZIPCODE','TOTAL HOUSES','PRICE','SQM ','PRICE/M2']
       
    
        c1.header('Average Metrics')
        c1.dataframe(df, height=600)
      
        
         
    
    # Statistcs Descriptive
        
        num_attributes= data.select_dtypes(include=['int64','float64'])
        num_attributes= num_attributes.drop(['id','waterfront','view'],axis=1)
        media= pd.DataFrame(num_attributes.apply(np.mean))
        mediana= pd.DataFrame(num_attributes.apply(np.median))
        std=pd.DataFrame(num_attributes.apply(np.std))
    
        max_= pd.DataFrame(num_attributes.apply(np.max))
        min_= pd.DataFrame(num_attributes.apply(np.min))
    
        df1=pd.concat([max_,min_,media,mediana,std],axis=1).reset_index()
        df1.columns=['attributes','max','min','mean','median','std']
    
        c2.header('Statistcs Descriptive')
        c2.dataframe(df1, height=600)
         
        return None

def portfolio_density(data,geofile):
    if options == 'Densidade de Portfólio': 
        progress=st.progress(0)
        for i in range(100):
            time.sleep(0.5)
            progress.progress(i+1)
    #====================================
    # Densidade de portfólio
    #====================================
        st.markdown("<h1 style='text-align: center; color: black;'>House Rocket Company</h1>", unsafe_allow_html=True)
        st.write('Esta seção é destinada a visualização geográfica do conjunto de dados, fornecendo um olhar sobre a densidade do portfólio e densidade de preço do portfólio.')
        st.title('Region Overview')
        # c1,c2 = st.beta_columns((2))
        st.header('Portfólio Density')
    
    
        
    
    # Base Map = Folium
        density_map=folium.Map(location=[data['lat'].mean(),
                           data['long'].mean()],
                           default_zoom_start=15)
        marker_cluster = MarkerCluster().add_to(density_map)
        for name, row in data.iterrows():
            folium.Marker([row['lat'],row['long']],
                      popup='Sold R${0} on: {1} Sqm Living: {2} Bedrooms: {3} Bathrooms: {4}   Year Built: {5}'.format(
                          row['price'],
                          row['date'],
                          row['sqm_living'],
                          row['bedrooms'],
                          row['bathrooms'],
                          row['yr_built'])).add_to(marker_cluster)
        
        folium_static(density_map)
    
    # Region Price Map
        st.header('Price Density')
    
        df= data[['price','zipcode']].groupby('zipcode').mean().reset_index()
        df.columns= ['ZIP','PRICE']
        
        geofile=geofile[geofile['ZIP'].isin(df['ZIP'].tolist())]
    
        region_price_map= folium.Map(location=[data['lat'].mean(),
                            data['long'].mean()],
                            default_zoom_start=15)
    
        region_price_map.choropleth(data=df,
                                geo_data=geofile,
                                columns=['ZIP','PRICE'],
                                key_on='feature.properties.ZIP',
                                fill_color='YlOrRd',
                                fill_opacity = 0.7,
                                line_opacity = 0.2,
                                legend_name='AVG PRICE')
    
        
        folium_static(region_price_map)
        return None    

def commercial_distribution(data):
    if options == 'Visualização de dados': 
        progress=st.progress(0)
        for i in range(100):
           time.sleep(0.1)
           progress.progress(i+1)
    #====================================
    # Distribuição dos imoveis por categorias comerciais
    #====================================
        st.markdown("<h1 style='text-align: center; color: black;'>House Rocket Company</h1>", unsafe_allow_html=True)
        st.write('Esta seção é destinada a apresentação de Dashboards sobre a relação de alguns atributos do conjunto de dados.')
        st.sidebar.title('Commercial Options')
        st.title('Commercial Attributes')
    
    #-------- Average Price per Year 
    #filters
        min_year_built = int(data["yr_built"].min())
        max_year_built = int(data["yr_built"].max())
    
        st.sidebar.subheader('Select Max Year Built')
        f_year_built= st.sidebar.slider('Year Built', min_year_built,
                                    max_year_built,min_year_built)
        st.header('Average Price per year built')
    #data selection
        df=data.loc[data['yr_built']<f_year_built]
        df=df[['yr_built','price']].groupby('yr_built').mean().reset_index()
    #plot
        fig = px.line(df,x='yr_built',y='price')
        st.plotly_chart(fig, use_cointainer_width=True)
    
    #-------- Average Price per Year 
    #filters
        min_date =datetime.strptime(data['date'].min(),'%Y-%m-%d')
        max_date =datetime.strptime(data['date'].max(),'%Y-%m-%d')
    
        df = data[['date', 'price']].groupby('date').mean().reset_index()
        st.header('Average Price per Year')
        f_date= st.sidebar.slider('Date Avaliable',min_date,max_date,min_date)
    
    #data filtering
        data['date']=pd.to_datetime(data['date'])
        df= data.loc[data['date']<f_date]
        df=df[['date','price']].groupby('date').mean().reset_index()
    #plot
        fig = px.line(df,x='date',y='price')
        st.plotly_chart(fig, use_cointainer_width=True)
    #------------------------ Histograma
        st.header('Price Distributions')
        st.sidebar.subheader('Select Max Price')
    
    #filter 
        min_price = int(data["price"].min())
        max_price = int(data["price"].max())
        avg_price = int(data["price"].mean())
    #data filtering
        f_price=st.sidebar.slider('Price',min_price,max_price,avg_price)
        df= data.loc[data['price'] < f_price]
    #data plot
        fig=px.histogram(df,x='price',nbins=50)
        st.plotly_chart(fig,use_container_width=True)

    return None
def attributes_distribution(data):
    if options == 'Visualização de dados': 
    #====================================
    # Distribuição dos imoveis por categorias fisicas
    #====================================
        st.sidebar.title('Attributes Options')
        st.title('House Attributes')
    # filters 
        f_waterview= st.sidebar.checkbox('Only Houses with water view') 
        c1,c2= st.beta_columns(2)
        c3,c4= st.beta_columns(2)
        if f_waterview:
            df = data[data['waterfront']==1]
            f_bedrooms = st.sidebar.selectbox('Max number of bedrooms', sorted(set(df['bedrooms'].unique())))
            f_bathrooms = st.sidebar.selectbox('Max number of bathrooms',sorted(set(df['bathrooms'].unique())))
            f_floors = st.sidebar.selectbox('Max number of floors',sorted(set(df['floors'].unique())))
        else:
            df= data.copy()
            f_bedrooms = st.sidebar.selectbox('Max number of bedrooms', sorted(set(data['bedrooms'].unique())))
            f_bathrooms = st.sidebar.selectbox('Max number of bathrooms',sorted(set(data['bathrooms'].unique())))
            f_floors = st.sidebar.selectbox('Max number of floors',sorted(set(data['floors'].unique())))
    
    
    
    
    # House per bedrooms
        c1.header('Houses per bedrooms')
        df1=df[df['bedrooms'] <= f_bedrooms]
        fig=px.histogram(df1, x='bedrooms',nbins=20)
        c1.plotly_chart(fig,use_container_width=True)
    # House per bathrooms
        c2.header('Houses per bathrooms')
        df1=df[data['bathrooms'] <= f_bathrooms]
        fig=px.histogram(df1, x='bathrooms',nbins=20)
        c2.plotly_chart(fig,use_container_width=True)
    # House per floors
        c3.header('Houses per floors')
        df1=df[df['floors'] <= f_floors]
        fig=px.histogram(df1, x='floors',nbins=20)
        c3.plotly_chart(fig,use_container_width=True)
    # House per waterview
        fig=px.histogram(df, x='waterfront',nbins=10)
    # c4.header('Houses with waterfront view')
    # c4.plotly_chart(fig,use_container_width=True)   
  
    return None

def  hipoteses (data):
    if options == 'Insights de Mercado':
        progress=st.progress(0)
        for i in range(100):
            time.sleep(0.1)
            progress.progress(i+1)
        #=========================================
        # ========== H1 ==========
        #==========================================        
        
        st.markdown("<h1 style='text-align: center; color: black;'>House Rocket Company</h1>", unsafe_allow_html=True)
        st.write('Esta seção é destinada analise de insights sobre o negócio, verificando a veracidade da hipótese criada com intuito descobrir novas oportunidades para a empresa.')
        st.header('Mas o que são Insights?')
        st.write('Insight é um substantivo com origem no idioma inglês e que significa compreensão súbita de alguma coisa ou determinada situação, o Insight também está relacionado com a capacidade de discernimento, pode ser descrito como uma espécie de epifania. Nos desenhos, o insight é representado com o desenho de uma lâmpada acesa em cima da cabeça do personagem, indicando um momento único de esclarecimento em que se fez luz.')
        st.markdown("<h1 style='text-align: center; color: black;'>Testando Hipóteses de Negócio</h1>", unsafe_allow_html=True)

        c1,c2 = st.beta_columns(2)

        c1.subheader('Hipótese 1:  Imóveis com vista para a água são em média 30% mais caros')
        c1.write('- Falsa, como observado se comparado a média de preços do conjunto de dados, imóveis com vista para a água são em média 300% mais caros.')
        h1 = data[['price', 'waterfront',  'sqft_lot']].groupby('waterfront').mean().reset_index()
        h1['waterfront'] = h1['waterfront'].astype(str)
        fig = px.bar(h1, x='waterfront', y = 'price', color = 'waterfront',  labels={"waterfront": "Visão para água",
                                                                                 "price": "Preço"},
                                                                                  template= 'simple_white')

        fig.update_layout(showlegend = False)
        c1.plotly_chart(fig, use_container_width= True)

        #=========================================
        # ========== H2 ==========
        #==========================================
        c2.subheader('Hipótese 2: Imóveis com data de construção menor que 1955 são em média 50% mais baratos')
        c2.write('- Falsa, como observado imóveis com data de construção anteriores a 1955 são apenas 0.56% mais baratos que a média total dos imóveis.')
        data['construcao'] = data['yr_built'].apply(lambda x: '> 1955' if x > 1955
                                                                   else '< 1955')

        h2 = data[['construcao', 'price',  'sqft_lot']].groupby('construcao').mean().reset_index()

        fig2 = px.bar(h2, x='construcao', y = 'price', color = 'construcao', labels = {"contrucao":"Ano da Construção",
                                                                                   'price': 'Preço'},
                                                                                    template='simple_white')




        fig2.update_layout(showlegend = False)
        c2.plotly_chart(fig2, use_container_width= True)

        #=========================================
        # ========== H3 ==========
        #==========================================
        c3,c4 = st.beta_columns(2)

        c3.subheader('Hipótese 3: Imóveis sem porão possuem área total 40% maiores que os imóveis com porão.')
        c3.write(' - Falsa, como observado imóveis sem porão são 12% maiores que imóveis com porão')
        data['porao'] = data['sqft_basement'].apply(lambda x: 'nao' if x == 0
                                                      else 'sim')

        h3 = data[['porao', 'sqft_lot', 'price']].groupby('porao').sum().reset_index()
        fig3 = px.bar(h3, x='porao', y = 'price', color = 'porao', labels = {'price': 'Preço',
                                                                             'sqft_lot': 'Área Total'},
                                                                            template= 'simple_white')
        fig3.update_layout(showlegend = False)
        c3.plotly_chart(fig3, use_container_width= True)

        #=========================================
        # ========== H4 ==========
        #==========================================
        c4.subheader('Hipótese 4: Imóveis que nunca sofreram reformadas são em média 30% mais baratos')
        c4.write(' - Verdadeira, como observado imóveis que nunca sofreram reformas são 30.21% mais baratos que os imóveis que ja sofreram algum tipo de reforma.')
        data['renovacao'] = data['yr_renovated'].apply(lambda x: 'sim' if x > 0 else
                                                         'nao'   )

        h6 = data[['price', 'renovacao']].groupby('renovacao').mean().reset_index()
        fig4 = px.bar(h6, x='renovacao', y = 'price', color = 'renovacao', labels = {'renovacao':'Renovação',
                                            'price': 'Preço'}, template = 'simple_white')
        fig4.update_layout(showlegend = False)
        c4.plotly_chart(fig4, use_container_width= True)

        #=========================================
        # ========== H5 ==========
        #==========================================
        c5, c6 = st.beta_columns(2)

        c5.subheader('Hipótese 5: Imóveis com mais banheiros são em média 15% mais caros')
        c5.write('Falsa, como observado imóveis com 3 a 5 banheiros são 130% mais caros que imoveis com 0 a 3 banheiros, e imóveis com 3 a 5 banheiros são 35.9% mais caros que imóveis com 5 a 8 banheiros.')
        data['banheiro'] =  data['bathrooms'].apply(lambda x: '0-3' if (x > 0 ) & (x < 3) else
                                                       '3-5' if (x > 3) & (x < 5) else
                                                       '5-8')

        h9 = data[['banheiro', 'price']].groupby('banheiro').mean().reset_index()
        fig7 = px.bar(h9, x = 'banheiro', y = 'price', color = 'banheiro', labels = {'price':'Preço','banheiro':
                                                                                'Quantidade de banheiros'},
                                                                                template= 'simple_white')


        fig7.update_layout(showlegend = False)
        c5.plotly_chart(fig7, use_container_width= True)

        #=========================================
        # ========== H6 ==========
        #==========================================
    

        c6.subheader('Hipótese 6: Imóveis com mais quartos são em média 15% mais caros')
        c6.write('Falsa, como observado imóveis com 6-9 quartos são mais caros sendo,149% mais caros se comparado a imóveis com 0 a 3 quartos, 48.9% mais caros se comparados a imóveis com 3 a 6 quartos e 107% mais caros se comparados a imóveis com 9 a 11 quartos.')
        data['quarto'] =  data['bedrooms'].apply(lambda x: '0-3' if (x > 0 ) & (x < 3) else
                                                       '3-6' if (x > 3) & (x < 6) else
                                                       '6-9' if (x > 6) & (x < 9) else
                                                       '9-11')

        h9 = data[['quarto', 'price']].groupby('quarto').mean().reset_index()
        fig7 = px.bar(h9, x = 'quarto', y = 'price', color = 'quarto', labels = {'price':'Preço','quarto':
                                                                                'Quantidade de quartos'},
                                                                                template= 'simple_white')


        fig7.update_layout(showlegend = False)
        c6.plotly_chart(fig7, use_container_width= True)
    
    
        #=========================================
        # ========== H7 ==========
        #==========================================
    
        st.subheader('Hipótese 7: Imóveis com 3 banheiros tem um crescimento MoM ( Month over Month) de 15%. ')
        
        st.write('- Falsa, como observado o crescimento month over month para imóveis com 3 banheiros atinge uma taxa de 10% e oscila ao longo do ano.')
        c1,c2= st.beta_columns(2)
        asset_info = '''
Lujan Rafael Rezende - House Rocket Company
'''
        def plot_this(df, title, figsize=None, ylabel='',
              bottom_adj=0.25,
              txt_ymin=-0.4, bar=False):
                if bar:
                    ax = df.plot.bar(title=title, figsize=figsize)
                    plt.text(0, txt_ymin, asset_info, transform=ax.transAxes, fontsize=11)
                else:
                    ax = df.plot(title=title, figsize=figsize)
                sns.despine()
                plt.ylabel(ylabel)
                plt.tight_layout()
        
                plt.xticks(rotation=60);
                plt.gcf().subplots_adjust(bottom=bottom_adj)
    
    
        pd.set_option('display.float_format', lambda x: '%.2f' % x) 
        df=pd.DataFrame() 
        data['year']=pd.to_datetime(data['date']).dt.strftime('%Y')
        data['month']=pd.to_datetime(data['date']).dt.strftime('%m')
        data = data.sort_values('month', ascending=1)
        data = data.sort_values('year', ascending=1)

        for i in range(len(data)):
            if data.loc[i,'bathrooms'] == 3:
                df.loc[i,'price'] = data.loc[i,'price']
                df.loc[i,'year']= data.loc[i,'year']
                df.loc[i,'month']= data.loc[i,'month']
        
        df = df.sort_values('month', ascending=1)
        df = df.sort_values('year', ascending=1)  
        df_mom= df[['price','year','month']].groupby(['year','month'])['price'].mean().pct_change()

        fig1=plot_this(df_mom, bar=True, title='Growth Analysis',
          ylabel='Growth Month over Month(%)', txt_ymin=-0.5, bottom_adj=0.25,
          )
        st.set_option('deprecation.showPyplotGlobalUse', False)
        c1.pyplot(fig1)
        fig2=plot_this(df_mom, bar=False, title='Growth Analysis',
          ylabel='Growth Month over Month(%)', txt_ymin=-0.5, bottom_adj=0.25,
          )
        c2.pyplot(fig2)
        
        #=========================================
        # ========== H8 ==========
        #==========================================

        # H4 - O crescimento do preço dos imóveis YoY( Year over Year) é de 10%
        st.subheader('Hipótese 8: O crescimento do preço dos imóveis YoY( Year over Year) é de 10%')
        
        st.write('- Não foi possível chegar a uma conclusão pois o periodo de dados do dataset é de somente um ano, sendo 8 meses em 2014 e 5 meses em 2015, sendo o aconselhado somente para periodos a cima de 2 anos, com os periodos começando e terminando nas mesmas datas por exemplo: de janeiro de ano x até janeiro do ano x+1.')
        h8=pd.to_datetime(data['date']).dt.strftime('%Y-%m')
        
        st.dataframe(h8.sort_values().unique(),height=400)


def house_rocket(df_buy):
    if options == 'Avaliação Imobiliária':
        progress=st.progress(0)
        for i in range(100):
            time.sleep(0.5)
            progress.progress(i+1)
        st.markdown("<h1 style='text-align: center; color: black;'>House Rocket Company</h1>", unsafe_allow_html=True)
        st.write('Como mencionado anteriormente a House Rocket é uma empresa que trabalha com o ramo imobiliário, focada na compra e venda de imóveis, a empresa busca as melhores oportunidades de compra dentro do mercado, para futuramente revender quando o mercado estiver em alta. Diante disto o trabalho do Cientista de dados da empresa é de orientar e propor as melhores alternativas, ajudando assim a empresa encontrar as melhores oportunidades de negócio.')
        st.markdown("<h1 style='text-align: center; color: black;'> Questões de Negócio</h1>", unsafe_allow_html=True)
        st.subheader('Quais são os imóveis que a House Rocket deveria comprar e por qual preço?') 
        st.write('Através do portfólio disponibilizado pela empresa e com base na mediana de preço de cada região e na condição dos imóveis, foram encontradas 10505 imovéis com alto potencial de venda.')
       

#         data['date']=pd.to_datetime(data['date']).dt.strftime('%Y-%m-%d')
#         data['month']= pd.to_datetime(data['date']).dt.strftime('%m').astype(int)
#         data['season']= data['month'].apply(lambda x:'spring' if (x >= 3) & (x< 6)  else
#                                         'summer' if (x >= 6) & (x < 9) else
#                                         'fall' if (x >= 9) & (x < 12) else 'winter')
        df_buy2= data[['price','zipcode']].groupby('zipcode').median().reset_index()
        data2=data1.copy()
        for i in range(len(data2)):
            for n in range(len(df_buy2)):
                if data2.loc[i,'zipcode'] == df_buy2.loc[n,'zipcode']:
                    data2.loc[i,'price_median']= df_buy2.loc[n,'price']
            if data2.loc[i,'price'] < data2.loc[i,'price_median']:
                if data2.loc[i,'condition']>=3:
                    data2.loc[i,'status']= 'Buy'
            else:
                data2.loc[i,'status']= 'Not Buy' 
            
#             if data.loc[i,'price'] > data.loc[i,'price_median']:
#                 data.loc[i,'status']= 'Not Buy'   
#         df_season= data[['date','month','price','season','zipcode']].groupby(['season','zipcode']).median().reset_index()  
#         df_buy=data[data['status']=='Buy'].reset_index()
#         df_buy=df_buy[['id','date','month','season','status','zipcode','price']]
#         df_buy.columns=['id','date','month','season','status','zipcode','buy_price']
#         for i in range(len(df_buy)):
#             for n in range(len(df_season)):
#                 if df_buy.loc[i,'zipcode'] == df_season.loc[n,'zipcode']:
#                     if df_season.loc[n,'season']== 'spring':
#                         if df_buy.loc[i,'buy_price']< df_season.loc[n,'price']:
#                             df_buy.loc[i,'spring_price']= df_buy.loc[i,'buy_price'] + (df_buy.loc[i,'buy_price']*0.3)
#                         else:
#                             df_buy.loc[i,'spring_price']= df_buy.loc[i,'buy_price'] + (df_buy.loc[i,'buy_price']*0.1)      
#                     if df_season.loc[n,'season']== 'summer':
#                         if df_buy.loc[i,'buy_price']< df_season.loc[n,'price']:
#                             df_buy.loc[i,'summer_price']= df_buy.loc[i,'buy_price'] + (df_buy.loc[i,'buy_price']*0.3)
#                         else:
#                             df_buy.loc[i,'summer_price']= df_buy.loc[i,'buy_price'] + (df_buy.loc[i,'buy_price']*0.1)       
#                     if df_season.loc[n,'season']== 'fall':
#                         if df_buy.loc[i,'buy_price']< df_season.loc[n,'price']:
#                             df_buy.loc[i,'fall_price']= df_buy.loc[i,'buy_price'] + (df_buy.loc[i,'buy_price']*0.3)
#                         else:
#                             df_buy.loc[i,'fall_price']= df_buy.loc[i,'buy_price'] + (df_buy.loc[i,'buy_price']*0.1)
#                         if df_season.loc[n,'season']== 'winter':
#                             if df_buy.loc[i,'buy_price']< df_season.loc[n,'price']:
#                                 df_buy.loc[i,'winter_price']= df_buy.loc[i,'buy_price'] + (df_buy.loc[i,'buy_price']*0.3)
#                         else:
#                             df_buy.loc[i,'winter_price']= df_buy.loc[i,'buy_price'] + (df_buy.loc[i,'buy_price']*0.1)        
        
#         df_buy['best_price']=df_buy.loc[:,['fall_price','spring_price','summer_price','winter_price']].max(1)
#         df_buy['Profit']= df_buy['best_price']-df_buy['buy_price']
#         df_buy['best_season_to_sell'] = df_buy.apply(lambda x:'summer,spring,fall,winter' if (x['best_price'] == x['summer_price']) & (x['best_price']==x['winter_price']) & (x['best_price']==x['spring_price']) & (x['best_price']==x['fall_price']) else
# 'summer,spring,winter' if (x['best_price'] == x['summer_price']) & (x['best_price']==x['winter_price']) & (x['best_price']==x['spring_price']) else
# 'winter,spring,fall' if (x['best_price'] == x['winter_price']) & (x['best_price']==x['fall_price']) & (x['best_price']==x['spring_price']) else                                             
# 'summer,winter,fall' if (x['best_price'] == x['summer_price']) & (x['best_price']==x['fall_price']) & (x['best_price']==x['winter_price']) else
# 'summer,spring,fall' if (x['best_price']== x['summer_price']) & (x['best_price']==x['fall_price']) & (x['best_price']==x['spring_price']) else
#  'spring,winter' if (x['best_price'] == x['spring_price']) & (x['best_price']==x['winter_price']) else
#  'spring,fall' if (x['best_price']== x['spring_price']) & (x['best_price']==x['fall_price']) else
#  'summer,winter' if (x['best_price'] == x['summer_price']) & (x['best_price']==x['winter_price']) else
#  'summer,fall' if (x['best_price']== x['summer_price']) & (x['best_price']==x['fall_price']) else
#  'summer,spring' if (x['best_price'] == x['summer_price']) & (x['best_price']==x['spring_price']) else
#  'spring' if x['best_price'] == x['spring_price'] else
# 'summer' if x['best_price'] == x['summer_price'] else
# 'fall'   if x['best_price'] == x['fall_price'] else 'winter', axis=1)
       #  df_buy.columns = ['id', 'date', 'month', 'season', 'status', 'zipcode', 'buy_price (U$)',
       # 'fall_price (U$)', 'spring_price (U$)', 'summer_price (U$)', 'winter_price (U$)',
       # 'best_price (U$)', 'Profit (U$)', 'best_season_to_sell']

            
        if st.checkbox('Mostrar o mapa de compra de imóveis'):
            for i, row in data2.iterrows():
                if (row['status'] == 'Buy'):
                    data2.loc[i,'marker_color'] = 'green'
                else:
                    data2.loc[i, 'marker_color'] = 'red'
            ############################################
            st.markdown('Mapa - Indicação de potenciais imóveis que se comprados podem gerar lucro para a empresa.')
            # st.markdown("""
            # <style>
            # .big-font {
            #     font-size:14px !important;
            # }
            # </style>
            # """, unsafe_allow_html=True)
        
            st.markdown('<p class="big-font"> Em verde os imóveis com alto potencial de venda '
                        '  <br> Em vermelho os imóveis com baixo potencial de venda </p>', unsafe_allow_html=True)
    
            mapa = folium.Map(width = 600, height = 300,
                                  location = [data2['lat'].mean(),data2[ 'long'].mean()],
                                  default_zoom_start=30)
            features = {}
            for row in pd.unique(data2['marker_color']):
                features[row] = folium.FeatureGroup(name=row)
            for index, row in data2.iterrows():
                circ = folium.Circle([row['lat'], row['long']],
                        radius=150, color=row['marker_color'], fill_color=row['marker_color'],
                        fill_opacity = 1, popup= 'Compra: {0}, Preço: {1}'.format(row['status'],
                                          row['price']))
                circ.add_to(features[row['marker_color']])
            
            for row in pd.unique(data2["marker_color"]):
                features[row].add_to(mapa)
            
            folium.LayerControl().add_to(mapa)
            folium_static(mapa)
       
        st.subheader('Uma vez o imóvel comprado, qual o melhor momento para vende-lo? e por qual preço?')   
        st.write('Para a venda dos imóveis comprados, foi analisado o comportamento dos preços para o ano anterior, buscando qual seria a melhor estação do ano para vender o imóvel, para isso foi realizado a mediana dos preços para cada região durante cada estação do ano, diante disso se o preço pelo qual o imóvel foi comprado fosse menor que a mediana da estação o imóvel seria vendido pelo preço que foi comprado +30%, e caso o preço de aquisição fosse maior que a mediana de estação o valor de venda seria o valor da compra + 10%.')
        st.write('Ao final foi disponibilizado uma tabela para a equipe de negócios, com todos os dados referentes a venda dos imóveis, incluindo o lucro esperado em quais estações vender o determinado imóvel.')
        if st.checkbox('Mostrar a tabela de vendas'):
            df_buy=df_buy.drop(['month','status'],axis=1) 
            info={'id':'Número de identificação do imóvel','date':'Data da compra','season':'Estação da compra do imóvel','zipcode':'Zipcode do ímóvel','buy_price':'Preço pelo qual o imóvel foi comprado','fall_price':'Preço para se vender o imóvel no outono','spring_price':'Preço para se vender imóvel na primavera','summer_price':'Preço para se vender o imóvel no verão','winter_price':'Preço para se vender o imóvel no inverno','best_price':'Melhor preço para se vender o imóvel dentre todas as estações','Profit':'Lucro esperado pela venda do imóvel','best_season_to_sell':'As melhores estações para se vender o imóvel'}
            info=pd.Series(info).to_frame('Explicação dos Atributos')
            st.table(info)
            st.dataframe(df_buy)
        
        st.markdown("<h1 style='text-align: center; color: black;'> Sugestão de compra de imóveis</h1>", unsafe_allow_html=True)
        st.write('Após a analise de melhor periodo para vende o Cientista de dados elencou os 20 imóveis mais lucrativos e sugeriu que a empresa devesse adquiri-los.')
        df=df_buy.sort_values('Profit',ascending=0).reset_index()
        df=df_buy.head(20)
        dic={"Investimento Inicial":df['buy_price'].sum(),'Lucro Esperado':df['Profit'].sum()}
        capital=pd.Series(dic).to_frame('Valor USD')
        st.table(capital)
        if st.checkbox('Mostrar a tabela de imóveis sugeridos'):
            df=df.sort_values('Profit',ascending=0).reset_index()
            st.dataframe(df)
            
        return None
    
if __name__ =='__main__':
    #ETL
    # Data Extraction
    path = 'kc_house_data.csv'
    path2= 'Df_buy.csv'
    url = 'https://opendata.arcgis.com/datasets/83fc2e72903343aabff6de8cb445b81c_2.geojson'
    data = get_data(path)
    data1 = get_data(path)
    geofile = get_geofile(url)
    df_buy=get_df_buy(path2)
    
    # Transformation
    data = set_feature(data)
    overview_data(data)
    portfolio_density(data,geofile)
    commercial_distribution(data)
    attributes_distribution(data)
    data = get_data(path)
    # business_question(data)
    hipoteses (data)
    data = get_data(path)
    
    house_rocket(df_buy)
    # Load












