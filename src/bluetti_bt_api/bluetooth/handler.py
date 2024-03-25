import asyncio
import logging
import time

from bleak import BleakError
from typing import Dict, List, cast

from .manager import DeviceManager
from ..base.device import BluettiDevice
from ..utils.commands import ReadHoldingRegisters
from ..exceptions import *


class DeviceHandler:
    def __init__(self, addresses: List[str], interval: int):
        self.manager = DeviceManager(addresses)
        self.devices: Dict[str, BluettiDevice] = {}
        self.interval = interval

    async def run(self):
        loop = asyncio.get_running_loop()

        # Start manager
        manager_task = loop.create_task(self.manager.run())

        # Poll the clients
        logging.info('Starting to poll clients...')
        polling_tasks = [self._poll(a) for a in self.manager.addresses]

        await asyncio.gather(*(polling_tasks + [manager_task]))

    async def _poll(self, address: str):
        while True:
            if not self.manager.is_ready(address):
                logging.debug(f'Waiting for connection to {address} to start polling...')
                await asyncio.sleep(1)
                continue

            device = self._get_device(address)

            # Send all polling commands
            start_time = time.monotonic()
            for command in device.polling_commands:
                await self._poll_with_command(device, command)
            elapsed = time.monotonic() - start_time

            # Limit polling rate if interval provided
            if self.interval > 0 and self.interval > elapsed:
                await asyncio.sleep(self.interval - elapsed)
    
    async def _poll_with_command(self, device: BluettiDevice, command: ReadHoldingRegisters):
        response_future = await self.manager.perform(device.address, command)
        try:
            response = cast(bytes, await response_future)
            body = command.parse_response(response)
            parsed = device.parse(command.starting_address, body)
            logging.debug(f'{parsed}')
        except ParseError:
            logging.debug('Got a parse exception...')
        except ModbusError as err:
            logging.debug(f'Got an invalid request error for {command}: {err}')
        except (BadConnectionError, BleakError) as err:
            logging.debug(f'Needed to disconnect due to error: {err}')

    def _get_device(self, address: str):
        if address not in self.devices:
            name = self.manager.get_name(address)
            self.devices[address] = build_device(address, name)
        return self.devices[address]