import pyautogui as pg

img1 = pg.screenshot()
img2 = pg.screenshot('my_sc.png')
img3 = pg.screenshot('my_sc_region.png', (0, 0, 300, 300))

print(img1, img2, img3)

img1.show()
img2.show()
img3.show()

# https://codetorial.net/pyautogui/locate_by_image.html
