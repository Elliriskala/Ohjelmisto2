# Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.
# Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan
# tekstin sekä lämpötilan Celsius-asteina. Perehdy rajapinnan dokumentaatioon riittävästi.
# Palveluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key).
# Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.

import requests

paikkakunta = input("Minkä paikkakunnan säätilan haluat tietää? ")

request = f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid=6fee9e90dcf3e47bb04a56828c171eee"

try:
    response = requests.get(request).json()
    print(f"Paikkakunnassa {paikkakunta} lämpötila: {response['main']['temp'] - 273.15:.1f} celsius-astetta.")
    print(f"Säätila: {response['weather'][0]['main']}.")
except requests.exceptions.RequestException as error:
    print("Network connection failed.")



