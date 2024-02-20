from flask import Flask, render_template, redirect, request, flash
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'EDUARDO'

logado = False

@app.route('/')
def home():
    global logado
    logado = False  #temos q definir 'logado' como False quando voltamos da pagina de adm
    return render_template('login.html')


@app.route('/admin')
def adm():
    if logado:
        with open('usuarios.json') as usuariosTemp:     
            usuarios = json.load(usuariosTemp)
        return render_template("admin.html", usuarios=usuarios)
    else:
        flash('ACESSO NÃO AUTORIZADO', 'acesso-negado')
        return redirect('/')
        


@app.route('/login', methods=['POST'])
def login():

    global logado       #define que a variável 'logado' pode ser usada dentro de funcoes

    nome = request.form.get('nome')
    senha = request.form.get('senha')

    with open('usuarios.json') as usuariosTemp:     #abre o arquivo json e joga em uma var temporaria
        usuarios = json.load(usuariosTemp)          #transforma o arquivo(TextIOWrapper) em uma lista q pode ser lida 

        count = 0

        if nome == 'adm' and senha == '000':
            logado = True
            return redirect('/admin')

        for usuario in usuarios:
            count += 1
            if usuario['nome'] == nome and usuario['senha'] == senha:
                return render_template("usuarios.html")
    
            if count >= len(usuarios):
                flash('USUARIO INVALIDO', 'acesso-negado')  #'acesso-negado' é um segundo argumento (classe para o css)
                return redirect("/")


@app.route('/cadastrarUsuario', methods=['POST'])     #rota quando o botão é clicado
def cadastrarUsuario():
    user = []                       #criamos uma lista para salvar os usuarios já cadastrados
    nome = request.form.get('nome')
    senha = request.form.get('senha')
    user = [
        {
            "nome": nome,
            "senha": senha
        }
    ]
    with open('usuarios.json') as usuariosTemp:
        usuarios = json.load(usuariosTemp)

    usuarioNovo = usuarios + user   #recebe a lista + os usuarios novos
    
    with open('usuarios.json', 'w') as gravarTemp:    #o 'w' escreve dentro da lista json
        json.dump(usuarioNovo, gravarTemp, indent=4)   #define uma identação de 4 linhas para os novos nomes e senhas  

    flash('USUARIO CADASTRADO')
    return redirect('/admin')

    




if __name__ in "__main__":
    app.run(debug=True)    


#O liveServer não executa o código python
    
#Para executar o código python e acessar a página, devemos usar
# a porta 5000 (onde o Flask a ouve)
    
#Devo usar o URL: http://127.0.0.1:5000
    
#Abrir o gitbash na pasta do arquivo python (root)
#digitar python main.py
#abrir o site no navegador com o URL acima