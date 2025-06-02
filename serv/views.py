from django.shortcuts import render, redirect
from .models import Type , category
from .forms import DDSRecordForm

def index(request):
    return render(request, 'serv/index.html')

def create_record(request):
    type_name = None
    category_name = None
    step = request.POST.get('step', '1')
    back = request.POST.get('back', None)
    form = DDSRecordForm(request.POST or None)

    if request.method == 'POST':
        
            if step == '1':
                type_id = form.data.get('type')
                type_name = None

                if type_id:
                    try:
                        type_obj = Type.objects.get(pk=int(type_id))
                        type_name = type_obj.type_name
                    except Exception:
                        type_name = "Тип не найден"
                else:
                    type_name = "Тип не выбран"
                step = '2'
            elif step == '2':
                type_id = form.data.get('type')
                type_name = None

                if type_id:
                    try:
                        type_obj = Type.objects.get(pk=int(type_id))
                        type_name = type_obj.type_name
                    except Exception:
                        type_name = "Тип не найден"
                else:
                    type_name = "Тип не выбран"
                
                category_id = form.data.get('category')
                category_name = None

                if category_id:
                    try:
                        category_obj = category.objects.get(pk=int(category_id))
                        category_name = category_obj.category_name
                    except Exception:
                        category_name = "Категория не найдена"
                else:
                    category_name = "Категория не выбранна не выбрана"


                step = '3'
            elif step == '3':


                form.save()
                return redirect('index')

    return render(request, 'serv/create_record.html', {
        'form': form,
        'step': step,
        'type_name': type_name,
        'category_name': category_name
    })
