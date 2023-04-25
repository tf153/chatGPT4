import os
import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = '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'


response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write a 800 words romantc horror story",
  temperature=0.7,
  max_tokens=2000,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)