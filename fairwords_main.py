"""
FairWords Backend API
Bias detection service using rule-based pattern matching
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fairwords_analyzer import BiasAnalyzer

app = FastAPI(
    title="FairWords API",
    description="Job description bias analyzer using research-backed pattern detection",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize analyzer
analyzer = BiasAnalyzer()


class AnalysisRequest(BaseModel):
    text: str


@app.get("/")
def read_root():
    return {
        "message": "FairWords API - Root-cause bias detection",
        "version": "1.0.0",
        "philosophy": "People first. Potential always. Context matters."
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "patterns_loaded": len(analyzer.patterns)
    }


@app.post("/analyze")
def analyze_text(request: AnalysisRequest):
    try:
        if not request.text or len(request.text.strip()) == 0:
            raise HTTPException(status_code=400, detail="Text cannot be empty")
        
        if len(request.text) > 50000:
            raise HTTPException(status_code=400, detail="Text too long")
        
        results = analyzer.analyze(request.text)
        
        if "error" in results:
            raise HTTPException(status_code=400, detail=results["error"])
        
        return {"success": True, "data": results}
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)