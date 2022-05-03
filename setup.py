from setuptools import setup

dependencies = [
    "multidict==5.1.0",  # Avoid 5.2.0 due to Avast
    "aiofiles==0.7.0",  # Async IO for files
    "blspy==1.0.8",  # Signature library
    "chiavdf==1.0.3",  # timelord and vdf verification
    "chiabip158==1.0",  # bip158-style wallet filters
    "chiapos==1.0.7",  # proof of space
    "clvm==0.9.7",
    "clvm_rs==0.1.17",
    "clvm_tools==0.4.3",
    "aiohttp==3.7.4",  # HTTP server for full node rpc
    "aiosqlite==0.17.0",  # asyncio wrapper for sqlite, to store blocks
    "bitstring==3.1.9",  # Binary data management library
    "colorama==0.4.4",  # Colorizes terminal output
    "colorlog==5.0.1",  # Adds color to logs
    "concurrent-log-handler==0.9.19",  # Concurrently log and rotate logs
    "cryptography==37.0.1",  # Python cryptography library for TLS - keyring conflict
    "fasteners==0.16.3",  # For interprocess file locking
    "keyring==23.0.1",  # Store keys in MacOS Keychain, Windows Credential Locker
    "keyrings.cryptfile==1.3.4",  # Secure storage for keys on Linux (Will be replaced)
    #  "keyrings.cryptfile==1.3.8",  # Secure storage for keys on Linux (Will be replaced)
    #  See https://github.com/frispete/keyrings.cryptfile/issues/15
    "PyYAML==5.4.1",  # Used for config file format
    "setproctitle==1.2.2",  # Gives the salvia processes readable names
    "sortedcontainers==2.4.0",  # For maintaining sorted mempools
    "websockets==8.1.0",  # For use in wallet RPC and electron UI
    "click==7.1.2",  # For the CLI
    "dnspythonchia==2.2.0",  # Query DNS seeds
    "watchdog==2.1.6",  # Filesystem event watching - watches keyring.yaml
    "dnslib==0.9.17",  # dns lib
    "typing-extensions==4.0.1",  # typing backports like Protocol and TypedDict
    "zstd==1.5.0.4",
    "packaging==21.0",
]

upnp_dependencies = [
    "miniupnpc==2.2.2",  # Allows users to open ports on their router
]

dev_dependencies = [
    "pre-commit",
    "pytest",
    "pytest-asyncio",
    "pytest-monitor; sys_platform == 'linux'",
    "pytest-xdist",
    "flake8",
    "mypy",
    "black",
    "aiohttp_cors",  # For blackd
    "ipython",  # For asyncio debugging
    "types-aiofiles",
    "types-click",
    "types-cryptography",
    "types-pkg_resources",
    "types-pyyaml",
    "types-setuptools",
]

kwargs = dict(
    name="salvia-blockchain",
    author="Salvia Team",
    author_email="contact@salvianetwork.net",
    description="Salvia blockchain full node, farmer, timelord, and wallet.",
    url="https://salvianetwork.net/",
    license="Apache License",
    python_requires=">=3.7, <4",
    keywords="salvia blockchain node",
    install_requires=dependencies,
    setup_requires=["setuptools_scm"],
    extras_require=dict(
        uvloop=["uvloop"],
        dev=dev_dependencies,
        upnp=upnp_dependencies,
    ),
    packages=[
        "build_scripts",
        "salvia",
        "salvia.cmds",
        "salvia.clvm",
        "salvia.consensus",
        "salvia.daemon",
        "salvia.full_node",
        "salvia.timelord",
        "salvia.farmer",
        "salvia.harvester",
        "salvia.introducer",
        "salvia.plotters",
        "salvia.plotting",
        "salvia.pools",
        "salvia.protocols",
        "salvia.rpc",
        "salvia.seeder",
        "salvia.seeder.util",
        "salvia.server",
        "salvia.simulator",
        "salvia.types.blockchain_format",
        "salvia.types",
        "salvia.util",
        "salvia.wallet",
        "salvia.wallet.puzzles",
        "salvia.wallet.rl_wallet",
        "salvia.wallet.cat_wallet",
        "salvia.wallet.did_wallet",
        "salvia.wallet.settings",
        "salvia.wallet.trading",
        "salvia.wallet.util",
        "salvia.ssl",
        "mozilla-ca",
    ],
    entry_points={
        "console_scripts": [
            "salvia = salvia.cmds.salvia:main",
            "salvia_wallet = salvia.server.start_wallet:main",
            "salvia_full_node = salvia.server.start_full_node:main",
            "salvia_harvester = salvia.server.start_harvester:main",
            "salvia_farmer = salvia.server.start_farmer:main",
            "salvia_introducer = salvia.server.start_introducer:main",
            "salvia_seeder = salvia.cmds.seeder:main",
            "salvia_seeder_crawler = salvia.seeder.start_crawler:main",
            "salvia_seeder_server = salvia.seeder.dns_server:main",
            "salvia_timelord = salvia.server.start_timelord:main",
            "salvia_timelord_launcher = salvia.timelord.timelord_launcher:main",
            "salvia_full_node_simulator = salvia.simulator.start_simulator:main",
        ]
    },
    package_data={
        "salvia": ["pyinstaller.spec"],
        "": ["*.clvm", "*.clvm.hex", "*.clib", "*.clinc", "*.clsp", "py.typed"],
        "salvia.util": ["initial-*.yaml", "english.txt"],
        "salvia.ssl": ["salvia_ca.crt", "salvia_ca.key", "dst_root_ca.pem"],
        "mozilla-ca": ["cacert.pem"],
    },
    use_scm_version={"fallback_version": "unknown-no-.git-directory"},
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
)


if __name__ == "__main__":
    setup(**kwargs)  # type: ignore
