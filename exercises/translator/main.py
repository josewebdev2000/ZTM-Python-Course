from translate import Translator
import asyncio
import aiofiles
import sys

async def main() -> None:
    
    # Translate to Spanish
    tr = Translator(to_lang="es")
    
    # Get content from original file
    ori_con = await get_file_content_str(sys.argv[1])
    
    # Translate the content to Spanish
    es_con = tr.translate(ori_con)
    
    # Print the content from the translated file
    print("Translated content to Spanish:\n\n")
    print(es_con)
    
    # Write translated content to spanish file
    await write_content_str(f"{sys.argv[1][:-4]}.txt", es_con)
    
async def get_file_content_str(filename: str) -> str:
    """Read content from a file asynchronously"""
    async with aiofiles.open(filename) as f:
        content = await f.read()
        return content

async def write_content_str(filename: str, content: str) -> None:
    """Write content to a file asynchronously"""
    async with aiofiles.open(filename, "w") as f:
        await f.write(content) 

if __name__ == "__main__":
    asyncio.run(main())