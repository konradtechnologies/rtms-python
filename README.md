# rtms-python
Python communication library for the KT-RTMS software.  You must have the KT-RTMS installed on a system with the 
Remote Control plug-in activated.  Please contact Konrad Technologies for assistance.

## Installing rtms-python
rtms-python can be installed using pip:

`pip install konradtechnologies-rtms-python`

## Examples
Example Python scripts can be found in the examples/ folder.

## Using rtms-python
The rtms-python package provides an overall class for communication to KT-RTMS, `RtmsClient`

    # Instantiate the RTMS client object (does not connect yet)
    rtms_client = RtmsClient(ip_address)

    # Connect to the instrument
    rtms_client.connect()
    ...
    # Perform functions
    ...
    # Disconnect from the instrument
    rtms_client.disconnect()

### Creating Radar Targets
Radar targets can be defined using the `RadarTarget` class and sent to the instrument

    # Create two radar targets
    target_list = [RadarTarget(distance=35, rcs=15, velocity=0, azimuth=0, elevation=0),
                   RadarTarget(distance=100, rcs=30, velocity=0, azimuth=0, elevation=0)]

    # Send the targets to RTMS
    rtms_client.set_radar_targets(target_list)

### Taking RF Measurements
If the KT-RTMS RF Measurements plug-in is activated on the system, one can take RF measurements.  This is typically
done in three steps: measurement configuration, initiating the measurement, and fetching results.

To configure the instrument for an RF measurement, there are typically a few parameters one should set:
* Measurement duration
* RF trigger parametesr
* Specific measurement parameters
* Enabling which specific measurements to take

As an example, this code sets the instrument up for a 1 msec acquisiton, measuring EIRP, occupied bandwidth, linearity,
and phase noise of the signal:

    # Set an acquisition time of 1 msec
    rtms_client.set_measurement_duration(1E-3)

    # Set up a rising edge trigger at 20 dBm
    rtms_client.configure_trigger(enabled=True, level=20, edge=RtmsTriggerEdge.RISING)

    # Configure the OBW and phase noise measurements
    rtms_client.configure_measurement_obw_percent(percent=99)
    rtms_client.configure_measurement_phasenoise(offset_frequencies=[10E3, 100E3, 1E6, 10E6])

    # Set all measurements active
    rtms_client.set_active_measurements(eirp=True, obw=True, linearity=True, phasenoise=True)

Then, once all the measurement configuration has been defined, one can initiate the measurement:

    # Initiate the measurement and block until complete and results are ready
    rtms_client.initiate_measurement(wait_until_complete=True)

Finally, the measurement results can be fetched.  Each measurement result is returned as a dictionary of measurements.

    # Fetch results
    eirp_results = rtms_client.get_measurement_results_eirp()
    print(eirp_results)

    obw_results = rtms_client.get_measurement_results_obw()
    print(obw_results)
