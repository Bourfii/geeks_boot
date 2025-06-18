your_longest_sentence = " " 
while True:
   longest_sen = input("Enter the lonest sentence you can without the character A : ")
   if 'A' in longest_sen:
       print("Error! The sentence containt the lettere 'A'")
       continue
   if len(longest_sen) > len(your_longest_sentence):
    print("It's the longest sentence")
   else:
      print("the sentence accepted,but it's not the longest one!")
       