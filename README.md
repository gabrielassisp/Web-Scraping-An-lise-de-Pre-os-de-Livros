# 📚 Web Scraping & Análise de Preços de Livros

## 💡 Sobre o projeto
Este projeto tem como objetivo demonstrar a aplicação de **web scraping** para coleta de dados reais e posterior análise exploratória e visualização. Utilizei o site [Books to Scrape](http://books.toscrape.com/) como base para extrair informações de livros disponíveis no catálogo.

## 🎯 Objetivos
- Automatizar a coleta de informações (título, preço e disponibilidade) diretamente do site.
- Organizar os dados em um **DataFrame** e salvar em CSV para análises futuras.
- Realizar análises exploratórias e gerar gráficos que facilitem insights sobre preços.

## 🕸️ Tecnologias e bibliotecas
- **Python** 
- `requests`
- `BeautifulSoup`
- `pandas`
- `matplotlib`
- `seaborn`

## 🔎 Dados coletados
- **Título do livro**
- **Preço (£)**
- **Disponibilidade em estoque**

As informações foram extraídas das 5 primeiras páginas do site, resultando em um conjunto representativo de livros.

## 📊 Análises realizadas
- **Histograma de preços**: Para visualizar a distribuição geral dos preços no catálogo.
- **Gráfico de barras dos 5 livros mais caros**: Destaque dos livros premium disponíveis.
- Estatísticas descritivas básicas para entender faixa de preços e dispersão.

## 💬 Principais insights
- A maior parte dos livros está concentrada na faixa de **£10 a £40**, indicando um posicionamento mais acessível.
- Alguns livros premium superam £50, mostrando potencial para segmentação em nichos de maior valor.
- A coleta também permite verificar disponibilidade, podendo ser usada em análises futuras de estoque ou previsão de demanda.

## 💾 Como executar
1. Clone este repositório.
2. Instale as dependências:
   ```bash
   pip install requests beautifulsoup4 pandas matplotlib seaborn
Execute o script de scraping:

bash
Copiar
Editar
python webscraping_livros.py
Abra e explore o arquivo CSV gerado (livros_webscraping.csv).

Execute o script de demonstração para visualizar gráficos:

bash
Copiar
Editar
python analise_livros.py
📥 Arquivos disponíveis
webscraping_livros.py: Script responsável pela coleta dos dados.

analise_livros.py: Script de análise e geração de gráficos.

livros_webscraping.csv: Base de dados gerada (exemplo).

🚀 Resultados
Este projeto demonstra minha habilidade em:

Automatizar processos com Python.

Coletar e tratar dados externos.

Transformar dados brutos em insights visuais e práticos.

Utilizar bibliotecas de visualização para comunicação clara e objetiva.
