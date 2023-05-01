# Example of how to read/write to files with asynchronously
import asyncio, aiofiles

async def main() -> None:
    
    fp = 'example.txt'
    await write_file(fp, 'Hello, World!')
    content = await read_file(fp)
    print(content)

async def write_file(file_path: str, content: str) -> None:
    """Write a string to a file asynchronously"""
    async with aiofiles.open(file_path, "w") as file:
        await file.write(content)

async def read_file(file_path: str) -> str:
    """Get content from a file as a string asynchronously"""
    async with aiofiles.open(file_path) as file:
        content = await file.read()
        return content

if __name__ == "__main__":
    asyncio.run(main())

