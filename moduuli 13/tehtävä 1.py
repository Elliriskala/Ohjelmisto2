# Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei.
# Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin. Esimerkiksi lukua 31
# vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31.
# Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.

from flask import Flask, request, Response
import json


app = Flask(__name__)

@app.route('/')
def get_root():
    return 'Prime number calculator:'

# jos luku on alle kaksi, niin koodia on turha suorittaa
@app.route('/isPrime/<number>')
def isPrime(number):
    try:
        number = int(number)
    except ValueError:
        response_data = {
            'msg': 'Input is not an integer',
            'input_number': number
        }
        status_code = 400
    else:
        if number >= 2:
            isPrime = True
            for i in range(2, number):
                if number % i == 0:
                    isPrime = False
            response_data = {
                'input number': number,
                'isPrime': isPrime
            }
            status_code = 200
        else:
            response_data = {
                'msg': 'Input out of bounds',
                'input number': number
            }
            status_code = 400

    response_data = json.dumps(response_data)
    response = Response(response=response_data, status=status_code, mimetype='application/json')
    return response

@app.errorhandler(404)
def page_not_found(error_code):
    answer = {
        "status" : "404",
        "msg" : "Url not found"
    }
    json_ans = json.dumps(answer)
    return Response(response=json_ans, status=404, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)