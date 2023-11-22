from flask import Flask, request, Response

app = Flask(__name__)

'''
# päätepiste / endpoint
@app.route('/')
def sano_moi():
    return "Heiiiii!"


@app.route('/tervehdys')
def tervehditään():
    return "Moikka!"

# argumentit
# http://127.0.0.1:3000/summa?num1=32&num2=34
@app.route('/summa')
def laske_summa():
    argumentit = request.args
    num1 = argumentit.get('num1')
    num2 = argumentit.get('num2')
    summa = int(num1) + int(num2)
    return {
        'summa': summa
    }

'''


# vaihtoehtoinen tapa
# http://127.0.0.1:3000/summa/32/34

@app.route('/sum/<first>/<last>')
def summa(first, last):
    first = int(first)
    last = int(last)
    for i in range(first, last + 1):
        sum = first + (first + i + 1)
    return {
        'first': first,
        'last': last,
        'sum': sum
    }


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
