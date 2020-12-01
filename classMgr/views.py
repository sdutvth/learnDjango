from django.shortcuts import render, redirect
from utils.sql_handler import get_list, get_one, modify

def get_class(request):
    # 取数据
    class_list = get_list('select class.id, class.title, GROUP_CONCAT(teacher2class.teacher_id) teacher_id, GROUP_CONCAT(teacher.name) teacher_name from class left join teacher2class on class.id=teacher2class.class_id left join teacher on teacher2class.teacher_id=teacher.id GROUP BY(class.id)', [])
    '''
    {'id': 12, 'title': '1班', 'teacher_id': '16,17', 'teacher_name': '老王,老李'}
    '''
    for item in class_list:
        if item['teacher_id']:
            tmp = item['teacher_id'].split(',')
            item['teacher_id'] = list(map(lambda x:int(x), tmp))
        if item['teacher_name']:
            item['teacher_name'] = item['teacher_name'].split(',')
    print(class_list)
    return render(request, 'class/get_class.html', {
        'classList': class_list
    })

def add_class(request):
    if request.method == 'GET':
        return render(request, 'class/add_class.html')
    else:
        title = request.POST.get('title')
        modify('insert into class (title) values (%s)', [title])
        return redirect('/get_class')

def update_class(request):
    if request.method == 'GET':
        mid = request.GET.get('mid')
        title = request.GET.get('title')
        return render(request, 'class/update_class.html', {
            'item':{
                'id': mid,
                'title': title
            }
        })
    else:
        uid = request.POST.get('uid')
        title = request.POST.get('title')
        modify('update class set title=%s where id=%s',[title, uid])
        return redirect('/get_class')

def del_class(request):
    did = request.GET.get('did')
    modify('delete from class where id=%s',[did])
    return redirect('/get_class')