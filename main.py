"""
Command to install generativeai:   pip install -q -U google-generativeai
Before executing the code, create an GoogleAI studio API and replace in the api_key variable
"""

import google.generativeai as genai

# Replace with your API key
api_key = "YOUR_API_KEY"

# Configure the API key
genai.configure(api_key=api_key)

# (Rest of your code using Gemini functionalities)

# To print the available model names
# for m in genai.list_models():
#     if 'generateContent' in m.supported_generation_methods:
#         print(m.name)

# Get the Gemini Pro model
model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("write a code python code to find first 100 even numbers")

print(response.text)


