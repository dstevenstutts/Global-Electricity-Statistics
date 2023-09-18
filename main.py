from src.data_preparation import data_list
from src.EDAnalysis import descriptive_stats
from src.visualization import save_plots


# This takes the data list and calculates descriptive statistics with it
stats_dict = descriptive_stats(data_list)

# This makes plots out of the descriptive statistics
save_plots(stats_dict)
