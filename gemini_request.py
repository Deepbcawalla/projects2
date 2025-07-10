import google.generativeai as genai
import user_config
import requests
import os
from datetime import datetime

# Configure the Gemini API
genai.configure(api_key=user_config.gemini_api_key)

def send_request(query):
    try:
        # Initialize the model - using the updated model name
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Generate response
        response = model.generate_content(query)
        
        return response.text
    except Exception as e:
        return f"Error: {str(e)}. Please check your Gemini API key in user_config.py"

