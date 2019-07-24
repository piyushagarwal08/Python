import pyautogui as pg
import time
pg.FAILSAFE = False
print('initiated')
pg.click(272,754) # firefox location
time.sleep(5)
print('clicked on firefox')

pg.click(550,46)  # click on search bar
time.sleep(1)
print('clicked on search bar')


pg.typewrite('web.whatsapp.com')  # opens whatsapp .com
pg.press('enter')
time.sleep(60)
print('whatsappweb opened' )


pg.click(164,247)   # clicks on chat search bar
time.sleep(3)

pg.typewrite('Harshita sharma')
time.sleep(3)

pg.click(198,383)   # clicks on harshita chat box
time.sleep(3)

pg.click(582,701)   # clicks on chat bar to start typing
time.sleep(3)

pg.typewrite('starting the test... pls gussa mat hona... bohat majedaar cheez hai ye')
pg.press('enter')  # clicks on enter
time.sleep(3)
count=0
time.sleep(10)
song = '''Ho O O O O........Ho O O O O Ho.......,
Aaja Main Hawaon Pe Bithake Le Chalu Tu Hi To
Tu Hi To Meri Dost Hain
Aaja Main Khalaon Mein Uthake Le Chalu
Tu Hi To Meri Dost Hain
Awaaz Ka Dariya Hoon, Behta Hoon Main Nili Raaton Mein
Main Jaagta Rehta Hoon, Nind Bhari Jheel Se Aankhon Mein
Awaaz Hoon Main
Aaja Main Hawaon Pe Bithake Le Chalu Tu Hi To
Tu Hi To Meri Dost Hain
Aaja Main Khalaon Mein Uthake Le Chalu
Tu Hi To Meri Dost Hain
Aaja Main Khalaon Mein Uthake Le Chalu
Tu Hi To Meri Dost Hain
Raat Mein Chandani Kabhi Aisi Gungunati Hain
Sun Jara Lagata Hain Tumase Awaaz Milaati Hain
Main Khayalo Ki Mehak Hu, Gungunaate Saaj Par
Ho Sake To Milale, Awaaj Ko Mere Saaj Par
Aaja Main Hawaon Pe Bithake Le Chalu Tu Hi To
Tu Hi To Meri Dost Hain
Aaja… '''
song = song.split('\n')
while True:
    pg.click(582,701)  # click on chat box
    pg.typewrite(f'song dedicated to you, count: {count}') # writes a message
    pg.press('enter')  # send the message
    for i in song:
        pg.click(582,701)   # click on chat box
        pg.typewrite(i)    # type the first line of song
        time.sleep(3)   # wait for 1 sec
        pg.press('enter')   # press enter and send message
    count = count + 1
          
