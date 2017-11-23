import cx_Oracle
import moment
from app.db import db

# Retorna o ranking de clientes com mais envios de SMS
# < limit, 10 > determina a quantidade de clientes que serao retornados
# < start [YYYY-MM-DD hh24:mi], now - 1 day > determina data inicial na qual sera contabilizado os envios
# < end [YYYY-MM-DD hh24:mi], now >  determina a data final na qual sera contabilizado os envios
def topSMS(limit=10, start=None, end=None):
    
    # inicia conexo com o banco de dados
    con = db.connect()
    
    # inicia cursor
    cur = con.cursor()
    
    # data inical padrao
    if start is None:
        start = moment.now().subtract(days=1).format("YYYY-MM-DD HH:mm")
    
    # data final padrap
    if end is None:
        end   = moment.now().format("YYYY-MM-DD HH:mm")
        
    # Qurery de busca
    sql = '''select max(total) as total, ORIG_ADDRESS_ADDRESS  as ORIG
            from (Select  ORIG_ADDRESS_ADDRESS, Count(ORIG_ADDRESS_ADDRESS) as total
                           from SMSC_CDR
                           where MSG_ORIG_SUBM_TIME_DATE >= TO_DATE('{start}', 'yyyy-mm-dd hh24:mi')
                           and MSG_ORIG_SUBM_TIME_DATE <= TO_DATE('{end}', 'yyyy-mm-dd hh24:mi')
                           group by ORIG_ADDRESS_ADDRESS
                           order by Count(ORIG_ADDRESS_ADDRESS) DESC)
                           
           Where ROWNUM <= {limit}
           group by ORIG_ADDRESS_ADDRESS
           order by total DESC'''.format(start=start, end=end, limit=limit)
    
    cur.execute(sql)
    
    # convert as linhas em dict list
    return db.rows_to_dict_list(cur)