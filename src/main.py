import pygame as pg
import player
import obstacle


pg.init()
screen = pg.display.set_mode((1000, 1000))
running = True
clock = pg.time.Clock()
obs_list = [
    obstacle.Obstacle(screen, (100, 100), (250, 250)),
    obstacle.Obstacle(screen, (100, 100), (750, 250)),
    obstacle.Obstacle(screen, (100, 100), (750, 750)),
    obstacle.Obstacle(screen, (100, 100), (250, 750))
]
pl = player.Player(screen, obs_list)


while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            raise SystemExit

    pressed = pg.key.get_pressed()
    if pressed[pg.K_LEFT]:
        pl.move_left()
    if pressed[pg.K_RIGHT]:
        pl.move_right()
    if pressed[pg.K_DOWN]:
        pl.move_down()
    if pressed[pg.K_UP]:
        pl.move_up()

    screen.fill((0, 0, 0))
    pl.udpate()
    for obs in obs_list:
        obs.update()

    pg.display.set_caption(f"{clock.get_fps()}")
    clock.tick(60)
    pg.display.update()