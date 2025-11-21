#pip freeze --> requirements od virtualnog okruzenja
import requests
import asyncio
import aiohttp
import time

#response = requests.get("http://catfact.ninja/fact")
#print(response.text)
lista = []
#t1 = time.perf_counter()

#for i in range (10):
 #   print(f"Saljem request za fact {i}")
  #  response = requests.get("http://catfact.ninja/fact")
   # lista.append(response.json())
#t2 = time.perf_counter()

#context manager - input output manager (with npr)
#asinkroni context manager
rezultati = []

async def dohvati_cat_fact(session: aiohttp.ClientSession):
    response = await session.get("http://catfact.ninja/fact")
    podatak = await response.json()
    print(f"podatak {podatak}")
    return podatak["fact"]

async def main():
    async with aiohttp.ClientSession() as session:
        rezultati = await asyncio.gather(*[dohvati_cat_fact(session) for i in range (10)])
        print(rezultati)
    print("zavrsava korutina")
#print(lista)
#print(f"Vrijeme izvrsavanja: {t2-t1}") 
t1 = time.perf_counter()
asyncio.run(main())
t2 = time.perf_counter()
print(f"vrijeme izvodenja: {t2-t1}")