import requests

class infoNegara:
    def __init__(self, nama, ibukota, matauang, populasi):
        self.nama = nama
        self.ibukota = ibukota
        self.matauang = matauang
        self.populasi = populasi

class libraryNegara:
    def get_info_negara(self, nama_negara):
        url = f"https://restcountries.com/v2/name/{nama_negara}"
        response = requests.get(url)

        if response.status_code == 200:
            data_negara = response.json()[0]
            nama = data_negara['name']
            ibukota = data_negara['capital']
            matauang = data_negara['currencies'][0]['name']
            populasi = data_negara['population']

            info_negara = infoNegara(nama, ibukota, matauang, populasi)
            return info_negara
        else:
            return None
