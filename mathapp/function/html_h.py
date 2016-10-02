#from django.shortcuts import render
from mathpy import gl

# import model
from mathapp.model.html_m import Layout, MenuItem
# import xml
from xml.etree import cElementTree as Et


# html layout
def set_template(nm='', sub_nm='',usr_in=False):
    #usr_in = False;
    l = Layout()
    l.menu = []
    l.sub_menu = []
    #l.class_c = class_c
    title_a = ''
    title_b = ''
    if nm is None:
        l.title = 'Not found'
        l.description = 'Nothing'
        l.footer = 'Nothing'
        return l
    # get xml element
    tree = Et.parse((gl.BASE_DIR + '/mathapp/data/xml/layout.xml'))
    root = tree.getroot()
    for child in root:
        if child.tag == 'menu':
            # select one from login/register items
            if child.attrib['name'] == 'account':
                if child.attrib['logged'] == 'no' and usr_in:
                    continue
                if child.attrib['logged'] == 'yes' and not usr_in:
                    continue
            # set item on or off
            if child.attrib['name'] == nm:
                for next_child in child:
                    if next_child.attrib['name'] == sub_nm:
                        cl = 'sub-on'
                    else:
                        cl = ''
                    href = '/' + nm + '/' + next_child.attrib['name']
                    m = MenuItem(next_child.attrib["val"], cl, href)
                    l.add_to_submenu(m)
                cl = 'h-off h-on'
                title_b = ' - ' + child.attrib["name"]
            else:
                cl = 'h-off'
            href = '/' + child.attrib['name']
            m = MenuItem(child.attrib["val"], cl, href)
            l.add_to_menu(m)
        elif l.title is None and child.tag == 'site-description':
            title_a = child.attrib["val"]
            l.description = child.text
            #l.image = ''
        elif child.tag == 'footer':
            l.footer = child.text
        #elem.clear()
        l.title = title_a + title_b
    return l


# page content
def content(nm, sub_nm):
    from mathapp.model.home_models import OnePage, Paragraph
    c = OnePage()
    # get xml element
    tree = Et.parse(gl.XML_CONTENT)
    root = tree.getroot()
    for itm in root:
        if itm.tag == 'item' and itm.attrib['name'] == nm:
            for chl_a in itm:
                if chl_a.tag == 'content' and chl_a.attrib['name'] == sub_nm:
                    c.p = []
                    p = Paragraph
                    for child_b in chl_a:
                        if child_b.tag == 'h1':
                            c.header_big = child_b.text
                        elif child_b.tag == 'h2':
                            c.header = child_b.text
                        elif child_b.tag == 'p':
                            p.title = child_b.attrib["title"]
                            p.body = child_b.text
                            c.p.append(p)
                        elif child_b.tag == 'img':
                            c.img = gl.PIC + child_b.attrib["name"]
                            c.img_title = child_b.attrib["title"]
                            c.img_hide = None
                    break
            break
    return c
