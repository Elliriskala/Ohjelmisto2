from flask import Flask, request, Response
import json

app = Flask(__name__)


@app.route('/')
def get_root():
    return 'Moro maailma!'


# example query: http://127.0.0.1:3000/kukkuu?name=Elli&age=22?moreparam=value
@app.route('/kukkuu')
def get_kukkuu():
    print(request.args)
    name = request.args.get('name')
    age = request.args.get('age')
    return f'no kukkuu vaan, {name}, {age} vuotta!'


# example query: http://127.0.0.1:3000/kukkuu/Elli/22
@app.route('/kukkuu/<name>/<age>')
def get_kukkuu_v2(name, age):
    return f'no kukkuu vaan, {name}, {age} vuotta!'


# example query: http://127.0.0.1:3000/multiply/5
# example response in json '{input_number: 5, result: 25}'
# input number must be between 0-100
@app.route('/multiply/<number>')
def multiply(number):
    try:
        number = int(number)
    except ValueError:
        response_data = {
            'msg': 'Input is not an integer',
            'input_number': number
        }
        status_code = 400
    else:
        if 0 < number < 100:
            result = number * number

            # response in dictionary format is translated to json automatically
            response_data = {
                'msg': 'Calculation done',
                'input number': number,
                'result': result
            }
            status_code = 200

        else:
            response_data = {
                'msg': 'Input out of bounds',
                'input number': number
            }
            status_code = 400

    # convert python dict to json format "manually"
    response_data = json.dumps(response_data)
    # setting up a status code for response needs Response object to be created
    response = Response(response=response_data, status=status_code, mimetype='application/json')
    return response


@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status": "404",
        "msg": "Url not found"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

