from django.shortcuts import render
import requests
import transbank
from transbank.webpay import webpay_plus
from transbank.webpay.webpay_plus.transaction import Transaction
from transbank.webpay.webpay_plus.mall_transaction import MallTransaction, MallTransactionCreateDetails
from transbank.webpay.webpay_plus import IntegrationType
from transbank.error.transbank_error import TransbankError
import random


def base(request):
       # El SDK apunta por defecto al ambiente de pruebas, no es necesario configurar lo siguiente
    try:
        # transbank.webpay.webpay_plus.webpay_plus_default_commerce_code = 597055555532
        # transbank.webpay.webpay_plus.default_api_key = "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C"
        # transbank.webpay.webpay_plus.default_integration_type = IntegrationType.TEST
        
        buy_order = str(random.randrange(1000000, 99999999))
        session_id = str(random.randrange(1000000, 99999999))
        amount = random.randrange(100000, 999999)       
        return_url = 'http://127.0.0.1:8000/exito'

        response = Transaction.create(buy_order, session_id, amount, return_url)
    
        token = request.GET.get("token_ws")
        response = Transaction.commit(token)

    except TransbankError as e:
        print(e.message)


    context = {
        'response': response,
        
    }
    
    return render(request, 'base.html', context)

def success(request):
    try:
        token = request.GET.get("token_ws")
        response = Transaction.commit(token)
        
    except TransbankError as e:
        print(e.message)

    context = {
        'response': response,
        
    }
    return render(request, 'success.html', context)
