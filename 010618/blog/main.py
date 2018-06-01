from flask import * 
from persistencia import *
from jinja2 import TemplateNotFound

# declarando meu modulo
admin = Blueprint('admin', __name__,
                        template_folder='admin/templates', static_folder = 'admin/static')

# declarando as rotas deste meu modulo
@admin.route('/')
def tela_login():
	return render_template("tela_login.html")	

@admin.before_request
def antes():	
	app.logger.debug(request.path)
	if ( request.path == "/admin/" or request.path == "/admin/login"):
		app.logger.debug("entrou aqui")			
	elif ('login' not in session and 'senha' not in session):
		app.logger.warning("entrou no segundo...")
		return "erro...faca login corretamente"		


@admin.route("/tela_adicionar")	
def tela_adicionar():
	return render_template("tela_adicionar.html")


@admin.route("/adicionar", methods = ['POST'])	
def adicionar():
	titulo = request.form['titulo']
	texto = request.form['texto']
	noticia = Noticia(titulo, texto)
	try:
		NoticiaDAO().adicionar(noticia)
		return render_template("pagina_inicial.html", vetNoticia = NoticiaDAO().listar())
	except Exception as e:
		# app.logger.error(str(e))
		return "deu erro no adicionar...."

	

@admin.route("/login", methods = ['POST'])	
def login():
	login = request.form['login']
	senha = request.form['senha']
	if (login == 'admin' and senha == 'admin'):
		session['login'] = login
		session['senha'] = senha
		return render_template("pagina_inicial.html", vetNoticia = NoticiaDAO().listar())
	else:
		flash("senha incorreta...no tenes senha corretita")
		return redirect("/admin/")
		# return "senha incorreta...no tenes senha corretita"	

@admin.route("/logout")
def logout():
    session.pop('login', None)
    session.pop('senha', None)
    return redirect("/admin/")


# final do meu modulo

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

# vinculando o modulo a (Craseado) minha aplicacao
app.register_blueprint(admin, url_prefix='/admin')


@app.route('/')
def index():
	return render_template("listar.html", vetNoticia = NoticiaDAO().listar())

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404












if __name__=='__main__':
	app.run(debug=True)
	# app.run(host='127.0.0.1',port=8089,debug=True)