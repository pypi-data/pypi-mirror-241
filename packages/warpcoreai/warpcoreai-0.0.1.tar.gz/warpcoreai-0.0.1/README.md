# warpcoreai

## Introduzione
warpcoreai è un pacchetto Python che permette di eseguire modelli di linguaggio.

## Installazione
Puoi installare warpcoreai tramite pip:
```bash
pip install warpcoreai
```

## Utilizzo

```python
from warpcoreai import WarpCoreAI

warpcore = WarpCoreAI()
warpcore.load_model("modello")
warpcore.load_tokenizer("tokenizer")
warpcore.load_config("config")
```