import logging
import os

import uvicorn

if __name__ == "__main__":
    uvicorn.run("fast_api.main:app",
                app_dir=os.path.dirname(os.path.abspath(__file__)),
                host="0.0.0.0",
                port=9000,
                # reload=True,
                )
