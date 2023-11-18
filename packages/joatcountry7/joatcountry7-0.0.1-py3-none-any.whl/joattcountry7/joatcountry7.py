import requests

class CountryInfo:
    def __init__(self, nama_negara):
        self.nama_negara = nama_negara
        self.url = f"https://restcountries.com/v3.1/name/{nama_negara}?fullText=true"
        self.country_info = self._get_country_info()

    def _get_country_info(self):
        response = requests.get(self.url)

        if response.status_code == 200:
            data = response.json()
            return data[0]
        else:
            print(f"Error: {response.status_code}")
            return None

    def print_info(self):
        if self.country_info:
            print("Nama Negara:", self.country_info['name']['common'])
            print("Kode Negara:", self.country_info['cca2'])
            print("Ibukota:", self.country_info['capital'])
            print("Populasi:", self.country_info['population'])
            print("Wilayah:", self.country_info['area'])
            print("Benua:", self.country_info['region'])
        else:
            print("Tidak dapat menemukan informasi negara.")
