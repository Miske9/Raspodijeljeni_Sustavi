import asyncio
import time
#korutine
#async def main():
    #print("hello")
    #await asyncio.sleep(2)
    #await time.sleep(1)
    #print("world")
    
#asyncio.run(main())
#coroutine_objekt = main()
#asyncio.run(coroutine_objekt)

#async def main():
 #   event_loop = asyncio.get_running_loop()
  #  print(f'trenutni aktivni event loop: {event_loop}')
#asyncio.run(main())
#event_loop = asyncio.get_running_loop()
#print(f'Nakon zavrsetka event loop: {event_loop}')

def fetch_data(param):
    print(f"Nesto radim s {param}...")
    time.sleep(int(param))
    print(f"Dovrsio sam s {param}.")
    return f"Rezultat za {param}"

def main():
    rez1 = fetch_data(1)
    print("Fetch 1 uspjesno zavrsen.")
    rez2 = fetch_data(2)
    print("Fetch 2 uspjesno zavrsen.")
    return[rez1, rez2]

rezultati = main()
print(f"Rezultati: {rezultati}")