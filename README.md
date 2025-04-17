# TesiLLMTesting

## 1. Installazione Ollama

## 2. Installazione LLama

ollama pull huihui_ai/llama3.2-abliterate:3b-instruct

ollama list

## 3. Esecuzione LLama

ollama run artifish/llama3.2-uncensored:latest

ollama run huihui_ai/llama3.2-abliterate:3b-instruct

ollama run huihui_ai/llama3.2-abliterate:1b-instruct

ollama run mannix/llama3.1-8b-abliterated:latest

ollama run huihui_ai/llama3.3-abliterated:70b-instruct-q4_K_M

## 4. Esecuzione con salvataggio

cd -->"Generazione con Llama"

python llama3bAbliterate_save.py

python llama3bUncensored_save.py

python llama8bAbliterate_save.py

python3 llama_saveMac.py

## 5. Esecizione con StreamLit

python -m streamlit run appWindows.py

streamlit run appMac.py

## 6. Casi di test

### 1. Test di Login con credenziali valide

#### Prompt:

L'utente naviga alla pagina di login.
L'utente inserisce username e password validi.
L'utente preme il pulsante "Accedi".
Il sistema verifica le credenziali e reindirizza l'utente alla dashboard.

#### Output atteso:

```json
{
  "testName": "Login con credenziali valide",
  "steps": [
    { "action": "goto", "url": "https://esempio.com/login" },
    { "action": "fill", "selector": "#username", "value": "utente_test" },
    { "action": "fill", "selector": "#password", "value": "password123" },
    { "action": "click", "selector": "#login-button" },
    { "action": "waitForNavigation" },
    {
      "action": "assert",
      "condition": {
        "type": "url",
        "expected": "https://esempio.com/dashboard"
      }
    }
  ]
}
```

#### Prompt effettivo totale(Mac 8B):

Sei un assistente AI specializzato nella generazione automatica di test script JSON per Playwright a partire da descrizioni testuali di casi d’uso UML.
Il tuo compito è trasformare una sequenza di passi descritti in linguaggio naturale in un formato JSON valido per Playwright.

