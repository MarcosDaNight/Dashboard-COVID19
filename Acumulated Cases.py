from matplotlib import pyplot as plt

days = ['28/02', '07/03', '09/03', '13/03', '15/03', '17/03',
        '19/03', '21/03', '23/03', '25/03', '27/03', '31/03', '02/04']

number_of_cases = [3, 77, 98,  200, 291, 621,
                   1128, 1891, 2433, 3417, 4256, 5717, 7910]

plt.plot(days, number_of_cases, color='blue', marker='o', linestyle='solid')

plt.title('Acumuleted Cases')

plt.show()
