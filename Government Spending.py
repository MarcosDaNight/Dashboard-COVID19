
from matplotlib import pyplot as plt

#data speding from Federal Government Plan
planes = ['Transferência para saúde', 'FPE e FPM', 'Assistência Social', 'Suspensão de dívidas da União', 'Renegociação com bancos']

spend = [8, 16, 2, 12.6, 9.3]

plt.axis("equal")

plt.pie(spend, labels=planes, autopct='%1.2f%%')

plt.title("Sepending for Federal Governmnt Plan")



