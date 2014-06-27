#################################
#Author:Shadowys 25/6/2014
#Description:
#Generate content
#################################

import re
import os
import down
import quill

#Reserved tags {({key}:({parsing_regex_type}, {fallback_value}))*}
reserved_tags={"template":(None,"../template/1skeleton.html"),
               "folder":(None,"../static"),
               "category":(", *","all")}

def transfer(original,extension=None,folder=None):
    """
    Moves the filename to another specified filepath.
    It reserves the original filename.
    """
    parsedpath=re.search("([\w. ]+)\.(\w+)$",original)
    if parsedpath:
        filename=re.sub("[\.\ ]+","-",parsedpath.group(1))
        if not extension : extension=parsedpath.group(2)
        if not folder : folder="static"
        if not os.path.exists(folder):
            os.mkdir(folder)
            print("Folder %s is created."%folder)
        newfilepath="%s/%s.%s"%(folder,filename,extension)
        return newfilepath
    else:
        print("The filename is not vaild : %s"%original)

def route(data,config,key, regex=None):
    """
    Get the element from the data dictionary.
    If the key does not exist/element is None,
    return the element from the configuration file.
    """
    if not regex: regex=r"\\"
    def uniform(parsed,key):
        return re.sub(regex,"/",parsed[key][0].strip(" \r\n")) if key in parsed else None
    if uniform(data,key): return uniform(data,key)
    elif uniform(config,key): return uniform(config,key)

def render(filepath,configpath,extradata=None,reserved=reserved_tags, **kwargs):
    """
    Renders the paths from markdown to a complete html.
    filepath -> path/to/your/markdown/text
    configpath -> path/to/your/configuration/file, for the default values.
    extradata -> a dictionary of user-script provided secondary markdown content.
    reserved -> reserved tags to be used when creating the file.
    **kwargs -> arguments for the markdown convertor.
    """
    if not extradata : extradata={}
    #File checking handled by quill module
    data=down.gen_content(filepath)
    conf=down.gen_config(configpath)
    if data and conf:
        for tag,reg in reserved.items():
            element = route(data,conf,tag,regex=reg[0])
            data[tag] = [element,"p"] if element else [reg[1],"p"]
        data = quill.translate(data)
        #User can escape the extradata dict by setting "safe_mode='escape'"
        extra = quill.translate(extradata,**kwargs)
        new_filename = transfer(filepath,"html",data["folder"])
        new_template = quill.load(data["template"])
        new_html = quill.scribe(new_filename,new_template,data,extra)
        return new_html
    else: print("render file failed for %s"%file)

def renderbatch(configpath,extradata=None,**kwargs):
    """Renders pages in batches specified in the config file."""
    if not extradata : extradata={}
    conf=down.gen_config(configpath)
    print("-"*40)
    if "pages" in conf:
        for file in conf["pages"]:
            render(file, configpath,extradata,**kwargs)
            print("-"*40)
    else: print("No page batch found.")

if __name__=="__main__":
    renderbatch("pages.txt")
    

