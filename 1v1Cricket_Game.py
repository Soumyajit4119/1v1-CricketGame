import random
import os
import time

# Clear screen function
def clear_screen():
   os.system('cls' if os.name == 'nt' else 'clear')


#1.Greet and start the game:
print("Welcome to 1v1 Cricket Game :)\n")
ans = input("Do you want to start the game (yes/no)? ")
if ans.lower() != "yes" and ans.lower() != "y":
   print("You are exiting the game...")
   time.sleep(2.4)
   exit()

##Dialogue initializations:-
sentences_for_choosing1 = ["It's your turn to choose your target run (1, 2, 4 or 6): ", "Your turn, go ahead and pick your target run (1, 2, 4 or 6): ", "Alright, it's your time, choose your target run (1, 2, 4 or 6): ", "Go ahead, time is yours, pick your target run (1, 2, 4 or 6): ", "Choose wisely, it's your turn, pick your target run (1, 2, 4 or 6): ", "Alright, it's your time to pick your target run (1, 2, 4 or 6): "]
sentences_for_choosing2 = ["It's your turn to choose your move (1, 2, 4 or 6): ", "Your turn, go ahead and pick (1, 2, 4 or 6): ", "Alright, it's your time, choose your move (1, 2, 4 or 6): ", "Go ahead, time is yours, pick (1, 2, 4 or 6): ", "Choose wisely, it's your turn, pick (1, 2, 4 or 6): ", "Alright, it's your time to choose your move (1, 2, 4 or 6): "]
sentences_for_string_input = ["Hey!", "Focus here!", "Pay attention!", "Eyes here!", "Come on! FOCUS,", "Snap out of it! You need to concentrate,"]
sentences_for_wrong_input = ["Oops, wrong choice! Try again.", "Nope, that's not correct.", "Wrong, give it another try.", "Unfortunately, that's not the right.", "Wrong pick, try again!"]
sentences_for_same_guess1 = ["Got you! I guessed the correct number.", "My assumption was correct—Spot on!", "Bingo! I picked the right number.", "My prediction was spot on—Nailed it!", "Caught you! I guessed the correct number."]
sentences_for_same_guess2 = ["Oh no, I guessed the same!", "My bad! I had to pick the other one.", "Whoops, I made the wrong choice.", "We guessed the same, bad luck!"]
words_for_victory = ["Victory!", "Hooray!", "Winner!", "Wahoo!", "I did it!"]
words_for_defeat = ["Oh no!", "Ah, man!", "Darn!", "No way!", "Unbelievable!"]

##Variables initializations:-
runs_list = [1, 2, 4, 6]
im_bowler = ur_batsman = 0          #here I refers to the computer.
my_balls = ur_runs = 0

while True:
   #2.Your Turn (You are the Batsman and I am the Bowler):
   while True:
         #2.1 Give input as a Batsman:
         ur_batsman = input(random.choice(sentences_for_choosing1))
         if ur_batsman.isdigit():
            ur_batsman = int(ur_batsman)           #integer conversion of input
            if ur_batsman != 1 and ur_batsman != 2 and ur_batsman != 4 and ur_batsman != 6:
               print(random.choice(sentences_for_wrong_input))
               continue
         else:
            clear_screen()
            print(random.choice(sentences_for_string_input), "you entered a string instead of digit.")
            continue

         #2.2 My random choice as a Bowler:
         im_bowler = random.choice(runs_list)
         print(f"Your target run is {ur_batsman} but I guessed {im_bowler}.")

         #2.3 Update runs, track balls and check out conditions:
         my_balls += 1                  #Count balls
         if ur_batsman != im_bowler:
            ur_runs += ur_batsman          #Count runs
            print(f"Your score is {ur_runs} run(s) in {my_balls} ball(s).\n")
         else:
            clear_screen()
            print(random.choice(sentences_for_same_guess1))
            print(f"We both choose {ur_batsman}. You'er OUT!!!")
            print(f"Your total run(s) {ur_runs} in {my_balls} ball(s). Well played.\n")
            break

   ##Variables initializations:-
   ur_bowler = im_batsman = 0
   ur_balls = my_runs = 0
   print(f"Okay, I'm next in line to bat, get ready. TARGET {ur_runs+1} in {my_balls} balls:-")

   #3.My Turn (I am the Batsman and You are the Bowler):
   while True:
         #3.1 Take input from user as a Bowler:
         ur_bowler = input(random.choice(sentences_for_choosing2))
         if ur_bowler.isdigit():
            ur_bowler = int(ur_bowler)           #integer conversion of input
            if ur_bowler != 1 and ur_bowler != 2 and ur_bowler != 4 and ur_bowler != 6:
               print(random.choice(sentences_for_wrong_input))
               continue
         else:
            clear_screen()
            print(random.choice(sentences_for_string_input), "you entered a string instead of digit.")
            continue

         #3.2 Generate Random Choice by the Computer as a Batsman:
         im_batsman = random.choice(runs_list)
         print(f"You choose {ur_bowler} and my target run is {im_batsman}.")

         #3.3 Update runs, track balls and check out conditions:
         ur_balls += 1                ##Count balls
         if ur_bowler != im_batsman:
            my_runs += im_batsman         ##Count runs
            print(f"My score is {my_runs} run(s) in {ur_balls} ball(s).\n")
         else:
            clear_screen()
            print(random.choice(sentences_for_same_guess2))
            print(f"We both choose {ur_bowler}. I'm OUT!!!")
            print(f"My total score is {my_runs} run(s) in {ur_balls} ball(s).")
            print(f"Your score was run(s) {ur_runs} in {my_balls} ball(s).\n")
            break
      
         if my_runs > ur_runs:
            clear_screen()
            print(random.choice(words_for_victory), f"I finally beat you by scoring {my_runs} runs in {ur_balls} ball(s).")
            print(f"Your score was run(s) {ur_runs} in {my_balls} ball(s).\n")
            break
         elif ur_balls > my_balls:
            clear_screen()
            print(random.choice(words_for_defeat), "I lost the match because no more balls are left.")
            print(f"My total score is {my_runs} run(s) in {ur_balls} ball(s).")
            print(f"Your score was run(s) {ur_runs} in {my_balls} ball(s).\n")
            break

   #4.Print results of the match:
   if ur_runs > my_runs:
      print(f"INNINGS OVER!!!\nCONGRATULATIONS, You win the match by {int(ur_runs)-int(my_runs)} run(s), {my_balls-ur_balls} ball(s) left.\n")
   else:
      print(f"INNINGS OVER!!!\nSORRY, I won the match by {int(my_runs)-int(ur_runs)} run(s), {my_balls-ur_balls} ball(s) left.\n")
   
   #5.Ask user whether he wants to play one more round or not:
   time.sleep(1.5)
   ans = input("Do you want to play another round (yes/no)? ")
   if ans.lower() != "yes" and ans.lower() != "y":
      print("You are exiting the game...")
      time.sleep(2.4)
      break
   else:
      continue
   