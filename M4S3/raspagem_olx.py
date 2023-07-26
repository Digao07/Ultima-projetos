from requests_html import HTMLSession

sessao = HTMLSession()
imoveis = []
url = 'https://www.olx.com.br/imoveis/estado-go/grande-goiania-e-anapolis'
resposta = sessao.get(url)
links = resposta.html.find('#ad-list li a')
for link in links:
    url_imovel = link.attrs["href"]
    resposta_imovel = sessao.get(url_imovel)
    titulo = resposta_imovel.html.find('h1', first = True).text
    preco = resposta_imovel.html.find('h2')[0].text
    imoveis.append({
        'url': url_imovel,
        'titulo': titulo,
        'preco': preco
    })

print(imoveis)