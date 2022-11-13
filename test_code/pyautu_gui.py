import pyautogui as pg

print(pg.position())
print(pg.size())

# pg.moveTo(200, 200)
# pg.click(1920, 1080, button='left', clicks=2, interval=0.1)

# pg.moveRel(0, 1000)
# pg.doubleClick()

# pg.dragTo(300, 300, button='left')
# pg.dragTo(400, 400, 2, button='left')
# pg.dragRel(30, 0, 2, button='right')

pg.click((3400, 1327))
pg.typewrite('메롱', interval=0.1)

# pg.typewrite(['a', 'b', 'c'], interval=0.1)
# pg.typewrite(pg.KEYBOARD_KEYS, interval=0.1)

pg.doubleClick()

pg.hotkey('ctrl', 'c')
pg.hotkey('ctrl', 'v')

pg.press('c')

