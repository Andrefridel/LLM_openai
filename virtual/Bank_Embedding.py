import openai
import pinecone
import yaml
import os
from pinecone import ServerlessSpec

class AIEmbeddingManager:
    def __init__(self, config_path, index_name='nlp'):
        with open(config_path, 'r') as config_file:
            config = yaml.safe_load(config_file)

        os.environ['PINECONE_API_KEY'] = config['PINECONE_API_KEY']
        openai.api_key = config['OPENAI_API_KEY']

        self.pinecone_client = pinecone.Pinecone(
            api_key=os.environ.get('PINECONE_API_KEY')
        )
        self.index_name = index_name

    def criar_indice(self, dimension=1536, metric='cosine', cloud='aws', region='us-east-1'):
        if self.index_name not in self.pinecone_client.list_indexes().names():
            try:
                self.pinecone_client.create_index(
                    name=self.index_name,
                    dimension=dimension,
                    metric=metric,
                    spec=ServerlessSpec(cloud=cloud, region=region)
                )
                print(f"O índice '{self.index_name}' foi criado com sucesso.")
            except pinecone.exceptions.PineconeApiException as e:
                print(f"Erro ao criar o índice: {e}. Continuando...")
        else:
            print(f"O índice '{self.index_name}' já existe. Continuando...")

        self.index = self.pinecone_client.Index(self.index_name)

    def gerar_embedding(self, texto):
        response = openai.Embedding.create(
            model="text-embedding-ada-002",
            input=texto
        )
        embedding = response['data'][0]['embedding']
        return embedding

    def inserir_atualizar_embedding(self, texto, id_unico):
        embedding = self.gerar_embedding(texto)
        self.index.upsert([(id_unico, embedding)])
        print(f"Embedding inserido ou atualizado com sucesso para o ID: {id_unico}")

    def deletar_embedding(self, id_unico):
        self.index.delete(ids=[id_unico])
        print(f"Embedding com ID {id_unico} deletado com sucesso")

    def acessar_embedding(self, id_unico):
        result = self.index.fetch([id_unico])
        if result:
            embedding = result['vectors'][id_unico]['values']
            print(f"Embedding recuperado para o ID {id_unico}: {embedding}")
            return embedding
        else:
            print(f"Embedding com ID {id_unico} não encontrado.")
            return None

    def calcular_similaridade(self, query_texto, top_k=3):
        query_embedding = self.gerar_embedding(query_texto)
        resultados = self.index.query(queries=[query_embedding], top_k=top_k)
        print("Embeddings mais semelhantes encontrados:")
        for match in resultados['matches']:
            print(f"ID: {match['id']}, Similaridade: {match['score']}")

if __name__ == "__main__":
    yaml_path = 'C:\\projectAI\\projetoIA\\config.yaml'
    manager = AIEmbeddingManager(yaml_path)
    
    manager.criar_indice(dimension=1536, metric='cosine', cloud='aws', region='us-east-1')
    
    texto = "Exemplos de texto para gerar um embedding novamente numero 2."
    id_unico = "exemplo_001"
    
    # manager.inserir_atualizar_embedding(texto, id_unico)
    
    manager.acessar_embedding(id_unico)

    # manager.deletar_embedding(id_unico)
