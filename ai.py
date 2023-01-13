import random
import csv
import pandas as pd
# columns=['Keyword','Response']
# row = [
# ['music','Music is so relaxing!'],
# ['pet',"Dogs are mans best friend"],
# ['book','I know about a lot of books.'],
# ['game','I like to play video games.']
# ]
# with open('aicsv.csv', 'w') as file:
#   writer = csv.writer(file)
#   writer.writerow(columns)
#   writer.writerows(row)
df=pd.read_csv('rename.csv')
# newdf=df['Keyword']
print(df)
greetings = ["Hello!", "What's up?!", "Howdy!", "Greetings!"]
goodbyes = ["Bye!", "Goodbye!", "See you later!", "See you soon!"]

keywords = ["hello"]
responses = ["hi"]

print(random.choice(greetings))
user = input("Say something (or type bye to quit): ")        
user = user.lower()
# print(str(user) in set(df['Keyword']))
# print((((df['Response'].where(df['Keyword'] == str(user))).dropna())).values[0])
def keywords_function():
  print("Bot: " + responses[index])
  keyword_found = True
  user = input("Say something (or type bye to quit): ")
  user = user.lower()

while (user != "bye"):
  keyword_found = False
  keyword_still_not_found=False
  # for i in range(0):
  if((user in set(df['Keyword'])) == True):
    keyword_found = True
    newdf=(df['Response'].where(df['Keyword'] == str(user)))
    newerdf=newdf.dropna()
    newererdf=str(newerdf.values[0])
    print(newererdf)
    user = input("Say something (or type bye to quit): ")
    user = user.lower()
    #print("Bot: " + responses[index])
    
  if (keyword_found == False):
    for index in range(len(keywords)):
      if (keywords[index] == user):
        keywords_function()
        break
        # print("Bot: " + responses[index])
        # keyword_found = True
        # user = input("Say something (or type bye to quit): ")
        # user = user.lower()
      # if (keywords[index] != user) and ('KEYWORD_FOUND_CONST' in globals())==False:
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
      # keywords.append(new_keyword)
      new_response = input("How should I respond to " + new_keyword + "? ")
      new_response=new_response.lower()
      thelist.append(new_response)
      responses.append(new_response)
      #responses.append(new_response)
      with open('rename.csv', 'a') as f_object:
        writer_object = csv.writer(f_object)
        
          # Pass the list as an argument into
          # the writerow()
        writer_object.writerow(thelist)
        
        # Close the file object
        f_object.close()
        thelist=[]
        keyword_still_not_found=False
      user = input("Say something (or type bye to quit): ")
      user = user.lower()


user = input("Say something (or type bye to quit): ")
user = user.lower()

print(random.choice(goodbyes))