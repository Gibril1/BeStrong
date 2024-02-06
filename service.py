import os
from dotenv import load_dotenv
load_dotenv()

from openai import AsyncOpenAI


OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
model_id = os.getenv('MODEL_ID')

class OpenAIService:
    def __init__(self):
        self.client = AsyncOpenAI(
            api_key=OPENAI_API_KEY
        )

    
    async def prompt(self, prompt:str):
        try:
            response = await self.client.chat.completions.create(
                model=model_id,
                messages=[
                    {
                        "role": "system",
                        "content": "Health Motivation Model: Providing support for various health conditions.",
                    },
                    {"role": "user", "content": prompt},
                ],
            )
            
            return {
                "success": True,
                "data": response.choices[0].message.content
            }
        except Exception as e:
            return {
                "success": False,
                "data": e.message
            }