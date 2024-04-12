
#------------- Small Strain Oedometer -------------#
small_strain_oedometer_modify_cps_flags = {
    "No changes needed": None
}

# Information about the sliding blocks
small_strain_oedometer_info = {
    "num_stages" : 1,
    "modify_cps_flags" : small_strain_oedometer_modify_cps_flags
}

#------------- EndSmall Strain Oedometer -------------#

#------------- 3D Triaixal -------------#
triaxial_modify_cps_flags = {
    "No changes needed": None
}

# Information about the sliding blocks
triaxial_info = {
    "num_stages" : 1,
    "modify_cps_flags" : triaxial_modify_cps_flags
}
#------------- End 3D Triaixal -------------#

#------------- Sliding Blocks -------------#
# The flag and what information should be written under that flag
sliding_blocks_modify_cps_flags = {
    "$$NUMBER_OF_LOADSTEPS" : "71",
    "$$TIME_PER_LOADSTEP" : "0.1",
    "$$QUASISTATIC_CONVERGENCE": "0",
    "$$HOMOGENEOUS_LOCAL_DAMPING" : "1 0.01",
    "$$CONTACT_FORMULATION" : "1"
}

# Information about the sliding blocks
sliding_blocks_info = {
    "num_stages" : 2,
    "modify_cps_flags" : sliding_blocks_modify_cps_flags
}
#------------- End Sliding Blocks -------------#

#------------- Column Collapse Info -------------# 
# The flag and what information should be written under that flag
column_collapse_modify_cps_flags = {
    "$$NUMBER_OF_LOADSTEPS" : "52",
    "$$TIME_PER_LOADSTEP" : "0.05",
    "$$QUASISTATIC_CONVERGENCE": "0",
    "$$HOMOGENEOUS_LOCAL_DAMPING" : "1 0.05",
    "$$REMOVE_FIXITIES" : "1 0 0"
}

# Information about the sliding blocks
column_collapse_info = {
    "num_stages" : 2,
    "modify_cps_flags" : column_collapse_modify_cps_flags
}
#------------- End Column Collapse Info -------------# 

#------------- Shallow Fndn info -------------#
# The flag and what information should be written under that flag
shallow_fndn_modify_cps_flags = {
    "No changes needed": None
}

# Information about the sliding blocks
shallow_fndn_info = {
    "num_stages" : 1,
    "modify_cps_flags" : shallow_fndn_modify_cps_flags
}
#------------- End Shallow Fndn info -------------#
