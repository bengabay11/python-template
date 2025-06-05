import asyncio
import logging

from src.logging_setup import LoggerHandlerType, SetupLoggerParams, setup_logger
from src.settings import settings

logger = logging.getLogger(__name__)


async def main() -> None:
    setup_logger(
        SetupLoggerParams(
            level=settings.logging.min_log_level,
            handler_types={LoggerHandlerType.STREAM, LoggerHandlerType.FILE},
            file_path=settings.logging.log_file_path,
        )
    )
    logger.info(f"Logging settings: {settings.logging}")
    logger.info(f"Starting the main function for {settings.core.app_name}")
    print("Hello, World!")


if __name__ == "__main__":
    asyncio.run(main())
