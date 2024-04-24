
import matplotlib.pyplot as plt

# Data
my_list = [i * 1.5 for i in range(20)]
res =[5211.666666666667, 2852.3, 4134.1, 2540.222222222222, 2020.0, 1666.2222222222222, 1612.4, 2103.0, 940.6, 752.2, 1479.4, 1867.9, 1307.4, 1675.2, 779.5, 2165.7, 1678.5, 1181.3, 1247.8, 1906.2]
full_data = [[], [78, 1375, 39, 486, 551, 183, 1435, 33, 1308, 279], [7158, 1385, 1387, 1811, 8256, 1562, 2246, 595, 4467, 568], [1759, 3398, 5329, 3791, 8261, 3062, 668, 8064, 2352], [1298, 6146, 1208, 6426, 5035, 6981, 7309, 972], [9497, 6493, 2462, 2297, 1759], [3079, 4028, 712, 101, 5338, 2562], [1205, 2213, 1023, 956, 9465, 3613, 1134], [2066, 2422, 649, 1085, 3145, 7039, 7289, 5357], [3144, 4015, 2306, 4346, 5902, 1247, 3094, 4136, 4524], [3333, 4038, 3708, 4421, 449, 2275, 345, 4173, 1508, 856], [3693, 25, 2843, 1130, 6855, 1152, 5418, 3361, 6819], [2544, 1175, 2064, 1158, 1777, 154, 1540, 489, 775, 1084], [1479, 531, 3202, 3946, 1946, 1618, 1576, 462, 2495, 8551], [1167, 1577, 1384, 2087, 316, 441, 479, 5705, 121, 1468], [458, 344, 84, 1794, 2128, 2452, 4090, 490, 146, 1576], [1089, 1703, 164, 503, 1432, 685, 1333, 229, 821, 522], [1565, 58, 151, 1513, 1598, 924, 187, 1046, 928, 320], [1965, 336, 594, 345, 251, 315, 569, 959, 530, 178], [815, 1593, 384, 304, 744, 421, 232, 187, 151, 398]]


# Plot
plt.plot(my_list, res, marker='o', linestyle='-')

# Labels and Title
plt.xlabel('Travel Step Amount')
plt.ylabel('Time Step of Synchronization')
plt.title('Effect of Travel Step Amount on Firefly Synchronization Time')

# Show plot
plt.grid(True)
plt.savefig('reports/graphs/travel_step.png')

plt.show()
