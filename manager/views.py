from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, TemplateView, DetailView, UpdateView, CreateView, DeleteView

from .models import ExpenseItem
from .forms import ContactForm, UserForm


@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(request.POST)
            # return HttpResponse(request.POST['name'])
            return HttpResponse("Got POST request...")
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def home(request):
    return render(request, "home.html", {})


class AddItemView(CreateView):
    queryset = ExpenseItem.objects.all()
    fields = ['title', 'type', 'account', 'date', 'amount',
              'description']
    template_name = 'manager/expenseitem_addnew.html'
    success_url = '/added'


class AddedItemView(TemplateView):
    template_name = "manager/expenseitem_added.html"


class ItemListView(ListView):
    # queryset = ExpenseItem.objects.all()
    def get_queryset(self):
        return ExpenseItem.objects.filter(owner=self.request.user)


class ItemDetailView(DetailView):
    queryset = ExpenseItem.objects.all()


class EditItemView(UpdateView):
    queryset = ExpenseItem.objects.all()
    fields = ['title', 'type', 'account', 'date', 'amount', 'description']

    def get_success_url(self):
        return "/detail/" + str(self.object.id)


class DeleteItemView(DeleteView):
    queryset = ExpenseItem.objects.all()
    success_url = "/viewall"


class UserDetailView(TemplateView):
    template_name = "profile.html"


def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                user = form.save()
                # user = authenticate(username=user.username, password=user.password)
                print(user.username, user.password)
                # login(request, user)
                return HttpResponseRedirect("/admin/login/?next=/")
        else:
            form = UserForm()
        return render(request, 'register.html', {'form': form})


def product_detail(request, pk):
    return HttpResponse("It is a free product" + pk)