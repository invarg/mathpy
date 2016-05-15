from django.shortcuts import render

# Create your view here.
from django.shortcuts import render
from django.http import HttpResponse
from mathpy import gl as gl
# import html helper
from .function.html_h import set_template

# import model
from mathapp.model.home_models import OnePage

ls = globals()


# load xml template data and redirect to function in view
def redirect(request, view='index', prm=None):
    try:
        if ls[view] in ls:
            pass
    except:
        # redirect to 404
        l = set_template(None)
        return render(request, '404.html', {'m': l})
    l = set_template('home', view)
    if prm is None:
        return ls[view](request, l)
    return ls[view](request, prm, l)


# index page
def index(request, l=set_template('home', '')):
    c = OnePage()
    from xml.etree import cElementTree as Et
    # get xml element
    tree = Et.parse(gl.XML_CONTENT)
    root = tree.getroot()
    for cnt in root:
        if cnt.tag == 'content' and cnt.attrib['name'] == 'home':
            c.paragraphs = []
            for fst_child in cnt:
                if fst_child.tag == 'h1':
                        c.header_big = fst_child.text
                else:
                    if fst_child.tag == 'h2':
                        c.header = fst_child.text
                    else:
                        if fst_child.tag == 'p':
                            c.paragraphs.append(fst_child.text);
            break

    connection = gl.conn()
    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "insert into test_table (test) value('test three'); SELECT test FROM site_db.test_table where idnew_table = 2;"
            cursor.execute(sql, ['2'])
            result = cursor.fetchone()
            r1 = result['test']
    finally:
        cursor.close()
        connection.close()
    return render(request, 'home/index.html', {'a': r1,'cont': c, 'm': l})


def first(request, l):
    c = OnePage()
    from xml.etree import cElementTree as Et
    # get xml element
    tree = Et.parse(gl.XML_CONTENT)
    root = tree.getroot()
    for cnt in root:
        if cnt.tag == 'content' and cnt.attrib['name'] == 'test':
            for fst_child in cnt:
                for snd_child in fst_child:
                    if snd_child.tag == 'h1':
                        c.header_big = snd_child.text
                    else:
                        if snd_child.tag == 'h2':
                            c.headers = snd_child.text
                            pass
                        else:
                            if snd_child.tag == 't':
                                c.paragraphs = snd_child.text
            break
    return render(request, 'home/test_main.html', {'cont': c, 'm': l})



def third(request, prm, l):
    return render(request, 'home/test2.html', {'m': l})


def results(request, question_id):
    response = "You're looking at the results of question s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)