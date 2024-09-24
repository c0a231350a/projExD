import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん") #ゲームのタイトル
    screen = pg.display.set_mode((800, 600)) #横縦の大きさ
    clock  = pg.time.Clock() 
    bg_img = pg.image.load("fig/pg_bg.jpg") #画像読み込み
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0]) #画像貼り付け
        screen.blit(kk_img, [300,200])
        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()