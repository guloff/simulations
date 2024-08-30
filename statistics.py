import csv
import matplotlib.pyplot as plt
from sim_object import RedObject, YellowObject, GreenObject
from config import RED_COLOR, YELLOW_COLOR, GREEN_COLOR

def display_general_statistics_on_screen(screen, elapsed_time, red_objects, yellow_objects, green_objects, font, fps):
    num_red = len(red_objects)
    num_yellow = len(yellow_objects)
    num_green = len(green_objects)
    total_energy_red = sum(obj.energy for obj in red_objects)
    total_energy_yellow = sum(obj.energy for obj in yellow_objects)
    total_energy_green = sum(obj.energy for obj in green_objects)

    stats_texts = [
        f"Time: {elapsed_time} s",
        f"FPS: {fps:.2f}",
        f"Rs: {num_red}",
        f"Ys: {num_yellow}",
        f"Gs: {num_green}",
        f"Rs' E: {total_energy_red:.2f}",
        f"Ys' E: {total_energy_yellow:.2f}",
        f"Gs' E: {total_energy_green:.2f}"
    ]

    y_offset = 10
    for text in stats_texts:
        text_surface = font.render(text, True, (255, 255, 255))
        screen.blit(text_surface, (10, y_offset))
        y_offset += 20

def save_object_statistics(timestamp, elapsed_time, all_objects, init=False):
    filename = f"stat/stat_{timestamp}.csv"

    if init:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Time", "Object_ID", "Color", "Energy", "Speed"])
        return

    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for obj in all_objects:
            writer.writerow([elapsed_time, id(obj), 'Red' if isinstance(obj, RedObject) else 'Yellow' if isinstance(obj, YellowObject) else 'Green', obj.energy, obj.speed])

def save_general_statistics(timestamp, elapsed_time, red_objects, yellow_objects, green_objects, init=False):
    filename = f"stat/stat_general_{timestamp}.csv"

    if init:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Time", "Red Objects", "Yellow Objects", "Green Objects", "Total Energy (Red)", "Total Energy (Yellow)", "Total Energy (Green)"])
        return

    num_red = len(red_objects)
    num_yellow = len(yellow_objects)
    num_green = len(green_objects)
    total_energy_red = sum(obj.energy for obj in red_objects)
    total_energy_yellow = sum(obj.energy for obj in yellow_objects)
    total_energy_green = sum(obj.energy for obj in green_objects)

    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([elapsed_time, num_red, num_yellow, num_green, total_energy_red, total_energy_yellow, total_energy_green])

def create_charts(timestamp):
    general_stats_file = f"stat/stat_general_{timestamp}.csv"
    object_stats_file = f"stat/stat_{timestamp}.csv"

    red_color = [c/255 for c in RED_COLOR]
    yellow_color = [c/255 for c in YELLOW_COLOR]
    green_color = [c/255 for c in GREEN_COLOR]

    times = []
    num_reds = []
    num_yellows = []
    num_greens = []
    with open(general_stats_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            times.append(int(row["Time"]))
            num_reds.append(int(row["Red Objects"]))
            num_yellows.append(int(row["Yellow Objects"]))
            num_greens.append(int(row["Green Objects"]))

    red_energies = []
    yellow_energies = []
    green_energies = []
    with open(object_stats_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["Color"] == "Red":
                red_energies.append(float(row["Energy"]))
            elif row["Color"] == "Yellow":
                yellow_energies.append(float(row["Energy"]))
            elif row["Color"] == "Green":
                green_energies.append(float(row["Energy"]))

    plt.figure(figsize=(10, 6))
    plt.plot(times, num_reds, label='Reds', color=red_color)
    plt.plot(times, num_yellows, label='Yellows', color=yellow_color)
    plt.plot(times, num_greens, label='Greens', color=green_color)
    plt.xlabel('Time')
    plt.ylabel('Number of Objects')
    plt.title('Number of Objects Over Time')
    plt.legend()
    plt.savefig(f"stat/num_objects_{timestamp}.png")
    plt.close()

    plt.figure(figsize=(10, 6))
    plt.hist(red_energies, bins=20, alpha=0.5, label='Reds', color=red_color)
    plt.hist(yellow_energies, bins=20, alpha=0.5, label='Yellows', color=yellow_color)
    plt.hist(green_energies, bins=20, alpha=0.5, label='Greens', color=green_color)
    plt.xlabel('Energy')
    plt.ylabel('Frequency')
    plt.title('Energy Distribution of Objects')
    plt.legend()
    plt.savefig(f"stat/energy_distribution_{timestamp}.png")
    plt.close()
