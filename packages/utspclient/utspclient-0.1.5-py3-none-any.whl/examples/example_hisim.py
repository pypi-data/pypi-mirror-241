"""Requests a file containing KPIs generated from HiSim"""

import json
import os
import time

from utspclient.client import request_time_series_and_wait_for_delivery
from utspclient.datastructures import TimeSeriesRequest


def main():
    # load a HiSim system configuration
    example_folder = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(example_folder, "input data\\hisim_config.json")
    with open(config_path, "r") as config_file:
        hisim_config = config_file.read()

    hisim_config = {
        "path_to_module": "system_setups/household_1_advanced_hp_diesel_car.py",
        "simulation_parameters": {
            "start_date": "2021-01-01T00:00:00",
            "end_date": "2021-01-02T00:00:00",
            "seconds_per_timestep": 900,
            "post_processing_options": [13, 19, 20, 22],
        },
        "building_config": {
            "name": "Building",
            "building_code": "DE.N.SFH.05.Gen.ReEx.001.002",
            "building_heat_capacity_class": "medium",
            "initial_internal_temperature_in_celsius": 23,
            "heating_reference_temperature_in_celsius": -14,
            "absolute_conditioned_floor_area_in_m2": 121.2,
            "total_base_area_in_m2": None,
            "number_of_apartments": 1,
            "predictive": False,
        },
    }
    hisim_config = json.dumps(hisim_config)

    # Define URL to time Series request
    URL = "http://134.94.131.167:443/api/v1/profilerequest"
    URL = "http://localhost:443/api/v1/profilerequest"
    API_KEY = "OrjpZY93BcNWw8lKaMp0BEchbCc"

    # Save start time for run time calculation
    start_time = time.time()

    # Call time series request function
    result_file_name = "kpi_config.json"
    request = TimeSeriesRequest(
        hisim_config,
        "hisim",
        guid="1",
        # required_result_files=dict.fromkeys([result_file_name]),
    )
    result = request_time_series_and_wait_for_delivery(URL, request, API_KEY)

    kpi = result.data[result_file_name].decode()

    print("Calculation took %s seconds" % (time.time() - start_time))
    # Print all results from the request
    print("Example HiSim request")
    print(f"Retrieved data: {kpi}")


if __name__ == "__main__":
    main()
