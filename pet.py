from flask import Flask, request, render_template

app = Flask(__name__, template_folder='paginaWeb')

@app.route('/')
def index():
    return render_template('formulario.html')

@app.route('/enviar_informacoes', methods=['POST'])
def enviar_informacoes():
    nome = request.form['nome']
    idade = request.form['idade']
    peso = request.form['peso']
    
    # Valida e processa as informações recebidas
    try:
        idade = int(idade)
        peso = float(peso)
        if idade < 0 or peso < 0:
            raise ValueError("Idade e peso devem ser não-negativos.")
    except ValueError as e:
        return f"Erro: {e}"

    return f"""
    <h1>Informações do Pet</h1>
    <p>Nome: {nome}</p>
    <p>Idade: {idade} anos</p>
    <p>Peso: {peso} kg</p>
    """
    
if __name__ == '__main__':
    app.run(debug=True)