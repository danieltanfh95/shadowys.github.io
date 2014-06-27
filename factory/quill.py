#################################
#Author:Shadowys 25/6/2014
#Description:
#Transcribes content
#################################

import markdown
import codecs
import re
import string
import os

def write(filename,data):
    with codecs.open(filename, 'w', encoding="utf-8") as f:
        print(data,file=f)
        print("%s is written."%filename)
    return data

def load(filename):
    if os.path.exists(filename):
        with codecs.open(filename, 'r', encoding="utf-8") as f:
            print("%s is read."%filename)
            return f.read()
    else:
        print("File not found %s" %filename)
        return ""

def translate(data,default_tag="p",**kwargs):
    """
    Translates markdown elements in a dictionary 
    parsed by down.gen_config into a dictionary
    of HTML contents.
    The dictionary passed in should be in the format:
    {({tagname}:[{markdown content},{HTML tag to discard}])*}
    """
    ExtensionsUsed=['toc','nl2br','headerid','extra',
                    'codehilite(noclasses=True,pygments_style=monokai)']
    for key in data.keys():
        if type(data[key])!=list:
            print("List not found in the dictionary element.\n"+
                  "element value is changed to list\n"+
                  "element changed : %s"%data[key])
            data[key]=[data[key],default_tag]
        data[key][0]=markdown.markdown(data[key][0],
                                       extensions=ExtensionsUsed,
                                       **kwargs)
        CapturePattern="^<%s>(.*)</%s>$"%(data[key][1],data[key][1]) \
                       if len(data[key])>1 else ""
        CapturedText=re.findall(CapturePattern, data[key][0])
        if CapturedText: data[key]=CapturedText[0]
        else: data[key]=data[key][0]
    return data

def showsep(*args):
    """Prints something so it's clamped by hyphens, for viewing."""
    for line in args:
        print("-"*40)
        print(line)
        print("-"*40)


def transcribe(template,data):
    #Safe substitution ensures that the secondary tags remain
    html=string.Template(template).safe_substitute(data)
    return html

def transcribe_safe(template,data,default=""):
    #Substitue secondary data and clears unused tags.
    class safesub(dict):
        def __missing__(self,key):return default
    html=string.Template(template).substitute(safesub(data))
    return html

def scribe(filename,template,data,extra=None):
    if not extra : extra={}
    html=transcribe(template,data)
    html=transcribe_safe(html,extra)
    write(filename,html)
    return html
