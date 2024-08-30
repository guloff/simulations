import pygame
import time
import random
from datetime import datetime
from config import *
from statistics import save_general_statistics, save_object_statistics, display_general_statistics_on_screen, create_charts
from sim_object import RedObject, YellowObject, GreenObject

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(WINDOW_CAPTION)

    font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)

    red_objects = [RedObject(random.randint(OBJECT_RADIUS, SCREEN_WIDTH - OBJECT_RADIUS),
                             random.randint(OBJECT_RADIUS, SCREEN_HEIGHT - OBJECT_RADIUS),
                             RED_COLOR, INITIAL_ENERGY, RED_VISION_RADIUS) for _ in range(NUM_RED_OBJECTS)]

    yellow_objects = [YellowObject(random.randint(OBJECT_RADIUS, SCREEN_WIDTH - OBJECT_RADIUS),
                                   random.randint(OBJECT_RADIUS, SCREEN_HEIGHT - OBJECT_RADIUS),
                                   YELLOW_COLOR, INITIAL_ENERGY, YELLOW_VISION_RADIUS) for _ in range(NUM_YELLOW_OBJECTS)]

    green_objects = [GreenObject(random.randint(OBJECT_RADIUS, SCREEN_WIDTH - OBJECT_RADIUS),
                                 random.randint(OBJECT_RADIUS, SCREEN_HEIGHT - OBJECT_RADIUS),
                                 GREEN_COLOR, INITIAL_ENERGY) for _ in range(NUM_GREEN_OBJECTS)]

    all_objects = red_objects + yellow_objects + green_objects

    clock = pygame.time.Clock()
    running = True

    start_time = time.time()
    timestamp = datetime.now().strftime(TIMESTAMP_FORMAT)
    elapsed_time = 0

    save_general_statistics(timestamp, elapsed_time, [], [], [], init=True)
    save_object_statistics(timestamp, elapsed_time, [], init=True)

    last_frame_time = time.time()

    while running:
        screen.fill(BACKGROUND_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for obj in all_objects[:]:
            obj.update(all_objects)
            obj.draw(screen)

            for other in all_objects[:]:
                if obj is not other and obj.detect_collision(other):
                    if isinstance(obj, RedObject) and isinstance(other, YellowObject):
                        obj.energy += other.energy
                        all_objects.remove(other)
                    elif isinstance(obj, YellowObject) and isinstance(other, GreenObject):
                        obj.energy += other.energy
                        all_objects.remove(other)

        red_objects = [obj for obj in all_objects if isinstance(obj, RedObject)]
        yellow_objects = [obj for obj in all_objects if isinstance(obj, YellowObject)]
        green_objects = [obj for obj in all_objects if isinstance(obj, GreenObject)]

        if time.time() - start_time >= TIME_INTERVAL:
            elapsed_time += 1
            save_general_statistics(timestamp, elapsed_time, red_objects, yellow_objects, green_objects)
            save_object_statistics(timestamp, elapsed_time, all_objects)

            for red in red_objects[:]:
                if red.energy <= 0:
                    all_objects.remove(red)
                    red_objects.remove(red)
                    for _ in range(NUM_NEW_GREEN_OBJECTS):
                        new_green = GreenObject(random.randint(OBJECT_RADIUS, SCREEN_WIDTH - OBJECT_RADIUS),
                                                random.randint(OBJECT_RADIUS, SCREEN_HEIGHT - OBJECT_RADIUS),
                                                GREEN_COLOR, INITIAL_ENERGY)
                        all_objects.append(new_green)
                        green_objects.append(new_green)

            all_objects = red_objects + yellow_objects + green_objects
            start_time = time.time()

        # Проверяем, есть ли еще объекты в симуляции
        if not all_objects:
            running = False  # Завершаем симуляцию, если объектов не осталось

        current_time = time.time()
        frame_duration = current_time - last_frame_time
        last_frame_time = current_time
        fps = 1.0 / frame_duration if frame_duration > 0 else MAX_FPS

        display_general_statistics_on_screen(screen, elapsed_time, red_objects, yellow_objects, green_objects, font, fps)

        target_fps = min(max(1.0 / frame_duration, MIN_FPS), MAX_FPS)
        pygame.display.flip()
        clock.tick(target_fps)

    create_charts(timestamp)
    pygame.quit()

if __name__ == "__main__":
    main()
