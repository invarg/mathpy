from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate as auth, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect   # Add this
from mathpy import gl as gl
# import html helper
from ..function.html_h import set_template, content

# import model


ls = globals()
#flag = None


# index page
def index(request, view='initial'):
    fl = request.user.is_authenticated()
    l = set_template('home', view, fl)
    c = content('home', view)
    from django.db import connection
    try:
        with connection.cursor() as cursor:
            # Read a single record
            prm = {'id': '2'}
            sql = """set @a = (SELECT test FROM site_db.test_table where idnew_table = "2");"""
            cursor.execute(sql)
            sql = " set @b = (SELECT test FROM site_db.test_table where idnew_table = %(id)s);"
            cursor.execute(sql, prm)
            sql = " set @c = (SELECT test FROM site_db.test_table where idnew_table = 3);"
            cursor.execute(sql)
            sql = " select concat(@a,'***', @b,'***',@c);"
            cursor.execute(sql)
            result = cursor.fetchone()
            r1 = result[0]
    finally:
        cursor.close()
        connection.close()
    return render(request, 'home/index.html', {'a': r1,'cont': c, 'm': l})


def numbers(request, view='initial'):
    l = set_template('numbers', view, request.user.is_authenticated())
    c = content('numbers', view)
    return render(request, 'home/index.html', {'cont': c, 'm': l})


def client(request, view='initial'):
    l = set_template('client', view, request.user.is_authenticated())
    c = content('client', view)
    return render(request, 'home/index.html', {'cont': c, 'm': l})


def contact(request, view='initial'):
    l = set_template('contact', view, request.user.is_authenticated())
    c = content('contact', view)
    return render(request, 'home/index.html', {'cont': c, 'm': l})


def practice(request, view='initial'):
    l = set_template('practice', view, request.user.is_authenticated())
    c = content('practice', view)
    return render(request, 'home/index.html', {'cont': c, 'm': l})


def results(request, question_id):
    response = "You're looking at the results of question s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
