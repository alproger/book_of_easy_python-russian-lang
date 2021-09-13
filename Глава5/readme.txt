Текстовые строки
Упражнения
5.1. Напишите с заглавной буквы слово, которое начинается с буквы m:
>>> song = """When an eel grabs your arm,
... And it causes great harm,
... That's - a moray!"""
5.2. Выведите на экран все вопросы из списка, а также правильные ответы в таком
виде:
Q: вопрос
A: ответ
>>> questions = [
...
"We don't serve strings around here. Are you a string?",
...
"What is said on Father's Day in the forest?",
...
"What makes the sound 'Sis! Boom! Bah!'?"
...
]
>>> answers = [
...
"An exploding sheep.",
...
"No, I'm a frayed knot.",
...
"'Pop!' goes the weasel."
...
]
5.3. Выведите на экран следующее стихотворение, используя старый стиль форма-
тирования. Подставьте в него такие строки: 'roast beef' , 'ham' , 'head' и 'clam' :
My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat fell on his %s
And now thinks he's a %s.

5.4. Напишите письмо с использованием нового стиля форматирования. Сохраните
предложенную строку в переменной letter (она понадобится вам в упражнении
ниже):
Dear {salutation} {name},
Thank you for your letter. We are sorry that our {product}
{verbed} in your {room}. Please note that it should never
be used in a {room}, especially near any {animals}.
Send us your receipt and {amount} for shipping and handling.
We will send you another {product} that, in our tests,
is {percent}% less likely to have {verbed}.
Thank you for your support.
Sincerely,
{spokesman}
{job_title}
5.5. Присвойте значения переменным 'salutation' , 'name' , 'product' , 'verbed'
(глагол в прошедшем времени), 'room' , 'animals' , 'percent' , 'spokesman'
и 'job_title' . С помощью функции letter.format() выведите на экран значе-
ние переменной letter , в которую подставлены эти значения.
5.6. После проведения публичных опросов с целью выбора имени появились: ан-
глийская подводная лодка Boaty McBoatface, австралийская беговая лошадь
Horsey McHorseface и шведский поезд Trainy McTrainface. Используйте фор-
матирование с символом % для того, чтобы вывести на экран победившие имена
для утки, тыквы и шпица.
5.7. Сделайте то же самое с помощью функции format() .
5.8. А теперь еще раз с использованием f-строк.
