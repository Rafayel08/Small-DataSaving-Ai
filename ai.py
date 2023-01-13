'''Just something important to mention: There is a bug where when you type in the same keyword twice it will ask you again for how to respond to it.
I will be trying to fix this bug while focusing on other projects, but overall don't type in the same thing twice in the meantime.'''
import random
import csv
import pandas as pd

df=pd.read_csv('DataSave.csv')

print(df)
greetings = ["Hello!", "What's up?!", "Howdy!", "Greetings!"]
goodbyes = ["Bye!", "Goodbye!", "See you later!", "See you soon!"]

keywords = ["hello"]
responses = ["hi"]

print(random.choice(greetings))
user = input("Say something (or type bye to quit): ")        
user = user.lower()

def keywords_function():
  print("Bot: " + responses[index])
  keyword_found = True
  user = input("Say something (or type bye to quit): ")
  user = user.lower()

while (user != "bye"):
  keyword_found = False
  keyword_still_not_found=False

  if((user in set(df['Keyword'])) == True):
    keyword_found = True
    newdf=(df['Response'].where(df['Keyword'] == str(user)))
    newerdf=newdf.dropna()
    newererdf=str(newerdf.values[0])
    print(newererdf)
    user = input("Say something (or type bye to quit): ")
    user = user.lower()

    
  if (keyword_found == False):
    for index in range(len(keywords)):
      if (keywords[index] == user):
        keywords_function()
        break

      else:
        keyword_still_not_found=True 
  

  if(keyword_still_not_found==True):
      print(keywords)
      print(responses)
      thelist=[]
      new_keyword = input("I'm not sure how to respond. Please type in the keyword(s) that I should respond to")
      new_keyword=new_keyword.lower()
      thelist.append(new_keyword)
      keywords.append(new_keyword)

      new_response = input("How should I respond to " + new_keyword + "? ")
      new_response=new_response.lower()
      thelist.append(new_response)
      responses.append(new_response)

      with open('rename.csv', 'a') as f_object:
        writer_object = csv.writer(f_object)
        writer_object.writerow(thelist)
        f_object.close()
        thelist=[]
        keyword_still_not_found=False
        
      user = input("Say something (or type bye to quit): ")
      user = user.lower()

print(random.choice(goodbyes))
