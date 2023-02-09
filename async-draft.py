import asyncio
import keyboard

async def main():
    print('start')
    task = asyncio.create_task(check_keyboard_input())
    await asyncio.sleep(5)
    print('termino')

async def check_keyboard_input():
    while True:
        if keyboard.is_pressed('space'):
            print('espacio')
    

asyncio.run(main())