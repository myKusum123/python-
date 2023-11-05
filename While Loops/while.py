'''The while Loop
With the while loop we can execute a set of statements as long as a condition is true.
( hamro condion chai jaba samma true hudae na taba samma execute vae ralhxa)
Note: remember to increment i, or else the loop will continue forever.(i+= (i vaneko chai variable ho while ko variable j xa tei rakhni ho) chai rakhnu parxa natra run vae rakhxa)

'''
# while condition
j = 1
while j < 6:
  print(j)
  j += 1

# The break Statement-With the break statement we can stop the loop even if the while condition is true:
# ( break statement ma chai yedi while condition true xa vani pni break hunxa)
i=10
while i<=20:
 print(i)
 if i==15:
  break 
 i+=1# yo chai lekhnu nai parxa yedi while statement run vae rakhna bata stop garna and yesle one plus pni garxa

# The continue Statement-With the continue statement we can stop the current iteration, and continue with the next:
i = 0
while i < 6:
  i += 1
  if i == 3:# output ma 3 print hunna aru sab continue vayera print hunxa 
    continue
  print(i)

#The else Statement-With the else statement we can run a block of code once when the condition no longer is true:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")# else pni print hunxa

