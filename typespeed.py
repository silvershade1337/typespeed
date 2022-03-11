from sys import stdout
from getch import getch
from time import time


flush = stdout.flush
out = stdout.write
# out('hello')
# out('\b\b')

typestr = "hello world, this is my typing speed test"
typelen = len(typestr)

out(f"You have to type:\n  {typestr}\n> ")

index = 0
starttime = None
scorenocor = [None]*typelen # score considering the characters typed the first time
scorecor = [False]*typelen # score after considering the corrections (backspaced and retyped)

while index < typelen:
  ch = getch()
  if starttime is None:
    starttime = time()
  # print(ord(ch)) # for checking special characters
  # backspace=127, space=32
  if ord(ch) == 127:
    out("\b \b")
    flush()
    index -= 1
    continue
  if ch == typestr[index]:
    print(f"\033[32m{ch}\033[0m", end="")
    scorecor[index] = True
    if scorenocor[index] is None:
      scorenocor[index] = True
  else:
    print('\a', end="")
    if ord(ch) == 32:
      print("\033[41m \033[0m", end="")
    else:
      print(f"\033[31m{ch}\033[0m", end="")
      scorecor[index] = False
      if scorenocor[index] is None:
        scorenocor[index] = False

  index += 1
  flush() # this outputs the print statements, which otherwise wouldn't be until \n was printed. you can also use print argument flush=True

duration = time() - starttime
# (CHarsCorrected) CORRECT CHARACTERS AFTER CORRECTIONS
chc = scorecor.count(True)
# (CHarsNotcorrected) CORRECT CHARACTERS BEFORE CORRECTIONS (INITIALLY TYPED CHARACTERS)
chn = scorenocor.count(True)
 
print('\n')
print(f"You took {round(duration, 2)} seconds to complete")
print("Scores: ")
print(f"With corrections - {chc}/{typelen}")
print(f"Without corrections - {chn}/{typelen}")

# characters typed / 5 = Words typed (approx)
# WPM(Words per Minute) = words typed / time taken in minutes
netwpm = (chc/5) / (duration/60)
print(f"Your Net Typing Speed:", int(round(netwpm, 0)), "WPM") 

# when space is pressed, insert '_'s and move the index to after the next space character
