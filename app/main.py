from flask_api import FlaskAPI
from flask import request
from flask_cors import CORS, cross_origin

import os

from datetime import datetime
import moment

from .blueprints.ranking import ranking_blueprint
from .blueprints.retencao import retencao_blueprint

# def create_app(setting=None):
    
# Inicia uma aplicacap flask
app = FlaskAPI(__name__)

if 'FLASK_CONFIG' in os.environ.keys():
    app.config.from_object('app.settings.' + os.environ['FLASK_CONFIG'])
else:
    app.config.from_object('app.settings.Development')


# if setting:
#     # atribui as configuracoes na aplicacao
#     app.config.from_object(setting)

# configura cors
# Essa configuracao permite que todas as requisicoes possam ser feitas,
# eliminando os erros de Requests que ocorrem em alguns navegadores
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# Rota padrao
# deve ser utilizado antes de qualquer outra rota
route_default = '/api/sms'


app.register_blueprint(ranking_blueprint, url_prefix= route_default+ "/ranking") # route /ranking

app.register_blueprint(retencao_blueprint, url_prefix= route_default+ "/retencao") # route /retencao

    # return app