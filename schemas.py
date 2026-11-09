from pydantic import BaseModel, Field

class PredictInput(BaseModel):
    idade: int = Field(..., ge=18, le=120, description="Idade do solicitante de crédito em anos.", json_schema_extra={"example": 35})
    renda_anual: float = Field(..., gt=0, description="Renda bruta anual do solicitante.", json_schema_extra={"example": 55000.0})
    historico_inadimplencia: int = Field(..., ge=0, le=1, description="Possui histórico de inadimplência? (1 para sim, 0 para não)", json_schema_extra={"example": 0})
    score_credito: int = Field(..., ge=300, le=850, description="Score de crédito do solicitante (Serasa/SPC)", json_schema_extra={"example": 720})

class PredictOutput(BaseModel):
    inadimplente_predito: int = Field(..., description="Predição final do modelo (1 para inadimplente, 0 para bom pagador).")
    probabilidade: float = Field(..., description="Probabilidade estimada do evento de inadimplência.")
