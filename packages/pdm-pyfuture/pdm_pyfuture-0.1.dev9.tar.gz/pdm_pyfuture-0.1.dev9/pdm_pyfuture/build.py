from pdm.backend.base import Context
from pathlib import Path
from typing import Any
from pyfuture.codemod import TransformTypeParametersCommand
import libcst as cst
from libcst.codemod import CodemodContext

class PyFutureBuildHook:

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

    def pdm_build_update_files(self, context: Context, files: dict[str, Path]) -> None:
        build_dir = context.ensure_build_dir()
        package_dir = Path(context.config.build_config.package_dir)
        includes = context.config.build_config.includes
        for include in includes:
            print(include)
            src_path = package_dir/include
            tgt_path = build_dir/include
            files[include] = tgt_path
            for src_file in src_path.glob("**/*.py"):
                tgt_file = tgt_path/src_file.relative_to(src_path)
                with src_file.open("r") as f:
                    content = f.read()
                    module = cst.parse_module(content)
                    new_module = TransformTypeParametersCommand(CodemodContext()).transform_module(module)
                with tgt_file.open("w") as f:
                    f.write(new_module.code)
                    
