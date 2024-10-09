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
Para visualizar o PDF, acesse [este link para o relatório](aplicacao.pdf).





---



### Documentação Resumida: Módulo **Bank_Embedding**

#### Descrição Geral
O módulo **Bank_Embedding** é uma aplicação desenvolvida em Python que tem como objetivo gerenciar embeddings de textos , utilizando a API **OpenAI** para gerar embeddings e o serviço **Pinecone** para armazená-los e acessá-los. O módulo permite criar, inserir, atualizar, deletar e consultar embeddings de textos financeiros, além de calcular a similaridade entre esses textos para facilitar a análise e a busca de informações relevantes.

#### Funcionalidades
1. **Criação de Índices no Pinecone**:
   - Cria um índice de embeddings no Pinecone com especificações definidas pelo usuário (dimensões, métrica de similaridade, e nuvem/ região).

2. **Geração de Embeddings**:
   - Gera embeddings a partir de textos fornecidos, utilizando o modelo **text-embedding-ada-002** da OpenAI, especializado em análise de texto.

3. **Inserção/Atualização de Embeddings**:
   - Insere ou atualiza embeddings gerados no índice Pinecone associado, identificando-os por um **ID único**.

4. **Deleção de Embeddings**:
   - Remove embeddings do índice no Pinecone, utilizando o **ID único** associado.

5. **Acesso a Embeddings**:
   - Recupera embeddings específicos de um índice, permitindo a análise ou reuso de embeddings armazenados anteriormente.

6. **Cálculo de Similaridade**:
   - Calcula a similaridade entre um embedding de texto de consulta e os embeddings armazenados no índice, retornando os resultados mais próximos.

#### Arquitetura
- **openai**: Biblioteca usada para gerar os embeddings de texto.
- **pinecone**: Serviço utilizado para armazenamento e busca dos embeddings.
- **yaml**: Usado para carregar configurações de chaves de API a partir de um arquivo YAML.
- **os**: Para gerenciar variáveis de ambiente, como as chaves de API.

#### Fluxo de Funcionamento
1. **Configuração**: O arquivo de configuração (`config.yaml`) contém as chaves da API do Pinecone e OpenAI. Essas chaves são carregadas no ambiente de execução.
   
2. **Criação do Índice**: Um índice de embeddings é criado no Pinecone, caso ainda não exista, com base em especificações de dimensão e métrica de similaridade definidas.
   
3. **Geração de Embedding**: O texto fornecido pelo usuário é processado pelo modelo OpenAI para gerar seu embedding.

4. **Inserção/Atualização no Índice**: O embedding gerado é inserido no índice Pinecone associado, identificado por um **ID único**.

5. **Consulta de Embeddings**: Através de um **ID único**, é possível recuperar um embedding específico do índice para análise.

6. **Cálculo de Similaridade**: A similaridade entre o embedding de uma consulta e os armazenados é calculada, e os resultados mais semelhantes são retornados.

#### Conclusão
O módulo **Bank_Embedding** fornece uma solução eficiente para gerenciar e consultar embeddings financeiros, facilitando a análise de semelhança entre textos e a organização de grandes volumes de dados relacionados ao setor financeiro.


## Visualizar PDF
Para visualizar o PDF, acesse [este link para o relatório](picone.pdf).

--- 

Essa documentação apresenta uma visão geral e resumida do funcionamento do módulo **Bank_Embedding**, cobrindo seus principais componentes e fluxos de uso.
