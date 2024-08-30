# Размеры экрана
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900

# Радиус объектов
OBJECT_RADIUS = 5
GREEN_OBJECT_RADIUS = 3

# Начальная энергия объектов
INITIAL_ENERGY = 100

# Потеря энергии
RED_ENERGY_LOSS = 0.1
GREEN_ENERGY_LOSS = 0.05
YELLOW_ENERGY_LOSS = 0.1

# Энергия для размножения
RED_REPRODUCE_ENERGY = 200
YELLOW_REPRODUCE_ENERGY = 200

# Количество потомков при размножении
YELLOW_REPRODUCE_COUNT = 2
RED_REPRODUCE_COUNT = 2

# Радиус видимости
RED_VISION_RADIUS = 150
YELLOW_VISION_RADIUS = 75

# Скорость объектов
BASE_SPEED = 0.7
SPEED_FACTOR = 25

# Интервал и энергия вознаграждения для желтых объектов
YELLOW_REWARD_INTERVAL = 100
YELLOW_REWARD_ENERGY = 0.1

# Цвета объектов
RED_COLOR = (255, 0, 0)
YELLOW_COLOR = (239, 243, 150)
GREEN_COLOR = (0, 255, 0)
BACKGROUND_COLOR = (0, 0, 0)

# Количество объектов каждого типа
NUM_RED_OBJECTS = 20
NUM_YELLOW_OBJECTS = 20
NUM_GREEN_OBJECTS = 30
NUM_NEW_GREEN_OBJECTS = 3

# Параметры окна
WINDOW_CAPTION = "Object Simulation"
FONT_NAME = None
FONT_SIZE = 24

# Параметры времени
TIMESTAMP_FORMAT = "%Y%m%d_%H%M%S"
TIME_INTERVAL = 1  # Интервал времени в секундах для сохранения статистики

# Минимальное и максимальное значение FPS
MIN_FPS = 30  # Минимальное значение FPS
MAX_FPS = 60  # Максимальное значение FPS
