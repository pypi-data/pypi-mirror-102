# Wallet one payments
 
Python 3 module for processing wallet one payments 
!https://www.walletone.com/

 ## Python

```python
from wallet_one import Payment

payment = Payment(
    merchant_id='195751850197',
    secret='4436657a5c785f354b76314a6c4a666e6832695e58356a5c475c60',
    amount=1000.00,
    description='Your payment description',
    url_success='https://your.url/success',
    url_fail='https://your.url/fail',
)

>>> payment.form
{
    'WMI_MERCHANT_ID': '195751850197', 
    'WMI_PAYMENT_AMOUNT': '1000.0', 
    'WMI_CURRENCY_ID': '643', 
    'WMI_DESCRIPTION': 'Your payment description', 
    'WMI_SUCCESS_URL': 'https://your.url/success', 
    'WMI_FAIL_URL': 'https://your.url/fail', 
    'WMI_SIGNATURE': 'b1VngBA5Y3aiWlPLPEdG9w==',
}

>>> payment.signature
'b1VngBA5Y3aiWlPLPEdG9w=='

```
