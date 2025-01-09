from src.app import app

import asyncio
import uvicorn


async def main() -> None:
    server_config = uvicorn.Config(app, host="0.0.0.0", port=8000)
    server = uvicorn.Server(server_config)

    await server.serve()

if __name__ == "__main__":
    asyncio.run(main())