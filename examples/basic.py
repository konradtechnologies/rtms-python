from konradtechnologies_rtms.rtms_client import *
from konradtechnologies_rtms.target import RadarTarget
from konradtechnologies_rtms.enum_types import *


def basic_example(ip_address):
    # Create RTMS object
    rtms_client = RtmsClient(ip_address)

    # Connect to RTMS
    rtms_client.connect()

    # Get and print the RTMS version
    print(rtms_client.get_rtms_version())

    # Disconnect
    rtms_client.disconnect()


def target_example(ip_address):
    # Create RTMS object
    rtms_client = RtmsClient(ip_address)

    # Connect to RTMS
    rtms_client.connect()

    # Create two radar targets
    target_list = [RadarTarget(distance=35, rcs=15, velocity=0, azimuth=0, elevation=0),
                   RadarTarget(distance=100, rcs=30, velocity=0, azimuth=0, elevation=0)]

    # Send the targets to RTMS
    rtms_client.set_radar_targets(target_list)

    # Get actual target list from RTMS and print them out
    simulated_targets = rtms_client.get_radar_targets()
    for target in simulated_targets:
        print(target)
        print("\n")

    # Disconnect
    rtms_client.disconnect()


def measurement_example_basic(ip_address):
    # Create RTMS object
    rtms_client = RtmsClient(ip_address)

    # Connect to RTMS
    rtms_client.connect()

    # Set an acquisition time of 1 msec
    rtms_client.set_measurement_duration(1E-3)
    # Set up a rising edge trigger at 20 dBm
    rtms_client.configure_trigger(enabled=True, level=20, edge=RtmsTriggerEdge.RISING)
    # Set the EIRP measurement active
    rtms_client.set_active_measurements(eirp=True)
    # Initiate the measurement and block until complete and results are ready
    rtms_client.initiate_measurement(wait_until_complete=True)

    # Fetch results
    eirp_results = rtms_client.get_measurement_results_eirp()
    print("Avg EIRP: {} dBm".format(eirp_results['avg']))

    # Disconnect
    rtms_client.disconnect()


def measurement_example_advanced(ip_address):
    # Create RTMS object
    rtms_client = RtmsClient(ip_address)

    # Connect to RTMS
    rtms_client.connect()

    # Get the system status
    print(rtms_client.get_system_status())

    # Set an acquisition time of 1 msec
    rtms_client.set_measurement_duration(1E-3)
    # Set up a rising edge trigger at 20 dBm
    rtms_client.configure_trigger(enabled=True, level=20, edge=RtmsTriggerEdge.RISING)
    # Configure the OBW and phase noise measurements
    rtms_client.configure_measurement_obw_percent(percent=99)
    rtms_client.configure_measurement_phasenoise(offset_frequencies=[10E3, 100E3, 1E6, 10E6])
    # Set all measurements active
    rtms_client.set_active_measurements(eirp=True, obw=True, linearity=True, phasenoise=True)
    # Initiate the measurement and block until complete and results are ready
    rtms_client.initiate_measurement(wait_until_complete=True)

    # Fetch results
    eirp_results = rtms_client.get_measurement_results_eirp()
    print(eirp_results)
    obw_results = rtms_client.get_measurement_results_obw()
    print(obw_results)
    linearity_results = rtms_client.get_measurement_results_linearity()
    print(linearity_results)
    phasenoise_results = rtms_client.get_measurement_results_phasenoise()
    print(phasenoise_results)

    # Disconnect
    rtms_client.disconnect()


def main():
    """Uncomment the example you'd like to run. For each example,
    replace the IP address with one that is appropriate for your
    connection to RTMS."""
    ip_address = "127.0.0.1"

    basic_example(ip_address)
    # target_example(ip_address)
    # measurement_example_basic(ip_address)
    # measurement_example_advanced(ip_address)


if __name__ == "__main__":
    main()
