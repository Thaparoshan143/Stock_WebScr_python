import requests
from bs4 import BeautifulSoup

def get_price():
    origin_url="https://merolagani.com/CompanyDetail.aspx?symbol="
    # Give the name of script you want to run below are given examples
    scripts_name=["nabil","mbjc","hhl","ntc"]
    scripts_tol=[500,250,200,700]

    for index,script in enumerate(scripts_name):
        target_url=origin_url+script
        # print(target_url)

        web_resp=requests.get(target_url)

        if web_resp.status_code==200:
            # print("Successfully response gone and opened file!")

            soup=BeautifulSoup(web_resp.text,'html.parser')

            strong_content=soup.find("strong")
            strong_content=str(strong_content)
            # print(strong_content)

            first_index=strong_content.find("\">")+2
            last_index=strong_content.find("</span>")

            price_content=strong_content[first_index:last_index]

            price_string=str(price_content)

            # replacing if it has , for thousand places
            if price_string.find(",")==-1:
                price_string=price_string
            else:
                price_string=price_string.replace(",","")

            price_int=int(float(price_string))
            # print(price_int)

            # checking if the current price is below tol
            if price_int<=scripts_tol[index]:
                print("Current Market Price is below the tol price mentioned")
            else:
                print("Market price is high")

            print(f'{price_int} - Mp and {scripts_tol[index]} -  tolerance :::-> {script}')

get_price()