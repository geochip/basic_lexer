10 LET secret_number = 42
20 LET guess = 0
30 PRINT "Guess a number between 1 and 100!"
40 LET guess = INPUT
50 IF guess == secret_number THEN PRINT "You win!"
60 ELSE IF guess < secret_number THEN PRINT "Too low!"
70 ELSE PRINT "Too high!"
80 GOTO 40
90 END
