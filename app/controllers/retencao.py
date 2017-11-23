from app import db
import moment

# Verify SMS snet to client with LA 6262 
# This verification is in accordance with the conditions that evaluate the delivery of tbe retention SMS
def verify(num, start=None, end=None, day=None):
    
    con = db.connect()
    
    cur = con.cursor()
    
    # default parameters
    
    # start date default
    if start is None:
        start = moment.now().subtract(days=1).format("YYYY/MM/DD")
        if end is None:
            end = moment.now().subtract(days=1).format("YYYY/MM/DD")
    
    # end date default
    if end is None:
        end   = moment.now().format("YYYY/MM/DD")
    
    # day default
    # today
    if day is not None:
        start = moment.date(day).format("YYYY/MM/DD")
        end = moment.date(start).format("YYYY/MM/DD")
    
    
    # Query for verify the quantity SMS sent
    sql_sent = '''
    Select count(RECIP_ADDRESS_ADDRESS)
    from SMSC_CDR
    where MSG_ORIG_SUBM_TIME_DATE between TO_DATE('{start} 00:00', 'yyyy/mm/dd hh24:mi') and TO_DATE('{end} 23:59', 'yyyy/mm/dd hh24:mi')
    and ORIG_ADDRESS_ADDRESS = '6262'
    and ORIG_APPL_ID = 'VASGWCONECTA_TR'
    and RECIP_APPL_ID = 'tpgsm_0340_ifx_R'
    and RECIP_ADDRESS_ADDRESS like '%{num}'
    and MSG_STATUS = '0'
    '''.format(start=start, end=end, num=num)
    
    # Query for verify the quantity SMS response
    sql_res = '''
        Select count(RECIP_ADDRESS_ADDRESS)
        from SMSC_CDR
        where MSG_ORIG_SUBM_TIME_DATE between TO_DATE('{start} 00:00', 'yyyy/mm/dd hh24:mi') and TO_DATE('{end} 23:59', 'yyyy/mm/dd hh24:mi')
        and ORIG_ADDRESS_ADDRESS like '%{num}'
        and RECIP_APPL_ID = 'VASGWCONECTA_R'
        and RECIP_ADDRESS_ADDRESS = '6262'
        '''.format(start=start, end=end, num=num)
        
    
    resul_sent = cur.execute(sql_sent)
    
    qtd_sent = 0
    qtd_res = 0
    
    for row in resul_sent:
        qtd_sent = row[0]
    
        
        
    if qtd_sent > 0:
        resul_res = cur.execute(sql_res)
        qtd_res = 0
        for row in resul_res:
            qtd_res = row[0]
    else:
        status = False
    
    
    if (qtd_res >= qtd_sent) and (qtd_sent is not 0):
        status = True
    else:
        status = False
    
    res = {
        'number': int(num),
        'date_start': start,
        'date_end': end,
        'sent' : qtd_sent,
        'res' : qtd_res,
        'status' : status,
    }
    
    return res

# This function verify numbers  which are sent retention SMS
# return all numbers
def sent_framework(start=None, end=None, day=None):
    
    # start date default
    if start is None:
        start = moment.now().subtract(days=1).format("YYYY/MM/DD")
        if end is None:
            end = moment.now().subtract(days=1).format("YYYY/MM/DD")
    
    # end date default
    if end is None:
        end = moment.now().format("YYYY/MM/DD")
    
    
    # day default
    # today
    if day is not None:
        start = moment.date(day).format("YYYY/MM/DD")
        end = moment.date(start).format("YYYY/MM/DD")
    
    
    
    conn = db.connect_mssql()
    cur = conn.cursor()
    
    cur.execute("""
        SELECT * FROM VW_RETENCAO_SMS_ENVIADO WHERE DATAENVIO between '{start}' AND '{end}'
    """.format(start=start, end=end))


    return list(cur)