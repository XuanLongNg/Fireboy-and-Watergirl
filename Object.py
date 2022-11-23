import pygame


class Lava:
    def __init__(self, object):
        ibs = 32
        self.object = [
            [
                object.subsurface(ibs*15 + ibs*0.5, ibs*42, ibs, ibs),  # 0
                object.subsurface(ibs*15 + ibs*0.5, ibs*42, ibs, ibs),
                object.subsurface(ibs*15 + ibs*0.5, ibs*42, ibs, ibs),
                object.subsurface(ibs*20 + ibs*0.5, ibs*42, ibs, ibs),
                object.subsurface(ibs*20 + ibs*0.5, ibs*42, ibs, ibs),
                object.subsurface(ibs*20 + ibs*0.5, ibs*42, ibs, ibs),  # 5
                object.subsurface(ibs*25 + ibs*0.6, ibs*42, ibs, ibs),
                object.subsurface(ibs*25 + ibs*0.6, ibs*42, ibs, ibs),
                object.subsurface(ibs*25 + ibs*0.6, ibs*42, ibs, ibs),
                object.subsurface(ibs*30 + ibs*0.7, ibs*42, ibs, ibs),
                object.subsurface(ibs*2, ibs*44 - ibs*0.3, ibs, ibs),  # 10
                object.subsurface(ibs*2, ibs*44 - ibs*0.3, ibs, ibs),
                object.subsurface(ibs*3 + ibs*0.7, ibs*44 - ibs*0.3, ibs, ibs),
                object.subsurface(ibs*3 + ibs*0.7, ibs*44 - ibs*0.3, ibs, ibs),
                object.subsurface(ibs*3 + ibs*0.7, ibs*44 - \
                                  ibs*0.3, ibs, ibs)  # 14
            ],
            [
                object.subsurface(ibs*2 - ibs/30, ibs*43 -
                                  ibs*0.82, ibs, ibs),  # 0
                object.subsurface(ibs*2 - ibs/30, ibs*43-ibs*0.82, ibs, ibs),
                object.subsurface(ibs*2 - ibs/30, ibs*43-ibs*0.82, ibs, ibs),
                object.subsurface(ibs*5 + ibs*0.33, ibs*43-ibs*0.82, ibs, ibs),
                object.subsurface(ibs*5 + ibs*0.33, ibs*43-ibs*0.82, ibs, ibs),
                object.subsurface(ibs*5 + ibs*0.33, ibs*43 - \
                                  ibs*0.82, ibs, ibs),  # 5
                object.subsurface(ibs*10 + ibs*0.4, ibs*43-ibs*0.82, ibs, ibs),
                object.subsurface(ibs*10 + ibs*0.4, ibs*43-ibs*0.82, ibs, ibs),
                object.subsurface(ibs*10 + ibs*0.4, ibs*43-ibs*0.82, ibs, ibs),
                object.subsurface(ibs*22 + ibs*0.2, ibs*40-ibs*1.05, ibs, ibs),
                object.subsurface(ibs*22 + ibs*0.2, ibs*40 - \
                                  ibs*1.05, ibs, ibs),  # 10
                object.subsurface(ibs*22 + ibs*0.2, ibs*40-ibs*1.05, ibs, ibs),
                object.subsurface(ibs*27+ibs*0.3, ibs*40-ibs*1.05, ibs, ibs),
                object.subsurface(ibs*27+ibs*0.3, ibs*40-ibs*1.05, ibs, ibs),
                object.subsurface(ibs*27+ibs*0.3, ibs*40 - \
                                  ibs*1.05, ibs, ibs)  # 14
            ],
        ]

    def update_animation(self, screen, lct_x, lcx_y, k):
        if k > 13:
            h = -1
        k += 1
        screen.blit(self.object[k], (lct_x, lcx_y))
        return k


class Diamond:
    def __init__(self, object):
        cs = 136
        self.object = [
            object.subsurface(0, cs*10-20, cs-26, cs-26),  # red blue
            object.subsurface(cs*6+33, cs*10-20, cs-26, cs-26),  # white
            object.subsurface(cs*7+17, cs*10-20, cs-26, cs-26),  # blue
            object.subsurface(cs*8-2, cs*10-20, cs-26, cs-26),  # red
        ]
    # update character's animation

    def update_animation(self, screen, lct_x, lcx_y, k, step):
        if round(abs(k)) == 5:
            step *= -1
        k += step
        screen.blit(self.object[2], (lct_x, lcx_y+k))
        return k, step
