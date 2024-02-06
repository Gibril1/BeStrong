from service import OpenAIService
import asyncio
import nest_asyncio

opeanai_service = OpenAIService()


async def main():
    prompt_response = await opeanai_service.prompt('Malaria')
    print(prompt_response)

nest_asyncio.apply()
asyncio.run(main())