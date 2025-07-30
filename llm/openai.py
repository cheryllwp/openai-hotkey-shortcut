# imports

import os
from dotenv import load_dotenv
from openai import OpenAI

#connect openai api
load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

#check key
if not api_key:
    print("Error: No API key was found")
elif not api_key.startswith("sk-proj-"):
    print("Error: API key found, but it doesn't start sk-proj")
elif api_key.strip() != api_key:
    print("Error: API key found, space or tab characters at the start or end")
else:
    print("API key found and looks good so far!")

my_openai = OpenAI()

# message example:
# messages = [
#     {"role": "system", "content": "You are a snarky assistant"},
#     {"role": "user", "content": "What is 2 + 2?"}
# ]

def ask_openai(sys_prompt, user_prompt):
    final_message = [
        {"role":"system", "content": sys_prompt},
        {"role":"user", "content":user_prompt}
    ]
    
    print('Just a moment...')

    response = my_openai.chat.completions.create(
            model = "gpt-4o-mini",
            messages = final_message
    )
    return response.choices[0].message.content
