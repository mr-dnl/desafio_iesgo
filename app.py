from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configurações de conexão
db_config = {
    'user': 'user',
    'password': 'password',
    'host': 'host',
    'database': 'database'
}

# Rotas e operações CRUD aqui...

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
