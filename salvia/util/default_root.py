import os
from pathlib import Path

DEFAULT_ROOT_PATH = Path(os.path.expanduser(os.getenv("SALVIA_ROOT", "~/.salvia/mainnet"))).resolve()

DEFAULT_KEYS_ROOT_PATH = Path(os.path.expanduser(os.getenv("SALVIA_KEYS_ROOT", "~/.salvia_keys"))).resolve()
