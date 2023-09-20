from src.data_preparation import data_list, BRICS_data_list, ASEAN_data_list, EU_data_list, G7_data_list, G19_data_list, OECD_data_list, OPEC_data_list
from src.data_preparation import Least_Developed_data_list, Developing_data_list, Developed_data_list
from src.data_preparation import Africa_data_list, Europe_data_list, Eurasia_data_list, North_America_data_list, Asia_Oceania_data_list, Central_South_America_data_list, Middle_East_data_list
from src.EDAnalysis import descriptive_stats
from src.visualization import save_plots


# This takes the data list and calculates descriptive statistics with it
ALL_stats_dict = descriptive_stats(data_list)
BRICS_stats_dict = descriptive_stats(BRICS_data_list)
ASEAN_stats_dict = descriptive_stats(ASEAN_data_list)
EU_stats_dict = descriptive_stats(EU_data_list)
G7_stats_dict = descriptive_stats(G7_data_list)
G19_stats_dict = descriptive_stats(G19_data_list)
OECD_stats_dict = descriptive_stats(OECD_data_list)
OPEC_stats_dict = descriptive_stats(OPEC_data_list)
Least_Developed_dict = descriptive_stats(Least_Developed_data_list)
Developing_dict = descriptive_stats(Developing_data_list)
Developed_dict = descriptive_stats(Developed_data_list)
Africa_dict = descriptive_stats(Africa_data_list)
Europe_dict = descriptive_stats(Europe_data_list)
Eurasia_dict = descriptive_stats(Eurasia_data_list)
North_America_dict = descriptive_stats(North_America_data_list)
Asia_Oceania_dict = descriptive_stats(Asia_Oceania_data_list)
Central_South_America_dict = descriptive_stats(Central_South_America_data_list)
Middle_East_dict = descriptive_stats(Middle_East_data_list)
# This makes plots out of the descriptive statistics
# save_plots(ALL_stats_dict, 'All-Countries')
# save_plots(BRICS_stats_dict, 'BRICS')
# save_plots(ASEAN_stats_dict, 'ASEAN')
# save_plots(EU_stats_dict, 'EU')
# save_plots(G7_stats_dict, 'G7')
# save_plots(G19_stats_dict, 'G19')
# save_plots(OECD_stats_dict, 'OECD')
# save_plots(OPEC_stats_dict, 'OPEC')
# save_plots(Least_Developed_dict, 'Least-Developed')
# save_plots(Developing_dict, 'Developing')
# save_plots(Developed_dict, 'Developed')
save_plots(Africa_dict, 'Africa')
save_plots(Europe_dict, 'Europe')
save_plots(Eurasia_dict, 'Eurasia')
save_plots(North_America_dict, 'North America')
save_plots(Asia_Oceania_dict, 'Asia & Oceania')
save_plots(Central_South_America_dict, 'Central & South America')
save_plots(Middle_East_dict, 'Middle East')
