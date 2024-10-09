import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
import os
import yaml

with open('config.yaml', "r") as config_file:
    config = yaml.safe_load(config_file)
os.environ['OPENAI_API_KEY'] = config['OPENAI_API_KEY']

chat_openai = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0)

template = '''
Você é um analista de dados jornalísticos.
Escreva um relatório jornalístico detalhado para a empresa "{empresa}" para o período {periodo}.
O relatório deverá ser escrito em {idioma} e incluir a seguinte análise:
{analise}

Forneça insights e conclusões para esta seção.
Formate o relatório utilizando o markdown.
'''

prompt_template = PromptTemplate(template=template)

empresas = ['Rede Globo', 'Portal da Transparência do Governo Federal (Brasil)', 'IBGE', 'Folha de S. Paulo', 'Agência Pública'] 
trimestres = ['Q1', 'Q2', 'Q3', 'Q4']
anos = [2021, 2022, 2023, 2024]
idiomas = ['Português', 'Inglês', 'Espanhol', 'Francês', 'Alemão', 'Chinês']
analises = [
    "Análise do impacto dos dados nas manchetes",
    "Análise de temas emergentes com potencial para gerar reportagens especiais ou séries investigativas",
    "Análise de previsões para coberturas de eventos futuros com base em dados históricos",
    "Análise de Cobertura de tendências com base em big data",
    "Análise da evolução dos dados no jornalismo digital",
    "Análise das previsões baseadas em dados para notícias",
    "Análise do Impacto dos Dados nas Manchetes Relacionadas às Eleições"
]

st.title('Gerador de Relatório de Tendências Jornalísticas Baseadas em Dados:')

empresa = st.sidebar.selectbox('Selecione a empresa:', empresas)
trimestre = st.sidebar.selectbox('Selecione o trimestre:', trimestres)
ano = st.sidebar.selectbox('Selecione o ano:', anos)
periodo = f"{trimestre} {ano}"
idioma = st.sidebar.select_slider('Selecione o idioma:', idiomas)
analise = st.sidebar.selectbox('Selecione o foco da análise', analises)

# Campo para o usuário digitar uma pergunta ou observação
pergunta_usuario = st.text_area("Digite sua pergunta ou observação:")

if st.sidebar.button('Gerar Relatório'):
    # Formatar a análise com base na entrada do usuário
    prompt = prompt_template.format(
        empresa=empresa,
        periodo=periodo,
        idioma=idioma,
        analise=analise,
    )
    
    # Adiciona a pergunta do usuário ao prompt
    if pergunta_usuario:
        prompt += f"\n\nAlém disso, aqui está uma pergunta do usuário: {pergunta_usuario}"
    
    response = chat_openai.invoke(prompt)
    
    st.subheader('Relatório Gerado:')
    st.write(response.content)

# Mover o botão para baixo do espaço onde o usuário digita
if st.button('Enviar Observação'):
    if pergunta_usuario:
        # Formatar o prompt com a observação do usuário
        prompt = prompt_template.format(
            empresa=empresa,
            periodo=periodo,
            idioma=idioma,
            analise=analise,
        )
        
        # Invocar o modelo com o prompt formatado
        response = chat_openai.invoke(prompt)
        
        st.subheader('Resposta do Modelo:')
        st.write(response.content)
    else:
        st.warning("Por favor, digite uma observação antes de enviar.")
