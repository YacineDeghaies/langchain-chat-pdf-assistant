# PDF-Chat-Assistent

Ein Python App das Benutzer erlaubt ihre PDF-Datei hochzuladen und fragen zu deren Inhalt zu stellen. Diese App nutzt ein LLM um Antworten zu generieren. Fragen die nicht im Zusammenhang mit dem PDF stehen werden nicht beantwortet

## So funktioniert es

Die App liest die PDF-Datei ein und splittet den Text in kleinere Chunks, die anschließend in ein LLM eingespeist werden können. Sie nutzt OpenAI-Embeddings, um Embeddings für die Chunks zu erstellen. Anschließend ermittelt die Anwendung die Chunks, die semantisch der vom Nutzer gestellten Frage ähneln, und speist diese Chunks in das LLM als Kontext ein, um eine Antwort zu generieren.

Die Anwendung nutzt Streamlit zur Erstellung der Benutzeroberfläche und OpenAI Responses API für die Anbindung an das LLM.

## Installation

### mit pip:

```
pip install -r requirements.txt
```

### mit conda:

```
conda env create -f environment.yml
```

erstelle anschließend eine `.env`-Datei im Projektverzeichnis und füge deinen OpenAI API Key hinzu:

```env

OPENAI_API_KEY=dein_api_key

```

## Nutzung

Um die App zu starten:

```
streamlit run app.py
```
## Todos
- Feature: Benutzer können das Modell selbst auswählen.