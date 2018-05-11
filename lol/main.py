from flask import *
import sys
import os
from persistencia import *

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/home/iapereira/lol/static/arquivos/'
# para sessao
app.secret_key = "chave_secreta"

@app.route("/")
def tela_login():
	return render_template("tela_login.html")

@app.route("/deslogar")
def deslogar():
	session.pop('login', None)
	session.pop('senha', None)
	return redirect(url_for("tela_login"))


@app.before_request
def antes_da_rota():
	print "==========================="
	print "antes.................."
	print request.path
	print "============================="
	if request.path != '/' and request.path != '/login':
		if 'login' not in session and 'senha' not in session:		
			return render_template("erro.html", mensagem = "operacao proibida")


@app.route("/login", methods = ['POST'])
def login():
	login = request.form['login']
	senha = request.form['senha']
	if (login == 'admin' and senha == 'admin'):
		session['login'] = login
		session['senha'] = senha
		return redirect(url_for("index"))
	else:
		return render_template("erro.html", mensagem = "login invalido...")
		# return redirect(url_for("tela_login"))


@app.route("/index")
def index():
	jogadorDAO = JogadorDAO()
	return render_template("index.html", vetJogador = jogadorDAO.listar())

@app.route("/upload", methods = ['POST'])
def upload():
	jogador = Jogador()
	jogador.nome = str(request.form['nome'])
	jogadorDAO = JogadorDAO()
	id = jogadorDAO.adicionarNome(jogador)
	jogador.id = id
	f = request.files['arquivo']
	# f.save(app.config['UPLOAD_FOLDER'] + f.filename)
	f.save(app.config['UPLOAD_FOLDER'] + str(id) + ".png")
	jogador.foto = str(id) + ".png"
	jogadorDAO.alterar(jogador)
	return redirect(url_for("index")) 


@app.route("/excluir/<id>")
def excluir(id):
	jogadorDAO = JogadorDAO()
	jogador = jogadorDAO.obter(int(id))	
	if (jogador.foto):
		os.remove(app.config['UPLOAD_FOLDER'] + jogador.foto)	
	jogadorDAO.excluir(int(jogador.id))
	return redirect(url_for("index"))


if __name__ == '__main__':
	reload(sys)
	sys.setdefaultencoding('UTF-8')
	app.run()