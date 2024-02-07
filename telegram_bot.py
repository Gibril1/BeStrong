import os, logging
from telethon import TelegramClient, events
from dotenv import load_dotenv
from service import OpenAIService
load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
bot_token = os.getenv('BOT_TOKEN')

client = TelegramClient('me', api_id, api_hash)
ai_service = OpenAIService()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info('Telegram Bot is running as expected')

@client.on(events.NewMessage)
async def handle_message(event):
    if event.is_private:
        # get the message
        user_input = event.message.text
        logging.info(f'The users prompt is {user_input}')

        response = await ai_service.prompt(user_input)
        logging.info(f'The response from the AI is {response}')

        await event.respond(response)


# Start the Telethon client
client.start(bot_token=bot_token)

# Run the client
client.run_until_disconnected()
 