
import requests
# https://www.google.com/search?client=opera-gx&q=udemy%2Bpython%2Bcourse
# url ="https://www.google.com/search?client=opera-gx&q=udemy"
# def array_results(course):
#     url_new=url+" course"
#     res=requests.get(url_new)
#     bs=BeautifulSoup(res.content,features="lxml")
#     bs.findAll("a")
#     for a in bs:
#         print(a['href'])

#     # print(bs.prettify())


# array_results("python")

class result_:
	def __init__(self,title,url,price):
		self.title = title
		self.url = url
		self.price = price


headers={
  "Accept": "application/json, text/plain, */*",
  "Authorization": "Basic azhGNElyWnVKT2lZSXpaTVhScUUxN3dTS2o1WGZXNllDTDVCcUxhSDpmQndTYkYybktJdE1VcTd1SmhrNjFxMm1Vcko5UjBHSEpqRmFxM0w4YUhkSE9lVUVPRjcyT0RFNzJudWhuZ0dFYlRIMVk0TFlybmw5VXQ0VWRSMHJoVVRnVzg4TTUzVVZLM2RZOXoxN1BEZGE0MlFWWlpib1gxNlVCbTNCeFBvcA==",
  "Content-Type": "application/json;charset=utf-8"
}
url="https://www.udemy.com/api-2.0/courses/"

def function(lang):


 		
	endpoint=url


	params={'page':'2','search':lang}
	res=requests.get(url,headers=headers,params=params)


	result=res.json()
	arr1=[]


 	# print(result)
 	# print(result['results'][0]['url'])
 	# for a in range(1):
 	# data=result['results'][1]['title'] +'\n' +"https://www.udemy.com"+result['results'][1]['url']+'\n'+result['results'][1]['price']+'\n'
 	# return data
	
	data1=result_(result['results'][1]['title'],"https://www.udemy.com"+result['results'][1]['url'],result['results'][1]['price'])
	data2=result_(result['results'][2]['title'],"https://www.udemy.com"+result['results'][2]['url'],result['results'][2]['price'])
	data3=result_(result['results'][3]['title'],"https://www.udemy.com"+result['results'][3]['url'],result['results'][3]['price'])
	arr1.append(data1)
	arr1.append(data2)
	arr1.append(data3)
	return arr1




 	# for a in range(5):

	#  	print(result['results'][a]['title'])
	#  	print("https://www.udemy.com"+result['results'][a]['url'])
	#  	print(result['results'][a]['price'])
	#  	print("**********************")









