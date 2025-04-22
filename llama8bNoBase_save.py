import requests
import os
from datetime import datetime

# Cartella di salvataggio
save_folder = os.path.expanduser("C:\\Users\\user\\Desktop\\Progetti\\MazzoleniTesiLLM\\LLama3.1_Output8BNoBase")
os.makedirs(save_folder, exist_ok=True)  # Crea la cartella se non esiste

# Prompt di base 
base_prompt = ""

#  Chiede il prompt all'utente e lo concatena al prompt di base
user_prompt = input("")
full_prompt = base_prompt + "\n" + user_prompt

# Imposta la richiesta al modello di Ollama con parametri ottimizzati
url = "http://localhost:11434/api/generate"  # Assicurarsi che Ollama sia in esecuzione!
data = {
    "model": "mannix/llama3.1-8b-abliterated:latest",
    "prompt": full_prompt,
    "stream": False,
    "temperature": 0.5,  
    "top_p": 1.0,  
    "top_k": 0,  
    "max_tokens": 4096,  # Aumentalo per garantire risposte più dettagliate

}

response = requests.post(url, json=data)

if response.status_code == 200:
    result = response.json()["response"]

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = os.path.join(save_folder, f"llama_output_{timestamp}.txt")

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(f"Prompt:\n{full_prompt}\n\nRisposta:\n{result}")

    print(f"{result}")
    print(f"Risposta salvata in {output_file}")
else:
    print("Errore nella richiesta:", response.text)
