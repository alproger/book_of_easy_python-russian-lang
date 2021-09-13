# Текстовые строки
# 5.5
salutation= 'Hello'
name = 'Yakhyokhon'
product = 'product'
room = 'room no 12'
verbed = 'verbed'
amount = 'amount'
animals = 'cat , dog'
percent = '50'
spokesman = 'spokesman'
job_title = 'Supporter'

letter = """Dear {} {} , 
Thank you for your letter. We are sorry that our {}
{} in your {}. Please note that it should never 
be used in a {}, especially near any {}.

Send us your receipt and {} for shipping and handling.
We will send you another {} that, in our tests,
is {}% less likely to have {}.

Thank you for your support.
Sincerely,
{}
{}
""".format(salutation,name,product,verbed,room,room,animals,amount,product,percent,verbed,spokesman,job_title)
print(letter)