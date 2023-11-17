from pdm.backend.base import Context


class MypycBuildHook:
    def pdm_build_hook_enabled(self, context: Context):
        return context.target == "wheel"

    def pdm_build_initialize(self, context: Context):
        context.ensure_build_dir()
        print("pdm_build_initialize")

