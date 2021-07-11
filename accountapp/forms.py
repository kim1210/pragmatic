from django.contrib.auth.forms import UserCreationForm

# 25강 / views.py에서 사용했던 UserCreationForm을 상속하여 customizing을 하겠다.
class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) #여기까지는 기존의 UserCreationForm과 다르지 않다.
        # 다음 줄부터 customizing되는 부분!
        self.fields['username'].disabled = True
