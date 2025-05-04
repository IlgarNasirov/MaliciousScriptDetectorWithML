from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib

malicious_script_model = joblib.load('malicious_script_model.pkl')

app = FastAPI()

class ScriptRequest(BaseModel):
    script: str = Field(..., min_length = 1)

@app.post('/predict')
def predict(data: ScriptRequest):
    script = data.script.strip()
    prediction = malicious_script_model.predict([script])
    result = 'Malicious!' if prediction[0] == 1 else 'Not malicious!'
    return {'script': script, 'result': result}