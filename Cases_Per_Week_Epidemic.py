from matplotlib import pyplot as plt

Cases_epidemic_confirmed = [2, 17, 102, 1007, 2775, 5153]

week_epidemic = ['9°', '10°', '11°', '12°', '13°', '14°']

xs = [i + 0.1 for i, _ in enumerate(week_epidemic)]

plt.bar(xs, Cases_epidemic_confirmed)

plt.ylabel('Number of Cases')
plt.title("Cases per epidemic week")

plt.xticks([i + 0.5 for i, _ in enumerate(week_epidemic)], week_epidemic)

plt.show()
