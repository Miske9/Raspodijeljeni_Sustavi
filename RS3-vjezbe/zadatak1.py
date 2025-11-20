import asyncio

async def dohvat_podataka():
    await asyncio.sleep(3)    
    podaci = [x for x in range(1, 11)] 
    print("Podaci dohvaćeni.")
    return podaci

async def main():
    rezultat = await dohvat_podataka()
    print("Rezultat:", rezultat)

asyncio.run(main())
