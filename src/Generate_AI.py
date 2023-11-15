from openai import OpenAI


class Generate_AI:
    def __init__(self, key):
        self.__KEY = key

    def response(self):
        ''' Возвращает обьект OpenAI '''
        return OpenAI(api_key=self.__KEY)

    @property
    def key(self):
        return self.__KEY

    def generate_response(self, text: str):
        response = self.response().completions.create(
            model='text-davinci-003',
            prompt=text,
            max_tokens=300,
            n=1,
            temperature=0.5
        )
        if response:
            return response.choices[0].text

