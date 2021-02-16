import json
from typing import List

from panda_puts.types.extras import Strategy


def list_saved_strategies() -> List[str]:
    return ["TODO"]


def save_strategy(strategy: Strategy) -> None:
    file_name = f"{strategy.ticker}_{strategy.name}_{strategy.expiry}.json"
    with open(file_name, "w") as sf:
        json.dump(strategy.to_json(), sf, indent=4)


def load_strategy(file_name: str) -> Strategy:
    with open(file_name, "r") as sf:
        return json.load(sf, object_hook=Strategy.from_json)
