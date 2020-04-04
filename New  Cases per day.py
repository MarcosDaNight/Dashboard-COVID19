from matplotlib import pyplot as plt

days = ['26/02', '29/02', '03/03', '06/03', '09/03', '12/03',
        '15/03', '18/03', '21/03', '24/03', '27/03', '30/03', '02/04']

number_of_cases = [1, 0, 4, 0, 25, 79, 137, 224, 418, 310, 502, 323, 1076]

plt.plot(days, number_of_cases, color='blue', marker='o', linestyle='solid')

plt.title('New Cases per Day')

plt.show()
