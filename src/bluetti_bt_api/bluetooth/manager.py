import asyncio
import logging

from typing import Dict, List

from .client import BluetoothClient
from ..utils.commands import DeviceCommand


class DeviceManager:
    clients: Dict[str, BluetoothClient]

    def __init__(self, addresses: List[str]):
        self.addresses = addresses
        self.clients = {}

    async def run(self):
        logging.info(f'Connecting to clients: {self.addresses}')

        # Start client loops
        self.clients = {a: BluetoothClient(a) for a in self.addresses}
        await asyncio.gather(*[c.run() for c in self.clients.values()])

    def is_ready(self, address: str):
        if address in self.clients:
            return self.clients[address].is_ready
        else:
            return False

    def get_name(self, address: str):
        if address in self.clients:
            return self.clients[address].name
        else:
            raise Exception('Unknown address')

    async def perform(self, address: str, command: DeviceCommand):
        if address in self.clients:
            return await self.clients[address].perform(command)
        else:
            raise Exception('Unknown address')

    async def perform_nowait(self, address: str, command: DeviceCommand):
        if address in self.clients:
            await self.clients[address].perform_nowait(command)
        else:
            raise Exception('Unknown address')