Esempio di Input (Descrizione Caso d'uso):\*\*

1.  L'utente naviga alla pagina di login.
2.  L'utente inserisce username e password.
3.  L'utente preme il pulsante "Accedi".
4.  Il sistema verifica le credenziali:

- Se valide → l'utente viene reindirizzato alla dashboard.
- Se errate → il sistema mostra un messaggio di errore.

Esempio di Output (JSON per Playwright):\*\*
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

Ora genera un test script JSON basato sulla seguente descrizione:

L'utente naviga alla pagina di login. L'utente inserisce username e password validi.L'utente preme il pulsante "Accedi". Il sistema verifica le credenziali e reindirizza l'utente alla dashboard.

#### Output effettivo(Mac 8B, 1024 tokens, t=02:21):

```json
{
  "testName": "Login utente",
  "steps": [
    { "action": "goto", "url": "https://esempio.com/login" },
    { "action": "fill", "selector": "#username", "value": "valid_username" },
    { "action": "fill", "selector": "#password", "value": "valid_password" },
    { "action": "click", "selector": "#login-button" },
    { "action": "waitForNavigation" },
    {
      "action": "assert",
      "condition": {
        "type": "url",
        "expected": "https://esempio.com/dashboard"
      }
    }
  ]
}
```

#### Output effettivo(2060 SUPER, 4096 tokens, t=00:16):

```json
{
  "testName": "Login utente",
  "steps": [
    { "action": "goto", "url": "https://esempio.com/login" },
    { "action": "fill", "selector": "#username", "value": "valid_username" },
    { "action": "fill", "selector": "#password", "value": "valid_password" },
    { "action": "click", "selector": "#login-button" },
    { "action": "waitForNavigation" },
    {
      "action": "assert",
      "condition": {
        "type": "url",
        "expected": "https://esempio.com/dashboard"
      }
    }
  ]
}
```

### 2. Test di Login con credenziali errate

#### Prompt:

L'utente naviga alla pagina di login.
L'utente inserisce credenziali errate.
L'utente preme il pulsante "Accedi".
Il sistema mostra un messaggio di errore.

#### Output atteso:

```json
{
  "testName": "Login con credenziali errate",
  "steps": [
    { "action": "goto", "url": "https://esempio.com/login" },
    { "action": "fill", "selector": "#username", "value": "utente_sbagliato" },
    { "action": "fill", "selector": "#password", "value": "password_errata" },
    { "action": "click", "selector": "#login-button" },
    {
      "action": "assert",
      "condition": {
        "type": "text",
        "selector": "#error-message",
        "expected": "Credenziali non valide"
      }
    }
  ]
}
```

#### Prompt effettivo totale(Mac 1B):

Sei un assistente AI specializzato nella generazione automatica di test script JSON per Playwright a partire da descrizioni testuali di casi d’uso UML.
Il tuo compito è trasformare una sequenza di passi descritti in linguaggio naturale in un formato JSON valido per Playwright.

Esempio di Input (Descrizione Caso d'uso):\*\*

1.  L'utente naviga alla pagina di login.
2.  L'utente inserisce username e password.
3.  L'utente preme il pulsante "Accedi".
4.  Il sistema verifica le credenziali:
    - Se valide → l'utente viene reindirizzato alla dashboard.
    - Se errate → il sistema mostra un messaggio di errore.

Esempio di Output (JSON per Playwright):\*\*
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

Ora genera un test script JSON basato sulla seguente descrizione:

L'utente naviga alla pagina di login. L'utente inserisce credenziali errate. L'utente preme il pulsante "Accedi". Il sistema mostra un messaggio di errore.

#### Output effettivo(Mac 1B, 1024 tokens, t=00:35):

"Ecco il test script JSON per l'esempio descritto:

```json
{
  "testName": "Login utente",
  "steps": [
    {
      "action": "goto",
      "url": "https://esempio.com/login"
    },
    {
      "action": "fill",
      "selector": "#username",
      "value": "non_test_user" // inserire credenziali errate
    },
    {
      "action": "fill",
      "selector": "#password",
      "value": "password123" // inserire credenziali errate
    },
    {
      "action": "click",
      "selector": "#login-button"
    },
    {
      "action": "waitForNavigation",
      "condition": {
        "type": "url",
        "expected": "https://esempio.com/dashboard"
      }
    },
    {
      "error": "errore di login"
    }
  ]
}
```

Nota che ho modificato alcune parti per adattarle al contesto:

- Ho deciso di utilizzare l'espressione "#username" e "#password" invece delle stringhe ` username` e `password`.
- Ho deciso di utilizzare `password123` invece della credenziale errata inserita.
- Ho aggiunto un error di login con il messaggio "errore di login"."

#### Output effettivo(2060 SUPER, 4096 tokens, t=00:03):

```json
{
  "testName": "Errore credenziali login",
  "steps": [
    { "action": "goto", "url": "https://esempio.com/login" },
    { "action": "fill", "selector": "#username", "value": "invalid_username" },
    { "action": "fill", "selector": "#password", "value": "wrong_password" },
    { "action": "click", "selector": "#login-button" },
    { "action": "waitForNavigation" },
    {
      "action": "assert",
      "condition": { "type": "text", "expected": "error_message" }
    }
  ]
}
```

### 3. Test di Logout

#### Prompt:

L'utente accede al portale e si trova nella dashboard.
L'utente clicca sul pulsante di logout.
Il sistema disconnette l'utente e reindirizza alla pagina di login.

#### Output atteso:

```json
{
  "testName": "Logout",
  "steps": [
    { "action": "click", "selector": "#logout-button" },
    { "action": "waitForNavigation" },
    {
      "action": "assert",
      "condition": { "type": "url", "expected": "https://esempio.com/login" }
    }
  ]
}
```

#### Prompt effettivo totale(Mac 1B):

Sei un assistente AI specializzato nella generazione automatica di test script JSON per Playwright a partire da descrizioni testuali di casi d’uso UML.
Il tuo compito è trasformare una sequenza di passi descritti in linguaggio naturale in un formato JSON valido per Playwright.

Esempio di Input (Descrizione Caso d'uso):\*\*

1.  L'utente naviga alla pagina di login.
2.  L'utente inserisce username e password.
3.  L'utente preme il pulsante "Accedi".
4.  Il sistema verifica le credenziali:
    - Se valide → l'utente viene reindirizzato alla dashboard.
    - Se errate → il sistema mostra un messaggio di errore.

Esempio di Output (JSON per Playwright):\*\*
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

L'utente accede al portale e si trova nella dashboard. L'utente clicca sul pulsante di logout. Il sistema disconnette l'utente e reindirizza alla pagina di login.

#### Output effettivo(Mac 1B, 4096 tokens, t=00:27):

"Ecco il test script JSON per corrispondere alle tue esigenze:

```json
{
  "testName": "Logout utente",
  "steps": [
    {
      "action": "click", // action è "click" o "mouse_move" o "keyboard"
      "selector": "#logout-button", // selector è il pulsante di logout, puoi sostituirlo con qualsiasi elemento
      "waitForNavigation": true // attende la navigazione alla pagina dopo l'azione
    },
    {
      "action": "getURL", // action è "get" (perché la URL deve essere accessibile al browser) o "input"
      "selector": "#logout-link", // selector è il pulsante di logout, puoi sostituirlo con qualsiasi elemento
      "value": "https://esempio.com/logout"
    },
    {
      "action": "waitForNavigation",
      "condition": { "type": "url", "expected": "https://esimpagina/ logout" }
    }
  ]
}
```

Nota che ho utilizzato `input` invece di `fill` per gli input, poiché non è un utente che inserisce una stringa ma piuttosto un elemento del DOM. Ecco come funzionerebbe nel codice:

```json
{
  "testName": "Logout utente",
  "steps": [
    {
      "action": "click", // action è "click" o "mouse_move" o "keyboard"
      "selector": "#logout-button", // selector è il pulsante di logout, puoi sostituirlo con qualsiasi elemento
      "waitForNavigation": true // attende la navigazione alla pagina dopo l'azione
    },
    {
      "action": "getURL",
      "selector": "#logout-link",
      "value": "https://esimpagina/ logout"
    }
  ]
}
```

"

#### Output effettivo(2060 SUPER, 4096 tokens, t=00:02):

```json
{
  "testName": "Logout utente",
  "steps": [
    { "action": "goto", "url": "" },
    { "action": "click", "selector": "#logout-button" },
    { "action": "waitForNavigation" },
    {
      "action": "assert",
      "condition": { "type": "url", "expected": "https://esempio.com/login" }
    }
  ]
}
```

### 4. Test di Registrazione nuovo utente

#### Prompt:

L'utente naviga alla pagina di registrazione.
L'utente compila il modulo con dati validi.
L'utente preme il pulsante "Registrati".
Il sistema conferma la registrazione e reindirizza alla dashboard.

#### Output atteso:

```json
{
  "testName": "Registrazione nuovo utente",
  "steps": [
    { "action": "goto", "url": "https://esempio.com/register" },
    { "action": "fill", "selector": "#username", "value": "nuovo_utente" },
    { "action": "fill", "selector": "#email", "value": "nuovo@esempio.com" },
    { "action": "fill", "selector": "#password", "value": "password123" },
    { "action": "click", "selector": "#register-button" },
    { "action": "waitForNavigation" },
    {
      "action": "assert",
      "condition": {
        "type": "url",
        "expected": "https://esempio.com/dashboard"
      }
    }
  ]
}
```

#### Prompt effettivo totale(Mac 8B):

Sei un assistente AI specializzato nella generazione automatica di test script JSON per Playwright a partire da descrizioni testuali di casi d’uso UML.
Il tuo compito è trasformare una sequenza di passi descritti in linguaggio naturale in un formato JSON valido per Playwright.

Esempio di Input (Descrizione Caso d'uso):\*\*

1.  L'utente naviga alla pagina di login.
2.  L'utente inserisce username e password.
3.  L'utente preme il pulsante "Accedi".
4.  Il sistema verifica le credenziali:

- Se valide → l'utente viene reindirizzato alla dashboard.
- Se errate → il sistema mostra un messaggio di errore.

Esempio di Output (JSON per Playwright):\*\*
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

L'utente naviga alla pagina di registrazione. L'utente compila il modulo con dati validi. L'utente preme il pulsante "Registrati". Il sistema conferma la registrazione e reindirizza alla dashboard.

#### Output effettivo(Mac 8B, 4096 tokens, t=05:55):

```json
{
  "testName": "Registrazione utente",
  "steps": [
    { "action": "goto", "url": "https://esempio.com/register" },
    { "action": "fill", "selector": "#nome", "value": "nome_utente" },
    { "action": "fill", "selector": "#cognome", "value": "cognome_utente" },
    { "action": "fill", "selector": "#email", "value": "utente@email.com" },
    { "action": "fill", "selector": "#password", "value": "password123" },
    { "action": "click", "selector": "#register-button" },
    { "action": "waitForNavigation" },
    {
      "action": "assert",
      "condition": {
        "type": "url",
        "expected": "https://esempio.com/dashboard"
      }
    }
  ]
}
```

#### Output effettivo(2060 SUPER, 4096 tokens, t=00:04):

```json
{
  "testName": "Registrazione utente",
  "steps": [
    { "action": "goto", "url": "https://esempio.com/register" },
    { "action": "fill", "selector": "#nome", "value": "John Doe" },
    { "action": "fill", "selector": "#cognome", "value": "Doe" },
    { "action": "fill", "selector": "#email", "value": "john.doe@example.com" },
    { "action": "fill", "selector": "#password", "value": "strong_password" },
    { "action": "click", "selector": "#register-button" },
    { "action": "waitForNavigation" }
  ]
}
```

### 5. Test di Recupero Password

#### Prompt:

L'utente naviga alla pagina di login.
L'utente clicca sul link "Password dimenticata".
L'utente inserisce il proprio indirizzo email.
Il sistema invia una mail di recupero password.

#### Output atteso:

```json
{
  "testName": "Recupero Password",
  "steps": [
    { "action": "goto", "url": "https://esempio.com/login" },
    { "action": "click", "selector": "#forgot-password" },
    { "action": "fill", "selector": "#email", "value": "utente@esempio.com" },
    { "action": "click", "selector": "#submit-button" },
    {
      "action": "assert",
      "condition": {
        "type": "text",
        "selector": "#confirmation-message",
        "expected": "Email inviata"
      }
    }
  ]
}
```

#### Prompt effettivo totale(Mac 3B):

#### Output effettivo(Mac 3B, 4096 tokens, t=01:20):

Ecco il test script JSON generato a partire dalla descrizione:

```
{
"testName": "Riconsegna password dimenticata",
"steps": [
   {"action": "goto", "url": "https://esempio.com/login"},
   {"action": "click", "selector": "#password_recovery_link"},
   {"action": "fill", "selector": "#email_field", "value": "test_email@example.com"}
]
}
```

Nota che ho preso alcune libertà con la descrizione per adattarla meglio al formato JSON richiesto. In particolare, non è stato specificato il tipo di selector utilizzare (ad esempio `id`, `.class`, `xpath`) e non sono stati menzionati i dettagli relativi all'invio della mail di recupero password. Pertanto, ho semplicemente inserito un testo per descrivere l'action "fill" che inserisce l'indirizzo email.

#### Output effettivo(Mac 8B, 500 tokens, t=05:00):

```json
{
  "testName": "Recupera Password",
  "steps": [
    { "action": "goto", "url": "https://esempio.com/login" },
    { "action": "click", "selector": "#forgot-password-link" },
    { "action": "fill", "selector": "#email", "value": "test_user@example.com" }
  ]
}
```

#### Output effettivo(Mac 8B, 4096 tokens, t=01:10)-->Aggiunta "L'utente clicca sul pulsante conferma":

```json
{
  "testName": "Recupera password",
  "steps": [
    { "action": "goto", "url": "https://esempio.com/login" },
    { "action": "click", "selector": "#forgot-password-link" },
    {
      "action": "fill",
      "selector": "#email",
      "value": "test_email@example.com"
    },
    { "action": "click", "selector": "#confirm-button" },
    { "assert": "waitForNavigation" }
  ]
}
```

#### Output effettivo(2060 SUPER, 4096 tokens, t=00:03):

```json
{
  "testName": "Recuperazione Password",
  "steps": [
    { "action": "goto", "url": "https://esempio.com/login" },
    { "action": "click", "selector": "#forgot-password-link" },
    { "action": "fill", "selector": "#email", "value": "example@example.com" },
    { "action": "waitForNavigation" }
  ]
}
```

### 6. Test di Navigazione alla pagina profilo

#### Prompt:

L'utente accede alla dashboard.
L'utente clicca sul proprio profilo.
Il sistema mostra la pagina del profilo.

#### Output atteso:

```json
{
  "testName": "Navigazione alla pagina profilo",
  "steps": [
    { "action": "click", "selector": "#profile-button" },
    { "action": "waitForNavigation" },
    {
      "action": "assert",
      "condition": { "type": "url", "expected": "https://esempio.com/profile" }
    }
  ]
}
```

#### Output effettivo(2060 SUPER, 4096 tokens, t=00:02):

```json
{
  "testName": "Accesso al profilo",
  "steps": [
    { "action": "goto", "url": "https://esempio.com/dashboard" },
    { "action": "click", "selector": "#profile-button" },
    {
      "action": "waitForContent",
      "condition": { "type": "selector", "expected": "#profile-page" }
    }
  ]
}
```

### 7. Test di Modifica delle informazioni profilo

#### Prompt:

L'utente accede alla pagina del profilo.
L'utente modifica il proprio nome e salva le modifiche.
Il sistema conferma l'aggiornamento delle informazioni.

#### Output atteso:

```json
{
  "testName": "Modifica delle informazioni profilo",
  "steps": [
    { "action": "fill", "selector": "#name", "value": "Nuovo Nome" },
    { "action": "click", "selector": "#save-button" },
    {
      "action": "assert",
      "condition": {
        "type": "text",
        "selector": "#confirmation-message",
        "expected": "Dati salvati con successo"
      }
    }
  ]
}
```

#### Output effettivo(2060 SUPER, 4096 tokens, t=00:16):

```json
{
  "testName": "Aggiorna Profilo Utente",
  "steps": [
    { "action": "goto", "url": "https://esempio.com/profilo" },
    { "action": "fill", "selector": "#nome", "value": "nuovo nome" },
    { "action": "click", "selector": "#salva-modifiche" },
    { "action": "waitForNavigation" },
    {
      "action": "assert",
      "condition": {
        "type": "containsText",
        "expected": "Informazioni aggiornate"
      }
    }
  ]
}
```

#### Prompt effettivo totale(Mac 8B):

#### Output effettivo(Mac 8B, 1024 tokens, t=02:21):

### 8. Test di Eliminazione Account

#### Prompt:

L'utente accede alla pagina del profilo.
L'utente clicca su "Elimina Account".
Il sistema chiede conferma.
L'utente conferma l'eliminazione.
Il sistema elimina l'account e reindirizza alla home page.

#### Output atteso:

```json
{
  "testName": "Eliminazione Account",
  "steps": [
    { "action": "click", "selector": "#delete-account-button" },
    { "action": "click", "selector": "#confirm-delete" },
    { "action": "waitForNavigation" },
    {
      "action": "assert",
      "condition": { "type": "url", "expected": "https://esempio.com/home" }
    }
  ]
}
```

#### Prompt effettivo totale(Mac 8B):

#### Output effettivo(Mac 8B, 1024 tokens, t=02:21):

#### Output effettivo(2060 SUPER, 4096 tokens, t=00:03):

```json
{
  "testName": "Eliminare account",
  "steps": [
    { "action": "goto", "url": "https://esempio.com/profilo" },
    { "action": "click", "selector": "#elimina-account" },
    { "action": "waitForDialog", "condition": "confirm" },
    { "action": "dialogConfirm" },
    { "action": "waitForNavigation" }
  ]
}
```
