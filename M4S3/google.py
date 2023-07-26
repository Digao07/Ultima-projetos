from requests_html import HTMLSession
url = 'http://raspagem.herokuapp.com/'
sessao = HTMLSession()
resposta = sessao.get(url)
print(resposta.text)
print(resposta.status_code)