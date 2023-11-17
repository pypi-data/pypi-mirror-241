import logging
from typing import Any

from pydantic import BaseModel

from ipfabric import models

logger = logging.getLogger("ipfabric")


class Platforms(BaseModel):
    client: Any = None

    @property
    def environment_power_supplies(self):
        return models.Table(client=self.client, endpoint="tables/inventory/power-supplies")

    @property
    def environment_power_supplies_fans(self):
        return models.Table(client=self.client, endpoint="tables/inventory/power-supplies-fans")

    @property
    def environment_fans(self):
        return models.Table(client=self.client, endpoint="tables/inventory/fans")

    @property
    def environment_modules(self):
        return models.Table(client=self.client, endpoint="tables/inventory/modules")

    @property
    def environment_temperature_sensors(self):
        return models.Table(client=self.client, endpoint="tables/inventory/temperature-sensors")

    @property
    def cisco_fabric_path_summary(self):
        return models.Table(client=self.client, endpoint="tables/platforms/fabric-path/summary")

    @property
    def cisco_fabric_path_isis_neighbors(self):
        return models.Table(client=self.client, endpoint="tables/platforms/fabric-path/neighbors")

    @property
    def cisco_fabric_path_switches(self):
        return models.Table(client=self.client, endpoint="tables/platforms/fabric-path/switches")

    @property
    def cisco_fabric_path_routes(self):
        return models.Table(client=self.client, endpoint="tables/platforms/fabric-path/routes")

    @property
    def juniper_cluster(self):
        return models.Table(client=self.client, endpoint="tables/platforms/cluster/srx")

    @property
    def cisco_fex_interfaces(self):
        return models.Table(client=self.client, endpoint="tables/platforms/fex/interfaces")

    @property
    def cisco_fex_modules(self):
        return models.Table(client=self.client, endpoint="tables/platforms/fex/modules")

    @property
    def cisco_vdc_devices(self):
        return models.Table(client=self.client, endpoint="tables/platforms/vdc/devices")

    @property
    def platform_cisco_vss(self):
        return models.Table(client=self.client, endpoint="tables/platforms/vss/overview")

    @property
    def cisco_vss_chassis(self):
        return models.Table(client=self.client, endpoint="tables/platforms/vss/chassis")

    @property
    def cisco_vss_vsl(self):
        return models.Table(client=self.client, endpoint="tables/platforms/vss/vsl")

    @property
    def poe_devices(self):
        return models.Table(client=self.client, endpoint="tables/platforms/poe/devices")

    @property
    def poe_interfaces(self):
        return models.Table(client=self.client, endpoint="tables/platforms/poe/interfaces")

    @property
    def poe_modules(self):
        return models.Table(client=self.client, endpoint="tables/platforms/poe/modules")

    @property
    def stacks(self):
        return models.Table(client=self.client, endpoint="tables/platforms/stacks")

    @property
    def stacks_members(self):
        return models.Table(client=self.client, endpoint="tables/platforms/stack/members")

    @property
    def stacks_stack_ports(self):
        return models.Table(client=self.client, endpoint="tables/platforms/stack/connections")

    @property
    def logical_devices(self):
        return models.Table(client=self.client, endpoint="tables/platforms/devices")
