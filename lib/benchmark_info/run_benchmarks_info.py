from lib.benchmark_info.tutorial_model_info import small_strain_oedometer_info, shallow_fndn_info, triaxial_info, sliding_blocks_info, \
                                                   column_collapse_info, shallow_fndn_info

# from lib.benchmark_info.benchmark_model_info.shallow_fndn_info import shallow_fndn_info
# from lib.benchmark_info.benchmark_model_info.column_collapse_info import column_collapse_info
# from lib.benchmark_info.benchmark_model_info.small_strain_oedometer import small_strain_oedometer_info
#  from lib.benchmark_info.benchmark_model_info.small_strain_oedometer import triaxial_model_info
# Store information about the benchmarks so that they can run

benchmark_info_dict = {
    "small_strain_oedometer": small_strain_oedometer_info,
    "shallow_fndn"   : shallow_fndn_info,
    "triaxial_model": triaxial_info,
    "column_collapse": column_collapse_info, 
    "sliding_blocks" : sliding_blocks_info,
}



# Information that needs to be stored here
    # Number of stages
    # Which MPs should be outputted


