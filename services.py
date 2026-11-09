import os
import joblib

# Container que guardará o modelo na memória RAM
ml_models = {}

def carregar_modelo():
    model_file = 'models/credit_model.joblib'
    if not os.path.exists(model_file):
        raise FileNotFoundError(f"O artefato do modelo não foi localizado em {model_file}")
    
    print("[LIFESPAN] Carregando o pipeline do modelo de Machine Learning para a memória RAM...")
    ml_models["credit_pipeline"] = joblib.load(model_file)
    print("[LIFESPAN] Modelo pronto para inferência.")

def limpar_modelo():
    print("[LIFESPAN] Limpando memória cache operacional...")
    ml_models.clear()

def obter_pipeline():
    return ml_models.get("credit_pipeline")
