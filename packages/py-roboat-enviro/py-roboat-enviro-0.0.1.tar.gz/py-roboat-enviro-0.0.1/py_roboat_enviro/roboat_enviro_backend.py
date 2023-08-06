import json

from uplink import *


class RoboatEnviroData(Consumer):
    """Client for the Roboat Environmental Data API

    Args:
        Consumer (uplink.Consumer): Base consumer class with which to define custom consumers.
    """

    @get("users")
    def get_users(self):
        """List all users."""
        return

    @get("users/{user_id}")
    def get_user_by_id(self, user_id: Path):
        """Get user by ID.

        Args:
            user_id (Path): [description]
        """
        return

    @post("users/search?filters={filters}")
    def search_users(self, filters):
        """Search users.

        Args:
            filters (list of dict): [description]
        """
        return

    @post("sensors?nickname={nickname}")
    def add_sensor(self, nickname):
        """Add a sensor.

        Args:
            nickname (str): [description]
        """
        return

    @get("sensors")
    def get_sensors(self):
        """List all sensors."""
        return

    @get("sensors/{sensor_sn}")
    def get_sensor_by_sn(self, sensor_sn: Path):
        """Get sensor by serial number.

        Args:
            sensor_sn (Path): [description]
        """
        return

    @post("sensors/search?filters={filters}")
    def search_sensors(self, filters):
        """Search sensors.

        Args:
            filters ([type]): [description]
        """
        return

    @delete("sensors/{sensor_sn}")
    def delete_sensor_by_sn(self, sensor_sn: Path):
        """[summary]

        Args:
            sensor_sn (Path): [description]
        """
        return

    @json
    @post("sensor_diagnostics")
    def add_sensor_diagnostics(self, sensor_diagnostics: Body):
        """Add sensor diagnostics.

        Args:
            sensor_diagnostics (Query): [description]
        """
        return

    @post("sensor_diagnostics/search?filters={filters}")
    def search_sensor_diagnostics(self, filters):
        """Search sensor diagnostics.

        Args:
            filters ([type]): [description]
        """
        return

    # TODO
    # @delete("sensor_diagnostics/{id}")

    @json
    @post("sensor_logs")
    def add_sensor_logs(self, sensor_logs: Body):
        """Add sensor logs.

        Args:
            sensor_logs (Query): [description]
        """
        return

    @post("sensor_logs/search?filters={filters}")
    def search_sensor_logs(self, filters):
        """Search sensor logs.

        Args:
            filters ([type]): [description]
        """
        return

    # TODO
    # @delete("sensor_logs/{id}")

    @json
    @post("gps_measurements")
    def add_gps_measurements(self, gps_measurements: Body):
        """Add GPS measurements.

        Args:
            gps_measurements (Query): [description]
        """
        return

    @post("gps_measurements/search?filters={filters}")
    def search_gps_measurements(self, filters):
        """Search GPS measurements.

        Args:
            filters ([type]): [description]
        """
        return

    # TODO
    # @delete("gps_measurements/{id}")

    @multipart
    @post("spec_measurement_metadata")
    def add_spectroscopy_measurement_metadata(self, scan_file: Part, metadata: Field):
        """Add spectroscopy measurement metadata.

        Args:
            spectroscopy_measurement_metadata (Query): [description]
        """
        return

    @post("spec_measurement_metadata/search?filters={filters}")
    def search_spectroscopy_measurement_metadata(self, filters):
        """Search spectroscopy measurement metadata.

        Args:
            filters ([type]): [description]
        """
        return

    @delete("spec_measurement_metadata/{filename}")
    def delete_spec_measurement_metadata_by_filename(self, filename):
        """Delete spectroscopy measurement and metadata by filename

        Args:
            filename (str): [description]
        """
        return

    @get("spec_measurements")
    def get_spec_measurement_filenames(self):
        """List all scan filenames."""
        return

    @get("spec_measurements/{filename}")
    def get_spec_measurements_by_filename(self, filename: Path):
        """Get scan file by filename.

        Args:
            filename (Path): [description]
        """
        return

    @delete("spec_measurements/{filename}")
    def delete_spec_spec_measurements_by_filename(self, filename):
        """Delete spectroscopy measurements by filename

        Args:
            filename (str): [description]
        """
        return
