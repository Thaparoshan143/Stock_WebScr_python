import requests
from bs4 import BeautifulSoup

# Class can be used to oraganize and get other stuffs, not used currently
# class Script:
#     def __init__(self,name,price=0,tol=0):
#         self.name=name
#         self.price=price
#         self.tol=tol

# opens the file and returns the string list 
# if string are in different lines
def getFileContentInList(fileName):
    new_lines=[]
    lines=fileName.readlines()
    for line in lines:
        new_lines.append(line.replace("\n",""))

    return new_lines

# takes the outer element and get the content inside the span in string form if it has , then it removes as well
def getSpanContent(oc):
    first_index=oc.find("\">")+2
    last_index=oc.find("</span>")

    span_content=oc[first_index:last_index]

    span_str=str(span_content)

    # replacing if it has , for thousand places
    if span_str.find(",")==-1:
        return span_str
    else:
        return span_str.replace(",","")

def getElementInString(text,element):
    strong_content=text.find(element)
    return str(strong_content)

def get_price():
    origin_url="https://merolagani.com/CompanyDetail.aspx?symbol="

    # object list might be useful for future
    # script_names_obj=[]

    script_names=[]
    script_tols=[]

    # name of file containing certain script with another tol can be used using input stream
    # scriptNameFileName=input()
    # scriptTolFileName=input()
    # scriptNameFileName=scriptNameFileName+".txt"
    # scriptTolFileName=scriptTolFileName+".txt"

    # For now just manually/forcing to default file names
    scriptNameFileName="Scripts_Name.txt"
    scriptTolFileName="Scripts_Tol.txt"

    # reading from files and arranging in list of string for script name and it's tol
    with open(scriptNameFileName,"r") as scriptFile:
        script_names=getFileContentInList(scriptFile)

    with open(scriptTolFileName,"r") as scriptFile:
        script_tols=getFileContentInList(scriptFile)


    # opening the new file for writing the stocks information with remarks
    MPFile=open("Scripts_MP.txt","w")
    MPFile.write("MP of given list [Format - Sn. Script_Name - Market_Price || Given Tol || Remarks(Buy/Sell)]\n\n")
    
    # make sure the tol and the script matches in length
    for index,script in enumerate(script_names):
        # constructing the given script url to parse data
        target_url=origin_url+script

        # requesting the given URL for data
        web_resp=requests.get(target_url)
    
        # This is only valid for the given website(above), element selected will be different for other website
        if web_resp.status_code==200:
            # parse entire the html code in soup
            soup=BeautifulSoup(web_resp.text,'html.parser')

            # finding the first element of strong, it contains the MP in the given website
            strong_content=getElementInString(soup,"strong")

            mpPrice_String = getSpanContent(strong_content)
            print(mpPrice_String)

            mpPrice_int=int(float(mpPrice_String))

            # this doesnt seem to work for out of index..., anyway gets the tolerance price for given script from file
            script_tol = int(script_tols[index]) if script_tols[index]!=None else 0

            if script_tol > mpPrice_int :
                remarks="Buy"
                print("==> " + script + " - RS " + mpPrice_String + " || Tol : " + str(script_tol) + " || Remarks : "+ remarks)
            else:
                remarks="Dont Buy Now !" 
            
            # Writing in File
            MPFile.write(str(index+1) + ". " + script + " - RS " + mpPrice_String + " || Tol : " + str(script_tol) + " || Remarks : "+ remarks + "\n")
            # script_names_obj.append(Script(script,mpPrice_int,script_tol))

    MPFile.close()

get_price()