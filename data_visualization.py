import matplotlib.pyplot as plt


def plot_motion(time, distance):
    """Plot distance against time."""
    plt.plot(time, distance, marker="o")
    plt.xlabel("Time (s)")
    plt.ylabel("Distance (m)")
    plt.title("Motion: Distance vs Time")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    time = [0, 1, 2, 3, 4, 5]
    distance = [0, 2, 4, 6, 8, 10]

    plot_motion(time, distance)
