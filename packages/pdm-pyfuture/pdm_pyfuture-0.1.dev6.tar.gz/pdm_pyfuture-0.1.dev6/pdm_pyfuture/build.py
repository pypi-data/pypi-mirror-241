from pdm.backend.base import Context
from pathlib import Path
from typing import Any
from pyfuture.codemod import TransformTypeParametersCommand
import libcst as cst
from libcst.codemod import CodemodContext

class PyFutureBuildHook:

    DEFAULT_TARGET_DIR = ".pyfuture_build"

    def hook_config(self, context: Context) -> dict[str, Any]:
        return (
            context.config.data.get("tool", {})
            .get("pdm", {})
            .get("build", {})
            .get("hooks", {})
            .get("pyfuture", {})
        )

    def pdm_build_hook_enabled(self, context: Context):
        return context.target == "sdist"

    def pdm_build_initialize(self, context: Context) -> None:
        # Save the change to the context
        context.config.data.setdefault("tool", {}).setdefault("pdm", {}).setdefault(
            "build", {}
        )

    def pdm_build_update_files(self, context: Context, files: dict[str, Path]) -> None:
        if not context.build_dir.exists():
            return
        for path in files.values():
            if path.name.endswith(".py"):
                with path.open("r") as f:
                    content = f.read()
                    module = cst.parse_module(content)
                    new_module = TransformTypeParametersCommand(CodemodContext()).transform_module(module)
                with path.open("w") as f:
                    f.write(new_module.code)
                
