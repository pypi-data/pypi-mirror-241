"""Requests a load profile that is generated using the Load Profile Generator (LPG)"""
# %% imports
import sys
import time
from utspclient.datastructures import TimeSeriesRequest
from utspclient.helpers import lpg_helper
import utspclient.client as utsp_client
from utspclient import result_file_filters
from utspclient.helpers.lpgdata import LoadTypes, Households, HouseTypes
from utspclient.helpers.lpgpythonbindings import CalcOption


def main():
    # %% Create a simulation configuration for the LPG
    simulation_config = lpg_helper.create_basic_lpg_config(
        Households.CHR03_Family_1_child_both_at_work,
        HouseTypes.HT06_Normal_house_with_15_000_kWh_Heating_Continuous_Flow_Gas_Heating,
        "2020-01-01",
        "2020-02-01",
        "00:01:00",
        calc_options=[
            CalcOption.HouseholdSumProfilesFromDetailedDats,
            CalcOption.HouseholdSumProfilesCsvNoFlex,
            CalcOption.BodilyActivityStatistics,
            CalcOption.TansportationDeviceJsons,
            CalcOption.FlexibilityEvents,
        ],
    )

    simulation_config_json = simulation_config.to_json(indent=4)  # type: ignore

    # %% Define connection parameters
    address = "134.94.131.109:5000"
    # address = "134.94.131.167:443"
    address = "localhost:443"
    REQUEST_URL = f"http://{address}/api/v1/profilerequest"
    API_KEY = "OrjpZY93BcNWw8lKaMp0BEchbCc"
    print(f"Server: {address}")

    # %% Prepare the time series request
    result_file = result_file_filters.LPGFilters.sum_hh1(LoadTypes.Electricity)
    request = TimeSeriesRequest(
        simulation_config_json,
        "LPG",
        guid="bugtest009",
        # required_result_files=dict.fromkeys([result_file]),
    )

    start_time = time.time()
    # %% Request the time series
    result = utsp_client.request_time_series_and_wait_for_delivery(
        REQUEST_URL, request, api_key=API_KEY
    )
    print("Calculation took %s seconds" % (time.time() - start_time))

    size = sum(sys.getsizeof(x) for x in result.data.values())
    print(f"Total result size: {round(size/1024**2, 2)} MB")

    # %% Decode result data
    file_content = result.data[result_file].decode()
    print(f"Results: {file_content[:10]}")


if __name__ == "__main__":
    main()
