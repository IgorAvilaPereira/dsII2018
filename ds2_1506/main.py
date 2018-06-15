from flask import *
from persistencia import *
import json

app = Flask(__name__)

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route('/')
def index():
    return render_template("index.html")
        
        
@app.route('/ajax', methods = ['POST'])
def ajax_request():
    username = request.form['username']
    return jsonify(username=username)

@app.route('/ajax_igor', methods = ['POST'])
def ajax_igor_request():
    campo = request.form['campo']

    # busca somente uma unica noticia
    # noticia = NoticiaDAO().busca(campo)
    
    vetNoticia = []

    # se o campo nao veio em branco
    if (len(campo) > 0):
        vetNoticia = NoticiaDAO().busca2(campo)
    
    resultado = ""
    for n in vetNoticia:
        resultado = resultado + n.obj2Str() +  "<br>"
    return resultado

    # SERIA O CORRETO
    # return json.dumps(vetNoticia)
    # return jsonify(titulo=noticia.titulo, texto=noticia.texto)
    
    
if __name__ == "__main__":
    app.run(debug = True)