import datetime
import feather,quill,down

def getdate():
    #Make sure the four Python scripts are on your Python Path\n
    today=datetime.datetime.now()
    date=today.strftime("%d-%m-%y")
    date={"date":[date,"p"]}
    return date

def main(configpath):
    config=down.gen_config(configpath)
    pages=config["pages"]
    for file in pages:
        date=getdate()
        feather.render(file,configpath,date)
        
if __name__=="__main__":
    main("pages.txt")
