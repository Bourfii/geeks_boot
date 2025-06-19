paragraph = "Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures,combined with dynamic typing and dynamic binding,make it very attractive for Rapid Application Development as well as for use as a scripting or glue language to connect existing components together."
lenght_par = len(paragraph)
print(f"The number of character containt this paragraph : {lenght_par}")
sentences = paragraph.split(".")
print("The sentences : ",len(sentences))
#for i, sentence in enumerate(sentences , 1):
    #if sentence.strip():
        #print(f"Sentences {i} : {sentence.strip()}")
words = paragraph.split(" ")
print("The numbers of the words in the paragrape : ",len(words))
print("\n",words)
word_uninque = set(words)
print("The numbers of the words unique : ",len(word_uninque))
