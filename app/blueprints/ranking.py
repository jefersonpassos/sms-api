from flask import current_app, request, Blueprint
import moment

from app.controllers.ranking import topSMS

ranking_blueprint  = Blueprint('ranking',__name__)

# Essa rota retorna o raking de clientes com o envio de SMS mais altos
# Essa rota possui tres parametros opcionais
# @limit < 10 > determina a quantidade maxima de clientes que serao retornados 
# @Start [yyyy-mm-dd hh:mm] <  now - 1 day > determina a data inicial na qual sera contabilizado a quantidade de envios
# @end [yyyy-mm-dd hh:mm] < now > determina a data final na qual sera contabilixado a quantidade de envios
@ranking_blueprint.route('/', methods=['GET'])
def rankingSMS():
    
        limit = request.args.get('limit', 10)
        start = request.args.get('start', moment.now().subtract(days=1).format("YYYY-MM-DD HH:mm"))
        end   = request.args.get('end', moment.now().format("YYYY-MM-DD HH:mm"))
        
        # convet a data para o formato ISO
        start = moment.utc(start).format("YYYY-MM-DD HH:mm")
        end   = moment.utc(end).format("YYYY-MM-DD HH:mm")
        
        return topSMS(limit, start, end)

