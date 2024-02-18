from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
# função
def home():
    variavel = "Game: Adivinhe o número"
    if request.method == "GET":
        return render_template('home.html', variavel=variavel)
    else:
        #variável utilizada para comparar
        numero = 0
        # salva o palpite da pessoa que ela colocou no formulário
        palpite = int(request.form.get("name"))

        if numero == palpite:
            return pagina1()# se a pessoa acertar o numero ela é direcionana para a página 1
        else:
            return 'Voce errou!'#aparece uma pensagem 

if __name__ == '__main__':
    app.run()


@app.route('/pagina1')
def pagina1():#função para renderizar a pagina 1
    return render_template('pagina1.html')


# define a variavel nome que a pessoa vai busar como URL
@app.route('/<string:nome>')

def error(nome):#função de erro
    # variavel a ser sibstituida na página em ERROR. HTML
    var = f'({nome})'
    # linka a variável do HTML com a em PYTHON
    return render_template("error.html", var=var)#função para renderizar a pagina error .html
