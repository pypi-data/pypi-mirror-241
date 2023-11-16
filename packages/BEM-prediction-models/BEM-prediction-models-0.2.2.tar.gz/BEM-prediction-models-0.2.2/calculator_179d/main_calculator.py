import calculator_179d.proposed_electricity_179d as pe179d
import calculator_179d.baseline_electricity_179d as be179d
import calculator_179d.proposed_naturalgas_179d as pn179d
import calculator_179d.baseline_naturalgas_179d as bn179d
import json
import numpy as np
import os
import sys

# 4 prediction models used to compute proposed electricity and naturalgas
# and baseline electricity and naturalgas
# prediction model outputs are in GJ, function converts outputs to kBTU
def calculate_model_outputs(property_info):
    gJ_to_kBTU_conversion = 947.817

    # proposed and baseline electricity 179d

    # create proposed electricity model object based on bulding type, climate zone, and system type
    proposed_electricity_179d_obj = pe179d.proposed_electricity_179d(property_info)
    # estimate annual electricity using proposed model, and user calculator inputs
    proposed_electricity_179d_value = proposed_electricity_179d_obj.estimate_annual_electricity(
        property_info
    )*gJ_to_kBTU_conversion
    # create baseline model object based on bulding type, climate zone, and system type
    baseline_electricity_179d_obj = be179d.baseline_electricity_179d(property_info)
    # estimate baseline annual electricity withe baseline model and user calculator inputs
    baseline_electricity_179d_value = baseline_electricity_179d_obj.estimate_annual_electricity(
        property_info
    )*gJ_to_kBTU_conversion

    # create proposed model object based on bulding type, climate zone, and system type
    proposed_naturalgas_179d_obj = pn179d.proposed_naturalgas_179d(property_info)
    # estimate annual electricity using proposed model, and user calculator inputs
    proposed_naturalgas_179d_value = proposed_naturalgas_179d_obj.estimate_annual_naturalgas(
        property_info
    )*gJ_to_kBTU_conversion
    # create baseline model object based on bulding type, climate zone, and system type
    baseline_naturalgas_179d_obj = bn179d.baseline_naturalgas_179d(property_info)
    # estimate baseline annual electricity withe baseline model and user calculator inputs
    baseline_naturalgas_179d_value = baseline_naturalgas_179d_obj.estimate_annual_naturalgas(
        property_info
    )*gJ_to_kBTU_conversion

    model_outputs = [
        proposed_electricity_179d_value,
        baseline_electricity_179d_value,
        proposed_naturalgas_179d_value,
        baseline_naturalgas_179d_value
    ]

    return model_outputs

def calculate_energy_and_energy_savings(model_outputs,property_info):
    # proposed electricity consumption per sqft
    proposed_electricity_per_sqft = (
        model_outputs[0]/
        property_info['gross_floor_area']
    )
    # baseline electricity consumption per sqft
    baseline_electricity_per_sqft = (
        model_outputs[1]/
        property_info['gross_floor_area']
    )

    # proposed naturalgas per sqft
    proposed_naturalgas_per_sqft = (
        model_outputs[2]/
        property_info['gross_floor_area']
    )
    # baseline naturalgas per sqft
    baseline_naturalgas_per_sqft = (
        model_outputs[3]/
        property_info['gross_floor_area']
    )

    # Calculate total energy
    #electricity +  natural gas consumption in GJ
    proposed_total_energy = model_outputs[0]+model_outputs[2]
    proposed_total_energy_per_sqft = (
        proposed_total_energy/
        property_info['gross_floor_area']
    )
    baseline_total_energy = model_outputs[1]+model_outputs[3]
    baseline_total_energy_per_sqft = (
        baseline_total_energy/
        property_info['gross_floor_area']
    )

    # Calculate energy savings
    electricity_savings = model_outputs[2] - model_outputs[0]
    if electricity_savings<0:
        electricity_savings=0
    electricity_savings_per_sqft = (
        electricity_savings/
        property_info['gross_floor_area']
    )
    naturalgas_savings = model_outputs[3]-model_outputs[1]
    if naturalgas_savings<0:
        naturalgas_savings = 0
    naturalgas_savings_per_sqft = (
        naturalgas_savings/
        property_info['gross_floor_area']
    )
    total_energy_savings = baseline_total_energy - proposed_total_energy
    if total_energy_savings<0:
        total_energy_savings = 0
    total_energy_savings_per_sqft = (
        total_energy_savings/
        property_info['gross_floor_area']
    )

    return {
        'proposed_electricity_per_sqft':proposed_electricity_per_sqft,
        'baseline_electricity_per_sqft':baseline_electricity_per_sqft,
        'proposed_naturalgas_per_sqft':proposed_naturalgas_per_sqft,
        'baseline_naturalgas_per_sqft':baseline_naturalgas_per_sqft,
        'proposed_total_energy':proposed_total_energy,
        'proposed_total_energy_per_sqft':proposed_total_energy_per_sqft,
        'baseline_total_energy':baseline_total_energy,
        'baseline_total_energy_per_sqft':baseline_total_energy_per_sqft,
        'electricity_savings':electricity_savings,
        'electricity_savings_per_sqft':electricity_savings_per_sqft,
        'naturalgas_savings':naturalgas_savings,
        'naturalgas_savings_per_sqft':naturalgas_savings_per_sqft,
        'total_energy_savings':total_energy_savings,
        'total_energy_savings_per_sqft':total_energy_savings_per_sqft
    }

