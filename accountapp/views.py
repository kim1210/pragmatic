from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

# Create your views here.
from django.views.generic import CreateView, DetailView

from accountapp.models import HelloWorld

def hello_world(request):

    if request.method == 'POST':

        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))

    else :
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list':hello_world_list})


# 21강
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    # 함수형에서는 reverse를 사용하고 class형에서는 reverse_lazy를 사용한다.

    template_name = 'accountapp/create.html'
    # 어떤 템플릿을 보여줄지 설정~

# 24강
class AccountDetailView(DetailView):
    model = User
    # CreateView와 달리 Read의 기능이기 때문에, form이나 success_url을 따로 지정할 필요가 없다.
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

