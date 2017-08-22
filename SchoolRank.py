# coding: utf-8
import requests
import re


def Login():
	loads = {"username":"******","userpass":"******","login":"Sign In"}
	s = requests.Session()
	html = s.post('http://acm.hdu.edu.cn/userloginex.php?action=login&cid=779&notice=0', data = loads)
	rankpage = s.get('http://acm.hdu.edu.cn/contests/contest_ranklist.php?cid=779&page=1').text
	pages = re.findall('<a href="./contest_ranklist.php.*?style=.*?>(.*?)</a>', rankpage , re.S)
	maxpage = pages[-1]
	tmpschool = re.findall('<tr.*?<td.*?<td.*?<br />\n (.*?)</td>', rankpage , re.S)
	findschool = list(set(tmpschool))
	findschool.sort(key = tmpschool.index)
	school = findschool
	for i in range(int(maxpage) - 1):
		rankhtml = s.get('http://acm.hdu.edu.cn/contests/contest_ranklist.php?cid=779&page='+str(i+2)).text
		tmpschool = re.findall('<tr.*?<td.*?<td.*?<br />\n (.*?)</td>', rankhtml , re.S)
		findschool = list(set(tmpschool))
		findschool.sort(key = tmpschool.index)
		school += findschool

	uniqueschool = list(set(school))
	uniqueschool.sort(key = school.index)
	return uniqueschool


def search(name = "哈尔滨工业大学(威海)", schoollist = []):
	for i in range(len(schoollist)):
		if schoollist[i] == name:
			print(i+1)
			break

def showschool(schoollist = []):
	for i in range(len(schoollist)):
		print(i+1,schoollist[i])

school = Login()
showschool(school)
search('哈尔滨工业大学(威海)' , school)
