import random
def primary():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.read().splitlines()
  f.close()
  
  lines = ['Happiness is when what you think, what you say', ' the years in your life that count']
  with open('quotes.txt', 'a') as f:
    for line in lines:
        f.write(line)
        f.write('\n')
  
  print(quotes)
  print(quotes[0])
  
  print(quotes[-1])
   
  last = last = len(quotes) - 1
  rnd = random.randint(0, last)
  print(quotes[rnd])
  for quote in quotes:
   print(quote)
  

if __name__== "__main__":
  primary()
