from dotenv import get_key
from openai import OpenAI


class Generate_AI:
    def __init__(self):
        self.__KEY = get_key('.env', 'KEY')
        self.__client = OpenAI(api_key=self.__KEY)

    def generate_response(self, text: str):
        response = self.__client.completions.create(
            model='text-davinci-003',
            prompt=text,
            max_tokens=100,
            n=1,
            temperature=0.5
        )
        if response:
            return response.choices[0].text
        return None


ai = Generate_AI()
response = ai.generate_response("Привет, как дела?")
print(response)