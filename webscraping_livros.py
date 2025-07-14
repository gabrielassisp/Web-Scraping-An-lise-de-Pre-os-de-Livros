import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# URL base
base_url = "http://books.toscrape.com/catalogue/page-{}.html"

# Listas para armazenar os dados
titulos = []
precos = []
estoques = []

for pagina in range(1, 6):  # 5 primeiras páginas (pode aumentar)
    url = base_url.format(pagina)
    resposta = requests.get(url)
    resposta.encoding = "utf-8"
    soup = BeautifulSoup(resposta.text, "html.parser")
    
    livros = soup.find_all("article", class_="product_pod")
    
    for livro in livros:
        titulo = livro.h3.a["title"]
        
        preco = livro.find("p", class_="price_color").text
        preco = preco.replace("£", "").strip()
        preco = re.sub(r"[^\d.]", "", preco)
        
        disponibilidade = livro.find("p", class_="instock availability").text.strip()
        
        titulos.append(titulo)
        precos.append(float(preco))
        estoques.append(disponibilidade)

# Cria DataFrame
df = pd.DataFrame({
    "Título": titulos,
    "Preço (£)": precos,
    "Disponibilidade": estoques
})

# Salva CSV
df.to_csv(r"C:\Users\Gabriel\Desktop\Nova pasta\livros_webscraping.csv", index=False, encoding="utf-8-sig")
print("CSV gerado com sucesso!")
