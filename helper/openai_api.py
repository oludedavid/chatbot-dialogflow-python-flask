from openai import OpenAI
import os
from dotenv import load_dotenv




load_dotenv()


OpenAI.api_key = os.environ.get("OPENAI_API_KEY")


client = OpenAI()


def text_completion(prompt: str) -> dict:
  '''
    Call Openai API for text completion
    Parameters:
        - prompt: user query (str)
    Returns:
        - dict
    '''
  try:
    response = client.completions.create(model='text-davinci-003',
                                        prompt=f'Human: {prompt}\nAI: ',
                                        temperature=0.9,
                                        max_tokens=150,
                                        top_p=1,
                                        frequency_penalty=0,
                                        presence_penalty=0.6,
                                        stop=['Human:', 'AI:'])
    return {'status': 1, 'response': response.choices[0].text}
  except Exception as e:
        return {'status': 0, 'response': str(e)}