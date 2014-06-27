#################################
#Author:Shadowys 25/6/2014
#Description:
#Restore content
#################################

import os
import re
import down
import quill
import feather

#Default folder regeneration values 
#{({key}:({folder path}, {extensions to watch}))*}
default_folders={"pages":("..\\md",["md","txt"]),
                 "template":("..\\template",["html"]),
                 "folder":("..\\",)}
#Arrangement in order of importance.
key_weight=["template","pages","folder"]
newline_separator="\r\n" if os.name=="nt" else "\n"

def get_files_in_folder(extensionlist, directory=".."):
    files=[]
    regex="%s$"%('$|'.join(extensionlist))
    for dirname, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if re.search(regex,filename):
                files.append(os.path.join(dirname, filename))
    return files

def sortunique(*args):
    """
    Returns a sorted list combined from all unique elements
    of the argument lists/sets
    """
    unsortedset=set()
    for unsortedlist in args : unsortedset|=set(unsortedlist)
    return sorted(unsortedset)

def scrub_config(configpath="pages.txt"):
    """
    Returns a restored data of the configuration file
    based on the default values. 
    """
    new_config=dict(template=[],pages=[])
    newline=newline_separator
    if os.path.exists(configpath):
        old_config=down.gen_config(configpath)
    else:
        new_file=open(configpath,'w').close()
        old_config={}
        print("File is created : %s"%configpath)
    for key, value in default_folders.items():
        if len(value)>1:
            pages=get_files_in_folder(value[1],value[0])
            new_config[key]=sortunique(new_config[key],pages)
        elif len(value)==1: new_config[key]=[value[0]]
    return (new_config)

def restore_config(configpath="pages.txt"):
    newline=newline_separator
    new_config=scrub_config(configpath)
    #Arrange the content so it follows the default order 
    new_content=[newline.join(new_config[key]) for key in key_weight]
    #Format : -{tag name} \n {content}
    new_config=newline.join(["-%s%s%s"%(key,newline,values) \
                             for key,values in zip(key_weight,new_content)])
    quill.showsep("Configuration file contents:",new_config)
    quill.write(configpath,new_config)
    return new_config

def scrub_skeleton(configpath="pages.txt"):
    """
    Returns a restored data of the skeleton markdown
    files based on the templates found in the configuration
    """
    if os.path.exists(configpath):
        config=down.gen_config(configpath)
        if "template" not in config:
            restore_config(configpath)
            scrub_skeleton(configpath)
        else:
            template_keylist=[]
            for template in config["template"]:
                template_data=quill.load(template)
                #Tags format : ${tag name}
                keys=re.findall("\$\{(\w+)\}",template_data)
                for reserved_key in feather.reserved_tags.keys():
                    if reserved_key not in keys: keys.insert(0,reserved_key)
                template_keylist.append([template,keys])
            return template_keylist
    else:
        restore_config(configpath)
        scrub_skeleton(configpath)

def restore_skeleton(configpath="pages.txt",special_tags={"navbar":"ul","body":""}):
    new_keylist=scrub_skeleton(configpath)
    newline=newline_separator
    for keylist in new_keylist:
        #Write the markdown file in the ../md folder.
        filepath=feather.transfer(keylist[0],"md","../md")
        skeleton_contents=""
        for key in keylist[1]:
            #Defaults to the <p> HTML tag 
            discarded_tag = "p" if key not in special_tags.keys()\
                            else special_tags[key]
            skeleton_contents+="-%s:%s%s%s"%(key,discarded_tag,newline,newline)
        quill.showsep("Skeleton file contents:",skeleton_contents)
        quill.write(filepath,skeleton_contents)
            
    
if __name__=="__main__":
    import sys
    args=sys.argv
    if len(args)>1:
        if args[1] =="config":
            restore_config()
        elif args[1] =="skeleton":
            restore_skeleton()

    
