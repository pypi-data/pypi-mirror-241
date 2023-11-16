# BEM Prediction Models

## Setup Instructions

Run `pip install -r requirements.txt` to install python packages.

Developed using Python version 3.9.7.

## Using this code as a library
After running the setup instructions, import the package into your code and call the
`calculate_savings(property_info)` function to calculate the savings for that property.

#### Parameters
`property_info` - a dictionary with the following required entries:
```
	building_type
	climate_zone
	hvac_system
	gross_floor_area
	number_of_floors
	aspect_ratio
	window_wall_ratio
	roof_thermal_perf_type
	wall_thermal_perf_type
	window_u_factor
	window_shgc
	proposed_lpd
	water_heating_energy_factor
	air_system_fan_total_efficiency
	boiler_average_efficiency
	dx_cooling_cop
	zone_hvac_fan_total_efficiency
	dx_heating_cop
	gas_coil_average_efficiency
	chiller_average_cop
	electricity_rate 
	naturalgas_rate
	energy_tax_deduction_rate_min
	energy_tax_deduction_rate_max
	all_179d_tax_deduction_rate_min
	all_179d_tax_deduction_rate_max
	increment_energy
	min_threshold_energy
	increment_all_179d
	min_threshold_all_179d

```

#### Driver program
The following is a test program you can use to check if you have correctly installed the library

```
from calculator_179d.main_calculator import calculate_savings

inputs = {
	"building_type": "small office",
	"climate_zone": "4A",
	"hvac_system":"PSZ-AC with gas coil",
	"gross_floor_area": 9160.804020,
	"number_of_floors": 3,
	"aspect_ratio": 2.130650,
	"window_wall_ratio":0.762412,
	"roof_thermal_perf_type": 0.238102,
	"wall_thermal_perf_type": 0.433408,
	"window_u_factor": 5.065000,
	"window_shgc": 0.568000,
	"proposed_lpd": 9.322412,
	"water_heating_energy_factor": 0.82,
	"air_system_fan_total_efficiency": 0.95,
	"boiler_average_efficiency": 0,
	"dx_cooling_cop": 3.276834,
	"zone_hvac_fan_total_efficiency": 0,
	"dx_heating_cop": 0,
	"gas_coil_average_efficiency": 0.866030,
	"chiller_average_cop": 0,
	"electricity_rate": 0.1059, 
	"naturalgas_rate": 10.4950,
	"energy_tax_deduction_rate_min":0.5,
	"energy_tax_deduction_rate_max":1,
	"all_179d_tax_deduction_rate_min":2.5,
	"all_179d_tax_deduction_rate_max":5,
	"increment_energy":0.02,
	"min_threshold_energy":0.25,
	"increment_all_179d":0.1,
	"min_threshold_all_179d":0.25
}

print("These are the savings:")
print(calculate_savings(inputs))
```


## Running the package as a standalone application
You may run this package as a standalone application instead of importing it as a library. To do so,
simply update the parameters in `calculator_179d/calculator_user_inputs.json` and execute the code using the
following command:

```
    cd calculator_179d/
    python3 main_calculator.py calculator_user_inputs.json
```

This will create an file at `calculator_179d/output_files/calculator_outputs.json` with the results from the models.

## Package Releasing and Publishing

1. Update package version in setup.py
1. Merge everything to develop and then make a single merge from develop to main
1. Make a release on GitHub (pointing to the main branch). List the updates that were made.
1. Make the package: `python setup.py sdist`
1. Install twine (if needed):  `pip install twine`
1. Upload to pypi: `twine upload dist/<name of package you just made>`

