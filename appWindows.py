import streamlit as st
import subprocess

st.set_page_config(page_title="LLama Test Script Generator", page_icon="🤖", layout="wide")

st.title("🎭 Generatore di Test Script JSON con LLama")

st.markdown("""
Questa applicazione utilizza un modello LLM per generare test script JSON per Playwright partendo da una descrizione testuale di un caso d'uso UML.
Inserisci la descrizione e clicca su **Genera Test Script** per ottenere il JSON corrispondente.
""")

if "output_text" not in st.session_state:
    st.session_state.output_text = ""

# Input per la descrizione del caso d'uso
user_prompt = st.text_area("📝 Inserisci la descrizione del caso d'uso:", height=200)

# Bottone per generare il test script
if st.button("🚀 Genera il Test"):
    if user_prompt.strip():
        # Esegue lo script llama_saveMac.py con il prompt come input
        result = subprocess.run(["python3", "llama8bAbliterate_save.py"], input=user_prompt, text=True, capture_output=True)

        st.session_state.output_text = result.stdout.strip()

        if result.stderr:
            st.error(f"Errore durante l'esecuzione: {result.stderr}")

if st.session_state.output_text:
    st.subheader("📄 Output Generato:")
    st.code(st.session_state.output_text, language="json")

    st.download_button("⬇️ Scarica TXT", st.session_state.output_text, file_name="test_script.txt", mime="text/plain")
    st.download_button("⬇️ Scarica JSON", st.session_state.output_text, file_name="test_script.json", mime="application/json")

elif st.session_state.output_text == "" and user_prompt.strip() == "":
    st.warning("⚠️ Inserisci una descrizione del caso d'uso prima di generare il test script!")
