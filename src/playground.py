# I use this file to run random commands that help me understand the data I'm working with

from data_preparation import data_df, filter_dataframes_by_conglomerate, conglomerate_names, conglomerate_list, data_names, data_list

filtered_data = filter_dataframes_by_conglomerate(
    conglomerate_names, conglomerate_list, data_names, data_list)

print(filtered_data['BRICS']['imports'])
