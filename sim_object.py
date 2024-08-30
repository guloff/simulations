import pygame
import random
import math
from config import *

class SimObject:
    def __init__(self, x, y, color, energy, vision_radius):
        self.x = x
        self.y = y
        self.color = color
        self.energy = energy
        self.vision_radius = vision_radius
        self.radius = OBJECT_RADIUS
        self.speed_x = random.uniform(-1, 1)
        self.speed_y = random.uniform(-1, 1)
        self.speed = BASE_SPEED

    def move(self):
        self.speed = BASE_SPEED * (self.energy / INITIAL_ENERGY)
        self.x += self.speed_x * self.speed
        self.y += self.speed_y * self.speed

        if self.x - self.radius <= 0 or self.x + self.radius >= SCREEN_WIDTH:
            self.speed_x = -self.speed_x
            self.x = max(self.radius, min(SCREEN_WIDTH - self.radius, self.x))

        if self.y - self.radius <= 0 or self.y + self.radius >= SCREEN_HEIGHT:
            self.speed_y = -self.speed_y
            self.y = max(self.radius, min(SCREEN_HEIGHT - self.radius, self.y))

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def detect_collision(self, other):
        distance = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        return distance < self.radius + other.radius

    def scan_for_targets(self, objects):
        for obj in objects:
            if obj is not self:
                distance = math.sqrt((self.x - obj.x)**2 + (self.y - obj.y)**2)
                if distance < self.vision_radius:
                    return obj
        return None

class RedObject(SimObject):
    def update(self, objects):
        self.energy -= RED_ENERGY_LOSS
        if self.energy <= 0:
            return

        if self.energy > RED_REPRODUCE_ENERGY:
            self.reproduce(objects)

        target = self.scan_for_targets(objects)
        if target and isinstance(target, YellowObject):
            self.speed_x = (target.x - self.x) / SPEED_FACTOR
            self.speed_y = (target.y - self.y) / SPEED_FACTOR
        self.move()

    def reproduce(self, objects):
        self.energy /= RED_REPRODUCE_COUNT
        for _ in range(RED_REPRODUCE_COUNT):
            objects.append(RedObject(self.x, self.y, self.color, self.energy, self.vision_radius))

class GreenObject(SimObject):
    def __init__(self, x, y, color, energy):
        super().__init__(x, y, color, energy, 0)
        self.radius = GREEN_OBJECT_RADIUS

    def update(self, objects):
        self.energy -= GREEN_ENERGY_LOSS
        if self.energy <= 0:
            objects.remove(self)

    def move(self):
        pass

class YellowObject(SimObject):
    def __init__(self, x, y, color, energy, vision_radius):
        super().__init__(x, y, color, energy, vision_radius)
        self.last_reward_time = pygame.time.get_ticks()

    def update(self, objects):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_reward_time >= YELLOW_REWARD_INTERVAL:
            self.energy += YELLOW_REWARD_ENERGY
            self.last_reward_time = current_time

        # Потеря энергии при движении
        self.energy -= YELLOW_ENERGY_LOSS
        
        if self.energy <= 0:
            objects.remove(self)

        if self.energy > YELLOW_REPRODUCE_ENERGY:
            self.reproduce(objects)

        # Проверка на наличие красных объектов в радиусе видимости и убегание от них
        target = self.scan_for_targets(objects)
        if target and isinstance(target, GreenObject):
            dx = target.x - self.x
            dy = target.y - self.y
            self.speed_x = dx / SPEED_FACTOR
            self.speed_y = dy / SPEED_FACTOR
        elif target and isinstance(target, RedObject):
            dx = self.x - target.x
            dy = self.y - target.y
            self.speed_x = dx / SPEED_FACTOR
            self.speed_y = dy / SPEED_FACTOR

        self.move()

    def reproduce(self, objects):
        self.energy /= YELLOW_REPRODUCE_COUNT
        for _ in range(YELLOW_REPRODUCE_COUNT):
            objects.append(YellowObject(self.x, self.y, self.color, self.energy, self.vision_radius))
