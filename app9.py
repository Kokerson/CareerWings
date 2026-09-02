import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from anthropic import (
    Anthropic,
    RateLimitError,
    APIConnectionError,
    AuthenticationError,
    APIError,
)

load_dotenv()
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

MODEL = "claude-haiku-5"
MAX_TOKENS = 1024
app = Flask(__name__)


def zapytaj_claude(tresc_pytania):
    try:
        odpowiedz = client.messages.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            messages=[{"role": "user", "content": tresc_pytania}],
        )
        return odpowiedz.content[0].text
    except AuthenticationError:
        return "BŁĄD: nieprawidłowy klucz API."
    except RateLimitError:
        return "BŁĄD: zbyt wiele zapytań. Spróbuj za chwilę."
    except APIConnectionError:
        return "BŁĄD: problem z połączeniem internetowym."
    except APIError as blad:
        return f"BŁĄD: {blad}"


@app.route("/")
def strona_glowna():
    return render_template("index.html", odpowiedz=None)


@app.route("/zapytaj", methods=["POST"])
def zapytaj():
    tresc_pytania = request.form.get("pytanie", "").strip()

    if tresc_pytania == "":
        return render_template("index.html", odpowiedz="Wpisz najpierw jakieś pytanie!")

    odpowiedz_claude = zapytaj_claude(tresc_pytania)
    return render_template("index.html", odpowiedz=odpowiedz_claude, pytanie=tresc_pytania)


if __name__ == "__main__":
    app.run(debug=True)
