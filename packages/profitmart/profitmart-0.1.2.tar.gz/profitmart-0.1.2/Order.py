import ProfitMart
import json
import utils
import customException

TRAN_BUY = 'B'
TRAN_SELL = 'S'

RET_DAY = 'DAY'
RET_IOC = 'IOC'
S_PRDT_ALI = 'CNC:CNC||CO:CO||MIS:MIS||NRML:NRML'

ORDER_SRC_TWS = 'TWS'  
ORDER_SRC_NESTREST = 'NEST_REST'

#key list for function args...
#key  =[publicKey4,publicKey4_hash,tomcatCount]

#All type of order...(Sent trigPrice='0' for non-trigger order)
def placeOrder(uid,exchg,ticker,direction,orderType,productType,qty,price,trigPrice,key):
    data_json = json.dumps({
    'Tsym': ticker,
    'exch': exchg,
    'Ttranstype': TRAN_BUY if direction=='Long' else TRAN_SELL,  # buy/sell    
    'prctyp': orderType,  #limit/market/SL order
    'Pcode': productType,   #MIS/CNC/CO/BO
    'Price': price,
    'qty': qty,
    'TrigPrice': trigPrice if trigPrice!='0' else '0',
    'Ret': RET_DAY,  # order is valid for entire day
    'orderSource': ORDER_SRC_TWS,
    'uid': uid,
    'actid': uid,   
    's_prdt_ali': S_PRDT_ALI,
    'discqty': '0',  # default
    'MktPro': 'NA',  # default
    'DateDays': 'NA',  # default
    'AMO': 'NO',    #not an AMO order
    'PosSquareFlg': 'N',    #not square-off
    'MinQty': '0'  # default
    })
    
    response = ProfitMart.POST('/PlaceOrder',utils.encryptKey(key[0],data_json.encode()),key[1],key[2])
    return response['NOrdNo']



#Cancel order...
def cancelOrder(uid,ordNo,key):
    data_json = json.dumps({
        'uid': uid,
        'NestOrd': ordNo,
        's_prdt_ali': S_PRDT_ALI
    })
    
    response = ProfitMart.POST('/CancelOrder',utils.encryptKey(key[0],data_json.encode()),key[1],key[2])
    return response['Result']

#Modify order...
def modifyOrder(uid,):
    pass

#get order Info...
def getOrderInfo(uid,ordNo,key):
    data_json = json.dumps({
        'uid': uid,
        's_prdt_ali': S_PRDT_ALI
    })

    response = ProfitMart.POST('/OrderBook',utils.encryptKey(key[0],data_json.encode()),key[1],key[2])
   
    for i in range(len(response)):
        if response[i]['Nstordno'] == ordNo:
            return response[i]
    
    #raise exception if order not found!
    raise customException.OrderNotFound(ordNo)
     

# try:
#     print(Order.getOrderInfo(uid,'210105000097245',key))
#     pass
# except Exception as e:
#     print(e.msg)
#     pass

