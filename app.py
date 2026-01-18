from flask import Flask, request, render_template_string

app = Flask(__name__)

# PIN secreto para validar os vales
PIN_CORRETO = "2016"

HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Vale para a Nane</title>
</head>
<body style="
    font-family: Arial, sans-serif;
    text-align: center;
    background-color: #ffe6f0;
    padding: 40px;
">

    <h1>💖 Vale para a Nane</h1>

    {% if not ativado %}
        <p>
            Esse vale é especial.<br>
            Ele é ativado junto com quem te ama 💕
        </p>

        {% if erro %}
            <p style="color:#c2185b;">
                💌 Quase lá…<br>
                Esse vale precisa da nossa confirmação juntos 💕
            </p>
        {% endif %}

        <form method="post">
            <input
                type="password"
                name="pin"
                placeholder="Digite o PIN"
                style="
                    padding: 10px;
                    font-size: 16px;
                    border-radius: 6px;
                    border: 1px solid #ccc;
                "
            >
            <br><br>
            <button
                type="submit"
                style="
                    padding: 10px 20px;
                    font-size: 16px;
                    background-color: #e91e63;
                    color: white;
                    border: none;
                    border-radius: 8px;
                "
            >
                Ativar vale
            </button>
        </form>

    {% else %}
        <h2>💖 Vale ativado, Nane ❤️</h2>
        <p>
            Hoje o meu tempo é todo seu.<br>
            Esse momento é só nosso 💞
        </p>
    {% endif %}

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    ativado = False
    erro = False

    if request.method == "POST":
        pin_digitado = request.form.get("pin")

        if pin_digitado == PIN_CORRETO:
            ativado = True
        else:
            erro = True

    return render_template_string(
        HTML,
        ativado=ativado,
        erro=erro
    )

if __name__ == "__main__":
    app.run()