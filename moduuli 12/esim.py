import requests

# query = "emmerdale"
query = input("Anna hakusana: ")
request = f"https://api.tvmaze.com/search/shows?q={query}"

# print(requests.get("https://api.tvmaze.com/search/shows?q=girls").json())

def print_show_data(show_data):
    for show in show_data:
        if show["score"] > 0.5:  # suodatetaan hakutulos näyttämään vain isoimmat match scoret
            print(show["show"]["name"])
            # print(show["score"])
            # tulostetaan genret
            for genre in show["show"]["genres"]:
                print(f"- {genre}")


try:
    response_content = requests.get(request).json()
    # print(response_content)
    print_show_data(response_content)
except requests.exceptions.RequestException as error:
    print("Network connection failed.")
    # print(error)
