import asyncio

from src.logging_setup import setup_logger
from src.settings import settings

logger = setup_logger(__name__)


def add(first_num: int, second_num: int) -> int:
    return first_num + second_num


async def main() -> None:
    logger.info(f"Logging settings: {settings.logging}")
    logger.info(f"Starting the main function for {settings.core.app_name}")
    print(f"Sum of 1 and 2 is: {add(1, 2)}")


if __name__ == "__main__":
    asyncio.run(main())
