import requests
from bs4 import BeautifulSoup

url = 'https://www.rainhadobrasil.com.br/lancamentos'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
ultimaPagina = soup.find('a', href='?pagina=4').get_text().strip()

ultimaPagina = int(ultimaPagina)

for i in range(1, (ultimaPagina+1)):
    
    url_atual = f'https://www.rainhadobrasil.com.br/lancamentos?pagina={i}'
    print('\n * * * * * * * * * * ' + url_atual + ' * * * * * * * * * * \n')

    site = requests.get(url_atual, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    todosLancamentos = soup.find_all('div', class_='info-produto')
    
    with open('PrecoCamisetas.csv', 'a', newline='', encoding='UTF-8') as f:
        
        for camisetas in todosLancamentos:
            try:
                descricao = camisetas.find('a', class_='nome-produto cor-secundaria').get_text().strip()
                price = camisetas.find('strong', class_='preco-venda cor-principal').get_text().strip()
                price = price[26:]
                
            except:
                descricao = 'vazio'
                price = '0'
                    
            linhaTabela = descricao + '   preço: R$' + price + '\n'
            print(linhaTabela)
              
            f.write(linhaTabela)
    print('')

