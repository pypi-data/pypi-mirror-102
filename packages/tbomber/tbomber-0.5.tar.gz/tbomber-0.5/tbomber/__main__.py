#!/bin/env python3.9

import asyncio
from abc import ABC, ABCMeta
from httpx import AsyncClient
import click
from click import echo, style

def load_services():
    import services as module

    services = set()
    for name in dir(module):
        attr = getattr(module, name)
        if isinstance(attr, ABCMeta) and attr not in (module.Service, ABC):
            services.add(attr())
    return services

async def send(client, phone, services):
    tasks = []
    for service in services:
        tasks.append(service.run(client, phone))

    for task in asyncio.as_completed(tasks):
        try:
            resp = await task
        except Exception:
            continue
        if resp.is_error:
            echo(style(f"{resp.url} returned an error HTTP code {resp.status_code}", fg="red"))
            continue
        echo(style(f"{resp.url} success", fg="green"))

@click.group()
@click.option("-c", "--crack", "crack")
async def cli(crack):
    client = AsyncClient()
    services = load_services()
    await send(client, "", services)
    await client.aclose()

asyncio.run(main())
