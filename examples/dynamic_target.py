from konradtechnologies_rtms.rtms_client import *
from konradtechnologies_rtms.target import RadarTarget, DynamicRadarTarget


def dynamic_target_example(ip_address):
    # Create RTMS object
    rtms_client = RtmsClient(ip_address)

    # Connect to RTMS
    rtms_client.connect()

    # Create two dynamic targets
    # The first target will move out from 20m to 80m, then back 40m
    moving_target_1 = [DynamicRadarTarget(start_x=0, start_y=20, end_x=0, end_y=80, rcs=30, velocity=10),
                       DynamicRadarTarget(start_x=0, start_y=80, end_x=0, end_y=40, rcs=30, velocity=20)]

    # The second target will move from 100m to 120m.
    moving_target_2 = [DynamicRadarTarget(start_x=0, start_y=100, end_x=0, end_y=120, rcs=30, velocity=5)]

    # Send the targets to RTMS
    rtms_client.set_dynamic_range_targets([moving_target_1, moving_target_2])

    # Disconnect
    rtms_client.disconnect()


def main():
    """Uncomment the example you'd like to run. For each example,
    replace the IP address with one that is appropriate for your
    connection to RTMS."""
    ip_address = "127.0.0.1"

    dynamic_target_example(ip_address)


if __name__ == "__main__":
    main()
