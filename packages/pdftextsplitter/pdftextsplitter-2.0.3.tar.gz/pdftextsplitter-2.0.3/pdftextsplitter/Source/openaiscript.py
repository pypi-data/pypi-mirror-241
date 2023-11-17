import sys
from openai import OpenAI

# Imports from TextPart code:
sys.path.insert(1, '../')
from TextPart.OpenAI_Keys import OpenAI_Keys

# Function to connect to free ChatGPT account:
TheKeys = OpenAI_Keys()
client = OpenAI(api_key=TheKeys.standard_key)

def generate_response(prompt):
    response = client.completions.create(
        model="text-davinci-002",
        prompt=prompt,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()
