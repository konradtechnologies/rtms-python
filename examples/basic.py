from konradtechnologies_rtms.rtms_client import *
from konradtechnologies_rtms.target import RadarTarget


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
