# Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia
# vastaavan lentokentän nimen ja kaupungin JSON-muodossa.
# Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta.
# Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa:
# http://127.0.0.1:3000/kenttä/EFHK. Vastauksen on oltava muodossa:
# {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.

from flask import Flask, request, Response
import json
import tietokantahaku


app = Flask(__name__)
app.debug = True
@app.route('/')
def get_root():
    return 'Get airport with the ICAO code'

@app.route('/airport/<icao>')
def find_airport(icao):
    try:
        airport, city = tietokantahaku.get_ICAO(icao)
        status_code = 200
        response_data = {
            'ICAO': icao,
            'Name': airport,
            'Municipality': city
        }

    except ValueError:
        response_data = {
            'ICAO': icao,
            'msg': 'ICAO code not found'
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


