from django.shortcuts import render, redirect, HttpResponse
from utils.sql_handler import get_list, get_one, modify
def get_teacher(request):
    '''
    get_teacher不仅要获取教师的信息, 还要获取教师任教的班级的信息
    教师信息在teacher表里, 教师对应的班级id在teacher2class表里,
    班级title在class表里, 所以这是个三表查询.
    :param request:
    :return:
    '''
    teacher_list = get_list('select id, name from teacher',[])
    teacher_list = get_list('')
    return render(request, 'teacher/get_teacher.html', {
        'teacherList': teacher_list
    })
def del_teacher(request):
    did = request.GET.get('did')
    modify('delete from teacher where id=%s', [did])
    return redirect('/get_teachers')
def add_teacher(request):
    name = request.POST.get('name')
    classes = request.POST.get('class')
    print(name)
    print(classes)
    return redirect('/get_teacher')