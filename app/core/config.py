from starlette.config import Config

config = Config(".env")

VERSION: str = "0.1"

PROJECT_NAME: str = config("PROJECT_NAME", default="Webbudy Project")

DESCRIPTION: str = config("DESCRIPTION", default="Webbudy project backend API")