#!/usr/bin/env python3
"""
Cross-platform launcher for the spark-mcp MCP server.

The spark-mcp package hardcodes macOS paths. This script patches the
database path before startup so it works on Windows too.

Prerequisites:
  pip install spark-mcp

Spark Desktop must be running when using this server.
"""
import os
import sys
import platform

if platform.system() == "Windows":
    local_app_data = os.environ.get("LOCALAPPDATA")
    if not local_app_data:
        print(
            "Error: LOCALAPPDATA environment variable not found. "
            "Is this running on Windows?",
            file=sys.stderr,
        )
        sys.exit(1)

    # Patch the hardcoded macOS path before the server module reads it
    import spark_mcp.db as _db
    _db.SPARK_DATA = os.path.join(local_app_data, "Spark Desktop", "core-data")

from spark_mcp.server import main

if __name__ == "__main__":
    main()
