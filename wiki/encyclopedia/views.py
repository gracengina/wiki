from django.shortcuts import render ,redirect

from . import util
import markdown2
import random



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def entry(request, title):
    content=util.get_entry(title)
    if content is None:
        #Return error message
        return render(request, "encyclopedia/error.html" ,{"title":title})
    else:
        #convert Markdown to Html
        html_content=markdown2.markdown(content)
        return render(request, "encyclopedia/entry.html", {"html_content":html_content , "title":title} )

def search(request):
    query=request.GET.get('q' ,'').strip()
    if not query:
       return redirect("index") 
    entries=util.list_entries()
    match=[entry for entry in entries if query.lower() in entry.lower() ]
    if len(match)==1:
        return redirect(f"wiki/{match[0]}")
    return render(request , "encyclopedia/matches.html",{"matches":match , "query":query})

def edit(request , title):
   if request.method =="GET":
        content=util.get_entry(title)
        if not content:
            return render(request,"encyclopedia/error.html" ,{"title":title ,"message":"That entry does not exist"})
        return render (request , "encyclopedia/edit.html" , {"title":title , "content":content})   
               
   if request.method == "POST":
           
         new_content=request.POST.get('content' , '').strip()
         if not new_content:
            return render(request, "encyclopedia/error1.html" ,{"title":title})
         else:
            util.save_entry(title , new_content)
            return redirect ("title", title=title)

def create(request):
    if request.method=="GET":
        return render(request, "encyclopedia/create.html")
    if request.method=="POST":
        title=request.POST.get("title")
        content=request.POST.get("content")
        if not title or not content:
             return render(request,"encyclopedia/error.html" ,{"title":title, "message":"title or content can not be empty"})
        if util.get_entry(title) is not None:
             return render(request,"encyclopedia/error.html" ,{"title":title, "message":"Title already exists"})
        util.save_entry(title, content)
        return redirect('title', title=title)
    
def random_page(request):
    entries=util.list_entries()
    if not entries:
        return render(request, "encyclopedia/error.html" ,{"message":"No entries"})
    page=random.choice(entries)
    return entry(request,page)
        


   