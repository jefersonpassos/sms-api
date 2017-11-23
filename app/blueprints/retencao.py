from app.controllers import retencao
from flask import current_app, request, Blueprint
import moment

retencao_blueprint  = Blueprint('retencao',__name__)

# rota para consultar quantidade de SMS enviados para o <number> e quantidade de respondidos para o 6262
@retencao_blueprint.route('/<number>', methods=['GET'])
def valid(number):
    
    start = request.args.get('start', None)
    end   = request.args.get('end', None)
    day = request.args.get('day', None)
    
    return retencao.verify(number, start, end, day)
    
# rota retorna todos o numeros que estao na lista do framework para receber SMS de retencao
@retencao_blueprint.route('/sent', methods=['GET'])
def sent():
    start = request.args.get('start', None)
    end   = request.args.get('end', None)
    day = request.args.get('day', None)
    
    return retencao.sent_framework(start, end, day)