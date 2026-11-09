import pandas as pd
from fastapi import APIRouter, HTTPException, status
from app.schemas import PredictInput, PredictOutput
from app.services import obter_pipeline

router = APIRouter()

@router.get("/health", tags=["Monitoramento"])
async def health_check():
    pipeline = obter_pipeline()
    if not pipeline:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Modelo preditivo não carregado na memória ou corrompido."
        )
    return {
        "status": "healthy",
        "model_loaded": True,
        "model_path": "models/credit_model.joblib"
    }

@router.post("/predict", response_model=PredictOutput, tags=["Inferência"])
async def predict(payload: PredictInput):
    try:
        pipeline = obter_pipeline()
        if not pipeline:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="O modelo não está instanciado na memória."
            )
        
        # Converter o payload validado em DataFrame estruturado
        input_data = pd.DataFrame([payload.model_dump()])
        
        # Executar inferências
        prediction = int(pipeline.predict(input_data)[0])
        probabilities = pipeline.predict_proba(input_data)[0]
        confidence = float(probabilities[prediction])
        
        return PredictOutput(
            inadimplente_predito=prediction,
            probabilidade=confidence
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Ocorreu uma inconsistência no processamento: {str(e)}"
        )
