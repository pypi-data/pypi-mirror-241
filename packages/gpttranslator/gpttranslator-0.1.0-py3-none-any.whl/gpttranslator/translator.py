import os
import openai
import random

prompts = [
    "Translate to {target_language}:",
    "Please translate this {source_language} text to {target_language}:",
    "Perform a direct translation of the following {source_language} text to {target_language} without adding any interpretations:",
    "Translate the following {source_language} sentence into {target_language}, preserving the original meaning and context:",
    "Directly translate this text from {source_language} to {target_language} without any modifications or interpretations:",
    "I need a faithful translation of this {source_language} text into {target_language}, keeping close to the original:",
    "Translate this from {source_language} to {target_language}, ensuring the tone and nuances are accurately conveyed:",
    "Translate the following from {source_language} to {target_language}, considering any cultural nuances:",
    "Convert this {source_language} text into {target_language}, focusing solely on the literal translation without adding context:",
    "Translate the following English phrase to Turkish, making sure to preserve its original essence and style:",
]


def translate(text,
              prompt='any',
              source_language="English",
              target_language="Turkish",
              api_key=os.environ.get('OPENAI_API_KEY')):

    client = openai.OpenAI(api_key=api_key)

    if isinstance(prompt, int):
        prompt = prompts[prompt]
    elif prompt == 'any':
        prompt = random.choice(prompts)
        print('Prompt:', prompt)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0.2,
        messages=[
            {"role": "system", "content": prompt.format(source_language=source_language,
                                                        target_language=target_language)},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content
