from django .shortcuts import render
from main.models import Categories,News

def home(request):
    category = Categories.objects.all()
    allNews= News.objects.all().order_by('-id') 
    topNews=News.objects.all().order_by('-id')[ :4] #% used for slice the news and display only limietd news#
    context={
            'categories': category,
            'allNews': allNews,
            'topNews':topNews
            
            } 
    return render(request,'index.html', context)


def india(request):
    category = Categories.objects.all()
    indiaNews= News.objects.filter(category__title="India News").order_by('-id') 
    topNews=News.objects.all().order_by('-id')[ :4] #% used for slice the news and display only limietd news#
    context={
            'categories': category,
            'indiaNews': indiaNews,
            'topNews':topNews
            
            } 

    return render (request,'categories/india.html',context)

def world(request):
    
    category = Categories.objects.all()
    worldNews= News.objects.filter(category__title="World News").order_by('-id') 
    topNews=News.objects.all().order_by('-id')[ :4] #% used for slice the news and display only limietd news#
    context={
            'categories': category,
            'worldNews': worldNews,
            'topNews':topNews
            
            } 
    return render (request,'categories/world.html', context)

def health(request):

    category = Categories.objects.all()
    healthNews= News.objects.filter(category__title="World News").order_by('-id') 
    topNews=News.objects.all().order_by('-id')[ :4] #% used for slice the news and display only limietd news#
    context={
            'categories': category,
            'worldNews': healthNews,
            'topNews':topNews
            
            } 
    return render (request,'categories/world.html', context)

def dynamic(request,id):
    category = Categories.objects.all()
    dynamicNews= News.objects.get(pk = id)
    topNews=News.objects.all().order_by('-id')
    context={
            'categories': category,
            'News': dynamicNews,
            'topNews': topNews
            
            } 
    
    return render(request,'dynamic.html',context)