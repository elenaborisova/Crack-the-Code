# Conditional Statements - Part 2

## 1.	Day of the week
Create a program which reads a whole number from the user and prints the day of the week to which this number corresponds. If the number is invalid, print “Error”. 

*Example input and output*
|       Input       |      Output       |
|-------------------|-------------------|
|1                  |Monday         |
|2                  |Tuesday         |
|3                  |Wednesday         |
|4                  |Thursday         |
|5                  |Friday         |
|6                  |Saturday         |
|7                  |Sunday         |
|-1                  |Error         |



## 2.	Weekend and work day
Create a program which reads a day of the week (text) from the user. If the day is a work day, the program should print on the console “Work day”, if it is Saturday or Sunday, it should print “Weekend”. If the user inputs an invalid day, the program should print “Error”.

*Example input and output*
|       Input       |      Output       |
|-------------------|-------------------|
|Monday                  |Work day         |
|Sunday                  |Weekend         |
|April                  |Error         |




## 3.	Type Animal
Create a program that prints the type of an animal depending on the animal’s name, inputted by the user. There are 2 types:  
1.	dog -> mammal  
2.	crocodile, tortoise, snake -> reptile  
3.	others -> unknown  

*Example input and output*
|       Input       |      Output       |
|-------------------|-------------------|
|dog                  |mammal         |
|snake                  |reptile         |
|cat                  |unknown         |



## 4.	Age and gender
Create a program which reads an age (floating point number) and gender (‘m’ of ‘f’) from the user, and prints one of the following:  
•	"Mr." – male (gender 'm') with age 16 or older  
•	"Master" – male (gender 'm') under 16 years  
•	"Ms." – female (gender 'f') 16 or older  
•	"Miss" – female (gender 'f') under 16  

*Example input and output*
|       Input       |      Output       |
|-------------------|-------------------|
|12<br>f                  |Miss         |
|17<br>m                  |Mr.         |
|25<br>f                  |Ms.         |
|13.5<br>m                  |Master         |




## 5.	Grocery store
There are different grocery stores in 3 cities that sell several items at different prices in each city:

|city/products   |__coffee__   |__water__   |__beer__   |__sweets__   |__peanuts__ |
|---|:-:|---|---|---|---|
|__Madrid__   |0.50   |0.80   |1.20   |1.45   |1.60 |
|__Paris__   |0.40   |0.70   |1.15   |1.30   |1.50 |
|__London__   |0.45   |0.70   |1.10   |1.35   |1.55 |


Create a program which reads a product (text), city (text), and quantity (decimal number) from the user; and calculates and prints the total cost of the product in the specific city.

*Example input and output*
|       Input       |      Output       |
|-------------------|-------------------|
|coffee<br>London<br>2                  |0.9         |
|peanuts<br>Paris<br>1                  |1.5         |
|beer<br>Madrid<br>6                  |7.2         |
|water<br>Paris<br>3                  |2.1         |
|sweets<br>Madrid<br>2.23                  |3.2335         |




## 6.	Number in the interval 
Create a program that checks whether a number (user input) is in the interval [-100, 100] and is not 0. If the number follows the conditions, print “Yes”, if it doesn’t, print “No”.

*Example input and output*
|       Input       |      Output       |
|-------------------|-------------------|
|-25                  |Yes         |
|0                  |No         |
|25                  |Yes         |



## 7.	Opening hours
Create a program that reads a time of the day (whole number) and a day of the week (text) from the user and checks whether the office is open. Office’s opening hours are 10-18h from Monday to Saturday (including). 

*Example input and output*
|       Input       |      Output       |
|-------------------|-------------------|
|11<br>Monday                  |open         |
|19<br>Friday                  |closed         |
|11<br>Sunday                  |closed         |



## 8.	Cinema ticket
Create a program which reads a day of the week (text) from the user and prints on the console the price of the cinema ticket depending on the day of the week:

| Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday |
|  :---: |  :---:  |  :---:    |  :---:   |  :---: |  :---:   |  :---: |
|12      |12       |14         |14        |12      |16        |16      |

*Example input and output*
|       Input       |      Output       |
|-------------------|-------------------|
|Monday                  |12         |
|Friday                  |12         |
|Sunday                  |16         |



## 9.	Fruit or vegetable
Create a program which reads a name of a product from the user and checks whether it is a fruit or vegetable:  
•	Fruit can be:  banana, apple, kiwi, cherry, lemon и grapes;  
•	Vegetable can be:  tomato, cucumber, pepper и carrot;  
•	Anything else: "unknown".  

*Example input and output*
|       Input       |      Output       |
|-------------------|-------------------|
|banana                 |fruit         |
|apple                  |fruit         |
|tomato                  |vegetable         |
|water                  |unknown         |



## 10.	Invalid number
A number is valid if it is in the interval [100…200] or it is 0. Create a program which reads a whole number from the user and prints “invalid” if the number is not valid.

*Example input and output*
|       Input       |      Output       |
|-------------------|-------------------|
|75                 |invalid         |
|150                  |(no output)         |
|220                  |invalid         |
|199                  |(no output)         |
|-1                  |invalid        |
|100                  |(no output)         |
|200                  |(no output)         |
|0                  |(no output)         |


