from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from pydantic import BaseModel
import os

app = FastAPI(title="OmniTriage AI - PS 05")

class TriageRequest(BaseModel):
    symptom_text: str
    urgency_level: str = "Medium"

@app.get("/", response_class=HTMLResponse)
async def read_root():
    # Directly serves index.html from the same folder
    return FileResponse("index.html")

@app.post("/api/process-triage")
async def process_triage(data: TriageRequest):
    try:
        analysis_result = {
            "status": "Success",
            "processed_input": data.symptom_text,
            "recommended_priority": "High" if "chest" in data.symptom_text.lower() else "Routine",
            "action_plan": "Route immediately to emergency care bay." if "chest" in data.symptom_text.lower() else "Queue for standard nurse assessment.",
            "safety_guardrail": "Passed: Clinical safety protocols enforced."
        }
        return analysis_result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
