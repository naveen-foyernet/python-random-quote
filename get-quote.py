import random
def primary():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  
  f = open("quotes.txt", "a")
  f.write("Happiness is when what you think, what you say")
  f.close()
  
    #print(quotes)
    # print(quotes[0])
  
  #print(quotes[-1])
   
  # last = 13
  # rnd = random.randint(0, last)
  # print(quotes[rnd])
  for quote in quotes:
   print(quote)

if __name__== "__main__":
  primary()
