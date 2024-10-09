# Documentação: Gerador de Relatórios Jornalísticos Baseados em Dados

## Descrição Geral
Este script é uma aplicação interativa desenvolvida com **Streamlit** que utiliza o modelo de linguagem **ChatOpenAI** para gerar relatórios jornalísticos detalhados e personalizados com base em dados fornecidos. A ferramenta oferece uma interface intuitiva para selecionar parâmetros como empresa, período, idioma e foco da análise, e possibilita a criação de relatórios em formato **markdown** com insights baseados em tendências de dados jornalísticos.

## Funcionalidades
1. **Entrada do Usuário**:
   - Seleção da empresa jornalística a ser analisada.
   - Definição do trimestre e ano para a análise.
   - Escolha do idioma para o relatório gerado.
   - Definição do foco da análise, com várias opções pré-definidas.
   - Campo de texto para o usuário adicionar perguntas ou observações adicionais.

2. **Geração do Relatório**:
   - O relatório é gerado automaticamente ao pressionar o botão "Gerar Relatório", utilizando os parâmetros selecionados.
   - A análise é personalizada para a empresa, período, idioma e foco definidos, com a opção de incluir perguntas do usuário.

3. **Resposta do Modelo**:
   - Ao clicar em "Enviar Observação", o modelo processa as perguntas ou observações do usuário e gera uma resposta baseada nos dados inseridos.

## Detalhes Técnicos
- **Bibliotecas Utilizadas**:
  - `streamlit`: Utilizada para criar a interface web interativa.
  - `langchain_openai`: Biblioteca que facilita a integração com a API do OpenAI.
  - `os` e `yaml`: Usadas para carregar e configurar a chave de API do OpenAI a partir de um arquivo de configuração (`config.yaml`).

- **Configuração**:
  - A chave da API OpenAI é carregada de um arquivo `config.yaml` e configurada no ambiente com `os.environ`.

- **Modelo OpenAI**:
  - O script utiliza o modelo **gpt-3.5-turbo** com uma temperatura de 0, configurado para gerar respostas consistentes e baseadas em fatos.

## Uso
O usuário interage com a interface via **sidebar** para selecionar a empresa, período e foco da análise. Após a seleção, o relatório é gerado com base nessas entradas, e o usuário pode adicionar perguntas ou observações para refinar o conteúdo.




## Visualizar PDF
Para visualizar o PDF, acesse [este link para o relatório](https://github.com/Andrefridel/LLM_openai/blob/main/virtual/LLM/VIRTUAL/aplicacao.pdf).
