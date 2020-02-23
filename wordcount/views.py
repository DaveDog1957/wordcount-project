from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
	return render(request, "home.html")

def about(request):
	return render(request, "about.html")

	
def count(request):
	allthetext=request.GET["allthetext"]
	listofwords = allthetext.split()
	worddictionary = {}
	for word in listofwords:
		if word in worddictionary:
			# increase the number
			worddictionary[word] += 1
		else:
			# add to dictionary
			worddictionary[word] = 1
			
	sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
	return render(request, "count.html",{"allthetext":allthetext,"lenofwords":len(listofwords), "sortedwords":sortedwords})