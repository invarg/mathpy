#from django.db import models

# the following lines added:
#import datetime
#from django.utils import timezone


class Site:
    def __init__(self, name, description):
        self.nm = name
        self.desc = description


class MenuItem:
        name = ''
        class_css = ''
        class_c = ''
        href = ''

        def __init__(self,name, class_css, href):
            self.name = name
            self.class_css = class_css
            self.href = href


class Layout:
    'Common base class for all employees'
    menu = []   #MenuItem
    sub_menu = []   #MenuItem
    title = None
    description = ''
    image = ''
    footer = ''
    paragraphs = ''

    def __init__(self):
        self

    def add_to_menu(self, item):
        self.menu.append(item)

    def add_to_submenu(self, item):
        self.sub_menu.append(item)