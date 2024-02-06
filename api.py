from fastapi import FastAPI
from pydantic import BaseModel
from service import OpenAIService


class PromptSchema(BaseModel):
    prompt: str

openai_service = OpenAIService()

app = FastAPI()

@app.get('/')
async def root():
    return {
        "success": True,
        "data": "The API is working on this port"
    }


@app.post('/prompt')
async def prompt(prompt:PromptSchema):
    if not prompt.prompt:
        return {
            "success": False,
            "message": "Please enter a prompt"
        }
    try:
        prompt_response = await openai_service.prompt(prompt.prompt)
        return {
            "success": True,
            "data": prompt_response
        }
    except Exception as e:
        return {
            "success":False,
            "message": str(e)
        }

