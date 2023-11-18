from pdm.backend.base import Context
from pathlib import Path
from typing import Any
from pyfuture.utils import transfer_file

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
        return context.target == "wheel"

    def pdm_build_update_files(self, context: Context, files: dict[str, Path]) -> None:
        build_dir = context.ensure_build_dir()
        package_dir = Path(context.config.build_config.package_dir)
        includes = context.config.build_config.includes
        for include in includes:
            src_path = package_dir/include
            tgt_path = build_dir/include
            for src_file in src_path.glob("**/*.py"):
                tgt_file = tgt_path/src_file.relative_to(src_path)
                files[f"{tgt_path.relative_to(build_dir)}"] = tgt_file
                # TODO: support config target
                transfer_file(src_file, tgt_file, target=(3, 8))
