from django.shortcuts import render, redirect
from django.http import HttpResponse
from lotto.models import GuessNumbers
from lotto.forms import PostForm

# Create your views here.
def index(request):

    lottos = GuessNumbers.objects.all()
    #랜더함수의 기본 모습: render(request, 'html경로', {'df':파이썬 변수를 넘김})
    # {'lottos':lottos} <- context라고 부름
    return render(request, 'lotto/default.html', {'lottos':lottos})



def hello(request):
    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>")


def post(request):
    # print('\n\n\n======================n\n\n\')
    # print(request.method) #이번에 들어온 요청이 get인지 post인지 보여준다
    # print('\n\n\n======================n\n\n\')


    #따라서 if로 갈라서 수행
    if request.method == 'POST':

        form = PostForm(request.POST)

        if form.is_vaild():
            lotto = form.save(commit=False)
            lotto.generate()

            return redirect('index')
        # #옵션1 :
        # user_name = request.Post['name']
        # user_text = request.Post['text']
        # row = GuessNumbers(name=user_name, text = user_test)
        # row.generate()


        # print('\n\n\n======================n\n\n\')
        # print(request.POST['name'])
        # print(type(request.POST['text']))
        # print('\n\n\n======================n\n\n\')


    else:
        form = PostForm() #빈양식 만들기
        return render(request, 'lotto/form.html', {'form':form})


def detail(request, lottokey): #url.py로부터 받아낸 키는 이렇게 받아낸다.
    lotto = GuessNumbers.objects.get(pk = lottokey) #id는 pk로 primary키로 만들어짐.
    return render(request, 'lotto/detail.html', {'lotto':lotto})

'''
def index(request):

    #이렇게 모델이 아닌 views에서도 바로 할 수 있다.
    row = GuessNumbers(name=request.POST['name'], text=request.POST['text'])

    row.lottos = ""
    origin = list(range(1,46))

    for _ in range(0, row.num_lotto):
        random.shuffle(origin)
        guess = origin[:6]
        guess.sort()
        row.lottos += str(guess) +'\n' # 로또 번호 str에 6개 번호 set 추가

    row.update_date = timezone.now()
    row.save() # commit

    return HttpResponse('<h1>Hello, world!</h1>')
'''
