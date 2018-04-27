
# importando a biblioteca flask
from flask import Flask
# habilitando o redirecionamento
from flask import abort, redirect, url_for
# importando a camada de persistencia, ou seja, os daos
from persistencia import *
# templates
from flask import render_template
# receber dados do formulario
from flask import request

# criando um objeto de Flask
app = Flask(__name__)

# definindo a rota index
@app.route('/')
def listar():
	anotacaoDAO = AnotacaoDAO()
	# return render_template("listar.html", vetAnotacao = anotacaoDAO.listar(), vetAnotacaoLixeira = anotacaoDAO.listar(True))
	return render_template("listar.html", vetAnotacao = anotacaoDAO.listar(), vetAnotacaoLixeira = anotacaoDAO.listar(True), nome = "Listagem...")

	# sem o uso de templates
	# o codigo fica misturado
	# retorno = "<table border='1'>"
	# vetAnotacao = anotacaoDAO.listar()
	# for a in vetAnotacao:
	# 	retorno = retorno + "<tr> <td> <a href='/excluir/"+ str(a.id) +"'> Excluir </a> </td> <td> " + a.titulo + "</td> </tr>"
	# retorno = retorno + "</table>"
	# return retorno

@app.route("/excluir/<id>")
def excluir(id):
	anotacaoDAO = AnotacaoDAO()
	anotacaoDAO.excluir(int(id))
	return redirect(url_for('listar'))

@app.route("/replicar/<id>")
def replicar(id):
	anotacaoDAO = AnotacaoDAO()
	anotacaoDAO.replicar(int(id))
	return redirect(url_for('listar'))

@app.route("/enviar_lixeira/<id>")
def enviar_lixeira(id):
	anotacaoDAO = AnotacaoDAO()
	anotacaoDAO.lixeira(int(id))
	return redirect(url_for('listar'))


@app.route("/restaurar_lixeira/<id>")
def restaurar_lixeira(id):
	anotacaoDAO = AnotacaoDAO()
	anotacaoDAO.lixeira(int(id), False)
	return redirect(url_for('listar'))

@app.route('/tela_alterar/<id>')
def tela_alterar(id):	
    return render_template("tela_alterar.html", anotacao = AnotacaoDAO().obter(int(id)))

@app.route('/tela_adicionar')
def tela_adicionar():	
    return render_template("tela_adicionar.html")


@app.route('/alterar', methods=['POST'])
def alterar():	
	anotacao = Anotacao()
	# por input hidden
	anotacao.id = int(request.form['id'])
	anotacao.titulo = str(request.form['titulo'])
	anotacao.descricao = str(request.form['descricao'])
	# print "====================="
	# print anotacao
	# print "====================="
	anotacaoDAO = AnotacaoDAO()
	anotacaoDAO.alterar(anotacao)
	return redirect(url_for("listar"))


@app.route('/adicionar', methods=['POST'])
def adicionar():	
	anotacao = Anotacao()
	anotacao.titulo = str(request.form['titulo'])
	anotacao.descricao = str(request.form['descricao'])
	# print "====================="
	# print anotacao
	# print "====================="
	anotacaoDAO = AnotacaoDAO()
	anotacaoDAO.adicionar(anotacao)
	return redirect(url_for("listar"))

# Como executa?

# Opcoes:

# 1) No terminal
# python main.py

# 2) No terminal:
# FLASK_APP=main.py FLASK_DEBUG=1 flask run

# Traduzindo o comando....
# Estou executando o arquivo main.py
# habilitei o debug

# startando....
if __name__ == '__main__':
	app.run(debug=True)