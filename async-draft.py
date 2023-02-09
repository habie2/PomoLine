import asyncio
import keyboard

async def main():
    print('start')
    task = asyncio.create_task(check_keyboard_input())
    await asyncio.sleep(5) 
    print('termino')

async def check_keyboard_input():
    press = False
    while True and not press:
        if keyboard.is_pressed('space'):
            print('espacio')
            press= True
            
    

asyncio.run(main())