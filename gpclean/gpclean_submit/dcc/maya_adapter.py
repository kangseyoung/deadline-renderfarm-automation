from ..core.types import SceneInfo, RenderSettings
from ..core.paths import to_unc, decide_output_ext

class MayaAdapter:
    def gather_scene_info(self) -> SceneInfo:
        try:
            import maya.cmds as cmds  # 지연 임포트
        except Exception as e:
            raise RuntimeError("Maya 환경이 아닙니다.") from e

        scene = to_unc(cmds.file(q=True, sn=True))
        proj  = to_unc(cmds.workspace(q=True, rd=True))
        # 렌더러블 카메라
        cams = cmds.ls(type='camera', long=True) or []
        camera = None
        for c in cams:
            try:
                if cmds.objExists(c + ".renderable") and cmds.getAttr(c + ".renderable"):
                    parents = cmds.listRelatives(c, parent=True, fullPath=True) or []
                    camera = parents[0] if parents else c
                    break
            except Exception:
                pass
        # 렌더 레이어(옵션)
        try:
            layers = [l for l in (cmds.ls(type='renderLayer') or []) if l != "defaultRenderLayer"]
        except Exception:
            layers = None
        return SceneInfo(dcc="maya", scene_file=scene, project_root=proj,
                         render_layers=layers or None, camera=camera)

    def gather_render_settings(self) -> RenderSettings:
        import maya.cmds as cmds
        renderer = cmds.getAttr("defaultRenderGlobals.currentRenderer")
        vyear = str(cmds.about(v=True))
        s = int(cmds.getAttr("defaultRenderGlobals.startFrame"))
        e = int(cmds.getAttr("defaultRenderGlobals.endFrame"))
        step = int(round(cmds.getAttr("defaultRenderGlobals.byFrameStep"))) or 1
        prefix = cmds.getAttr("defaultRenderGlobals.imageFilePrefix") or "<Scene>/<RenderLayer>/<Camera>"
        images_dir = cmds.workspace("images", q=True, fre=True) or "images"
        outdir = to_unc(cmds.workspace(q=True, rd=True) + images_dir)
        ext = decide_output_ext(renderer, default_ext="exr")
        return RenderSettings(renderer=renderer, version=vyear,
                              frame_start=s, frame_end=e, frame_step=max(1, step),
                              image_prefix=prefix, output_ext=ext, output_dir=outdir)

    def validate(self) -> None:
        import maya.cmds as cmds
        rend = cmds.getAttr("defaultRenderGlobals.currentRenderer") or ""
        if rend.lower() in ("arnold", "mtoa"):
            try:
                if not cmds.pluginInfo("mtoa", q=True, loaded=True):
                    cmds.loadPlugin("mtoa")
            except Exception:
                raise RuntimeError("Arnold(mtoa) 플러그인이 로드되지 않았습니다.")
