# Session 4 - For Loops


## 1.	Numbers from 1 to 100
Create a program which prints on the console the numbers from 1 to 100, each on a new line.

*Example input and output*
|       Input       |      Output       |
|-------------------|-------------------|
|(no input)                  |1<br>2<br>3<br>...<br>98<br>99<br>100         |




## 2.	Numbers from 1 to N with a step
Create a program which takes a number N from the user, and prints on the console the numbers from 1 to N with a step 3.

*Example input and output*
|       Input       |      Output       |
|-------------------|-------------------|
|10                 |1<br>4<br>7<br>10         |
|7                 |1<br>4<br>7         |
|15                 |1<br>4<br>7<br>10<br>13         |



## 3.	Even powers of 2
Create a program which takes a number N from the user, and prints on the console all the even powers of 2 until N. For more clarification, see the examples below:  
2 ≤ 2n: 20, 22, 24, 26, …, 2n. 

*Example input and output*
|       Input       |      Output       |
|-------------------|-------------------|
|3                 |1<br>4        |
|4                 |1<br>4<br>16         |
|5                 |1<br>4<br>16         |



## 4.	Numbers from N to 1 in reverse order
Create a program which takes a whole positive number N from the user, and prints the numbers from N to 1 in a reverse order (from the biggest to the smallest one).

*Example input and output*
|       Input       |      Output       |
|-------------------|-------------------|
|2                 |2<br>1        |
|3                 |3<br>2<br>1         |
|5                 |5<br>4<br>3<br>2<br>1         |




## 5.	Character sequence
Create a program that takes a text (string) from the user, and prints every symbol of the text on a new line.

*Example input and output*
|       Input       |      Output       |
|-------------------|-------------------|
|ieuniversity                 |i<br>e<br>u<br>n<br>i<br>v<br>e<br>r<br>s<br>i<br>t<br>y        |
|ice cream                 |i<br>c<br>e<br> <br>c<br>r<br>e<br>a<br>m         |



## 6.	Vowels sum
Create a program which takes a text (string) from the user, and calculates and prints the sum of the corresponding values of each vowel letter according to the table below:

|__letter__   |a   |e   |i   |o   |u |
|---|:-:|---|---|---|---|
|__value__   |1   |2   |3   |4   |5 |

*Example input and output*
|       Input       |      Output       |  Comment  | 
|-------------------|-------------------|-----------|
|hello |5      |e + o = 2 + 4 = 6 |
|hi  |3  |i = 3 |
|bamboo |9 |a + o + o = 1 + 4 + 4 = 9 |
|beer |4 |e + e = 2 + 2 = 4 |



## 7.	Sum numbers
Create a program which takes n count whole (integer) numbers from the user and sums them up.  
•	First line of input: count of numbers n  
•	On each of the following n lines: one integer number  
The program has to takes all numbers, sum them up and prints their sum.

*Example input and output*
|       Input       |      Output       |
|-------------------|-------------------|
|2<br>10<br>20                 |30        |
|3<br>-10<br>-20<br>-30                 |-60        |
|4<br>45<br>-20<br>7<br>11 |43 |



## 8.	Number sequence
Create a program which takes N count integer numbers. Print the biggest and the smallest number amongst them.


*Example input and output*
|       Input       |      Output       |
|-------------------|-------------------|
|5<br>10<br>20<br>304<br>0<br>50                 |Max number: 304<br>Min number: 0        |
|6<br>250<br>5<br>2<br>0<br>100<br>1000                 |Max number: 1000<br>Min number: 0        |




## 9.	Left and right sum
Create a program which takes N count from the user, and then for each N * 2 -> two more numbers inputted from the user. The program should check if the sum of the first pair is equal to the sum of the second pair of numbers.  
If the sums are equal, it should print “Yes, sum = “ + the sum  
If the sums are different, it should print “No, diff = “ + the difference  

*The difference is calculated as an absolute value (positive number)*  

*Example input and output*
|       Input       |      Output       |  Comment  | 
|-------------------|-------------------|-----------|
|2<br>10<br>90<br>60<br>40 |Yes, sum = 100      |10 + 90 = 60 + 40 = 100 |
|2<br>90<br>9<br>50<br>50 |No, diff = 1     |90 + 9 != 50 + 50<br>Difference = \|99-100\| = 1  |





