from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de perguntas: (texto, pessoa se for "chave", senão None)
perguntas = [
    ("A pessoa é xará de um personagem do Chaves?", "Nhonho"),
    ("Ela tem o maior pau do grupo?", "Dudu"),  # zoeira
    ("Ela mora em São Paulo?", None),
    ("Ela é gay e não sabe dirigir?", "Álvaro"),
    ("Ela largou os brother por uma ruiva?", "Hugozado"),
    ("Ela tem irmão (HOMEM)?", None),
    ("Ela namora?", None),
    ("Ela já ganhou uma lixa de skate?", "Nathan"),
    ("Ela aguenta beber mais de 2 latinhas?", None),  # zoeira
    ("Ela tá na coleira da Fefê?", "Pelebosta"),
    ("Já pegou a Sa trepiche?", "Franchico"),
    ("Já perdeu umas coisas estranhas em Bariloche?", "Nera apeludo"),
    ("Palmeirense?", "GeBe")
]

@app.route('/')
def index():
    return redirect(url_for('pergunta', numero=0))

@app.route('/pergunta/<int:numero>', methods=['GET', 'POST'])
def pergunta(numero):
    if numero >= len(perguntas):
        return render_template('resultado.html', pessoa=None)

    texto, pessoa = perguntas[numero]

    if request.method == 'POST':
        resposta = request.form['resposta']
        if resposta == 's' and pessoa:
            return render_template('resultado.html', pessoa=pessoa)
        return redirect(url_for('pergunta', numero=numero + 1))

    return render_template('index.html', numero=numero, pergunta=texto)

if __name__ == "__main__":
    app.run(debug=True)