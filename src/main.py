import asyncio
import logging

from dotenv import load_dotenv

from src.logging_setup import LoggerHandlerType, SetupLoggerParams, setup_logger
from src.settings import AppSettings

logger = logging.getLogger(__name__)


async def main() -> None:
    load_dotenv()
    settings = AppSettings()
    setup_logger(
        SetupLoggerParams(
            level=settings.logging.min_log_level,
            handler_types={LoggerHandlerType.STREAM, LoggerHandlerType.FILE},
            file_path=settings.logging.log_file_path,
        ),
    )
    logger.info("Logging settings: %s", settings.logging)
    logger.info("Starting the main function for %s", settings.core.app_name)


if __name__ == "__main__":
    asyncio.run(main())
