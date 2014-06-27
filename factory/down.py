#################################
#Author:Shadowys 25/6/2014
#Description:
#Parse content
#################################

import os
import re
import quill

def parse_file(filepath,default_key="body",default_tag="p"):
    """
    Parses files that have the format of 
    -{tagname}:{HTML tag to discard}
    {content}
    The parsed content is arranged into a dictionary
    The default key is the key to allocate if the first line
    of the content does not have a tag. 
    The default tag is the HTML tag to be discarded later on if 
    the tag do not have a HTML tag written.
    """
    file=quill.load(filepath).split("\n")
    if file:
        file=[line.strip("\r") for line in file]
        data={}
        currentkey=""
        for line in file :
            matched=re.match("-(\w+):?(\w+)*",line)
            if matched :
                data[matched.group(1)]=[[],matched.group(2)]
                currentkey=matched.group(1)
            else:
                if not currentkey:
                    currentkey=default_key
                    data[currentkey]=[[],default_tag]
                data[currentkey][0].append(line)
        return data
    else: return {}

def gen_config(filepath):
    config=parse_file(filepath)
    #Config files do not need the discarded tag value.
    config={key:value[0] for key,value in config.items()}
    return config

def gen_content(filepath,default_key="body",default_tag="p"):
    content=parse_file(filepath,default_key,default_tag)
    #Content should be continuous.
    content={key:["\n".join(value[0]),value[1]]\
             for key,value in content.items()}
    return content
