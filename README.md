# Sistema de Integração e Avaliação de LLMs

## Visão Geral

Esta aplicação Python conecta-se às APIs do ChatGPT e Gemini para gerar, avaliar e apresentar resultados. A aplicação utiliza vários padrões de projeto, incluindo Factory, Command, Strategy e Observer, para oferecer uma experiência robusta, modular e amigável ao usuário.

## Funcionalidades

1. **Integração com APIs**:
   - Conecta-se ao ChatGPT e a outro LLM (ex: Gemini).
   - Utiliza o padrão Factory para abstrair a criação de conexões com APIs.

2. **Interface de Linha de Comando (CLI)**:
   - Permite aos usuários enviar perguntas para os modelos.
   - Utiliza o padrão Command para encapsular solicitações.

3. **Processamento de Respostas**:
   - Avalia respostas utilizando algoritmos baseados no padrão Strategy.
   - Suporta diferentes estratégias de avaliação (ex: contagem de palavras, presença de palavras-chave).

4. **Apresentação dos Resultados**:
   - Exibe resultados com explicações.
   - Utiliza o padrão Observer para notificar os usuários sobre mudanças.

## Instalação

### Pré-requisitos

- Python 3.8+
- Bibliotecas necessárias (veja `requirements.txt`)

### Configuração

1. **Clone o repositório**:

    ```bash
    git clone https://github.com/owhenrique/llm-integration.git
    cd llm-integration
    ```

2. **Instale as dependências**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure o arquivo de configuração**:

    Crie um arquivo `config.ini` no diretório raiz com o seguinte conteúdo:

    ```ini
    [API_KEYS]
    GEMINI_API_KEY = sua_chave_api_gemini
    CHATGPT_API_KEY = sua_chave_api_chatgpt
    ```

## Uso

### Interface de Linha de Comando

Para enviar uma pergunta aos modelos e avaliar as respostas:

1. **Usando a estratégia de contagem de palavras**:

    ```bash
    python main.py "Qual é a diferença entre IA e aprendizado de máquina?"
    ```

2. **Usando a estratégia de presença de palavras-chave**:

    ```bash
    python main.py "Explique o aprendizado profundo." --strategy keyword_presence --keywords "aprendizado profundo" "redes neurais"
    ```

### Estratégias Disponíveis

- **word_count**: Avalia com base no número de palavras na resposta.
- **keyword_presence**: Avalia com base na presença de palavras-chave especificadas.

## Estrutura do Código

- `LLM_interface.py`: Define a interface abstrata para modelos de linguagem.
- `LLM_factory.py`: Implementa métodos de fábrica para criar instâncias de LLM.
- `api_chatgpt.py`: Contém a implementação para a API do ChatGPT.
- `api_gemini.py`: Contém a implementação para a API do Gemini.
- `cli.py`: Gerencia a interface de linha de comando.
- `command.py`:
- `evaluation_strategy.py`:
- `strategies.py`: Define estratégias de avaliação (padrão Strategy).
- `observer.py`: Implementa o padrão Observer para notificação de resultados.
- `main.py`: O ponto de entrada da aplicação.

## Testes

1. **Executar testes**:

    ```bash
    pytest
    ```

2. **Cobertura**:

    Para verificar a cobertura do código, use:

    ```bash
    pytest --cov=src
    ```

## Contribuindo

1. Faça um fork do repositório.
2. Crie uma nova branch (`git checkout -b feature/SuaFeature`).
3. Faça commit das suas alterações (`git commit -am 'feat:Adicionar nova feature'`).
4. Envie para a branch (`git push origin feature/SuaFeature`).
5. Crie um novo Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
