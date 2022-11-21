from django.shortcuts import render
def main(request):
    cities = ['Москва','Санкт-Петербург','Ярославль','Сочи','Тула','Ростов Великий','Ставрополь','Владимир','Челябинск','Муром']
    path = request.path

    path = path.replace('/','')
    if path == "":
        path="main"
    return render(request,f'{path}.html',{'cities': cities})

