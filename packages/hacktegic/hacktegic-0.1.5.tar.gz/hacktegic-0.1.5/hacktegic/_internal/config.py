import os

import aiofiles
import platformdirs
import tomlkit


class ConfigManager:
    def __init__(self) -> None:
        self.config = None
        self.__config_path = (
            platformdirs.user_config_dir("hacktegic", ensure_exists=True)
            + "/config.toml"
        )

    async def load(self) -> None:
        """
        Load the config from file.
        """
        if not os.path.exists(self.__config_path):
            return
        async with aiofiles.open(self.__config_path, mode="r") as f:
            doc = tomlkit.loads(await f.read())
            self.config = doc["hacktegic"]

    async def save(self) -> None:
        """
        Save the config to file.
        """
        async with aiofiles.open(self.__config_path, mode="w") as f:
            await f.write(tomlkit.dumps({"hacktegic": self.config}))
