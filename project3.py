# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''


# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?


#In this version,use dictionary to encapsulate data
game_data = {
   'easy': {
        'quiz': '1___ is a game where you throw or shoot a ball through a hoop. A 1___ is an orange/brown color.it is opposite game for two 2___.Each 2___ has 3___ players and one 4___.Micheal 5___ is the greatst play in the history.',
        'answers': ['basketball','team','five','coach','jordan']
    },
   'medium': {
        'quiz': 'A 1___, beefburger or burger is a 4___ consisting of one or more cooked patties of ground meat, usually beef, placed inside a sliced bread roll or bun. The patty may be pan fried, barbecued, or flame broiled. 1___ is often served with 2___, lettuce, tomato, bacon, onion, pickles, or chiles; condiments such as mustard, mayonnaise, 3___, relish, or "special sauce"; and are frequently placed on sesame seed buns. A 1___ topped with 2___ is called a cheeseburger.',
        'answers': ['hamburger','cheese','ketchup','sandwich']
    },
   'hard': {
        'quiz': 'Canada is a 1___ in North America, located to the 2___ of the United States. Its land reaches from the Atlantic Ocean in the east to the Pacific Ocean in the 4___ and the Arctic Ocean to the 2___, covering 9.98 million square kilometres (3.85 million square miles), making it the 3___ second-largest 1___ by total area and the fourth-largest 1___ by land area. It has the 3___ longest coastline and is the only one to touch three oceans.',
        'answers': ['country','north','world','west']
    }
}

#The user should type one of the three level
def level_select():
   print 'Please select a game difficulty by typing it in!'
   print 'Possible choices include easy, medium, and hard.'
   level=raw_input().lower()
   option=['easy','medium','hard']
   while level not in option:    #use <element> in <list> instead of multipile 'or/and' parallel
     if level in option:
       print 'you select '+level+', enjoy the game!'
       print ' '
       break
     print 'That is not an option!Possible choices include easy, medium, and hard.'
     level=raw_input().lower()
   return level

#it is a global varaible because more than one module will use it,and value does't change since the game difficultyis selected
level=level_select()

#this function is a reusable function, the input are:i is the number of blank word,like"1___";paragraph is the current passing paragraph;
def guess_game(i,paragraph):
  print paragraph
  print ' '
  print 'What should be substituted in for '+str(i+1)+'___?'
  max_try_time=3
  index=0
  user_input=raw_input().lower()
  while user_input!=game_data[level]['answers'][i] and index<max_try_time:
    if user_input==game_data[level]['answers'][i]:
      #when user hits the right answer,the whole paragraph will be given,and game continues
      break
    print 'you have '+str(max_try_time-index)+' more chance'+'s'*((max_try_time-index)/2) #in oder to distinguish Single and Plural
    user_input=raw_input().lower()
    index+=1
    if index==3:
      print 'This is the correct answer for '+str(i+1)+'___,keep trying the next question'
#if the user can not type correct answer in 3 times, the correct answer will be given,and the game continues
  print ' '
  return paragraph.replace((str(i+1)+'___'),game_data[level]['answers'][i])


#this is the main function,the level is the user_input,there is not output but print the final answer
def game():
  paragraph=game_data[level]['quiz']
  i=0
  while i<len(game_data[level]['answers']):
    paragraph=guess_game(i,paragraph)
    i+=1
  print paragraph
  print 'Awsome,you finished the game!'

game()
