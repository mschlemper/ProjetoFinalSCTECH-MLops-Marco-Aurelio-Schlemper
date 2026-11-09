[README.md](https://github.com/user-attachments/files/34587201/README.md)
# API de Análise Preditiva de Risco de Crédito (Score de Crédito)

Este repositório contém a implementação completa de um microsserviço assíncrono baseado em **FastAPI** para disponibilização de um modelo preditivo de Machine Learning treinado para a classificação e análise de risco/score de crédito.

Este projeto foi desenvolvido como requisito obrigatório para o **Projeto Avaliativo do Módulo 2 (Semana 13)** da disciplina de Desenvolvimento de IA para Análise Preditiva.

---

## 1. Problema de Negócio e Objetivo do Sistema

No setor financeiro, a velocidade e a precisão no processo de concessão de crédito são determinantes. O objetivo desta API é analisar dados cadastrais e financeiros básicos de um cliente em tempo real para predizer se ele apresenta alto risco de inadimplência (`inadimplente_predito = 1`) ou baixo risco (`inadimplente_predito = 0`).

O modelo preditivo analisa de forma combinada variáveis como **idade**, **renda anual**, **score de crédito** e **histórico prévio de inadimplência**.

---

## 2. Tecnologias Utilizadas

*   **Python 3.10+**
*   **FastAPI**: Framework web assíncrono moderno e de alto desempenho.
*   **Pydantic (v2)**: Validação e tipagem de dados estrita em tempo de execução.
*   **Scikit-Learn**: Treinamento do pipeline offline (`StandardScaler`, `SimpleImputer` e `RandomForestClassifier`).
*   **Joblib**: Serialização e desserialização eficiente do pipeline preditivo.
*   **Uvicorn**: Servidor web ASGI para execução de alta performance.
*   **Pandas & NumPy**: Pré-processamento e manipulação dos conjuntos de dados.

---

## 3. Estrutura Modular da API

A arquitetura do projeto segue um padrão desacoplado em camadas para facilitar a manutenção e escalabilidade:

```text
├── models/
│   └── credit_model.joblib      # Pipeline completo serializado (Fase 1)
├── app/
│   ├── __init__.py
│   ├── main.py                  # Ponto de entrada, configuração do ciclo de vida Lifespan (Fase 3)
│   ├── schemas.py               # Modelos Pydantic de entrada e saída (Fase 4)
│   ├── routers.py               # Endpoints da aplicação (/health e /predict) (Fase 5)
│   └── services.py              # Inicialização do modelo em memória RAM (Services)
├── requirements.txt             # Dependências determinísticas para reprodutibilidade
└── README.md                    # Esta documentação
```

---

## 4. Instruções de Instalação e Execução Local

Siga o passo a passo abaixo para rodar a aplicação localmente no seu computador:

### Passo 1: Clonar o repositório e acessar a pasta
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### Passo 2: Criar e ativar um ambiente virtual (venv)
No Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```
No Linux/macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

### Passo 3: Instalar as dependências necessárias
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Passo 4: Executar a API com o Uvicorn
```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Após o início do servidor, a API estará acessível em `http://127.0.0.1:8000`.

---

## 5. Documentação e Teste dos Endpoints

A documentação interativa oficial gerada automaticamente pelo FastAPI estará disponível em:
*   **Swagger UI**: `http://127.0.0.1:8000/docs`
*   **ReDoc**: `http://127.0.0.1:8000/redoc`

### 5.1 Endpoint de Saúde: `GET /health`
Rota de checagem que valida se a API está ativa e se o modelo do classificador reside corretamente na memória RAM.

**Exemplo de Resposta (Status `200 OK`):**
```json
{
  "status": "healthy",
  "model_loaded": true,
  "model_path": "models/credit_model.joblib"
}
```

### 5.2 Endpoint de Inferência Preditiva: `POST /predict`

#### Exemplo 1: Payload de Entrada Válido

**Requisição (`POST /predict`):**
```json
{
  "idade": 35,
  "renda_anual": 55000.0,
  "historico_inadimplencia": 0,
  "score_credito": 720
}
```

**Resposta Esperada (Status `200 OK`):**
```json
{
  "inadimplente_predito": 0,
  "probabilidade": 1.0
}
```

#### Exemplo 2: Payload de Entrada Inválido (Erro do Pydantic)
Idade informada como menor que `18` (regra mínima de negócio definida no Schema do Pydantic).

**Requisição (`POST /predict`):**
```json
{
  "idade": 12,
  "renda_anual": 25000.0,
  "historico_inadimplencia": 0,
  "score_credito": 600
}
```

**Resposta Esperada (Status `422 Unprocessable Entity`):**
```json
{
  "detail": [
    {
      "type": "greater_than_equal",
      "loc": [
        "body",
        "idade"
      ],
      "msg": "Input should be greater than or equal to 18",
      "input": 12,
      "ctx": {
        "ge": 18
      }
    }
  ]
}
```

---

## 6. Links de Evidências (Entrega)

*   **Link do Repositório GitHub**: `https://github.com/seu-usuario/seu-repositorio` *(Substitua pelo seu link público)*
*   **Link da Vídeo-Apresentação (Google Drive)**: `https://drive.google.com/open?id=seu-link-de-compartilhamento` *(Substitua pelo seu link em modo leitor)*
