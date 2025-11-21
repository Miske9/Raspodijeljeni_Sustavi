import asyncio

async def timer(sec: int):
    print(f'izvrsavam timer {sec}.')
    await asyncio.sleep(sec)
    print(f"Zavrsavam timer {sec}")
    return f"Rezultat timera {sec}"

async def autentifikacija():
    await asyncio.sleep(5)
    raise Exception

async def main():
    #timer_cor = timer(1)
    #timer_cor2 = timer(2)
    #timer_cor3 = timer(3)
    #task = asyncio.create_task(timer_cor)
    #task2 = asyncio.create_task(timer_cor2)
    #task3 = asyncio.create_task(timer_cor3)
    
    #task objekte nemora se raditi kad se koristi gather
    lista_korutina = [asyncio.create_task(timer(n)) for n in range (1, 4)]
    #rez = await asyncio.gather(timer_cor, timer_cor2, timer_cor3) #schedule and run and gather
    rez = await asyncio.gather(*lista_korutina)
    #rezultat = await task2 #event loop se gasi ovdje
    print(rez)

asyncio.run(main())