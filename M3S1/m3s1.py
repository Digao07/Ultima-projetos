import requests

url_marcas = "https://parallelum.com.br/fipe/api/v1/carros/marcas/7/modelos"
headers = {
    "User-Agent": "MyApp/1.0"
}

response = requests.get(url_marcas, headers=headers)

if response.status_code == 200:

    data = response.json()
else:
    print("Ocorreu um erro ao obter os dados da API.")


class MarcaCarro:
    
    def __init__(self, id_marca: str):
        
        
        id = id_marca

  
        url = f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{id}/modelos"

     
        response = requests.get(url_marcas, headers=headers)

  
        data = response.json()
        
      
        self.modelos = data["modelos"]
        
     
        self.current = 0
        self.end = len(self.modelos)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        result = self.modelos[self.current]
        self.current += 1
        return result
    
bit = MarcaCarro('7')


for modelo in bit:
    print(f"Os modelos são {modelo['nome']}")