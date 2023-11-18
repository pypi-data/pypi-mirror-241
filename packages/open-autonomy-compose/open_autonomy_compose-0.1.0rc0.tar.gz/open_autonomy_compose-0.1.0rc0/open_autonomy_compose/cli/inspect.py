"""Start an inspect server."""

import webbrowser
from pathlib import Path

from autonomy.cli.helpers.analyse import load_package_tree
from clea import Boolean, Directory, Integer, String, command
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import HTMLResponse, JSONResponse
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles
from typing_extensions import Annotated
from uvicorn.main import run as uvicorn

from open_autonomy_compose.data import DATA_DIR
from open_autonomy_compose.fsm.composition import Composition
from open_autonomy_compose.fsm.specification import FSMSpecification


class Inspect:
    """View-Controller for inspect tool."""

    def __init__(self, app: Path) -> None:
        """Initialize object."""
        self._app = app

    def spec(self) -> FSMSpecification:
        """Load FSM spec."""
        load_package_tree(self._app.parent.parent.parent)
        return FSMSpecification.from_compostion(
            composition=Composition.from_path(
                path=self._app,
            ),
        )

    def index(self, request: Request) -> HTMLResponse:
        """Index page."""
        return HTMLResponse(
            content=(DATA_DIR / "site" / "index.html").read_text(encoding="utf-8")
        )

    def get_fsm(self, request: Request) -> JSONResponse:
        """Returns FSM as json."""
        return JSONResponse(
            content=self.spec().to_json(include_parent=True),
        )


@command
def inspect(
    app: Annotated[Path, Directory(exists=True, resolve=True)],
    browser: Annotated[bool, Boolean()],
    host: Annotated[str, String()] = "localhost",
    port: Annotated[int, Integer()] = 8000,
) -> None:
    """Inspect a ABCI app composition in a webview."""

    def _on_startup() -> None:
        """On startup."""
        if browser:
            webbrowser.open(url=f"http://{host}:{port}")

    ivc = Inspect(
        app=app,
    )
    uvicorn(
        app=Starlette(
            debug=True,
            routes=[
                Route("/", ivc.index),
                Route("/fsm", ivc.get_fsm),
                Mount(
                    "/_next",
                    app=StaticFiles(directory=(DATA_DIR / "site" / "_next")),
                    name="static",
                ),
            ],
            middleware=[Middleware(CORSMiddleware, allow_origins=["*"])],
            on_startup=[_on_startup],
        ),
        host=host,
        port=port,
    )
