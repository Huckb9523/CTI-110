Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Calculate sales predictions.
>>> #October, 4th, 2019.
>>> #CTI-110 P2T1 - Sales prediction.
>>> #Brandon Huck
>>> #
>>> 
>>> 
>>> #GEt the projected total sales.
>>> total_sales = float(input('Enter the projected sales: '))
Enter the projected sales: 1,000,000
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    total_sales = float(input('Enter the projected sales: '))
ValueError: could not convert string to float: '1,000,000'
>>> #Get the projected total sales.
>>> total_sales = float(input('Enter the projected sales: '))
Enter the projected sales: 1000
>>> #calculate the profit as 23 percent of total sales.
>>> profit = total_sales * 0.23
>>> #Display the profit.
>>> print('The profit is $', profit)
The profit is $ 230.0
>>> print('The profit is $', format(profit, ',.2f'))
The profit is $ 230.00
>>> 
