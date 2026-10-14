#Ejemplo de uso de la librería requests para hacer una solicitud HTTP post a la API de Docker Models AI
import requests

url = "http://localhost:12434/engines/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "YOUR_API_KEY"
}
data = {
  "model": "gemma4:e4b",
  "messages": [
    {
      "role": "system",
      "content": "Eres un asistente experto en pastelería."
    },
    {
      "role": "user",
      "content": "Quien eres?"
    }
  ],
  "temperature": 1.0,
  "top_p": 0.95,
  "stream": False
}

response = requests.post(url, headers=headers, json=data)
contenido = response.json().get("choices", [{}])[0].get("message", {}).get("content", "")
print(contenido)