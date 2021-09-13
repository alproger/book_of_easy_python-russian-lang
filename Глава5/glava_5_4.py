# Текстовые строки
# 5.4
l_m = {
                     'salutation' : 'Hello',
                     'name' : 'Yakhyokhon',
                     'product' : 'product',
                     'room' : 'room no 12',
                     'verbed' : 'verbed',
                      'amount' : 'amount',
                     'animals' : 'cat , dog',
                     'percent' : '50',
                     'spokesman' : 'spokesman',
                     'job_title' : 'Supporter'
                   }
letter = f"""Dear {l_m['salutation']} {l_m['name']} , 
Thank you for your letter. We are sorry that our {l_m['product']}
{l_m['verbed']} in your {l_m['room']}. Please note that it should never 
be used in a {l_m['room']}, especially near any {l_m['animals']}.

Send us your receipt and {l_m['amount']} for shipping and handling.
We will send you another {l_m['product']} that, in our tests,
is {l_m['percent']}% less likely to have {l_m['verbed']}.

Thank you for your support.
Sincerely,
{l_m['spokesman']}
{l_m['job_title']}
"""
print(letter)