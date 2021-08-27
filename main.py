import pygame as pg
pg.init()
from Destructible import Destructible
WIDTH, HEIGHT = 650, 650
WIN = pg.display.set_mode((WIDTH, HEIGHT))


def draw(*args, rect):
    WIN.fill((0, 0, 0))
    for arg in args:
        WIN.blit(arg.surface, arg.rect)
    pg.draw.rect(WIN, pg.Color(255, 48, 0, a=128), rect)
    pg.display.update()


def main():
    hq = Destructible(image='HQ')
    hq.rect.x = (WIDTH - hq.rect.width) / 2
    hq.rect.y = (HEIGHT - hq.rect.height) / 2
    play = True
    active_drag = False
    drag_origin = None
    def current_rect():
        r = pg.Rect(drag_origin, (pg.mouse.get_pos()[0]-drag_origin[0], pg.mouse.get_pos()[1]-drag_origin[1]))
        r.normalize()
        return r
    empty_rect = pg.Rect((0, 0), (0, 0))
    while play:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                play = False
        if pg.mouse.get_pressed(num_buttons=3)[0]:
            if active_drag:
                pass
            else:
                active_drag = True
                drag_origin = pg.mouse.get_pos()
        else:
            active_drag = False
            drag_origin = None
        draw(hq, rect=(current_rect() if active_drag else empty_rect))
        # draw(hq, rect=empty_rect)


if __name__ == '__main__':
    main()
