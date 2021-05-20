from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.

def index(response, id):
    tdl = ToDoList.objects.get(id=id)

    if response.method == "POST":
        print(response.POST)

        if response.POST.get("save"):   #  reponse.POST is a dictionary (key: input name, value: user entry)
            for item in tdl.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False

                item.save()

        elif response.POST.get("newItem"):
            text = response.POST.get("newItemText")

            if len(text) > 2:
                tdl.item_set.create(text=text, complete=False)
            else:
                print("Invalid input!")

    return render(response, "main/list.html", {"tdl": tdl})

def home(response):
    return render(response, "main/home.html", {})

def create(response):
    # response.user.is_authenticated
    if response.method == "POST":
        form = CreateNewList(response.POST)
        
        if form.is_valid():
            n = form.cleaned_data["name"]
            response.user.todolist_set.create(name=n)
            # t = ToDoList(name=n)
            # t.save()
        
        return HttpResponseRedirect("/%i" % t.id)
    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form": form})

def view(response):
    return render(response, "main/view.html", {})