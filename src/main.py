import asyncio

from logger import setup_logger

logger = setup_logger(__name__)


def add(first_num: int, second_num: int) -> int:
    return first_num + second_num


async def main() -> None:
    print(f"Sum of 1 and 2 is: {add(1, 2)}")


if __name__ == "__main__":
    asyncio.run(main())
