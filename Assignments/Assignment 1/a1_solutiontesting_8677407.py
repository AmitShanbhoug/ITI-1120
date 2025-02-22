Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:\Users\AmitS\OneDrive\Documents\2018 Fall\ITI 1120\Assignment 1\a1_8677407.py 
>>> # testing Question 1
>>> 
>>> pythagorean_pair(2,2)
False
>>> pythagorean_pair(6,2)
False
>>> pythagorean_pair(6,8)
True
>>> pythagorean_pair(300,-400)
True
>>> 
>>> # testing Question 2
>>> 
>>> 
>>> mh2kh(5)
8.0467
>>> 
>>> mh2kh(110.4)
177.67113600000002
>>> 
>>> 
>>> # testing Question 3
>>> 
>>> in_out(0,0,2.5)
Enter a number for the x coordinate of a query point: 0
Enter a number for the y coordinate of a query point: 1.2
True
>>> in_out(2.5,1,1)
Enter a number for the x coordinate of a query point: -1
Enter a number for the y coordinate of a query point: 1.5
False
>>> in_out(-2.5,1,2.1)
Enter a number for the x coordinate of a query point: -1
Enter a number for the y coordinate of a query point: 1.5
True
>>> 
>>> 
>>> # testing Question 4
>>> 
>>> safe(93)
False
>>> safe(82)
True
>>> safe(29)
False
>>> safe(36)
False
>>> safe(9)
False
>>> safe(7)
True
>>> 
>>> 
>>> # testing Question 5
>>> 
>>> quote_maker("Everything should be made as simple as possible but not simpler.", "Albert Einstein", 1933)
'In 1933, a person called Albert Einstein said: "Everything should be made as simple as possible but not simpler."'
>>> quote_maker("I would never die for my beliefs because I might be wrong.", "Bertrand Russell", 1951)
'In 1951, a person called Bertrand Russell said: "I would never die for my beliefs because I might be wrong."'
>>> 
>>> 
>>> # testing Question 6
>>> 
>>> quote_displayer()
Give me a quote: The best lack all conviction while the worst are full of passionate intensity.
Who said that? Bertrand Russell
What year did she/he say that? 1960
In 1960, a person called Bertrand Russell said: "The best lack all conviction while the worst are full of passionate intensity."
>>> 
>>> 
>>> # testing Question 7
>>> 
>>> rps_winner()
What choice did player 1 make? 
Type one of the following options: 'rock', 'paper', 'scissors': rock
What choice did player 2 make? 
Type one of the following options: 'rock', 'paper', 'scissors': paper
Player 1 wins. That is False.
It is a tie. That is not True
>>> rps_winner()
What choice did player 1 make? 
Type one of the following options: 'rock', 'paper', 'scissors': paper
What choice did player 2 make? 
Type one of the following options: 'rock', 'paper', 'scissors': rock
Player 1 wins. That is True.
It is a tie. That is not True
>>> rps_winner()
What choice did player 1 make? 
Type one of the following options: 'rock', 'paper', 'scissors': scissors
What choice did player 2 make? 
Type one of the following options: 'rock', 'paper', 'scissors': paper
Player 1 wins. That is True.
It is a tie. That is not True
>>> rps_winner()
What choice did player 1 make? 
Type one of the following options: 'rock', 'paper', 'scissors': paper
What choice did player 2 make? 
Type one of the following options: 'rock', 'paper', 'scissors': paper
Player 1 wins. That is False.
It is a tie. That is not True
>>> 
>>> 
>>> # testing Question 8
>>> 
>>> fun(7)
0.25
>>> fun(20)
0.3404319590043982
>>> fun(999999997)
2.25
>>> fun(0.1)
0.12284042345856817
>>> 
>>> 
>>> # testing Question 9
>>> 
>>> ascii_name_plaque("vida")
**************
*            *
*  __vida__  *
*            *
**************
>>> ascii_name_plaque("Captain Kara 'Starbuck' Thrace")
****************************************
*                                      *
*  __Captain Kara 'Starbuck' Thrace__  *
*                                      *
****************************************
>>> ascii_name_plaque("Seven of Nine")
***********************
*                     *
*  __Seven of Nine__  *
*                     *
***********************
>>> 
>>> 
>>> # testing Question 10
>>> 
>>> draw_car()
>>> 
>>> 
>>> # testing Question 11
>>> 
>>> alogical(5.4)
3
>>> alogical(4)
2
>>> alogical(1000)
10
>>> alogical(4200231)
23
>>> 
>>> 
>>> # testing Question 12
>>> 
>>> time_format(8,0)
"8 o'clock"
>>> time_format(8,2)
"8 o'clock"
>>> time_format(8,59)
"9 o'clock"
>>> time_format(8,8)
"10 minutes past 8 o'clock"
>>> time_format(8,32)
"30 Half past 8 o'clock"
>>> time_format(8,48)
"10 minutes past 9 o'clock"
>>> time_format(17,42)
"20 minutes past 18 o'clock"
>>> 
 RESTART: C:\Users\AmitS\OneDrive\Documents\2018 Fall\ITI 1120\Assignment 1\a1_8677407.py 
>>> time_format(8,48)
"10 minutes to 7 o'clock"
>>> 
 RESTART: C:\Users\AmitS\OneDrive\Documents\2018 Fall\ITI 1120\Assignment 1\a1_8677407.py 
>>> time_format(8,48)
"10 minutes to 9 o'clock"
>>> time_format(17,42)
"20 minutes to 18 o'clock"
>>> time_format(23,13)
"15 minutes past 23 o'clock"
>>> time_format(23,42)
"20 minutes to 24 o'clock"
>>> time_format(0,29)
"30 Half past 0 o'clock"
>>> time_format(11,59)
"12 o'clock"
>>> time_format(23,58)
"24 o'clock"
>>> time_format(0,1)
"0 o'clock"
>>> time_format(11,1)
"11 o'clock"
>>> 
>>> 
>>> # testing Question 13
>>> 
>>> cad_cashier(10.58,11)
0.4
>>> cad_cashier(98.87,100)
1.15
>>> cad_cashier(10.58,15)
4.4
>>> cad_cashier(10.55,15)
4.45
>>> cad_cashier(10.54,15)
4.45
>>> cad_cashier(10.52,15)
4.5
>>> cad_cashier(10.50,15)
4.5
>>> 
>>> 
>>> # testing Question 14
>>> 
>>> min_CAD_coins(10.58,11)
(0, 0, 1, 1, 1)
>>> min_CAD_coins(98.87,100)
(0, 1, 0, 1, 0)
>>> min_CAD_coins(10.58,15)
(2, 0, 1, 1, 1)
>>> min_CAD_coins(10.55,15)
(2, 0, 1, 2, 0)
>>>  min_CAD_coins(10.54,15)
SyntaxError: unexpected indent
>>> min_CAD_coins(10.55,15)
(2, 0, 1, 2, 0)
>>> min_CAD_coins(10.52,15)
(2, 0, 2, 0, 0)
>>> min_CAD_coins(10.50,15)
(2, 0, 2, 0, 0)
>>> min_CAD_coins(3, 20)
(8, 1, 0, 0, 0)
>>> 
