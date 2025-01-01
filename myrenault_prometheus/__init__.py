import os
import asyncio
import aiohttp

from prometheus_client import start_http_server, Gauge

from renault_api.cli.__main__ import renault_vehicle, renault_settings
from renault_api.credential_store import FileCredentialStore

DefaultRefreshPeriod = 600

battery_level = Gauge("battery_level", "")
battery_temperature = Gauge("battery_temperature", "")
battery_autonomy = Gauge("battery_autonomy", "")
battery_available_energy = Gauge("battery_available_energy", "")
plug_status = Gauge("plug_status", "")
charging_status = Gauge("charging_status", "")
charging_remaining_time = Gauge("charging_remaining_time", "")
charging_instantaneous_power = Gauge("charging_instantaneous_power", "")

total_mileage = Gauge("total_mileage", "")


async def run():
    async with aiohttp.ClientSession() as websession:
        ctx = {}
        ctx["credential_store"] = FileCredentialStore(
            os.path.expanduser(renault_settings.CREDENTIAL_PATH)
        )
        vehicle = await renault_vehicle.get_vehicle(websession, ctx)

        while True:
            battery_status = await vehicle.get_battery_status()

            if battery_status.batteryLevel != None:
                battery_level.set(battery_status.batteryLevel)
            if battery_status.batteryTemperature != None:
                battery_temperature.set(battery_status.batteryTemperature)
            if battery_status.batteryAutonomy != None:
                battery_autonomy.set(battery_status.batteryAutonomy)
            if battery_status.batteryAvailableEnergy != None:
                battery_available_energy.set(battery_status.batteryAvailableEnergy)
            if battery_status.plugStatus != None:
                plug_status.set(battery_status.plugStatus)
            if battery_status.chargingStatus != None:
                charging_status.set(battery_status.chargingStatus)
            if battery_status.chargingRemainingTime != None:
                charging_remaining_time.set(battery_status.chargingRemainingTime)
            if battery_status.chargingInstantaneousPower != None:
                charging_instantaneous_power.set(battery_status.chargingInstantaneousPower)

            cockpit = await vehicle.get_cockpit()
            total_mileage.set(cockpit.totalMileage)

            await asyncio.sleep(DefaultRefreshPeriod)


def main():
    start_http_server(8082, addr="0.0.0.0")
    asyncio.run(run())
