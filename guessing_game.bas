100 REM Can be tested with https://www.quitebasic.com/
10 LET S=42
20 LET G=0
30 PRINT "Guess a number between 1 and 100!"
40 INPUT "hello"; G
50 IF G = S THEN PRINT "You win!" ELSE IF G < S THEN PRINT "Too low!" ELSE PRINT "Too high!"
60 GOTO 40
70 END
