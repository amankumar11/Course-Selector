from bs4 import BeautifulSoup
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
 	# print(result)
 	# print(result['results'][0]['url'])
 	# for a in range(1):
 	data=result['results'][1]['title'] +'\n' +"https://www.udemy.com"+result['results'][1]['url']+'\n'+result['results'][1]['price']+'\n'
 	return data

 	# print(result['results'][1]['title'])
 	# print("https://www.udemy.com"+result['results'][1]['url'])
 	# print(result['results'][1]['price'])
 	# print("**********************")


function("python")




