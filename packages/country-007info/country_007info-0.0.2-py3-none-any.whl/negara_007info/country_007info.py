# country_info.py
import requests

def get_country_info(nama_negara):
    url = f"https://restcountries.com/v3.1/name/{nama_negara}?fullText=true"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data[0]
    else:
        print(f"Error: {response.status_code}")
        return None

def print_country_info(country_info):
    print("Nama Negara:", country_info['name']['common'])
    print("Kode Negara:", country_info['cca2'])
    print("Ibukota:", country_info['capital'])
    print("Populasi:", country_info['population'])
    print("Wilayah:", country_info['area'])
    print("Benua:", country_info['region'])
