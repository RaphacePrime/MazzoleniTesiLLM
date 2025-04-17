import requests
import os
from datetime import datetime

# Cartella di salvataggio
save_folder = os.path.expanduser("C:\\Users\\user\\Desktop\\Progetti\\TesiLLMTesting\\GenerazioneLLama\\LLama3.1Abliterate_Output8B")
os.makedirs(save_folder, exist_ok=True)  # Crea la cartella se non esiste

# Prompt di base 
base_prompt = """ 
Sei un assistente AI specializzato nella generazione automatica di test script JSON per Playwright a partire da descrizioni testuali di casi d’uso UML. 
Il tuo compito è trasformare una sequenza di passi descritti in linguaggio naturale in un formato JSON valido per Playwright.

**Esempio di Input (Descrizione Caso d'uso):**
1. L'utente naviga alla pagina di login.
2. L'utente inserisce username e password.
3. L'utente preme il pulsante "Accedi".
4. Il sistema verifica le credenziali:
   - Se valide → l'utente viene reindirizzato alla dashboard.
   - Se errate → il sistema mostra un messaggio di errore.

**Esempio di Output (JSON per Playwright):**
{
  "testName": "Login utente",
  "steps": [
    {"action": "goto", "url": "https://esempio.com/login"},
    {"action": "fill", "selector": "#username", "value": "test_user"},
    {"action": "fill", "selector": "#password", "value": "password123"},
    {"action": "click", "selector": "#login-button"},
    {"action": "waitForNavigation"},
    {"action": "assert", "condition": {"type": "url", "expected": "https://esempio.com/dashboard"}}
  ]
}

L'output deve essere un JSON ben formato con i seguenti campi obbligatori: testName, steps, dove ogni step è un oggetto con action e relativi parametri.

Ora genera un test script JSON basato sulla seguente descrizione:
"""

#  Chiede il prompt all'utente e lo concatena al prompt di base
user_prompt = input("")
full_prompt = base_prompt + "\n" + user_prompt

# Imposta la richiesta al modello di Ollama con parametri ottimizzati
url = "http://localhost:11434/api/generate"  # Assicurarsi che Ollama sia in esecuzione!
data = {
    "model": "mannix/llama3.1-8b-abliterated:latest",
    "prompt": full_prompt,
    "stream": False,
    "temperature": 0.0,  
    "top_p": 1.0,  
    "top_k": 0,  
    "max_tokens": 4096,  # Aumentato per garantire risposte più dettagliate
    "stop": ["\n\n", "###"]  

}

response = requests.post(url, json=data)

if response.status_code == 200:
    result = response.json()["response"]

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = os.path.join(save_folder, f"llama_output_{timestamp}.txt")

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(f"Prompt:\n{full_prompt}\n\nRisposta:\n{result}")

    print(f"{result}")
    print(f"✅ Risposta salvata in {output_file}")
else:
    print("❌ Errore nella richiesta:", response.text)
