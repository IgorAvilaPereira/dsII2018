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
	# somente as rotas / e /login sao publicas. Para as demais rotas eh preciso estar, previamente, logado (sessao criada e setada)
	if request.path != '/' and request.path != '/login':
		if 'login' not in session and 'senha' not in session:		
			return render_template("erro.html", mensagem = "operacao proibida")

# somente por form (method post) que os dados devem ser direcionados para esta rota.
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

@app.route("/index")
def index():
	jogadorDAO = JogadorDAO()
	return render_template("index.html", vetJogador = jogadorDAO.listar())

@app.route("/upload", methods = ['POST'])
def upload():

	jogador = Jogador()
	jogador.nome = str(request.form['nome'])
	jogadorDAO = JogadorDAO()
	

	# se ha arquivo vindo do form
	if ('arquivo' in request.files):

		f = request.files['arquivo']	
		
		# mantendo o nome do arquivo
		# f.save(app.config['UPLOAD_FOLDER'] + f.filename)
		
		# renomeando o arquivo de acordo com o id do jogador (dado pelo sgbd)
		extensao = f.filename.rsplit('.', 1)[1].lower()

		if (extensao == 'png' or extensao == 'jpg' or extensao == 'jpeg'):
				
			jogador.id = jogadorDAO.adicionarNome(jogador)

			f.save(app.config['UPLOAD_FOLDER'] + str(jogador.id) + "." + extensao)

			# atualizando o objeto jogador (da memoria) com o nome de sua imagem
			jogador.foto = str(jogador.id) + "." + extensao
			
			# chamando o alterar a fim de atribuir o nome da foto a coluna que estava em branco
			jogadorDAO.alterar(jogador)
		
		else:
			return render_template("erro.html", mensagem = "formato de imagem nao suportado.")
	else:
		# adicionando o jogador sem imagem....
		jogador.id = jogadorDAO.adicionarNome(jogador)		
	
	return redirect(url_for("index")) 


@app.route("/excluir/<id>")
def excluir(id):
	jogadorDAO = JogadorDAO()
	jogador = jogadorDAO.obter(int(id))	
	# caso o jogador tenha foto
	if (jogador.foto):
		try:
			# eh preciso remover o arquivo (foto) do diretorio de arquivos
			os.remove(app.config['UPLOAD_FOLDER'] + jogador.foto)				
			jogadorDAO.excluir(int(jogador.id))
		except Exception as e:			
			return render_template("erro.html", mensagem = "imagem nao encontrada. nao foi possivel excluir o jogador...")			
	else:
		jogadorDAO.excluir(int(jogador.id))
	return redirect(url_for("index"))


if __name__ == '__main__':
	# para arrumar os acentos (principalmente no windows)
	reload(sys)
	sys.setdefaultencoding('UTF-8')
	app.run()