from bs4 import BeautifulSoup
import requests as rq 
import pandas as pd

class pricedata():
    def T_M_B_converter(self,lemment):
        if "T" in elemment:
            elemment = elemment.replace("T","")
            elemment = elemment.replace(",","")
            elemment = float(elemment) * 1000000000000
        else:
            if "B" in elemment:
                elemment = elemment.replace("B","")
                elemment = elemment.replace(",","")
                elemment = float(elemment) * 1000000000
            else:
                if "M" in elemment:
                    elemment = elemment.replace("M","")
                    elemment = elemment.replace(",","")
                    elemment = float(elemment) * 1000000
                else:
                    print("Error - in value")

        return float(elemment)


    def get_current_price(self,stock):
        url = f"https://in.finance.yahoo.com/quote/{stock}.NS"
        html = rq.get(url).text    
        soup = BeautifulSoup(html,"lxml")
        price1 = soup.find("div",id="quote-header-info")
        price2 = price1.find("span", class_ ="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
        price3 = price2.text
        price = price3.replace(",","")

        return float(price)

    def get_stock_volume(self,stock):
        url = f"https://in.finance.yahoo.com/quote/{stock}.NS"
        data = pd.read_html(url)
        volume = data[0].at[6,1]
        volume = volume.replace(",","")

        return float(volume)
