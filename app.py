from flask import Flask, render_template, redirect
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sequencia/<nome>')
def sequencia_livros(nome):
    livros_biblia = {
        "AT": ['Gênesis'],
        'NT': [
                {'nome': 'Mateus', 'abreviacao': 'Mt'}, {'nome': 'Marcos', 'abreviacao': 'Mc'},
                {'nome': 'Lucas', 'abreviacao': 'Lc'}, {'nome': 'João', 'abreviacao': 'Jo'},
                {'nome': 'Atos', 'abreviacao': 'At'}, {'nome': 'Romanos', 'abreviacao': 'Ro'},
                {'nome': '1 Coríntios', 'abreviacao': '1Co'}, {'nome': '2 Coríntios', 'abreviacao': '2Co'},
                {'nome': 'Gálatas', 'abreviacao': 'Gl'}, {'nome': 'Efésios', 'abreviacao': 'Ef'},
                {'nome': 'Filipenses', 'abreviacao': 'Fp'}, {'nome': 'Colossenses', 'abreviacao': 'Cl'},
                {'nome': '1 Tessalonicenses', 'abreviacao': '1Ts'}, {'nome': '2 Tessalonicenses', 'abreviacao': '2Ts'},
                {'nome': '1 Timóteo', 'abreviacao': '1Tm'}, {'nome': '2 Timóteo', 'abreviacao': '2Tm'},
                {'nome': 'Tito', 'abreviacao': 'Tt'}, {'nome': 'Filemom', 'abreviacao': 'Fm'},
                {'nome': 'Hebreus', 'abreviacao': 'Hb'}, {'nome': 'Tiago', 'abreviacao': 'Tg'},
                {'nome': '1 Pedro', 'abreviacao': '1Pe'}, {'nome': '2 Pedro', 'abreviacao': '2Pe'},
                {'nome': '1 João', 'abreviacao': '1Jo'}, {'nome': '2 João', 'abreviacao': '2Jo'},
                {'nome': '3 João', 'abreviacao': '3Jo'}, {'nome': 'Judas', 'abreviacao': 'Jd'},
                {'nome': 'Apocalipse', 'abreviacao': 'Ap'}
               ],
    }

    livro_biblia = ""

    if nome == 'at':
        livros = livros_biblia['AT']
        livro_biblia = livros[0]

    elif nome == 'nt':
        livros = livros_biblia['NT']
        livro_biblia = livros[0]

    else:
        redirect('index')

    return render_template("index.html", livro_biblia=livro_biblia)

if __name__=="__main__":
    app.run(host='0.0.0.0', debug=False)