import random
from words import word_list

def home():
   while True:
      print("---------------------------------------------------------")
      print("               WELCOME TO FUN LAND GAMES                 ")
      print("---------------------------------------------------------")
      print("|              Which game do you wanna play?            |")
      print("| 1. Guess The Number                                   |")
      print("| 2. Hangman                                            |")
      print("| 3. Exit                                               |")
      print("---------------------------------------------------------")
      answer = int(input('Input the number : '))
      print()
      if(answer==1):
         guess_number()
      elif(answer==2):
        hangman()
      else:
        exit()
        break

def exit():
    print("---------------------------------------------------------")
    print("            Thank You For Playing With Me!               ")
    print("                 \See You Next Time/                     ")
    print("---------------------------------------------------------")
        
def guess_number():
   while True:
      print("---------------------------------------------------------")
      print("              ~~ Let's Play The Game ~~                  ")
      print("                Game Guess The Number                    ")
      print("---------------------------------------------------------")
      print("|                 Choose your level game                |")
      print("| 1. Easy (range 1-10)                                  |") 
      print("| 2. Medium (range 1-30)                                |") 
      print("| 3. Hard (range 1-50)                                  |")
      print("---------------------------------------------------------")
      level = int(input('Input the number : '))
      if level == 1:
         chance = 3
         bilRandom = random.randint(1,10)
      elif level == 2:
         chance = 5
         bilRandom = random.randint(1,30)
      elif level == 3:
         chance = 7
         bilRandom = random.randint(1,50)
      print("Level", level, "with", chance, "chance to play")

      #looping tebak angka
      while(chance >= 0): 
         if chance == 0:
            print("---------------------------------------------------------")
            print("                 The number is :", bilRandom              )
            print("")
            print("          ******      **     ***  ***  *******           ") 
            print("          *          *  *    *  **  *  *                 ")                           
            print("          *  ***    ******   *   *  *  *******           ")                            
            print("          *    *   *      *  *      *  *                 ")                           
            print("          ******  *        * *      *  *******           ")
            print("")
            print("           **    *       *  *******  **** * *            ")
            print("         *    *   *     *   *        *       *           ")                                
            print("         *    *    *   *    *******  ** * * *            ")                             
            print("         *    *     * *     *        *   *               ")                            
            print("           **        *      *******  *      *            ")                                             
            print("---------------------------------------------------------")
            break
         else:
            print("Chance : ", chance)
            print("\n")
            tebak = int(input("Input the number to guess : "))
            if tebak == bilRandom:
               print("---------------------------------------------------------")
               print("                      Incredible!!!                      ")
               print()
               print("      *     *   **    *    *   *        *  *  *     *    ")
               print("       *   *   *  *   *    *    *   *  *   *  * *   *    ") 
               print("         *     *  *   *    *     * ** *    *  *   * *    ")   
               print("         *      **      * *       *  *     *  *     *    ") 
               print("---------------------------------------------------------")
               break
            elif tebak > bilRandom:
               print("---------------------------------------------------------")
               print("The number less than", tebak )
               chance -= 1
            elif tebak < bilRandom:
               print("---------------------------------------------------------")
               print("The number greater than", tebak)
               chance -= 1
      #konfirmasi ulang
      ulang = input("Do you wanna play again? (Yes/No) : ")
      print("\n")
      if ulang == "Yes" :
         guess_number()
      elif ulang == "No" :
         print("---------------------------------------------------------")
         print("          *** Thank You! See you next time! ***          ") 
         print("---------------------------------------------------------")
         break
         home()
      return
#pemilihan game 2

def hangman():
   def get_word():
     word = random.choice(word_list)
     return word.upper()
   def play(word):
      word_completion = "-" * len(word)
      guessed = False
      guessed_letters = []
      guessed_words = []
      tries = 6
      print("---------------------------------------------------------")
      print("              ~~ Let's Play The Game ~~                  ")
      print("                        Hangman                          ")
      print(display_hangman(tries))
      print(word_completion)
      print("\n")
      while not guessed and tries > 0:
         print("---------------------------------------------------------")
         guess = input("Please guess a letter or word : ").upper()
         if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
               print("You already guessed the letter", guess)
               
            elif guess not in word:
               print(guess, "is not in the word.")
               tries -= 1
               guessed_letters.append(guess)
            else:
               print("Good job,", guess, "is in the word!")
               guessed_letters.append(guess)
               word_as_list = list(word_completion)
               indices = [i for i, letter in enumerate(word) if letter == guess]
               for index in indices:
                  word_as_list[index] = guess
               word_completion = "".join(word_as_list)
               if "-" not in word_completion:
                  guessed = True
         elif len(guess) == len(word) and guess.isalpha():
               if guess in guessed_words:
                  print("You already guessed the word", guess)
               elif guess != word:
                  print(guess, "is not the word.")
               else:
                  guessed = True
                  word_completion = word
         else:
            print("Not a valid guess.")
         print(display_hangman(tries))
         print(word_completion)
         print("\n")

      if guessed == True :
         print("---------------------------------------------------------")
         print("            Congrats, you guessed the word!              ")
         print()
         print("      *     *   **    *    *   *        *  *  *     *    ")
         print("       *   *   *  *   *    *    *   *  *   *  * *   *    ") 
         print("         *     *  *   *    *     * ** *    *  *   * *    ")   
         print("         *      **      * *       *  *     *  *     *    ")  
         print("---------------------------------------------------------")
         
      else :
         print("---------------------------------------------------------")
         print("   Sorry, you ran out of tries. The word was " + word     )
         print("")
         print("          ******      **     ***  ***  *******           ") 
         print("          *          *  *    *  **  *  *                 ")                           
         print("          *  ***    ******   *   *  *  *******           ")                            
         print("          *    *   *      *  *      *  *                 ")                           
         print("          ******  *        * *      *  *******           ")
         print("")
         print("           **    *       *  *******  **** * *            ")
         print("         *    *   *     *   *        *       *           ")                                
         print("         *    *    *   *    *******  ** * * *            ")                             
         print("         *    *     * *     *        *   *               ")                            
         print("           **        *      *******  *      *            ")                                             
         print("---------------------------------------------------------")

   def display_hangman(tries):
         stages = [   """
                        --------
                        |      |
                        |      O
                        |     \\|/
                        |      |
                        |     / \\
                        -
                     """
                        ,
                     """
                        --------
                        |      |
                        |      O
                        |     \\|/
                        |      |
                        |     /
                        -
                     """
                        ,
                     """
                        --------
                        |      |
                        |      O
                        |     \\|/
                        |      |
                        |
                        -
                     """
                        ,
                     """
                        --------
                        |      |
                        |      O
                        |     \\|
                        |      |
                        |
                        -
                     """
                        ,
                     """
                        --------
                        |      |
                        |      O
                        |      |
                        |      |
                        |
                        -
                     """
                        ,
                     """
                        --------
                        |      |
                        |      O
                        |
                        |
                        |
                        -
                     """
                        ,
                     """
                        --------
                        |      |
                        |
                        |
                        |
                        |
                        -
                     """
                  ]
         return stages[tries]

   def main():
      word = get_word()
      play(word)
      while True:
         ask = input("Do you wanna play again? (Yes/No): ")
         if ask == "Yes":
            word = get_word()
            play(word)
         else:
            print("---------------------------------------------------------")
            print("          *** Thank You! See you next time! ***          ") 
            print("---------------------------------------------------------")
            break
            home()

   if __name__ == "__main__":
      main()

home()