import os
import matplotlib.pyplot as plt


# Plotting function

def save_plots(stats_dict, folder):
    # Parent directory
    parent_dir = os.path.join('Summary-Data', folder)

    # First, create the parent folder if it doesn't exist
    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir)

    for name, stats in stats_dict.items():
        # Create a folder for each feature within the Summary-Data/All-Countries folder
        folder_path = os.path.join(parent_dir, name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        for statistic, values in stats.items():
            plt.figure(figsize=(10, 6))
            plt.plot(values)
            plt.title(f'{name} - {statistic}')
            plt.xlabel('Year')
            plt.ylabel(statistic.capitalize())
            plt.xticks(ticks=values.index[::5])
            plt.tight_layout()

            # Save the figure to the respective folder
            plt.savefig(os.path.join(folder_path, f'{statistic}.png'))
            plt.close()
