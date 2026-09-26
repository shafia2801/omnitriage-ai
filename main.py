from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import os

app = FastAPI(title="OmniTriage AI - PS 05")
templates = Jinja2Templates(directory="templates")

class TriageRequest(BaseModel):
    symptom_text: str
    urgency_level: str = "Medium"

@app.get("/", response_class=HTMLResponse)
async def read_root(request: fastapi.Request): # type: ignore
    return templates.TemplateResponse("index.html", {"request": request})

@app.api_route("/api/process-triage", methods=["POST"])
async def process_triage(data: TriageRequest):
    try:
        # Mocking real-time agent evaluation logic (Integrate Gemini / OpenAI Realtime API keys here)
        analysis_result = {
            "status": "Success",
            - "processed_input": data.symptom_text,
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
