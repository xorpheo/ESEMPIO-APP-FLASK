# Importa la classe Flask dal modulo flask
from flask import Flask

# Crea un'istanza dell'app Flask
app = Flask(__name__)

# ---------------------------
# DEFINIZIONE DELLE ROUTE
# ---------------------------

# Route principale ('/')
@app.route('/')
def home():
    # Quando un utente visita http://localhost:5000/
    # Flask risponde con il messaggio 'OK'
    return "OK"

# Route /contatti
@app.route('/contatti')
def contatti():
    # Quando un utente visita http://localhost:5000/contatti
    # Flask risponde con una stringa HTML
    return "<h1>Pagina dei contatti</h1>"

# ---------------------------
# AVVIO DELL'APPLICAZIONE
# ---------------------------

if __name__ == '__main__':
    # Avvia il server Flask in modalità debug
    # (utile durante lo sviluppo per vedere errori e aggiornamenti automatici)
    app.run(debug=True, host='0.0.0.0', port=5000)