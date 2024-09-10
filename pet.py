from flask import Flask, request, render_template

# alteração do direotio padrão para paginaWeb
app = Flask(__name__, template_folder='paginaWeb')

def validar_idade(idade):
    try:
        idade = int(idade)
        if idade < 0:
            raise ValueError("A idade não pode ser negativa.")
        return idade
    except ValueError as e:
        raise ValueError(f"Erro na idade: {e}")

def validar_peso(peso):
    try:
        peso = float(peso)
        if peso < 0:
            raise ValueError("O peso não pode ser negativo.")
        return peso
    except ValueError as e:
        raise ValueError(f"Erro no peso: {e}")

@app.route('/')
def index():
    return render_template('formulario.html')

@app.route('/enviar_informacoes', methods=['POST'])
def enviar_informacoes():
    nome = request.form['nome']
    idade = request.form['idade']
    peso = request.form['peso']
    
    try:
        idade = validar_idade(idade)
        peso = validar_peso(peso)
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