def calculate_cost_and_cost_savings(model_outputs,property_info):
    kBTU_to_kWh = 0.293014
    kBTU_to_thousand_cuft = 1./1039
    cents_to_dollar = 1./100

    # calculate costs
    # baseline costs
    baseline_179d_electricity_cost = (
        property_info['electricity_rate']*cents_to_dollar*
        model_outputs[1]*kBTU_to_kWh
    )
    baseline_179d_electricity_cost_per_sqft = (
        baseline_179d_electricity_cost/
        property_info['gross_floor_area']
    )
    baseline_179d_naturalgas_cost=(
        property_info['naturalgas_rate']*
        model_outputs[3]*kBTU_to_thousand_cuft
    )
    baseline_179d_naturalgas_cost_per_sqft = (
        baseline_179d_naturalgas_cost/
        property_info['gross_floor_area']
    )
    baseline_179d_totalcost = (
        baseline_179d_electricity_cost+
        baseline_179d_naturalgas_cost
    )
    baseline_179d_totalcost_per_sqft = (
        baseline_179d_totalcost/
        property_info['gross_floor_area']
    )

    # proposed costs
    proposed_179d_electricity_cost = (
        property_info['electricity_rate']*cents_to_dollar*
        model_outputs[0]*kBTU_to_kWh
    )
    proposed_179d_electricity_cost_per_sqft = (
        proposed_179d_electricity_cost/
        property_info['gross_floor_area']
    )
    proposed_179d_naturalgas_cost = (
        property_info['naturalgas_rate']*
        model_outputs[2]*kBTU_to_thousand_cuft
    )
    proposed_179d_naturalgas_cost_per_sqft = (
        proposed_179d_naturalgas_cost/
        property_info['gross_floor_area']
    )
    proposed_179d_totalcost = (
        proposed_179d_electricity_cost+
        proposed_179d_naturalgas_cost
    )
    proposed_179d_totalcost_per_sqft = (
        proposed_179d_totalcost/
        property_info['gross_floor_area']
    )

    # calculate cost savings
    electricity_cost_savings = (
        baseline_179d_electricity_cost-
        proposed_179d_electricity_cost
    )
    if electricity_cost_savings<0:
        electricity_cost_savings=0
    electricity_cost_savings_per_sqft = (
        electricity_cost_savings/
        property_info['gross_floor_area']
    )
    naturalgas_cost_savings = (
        baseline_179d_naturalgas_cost-
        proposed_179d_naturalgas_cost
    )
    if naturalgas_cost_savings<0:
        naturalgas_cost_savings=0
    naturalgas_cost_savings_per_sqft = (
        naturalgas_cost_savings/
        property_info['gross_floor_area']
    )
    total_cost_savings = (
        baseline_179d_totalcost-
        proposed_179d_totalcost
    )
    if total_cost_savings<0:
        total_cost_savings=0
    total_cost_savings_per_sqft = (
        total_cost_savings/
        property_info['gross_floor_area']
    )

    # Cost savings percentage
    Percent_Savings=round(
        (
            (baseline_179d_totalcost-proposed_179d_totalcost)/
            baseline_179d_totalcost
        )*100
    )
    if Percent_Savings<0:
        Percent_Savings=0
    Percent_Savings_Electricity=(
        round(
            ((baseline_179d_electricity_cost-
              proposed_179d_electricity_cost)/
            baseline_179d_electricity_cost)*100
        )
    )
    if Percent_Savings_Electricity<0:
        Percent_Savings_Electricity=0
    Percent_Savings_Naturalgas=(
        round(
            ((baseline_179d_naturalgas_cost-
              proposed_179d_naturalgas_cost)/
            baseline_179d_naturalgas_cost)*100
        )
    )
    if Percent_Savings_Naturalgas<0:
        Percent_Savings_Naturalgas=0
    Percent_Savings_per_sqft = (
        Percent_Savings/
        property_info['gross_floor_area']
    )

    return {
        'proposed_179d_electricity_cost':proposed_179d_electricity_cost,
        'baseline_179d_electricity_cost':baseline_179d_electricity_cost,
        'proposed_179d_electricity_cost_per_sqft':proposed_179d_electricity_cost_per_sqft,
        'baseline_179d_electricity_cost_per_sqft':baseline_179d_electricity_cost_per_sqft,
        'proposed_179d_naturalgas_cost':proposed_179d_naturalgas_cost,
        'proposed_179d_naturalgas_cost_per_sqft':proposed_179d_naturalgas_cost_per_sqft,
        'proposed_179d_totalcost':proposed_179d_totalcost,
        'proposed_179d_totalcost_per_sqft':proposed_179d_totalcost_per_sqft,
        'baseline_179d_totalcost':baseline_179d_totalcost,
        'baseline_179d_totalcost_per_sqft':baseline_179d_totalcost_per_sqft,
        'electricity_cost_savings':electricity_cost_savings,
        'electricity_cost_savings_per_sqft':electricity_cost_savings_per_sqft,
        'naturalgas_cost_savings':naturalgas_cost_savings,
        'naturalgas_cost_savings_per_sqft':naturalgas_cost_savings_per_sqft,
        'total_cost_savings':total_cost_savings,
        'total_cost_savings_per_sqft':total_cost_savings_per_sqft,
        'percent_savings_electricity':Percent_Savings_Electricity,
        'percent_savings_naturalgas':Percent_Savings_Naturalgas,
        'percent_savings':Percent_Savings,
        'percent_savings_total_per_sqft':Percent_Savings_per_sqft
    }


