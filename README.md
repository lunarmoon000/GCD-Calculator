# GCD-Calculator


![main_gif](https://media1.tenor.com/m/YqsR6Tq0ciIAAAAC/1984-literally1984.gif)
## General Description
The Euclidean Algorithm implemented with code!
## Instructions
download the python file gcd.py, run it on your terminal and you will see this:

```
Welcome to GCD Calculator
What would you like to calculate?
input two numbers separated by a comma, -1 to exit:
```
the input prompt loops until it gets a valid pair to work with.
If you type less than 2 numbers, it will print this:

```
not enough arguments! please input two numbers!
```

If you input invalid numbers such as "a", -2, or 0, it will print this:

```
at least one of those is not a valid number! try again!
```
But if you do input a valid pair , it will execute the Euclidean algorithm and stop the loop once it has printed the outcome.
```
gcd( 421 , 134 )

421 / 134 = 3 r 19
-------------------------
134 / 19 = 7 r 1
-------------------------
19 / 1 = 19 r 0
-------------------------
gcd = 1
```
Alternatively, if you want to exit the loop without getting a GCD, type -1 and the program will print this and end:

```

Goodbye!

```
