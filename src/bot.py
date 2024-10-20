import os

import telebot
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


TELEGRAM_BOT_API_TOKEN = os.getenv("TELEGRAM_BOT_API_TOKEN")

from openai import OpenAI


def get_gpt_response(user_query):
    client = OpenAI()

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"{user_query}",
            }
        ],
        model="gpt-4o",
    )

    response = chat_completion.choices[0].message.content

    return response


bot = telebot.TeleBot(TELEGRAM_BOT_API_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I'm your GPT chatbot. Ask me anything.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_query = message.text
    response = get_gpt_response(user_query)
    bot.reply_to(message, response)

# Start polling for messages
bot.polling()