def calculate_savings(property_info):
    # calculate model outputs
    model_outputs = calculate_model_outputs(property_info)

    # output dictionary
    dict_outputs = {
        'proposed_179d_electricity':model_outputs[0],
        'baseline_179d_electricity':model_outputs[1],
        'proposed_179d_naturalgas':model_outputs[2],
        'baseline179d_natualgas':model_outputs[3]
    }

    # calculate energy and energy savings
    dict_outputs.update(calculate_energy_and_energy_savings(
        model_outputs,
        property_info
    )
    )

    # calculate cost and cost savings
    dict_outputs.update(
        calculate_cost_and_cost_savings(
            model_outputs,
            property_info
        )
    )

    BinSavings=np.arange(property_info['min_threshold_energy']*100,51, 1).tolist()
    # print(BinSavings)
    # print(dict_outputs['percent_savings'])

    RateList_energy=np.arange(
        property_info['energy_tax_deduction_rate_min'],
        property_info['energy_tax_deduction_rate_max']+property_info['increment_energy'],
        property_info['increment_energy']
    ).tolist()
    RateList_all=np.arange(
        property_info['all_179d_tax_deduction_rate_min'],
        property_info['all_179d_tax_deduction_rate_max'] + property_info['increment_all_179d'],
        property_info['increment_all_179d']
    ).tolist()

    if dict_outputs['percent_savings']>=property_info['min_threshold_energy']*100:
        Tax_deduction_Rate=RateList_energy[
            np.digitize(dict_outputs['percent_savings'],BinSavings)-1
        ]  # $/sqft
        dict_outputs['tax_deduction_rate_energy'] = Tax_deduction_Rate

    else:
        Tax_deduction_Rate=0
        dict_outputs['tax_deduction_rate_energy'] = Tax_deduction_Rate
        print("Minimum savings requirement not met and not qualified for 179D tax deduction")
    if dict_outputs['percent_savings']>=property_info['min_threshold_all_179d']*100:
        Tax_deduction_Rate_all=RateList_all[
            np.digitize(dict_outputs['percent_savings'],BinSavings)-1
        ]  # $/sqft

        dict_outputs['tax_deduction_rate_all'] = Tax_deduction_Rate_all
    else:
        dict_outputs['tax_deduction_rate_all'] = 0


    return dict_outputs





#if __name__ == "__main__":
#    json_file = sys.argv[1:][0]
#    #load json file given as argument in command line
#    with open(json_file) as f:
#        property_info = json.load(f)
#        #compute outputs and save in calculator_outputs.json
#        output = calculate_savings(property_info)
#        with open(r'./output_files/calculator_outputs.json', 'w') as fp:
#            json.dump(output, fp)



if __name__ == "__main__":
    json_file = sys.argv[1:][0]
    # load json file given as argument in command line
    f = open(json_file)
    calculator_user_inputs = json.load(f)
    # compute outputs and save in calculator_outputs.json
    calculate_savings(calculator_user_inputs)