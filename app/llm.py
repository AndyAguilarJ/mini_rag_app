import requests
import json

def generate(prompt):
    # This matches the default port llama-server.exe uses
    url = "http://127.0.0.1:8080/v1/chat/completions" 
    
    payload = {
        "messages": [
            {"role": "system", "content": "You are a helpful local assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "stream": False
    }

    try:
        response = requests.post(url, json=payload, timeout=60)
        response.raise_for_status() # Check if the server is actually there
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except requests.exceptions.ConnectionError:
        return "Error: Could not connect to the local LLM engine. Is llama-server.exe running?"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"