from bs4 import BeautifulSoup
import requests
import time
from win10toast import ToastNotifier


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

req = requests.get("https://www.google.com/search?q=tempo+aparecida&sxsrf=AOaemvIiDIuIAVSNrHNwQp8HiGywxo69ng%3A1630077317645&ei=hQEpYbPiJp_Q1sQPwc20-Ac&oq=tempo+apa&gs_lcp=Cgdnd3Mtd2l6EAMYATIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgjELADECc6BwgAEEcQsAM6BwgAELADEEM6DggjECcQExCdAhBGEIACOgYIABAeEBM6BwgjEOoCECc6BwguEOoCECc6BwguECcQkwI6BAgjECc6CwgAEIAEELEDEIMBOhEILhCABBCxAxCDARDHARDRAzoICAAQgAQQsQM6EQguEIAEELEDEIMBEMcBEKMCOgQIABBDOgoIABCxAxCDARBDOg0IABCxAxCDARDJAxBDOgUIABCSAzoICAAQsQMQgwE6DggAEIAEELEDEIMBEMkDOgoIABCxAxCDARAKSgQIQRgAULYNWOwqYPs4aAJwAngGgAGfA4gBwRiSAQowLjE0LjIuMS4xmAEAoAEBsAEKyAEKwAEB&sclient=gws-wiz", headers=headers)

soup = BeautifulSoup(req.text, 'html.parser')

cidade = soup.select("#wob_loc")[0].getText().strip()
temperatura = soup.select("#wob_tm")[0].getText().strip()
dia_hora = soup.select("#wob_dts")[0].getText().strip()
clima = soup.select("#wob_dc")[0].getText().strip()

cidade2=cidade.replace(", SP","-SP")
dia = dia_hora[0:14].replace(","," ")
hora = dia_hora[13:]
hora = hora.replace(":","h")

informe = f"{dia}-{hora}\n{cidade2}\n{temperatura} °C\n{clima}"

toaster = ToastNotifier()
toaster.show_toast("Tempo agora:", f"{informe}", duration=10)



