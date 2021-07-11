from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccountCreateView, AccountDetailView

app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    # login과 logout은 작성해야 할 세부사항이 많지 않으므로 views.py에서 별도로 지정하지 않고,
    # urls.py에서 바로 가져와도 괜찮다.
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # 함수형으로 가져올 때와 달리, class형을 가져올 때는, .as_view()를 붙여와야 한다.
    # 그래야 함수형처럼 기능을 한다.
    path('create/', AccountCreateView.as_view(), name='create'),
    # 24강
    # <int:pk>로 몇 번 유저에 접근할 것인지 지정해주도록 한다.
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),

]