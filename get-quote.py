def main():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  print("all sentences are:",quotes)
  print("first sentence is:",quotes[0])
  print("last sentence is:",quotes[-1])
   

  

if __name__== "__main__":
  main()
