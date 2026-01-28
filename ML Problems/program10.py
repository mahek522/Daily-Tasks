'''10. Write a Python program to find the real and imaginary parts of an array of complex
numbers.
Expected Output:
Original array [ 1.00000000+0.j 0.70710678+0.70710678j]
Real part of the array:
[ 1. 0.70710678]
Imaginary part of the array:
[ 0. 0.70710678] '''
#import numpy as np
#complex_arr = np.array([1+0j, 0.70710678+0.70710678j])
#print(complex_arr)
#real_part = np.real(complex_arr)
#imag_part = np.imag(complex_arr)
#print(real_part)
#print(imag_part)

import numpy as np

# Example sales data (30 days × 5 products)
sales = np.random.randint(-20, 100, size=(30, 5))

# Replace negative values with 0
sales[sales < 0] = 0
# Take only first 28 days (4 weeks)
weekly_data = sales[:28]

# Reshape to (4 weeks, 7 days, 5 products)
weekly_data = weekly_data.reshape(4, 7, 5)

# Total sales per week per product
weekly_sales = weekly_data.sum(axis=1)

# Average weekly sales per product
avg_weekly_sales = weekly_sales.mean(axis=0)

print("Average weekly sales per product:")
print(avg_weekly_sales)

highest_product = np.argmax(avg_weekly_sales)

print("Product with highest average weekly sales:", highest_product)
