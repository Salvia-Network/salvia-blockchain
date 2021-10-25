from typing import Dict

# The rest of the codebase uses seeds everywhere.
# Only use these units for user facing interfaces.
units: Dict[str, int] = {
    "salvia": 10 ** 12,  # 1 salvia (XCH) is 1,000,000,000,000 seed (1 trillion)
    "seed": 1,
    "colouredcoin": 10 ** 3,  # 1 coloured coin is 1000 colouredcoin seeds
}
