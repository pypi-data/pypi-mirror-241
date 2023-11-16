import numpy as np

def calculate_ext_wall_surface_area(calculator_user_inputs):

    floor_to_floor_height= 10*0.3048 # floor height in m
    #floor area in m^2
    AF = 0.092903*(
        calculator_user_inputs['gross_floor_area']/
        calculator_user_inputs['number_of_floors']
    )
    #gross ext wall surface area in m^2
    ext_wall_surface_area_gross= (
        2*floor_to_floor_height*(
            np.sqrt(
                calculator_user_inputs['aspect_ratio']*AF
            )+
            np.sqrt(
                AF/calculator_user_inputs['aspect_ratio']
            )
        )
    )*calculator_user_inputs['number_of_floors']
    #opaque ext wall surface area in m^2
    ext_wall_surface_area = (
        (1-calculator_user_inputs['window_wall_ratio'])*
        ext_wall_surface_area_gross
    )

    return ext_wall_surface_area

def calculate_window_area(calculator_user_inputs):

    #opaque ext wall surface area
    ext_wall_surface_area = calculate_ext_wall_surface_area(calculator_user_inputs)
    #gross ext wall surface area 
    ext_wall_surface_area_gross = (
        ext_wall_surface_area/
        (1-calculator_user_inputs['window_wall_ratio'])
    )
    window_area = (
        calculator_user_inputs['window_wall_ratio']*
        ext_wall_surface_area_gross
    )

    return window_area


def calculate_roof_area(calculator_user_inputs):

    #gross floor area is in ft^2
    gross_floor_area = calculator_user_inputs['gross_floor_area']
    n_stories = calculator_user_inputs['number_of_floors']
    #roof area in m^2
    roof_area = 0.092903*(gross_floor_area/n_stories)

    return roof_area


def calculate_ACH_infiltration(calculator_user_inputs):

    bldg_type = calculator_user_inputs['building_type']
    if bldg_type == 'small office':
        AF = 0.092903*(
            calculator_user_inputs['gross_floor_area']/
            calculator_user_inputs['number_of_floors']
        )

        I = 0.012 #cmm/sm
        ACH_infiltration = (
            (I*120*(
                np.sqrt(calculator_user_inputs['aspect_ratio']*AF)+
                np.sqrt(AF/calculator_user_inputs['aspect_ratio'])
                )
            )/(
                AF*calculator_user_inputs['number_of_floors']
            )
        )*calculator_user_inputs['number_of_floors']

    return ACH_infiltration


def calculate_ua_bldg(calculator_user_inputs):

    # calculate external wall surface area
    ext_wall_surface_area = calculate_ext_wall_surface_area(calculator_user_inputs)
    #calculate roof area
    roof_area = calculate_roof_area(calculator_user_inputs)
    # calculate window area
    window_area = calculate_window_area(calculator_user_inputs)

    #calculate ua_bldg
    ua_bldg = (
        roof_area*calculator_user_inputs['roof_thermal_perf_type'] +
        ext_wall_surface_area*calculator_user_inputs['wall_thermal_perf_type'] +
        window_area*calculator_user_inputs['window_u_factor']
    )

    return ua_bldg


def calculate_sa_to_vol_ratio(calculator_user_inputs):

    # calculate roof area
    roof_area = calculate_roof_area(calculator_user_inputs)
    #calculate surface to volume ratio
    sa_to_vol_ratio = (
        2. * ((
            calculator_user_inputs['aspect_ratio']/roof_area
            ) ** 0.5 + 
            (1./(calculator_user_inputs['aspect_ratio']*roof_area)
            ) **0.5) +
        (1./(10.*calculator_user_inputs["number_of_floors"]))
    )

    return sa_to_vol_ratio