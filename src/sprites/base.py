
import pygame

from src.enums import LAYER


class Sprite(pygame.sprite.Sprite):
    def __init__(self,
                 pos: tuple[int | float,
                            int | float],
                 surf: pygame.Surface,
                 groups: tuple[pygame.sprite.Group, ...] | pygame.sprite.Group,
                 z: int = LAYER.MAIN,
                 name: str | None = None):
        super().__init__(groups)
        self.surf = surf
        self.image = surf
        self.rect = self.image.get_frect(topleft=pos)
        self.z = z
        self.name = name


class CollideableSprite(Sprite):
    def __init__(self, pos, surf, groups, shrink, z=LAYER.MAIN):
        super().__init__(pos, surf, groups, z)
        self.hitbox_rect = self.rect.inflate(-shrink[0], -shrink[1])


class AnimatedSprite(Sprite):
    def __init__(self, pos, frames, groups, z=LAYER.MAIN):
        self.frames, self.frame_index = frames, 0
        super().__init__(pos, frames[0], groups, z)

    def animate(self, dt):
        self.frame_index += 2 * dt
        self.image = self.frames[int(self.frame_index) % len(self.frames)]

    def update(self, dt):
        self.animate(dt)
