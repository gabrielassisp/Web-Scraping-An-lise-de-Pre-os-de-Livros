import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar CSV gerado
df = pd.read_csv("books_scraping.csv")

# Informações gerais
print(df.info())
print(df.describe())

# Histograma geral
plt.figure(figsize=(10, 5))
sns.histplot(df["Preço (£)"], bins=20, color="skyblue", kde=True)
plt.title("Distribuição de Preços dos Livros")
plt.xlabel("Preço (£)")
plt.ylabel("Quantidade de Livros")
plt.show()

# Gráfico de barras Top 5
top5 = df.sort_values(by="Preço (£)", ascending=False).head(5)

plt.figure(figsize=(12, 6))
bars = plt.bar(top5["Título"], top5["Preço (£)"], color="orange")
plt.title("Top 5 Livros Mais Caros")
plt.ylabel("Preço (£)")

# Rotaciona menos e ajusta para não cortar
plt.xticks(rotation=30, ha="right", wrap=True)

# Adiciona rótulos de dados
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, f"£{yval:.2f}", ha="center", va="bottom", fontsize=9)

plt.tight_layout()
plt.show()

# Print texto
print("Top 5 livros mais caros:")
print(top5[["Título", "Preço (£)"]])
