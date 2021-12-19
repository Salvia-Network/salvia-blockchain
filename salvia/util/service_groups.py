from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": "salvia_harvester salvia_timelord_launcher salvia_timelord salvia_farmer salvia_full_node salvia_wallet".split(),
    "node": "salvia_full_node".split(),
    "harvester": "salvia_harvester".split(),
    "farmer": "salvia_harvester salvia_farmer salvia_full_node salvia_wallet".split(),
    "farmer-no-wallet": "salvia_harvester salvia_farmer salvia_full_node".split(),
    "farmer-only": "salvia_farmer".split(),
    "timelord": "salvia_timelord_launcher salvia_timelord salvia_full_node".split(),
    "timelord-only": "salvia_timelord".split(),
    "timelord-launcher-only": "salvia_timelord_launcher".split(),
    "wallet": "salvia_wallet salvia_full_node".split(),
    "wallet-only": "salvia_wallet".split(),
    "introducer": "salvia_introducer".split(),
    "simulator": "salvia_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
