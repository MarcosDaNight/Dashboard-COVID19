from matplotlib import pyplot as plt

#data speding from Federal Government Plan
planes = ['Transferência para saúde', 'FPE e FPM', 'Assistência Social', 'Suspensão de dívidas dos estados com a União', 'Renegociação com bancos', 'federais', 'crédito']

spend = [8, 16, 2, 12.6, 9.6]

xs = [i + 0.1 for i, _ in enumerate(planes)]

plt.bar(xs, spend)

plt.ylabel("Spending for Bilions of R$")
plt.title("Sepending for Federal Governmnt Plan ")

plt.xticks([i + 0.5 for i, _ in enumerate(planes)], planes)
plt.show()