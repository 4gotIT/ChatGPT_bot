import telebot
from Generate_AI import Generate_AI
from dotenv import get_key
from openai import OpenAI


class MyBot:
    def __init__(self, tg_key, ai_key):
        self.ai_key = ai_key
        self.bot = telebot.TeleBot(tg_key)
        self.ai = Generate_AI(ai_key)

    def start(self):
        @self.bot.message_handler(commands=['start'])
        def send_message(message):
            self.bot.send_message(message.chat.id, 'Привет!')

        @self.bot.message_handler(content_types=['text'])
        def main(message):
            self.client = self.ai.response()
            self.res = self.ai.generate_response(message.text)
            self.bot.send_message(message.chat.id, self.res)

        # @self.bot.message_handler(content_types=['text'])
        # def main(message):
        #     self.client = OpenAI(api_key=self.ai_key)
        #     self.res = self.client.completions.create(
        #         model='text-davinci-003',
        #         prompt=message.text,
        #         max_tokens=100,
        #         n=1,
        #         temperature=0.5
        #     )
        #     self.generate_answer = self.res.choices[0].text
        #     self.bot.send_message(message.chat.id, self.generate_answer)

        self.bot.polling()


if __name__ == '__main__':
    KEY_TG = get_key('.env', 'tg_key')
    AI_KEY = get_key('.env', 'gpt_key')
    bot = MyBot(KEY_TG, AI_KEY)
    bot.start()
