import urllib.request as req
import os
link = "https://en.wikipedia.org/wiki/List_of_most_popular_websites"
response = requests.get(link)
print(type(response))
print(response.read())

content = response.read()
#Create a html file with the content received as 'content'
file = open(os.getcwd()+os.sep+"tests"+os.sep+"wikipopular.html","wb")
file.write(content)
file.close()
#print(content)  
