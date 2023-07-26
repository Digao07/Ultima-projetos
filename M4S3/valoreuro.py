from requests_html import HTMLSession
sessao = HTMLSession()
campo = '#taxa-comercial'
url = 'https://www.melhorcambio.com/euro-hoje'
resposta = sessao.get(url)
euro = resposta.html.find(campo, first=True)
print(euro)
print(euro.attrs['value'])