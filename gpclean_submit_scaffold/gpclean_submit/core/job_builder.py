from .types import SceneInfo, RenderSettings, JobSpec
from .paths import safe_join, to_unc

def build_job_info(scene: SceneInfo, rend: RenderSettings, spec: JobSpec) -> str:
    plugin = "MayaBatch" if scene.dcc == "maya" else "Blender"
    lines = [
        f"Plugin={plugin}",
        f"Name={spec.name}",
        f"Comment={spec.comment}",
        f"Frames={rend.frame_start}-{rend.frame_end}",
        f"FrameStep={rend.frame_step}",
        f"ChunkSize={spec.chunk_size}",
        f"Priority={spec.priority}",
        f"Pool={spec.pool}",
        f"Group={spec.group}",
    ]
    if rend.output_dir:
        out_full = safe_join(rend.output_dir, rend.image_prefix, rend.output_ext)
        lines.append(f"OutputFilename0={to_unc(out_full).replace('\\', r'\\')}")
    if spec.env:
        for i, (k, v) in enumerate(spec.env.items()):
            lines.append(f"EnvironmentKeyValue{i}={k};{v}")
    return "\n".join(lines) + "\n"

def build_plugin_info(scene: SceneInfo, rend: RenderSettings) -> str:
    if scene.dcc == "maya":
        return _maya(scene, rend)
    else:
        return _blender(scene, rend)

def _maya(scene: SceneInfo, rend: RenderSettings) -> str:
    lines = [
        f"SceneFile={scene.scene_file.replace('\\', r'\\')}",
        f"Version={rend.version}",
        f"ProjectPath={(scene.project_root or '').replace('\\', r'\\')}",
        f"Renderer={rend.renderer}",
    ]
    if scene.camera:
        lines.append(f"Camera={scene.camera}")
    return "\n".join(lines) + "\n"

def _blender(scene: SceneInfo, rend: RenderSettings) -> str:
    lines = [
        f"SceneFile={scene.scene_file.replace('\\', r'\\')}",
        f"Version={rend.version}",
        f"OutputFilePath={(rend.output_dir or '').replace('\\', r'\\')}",
        f"OutputFilePrefix={rend.image_prefix}",
        f"Renderer={rend.renderer}",
    ]
    return "\n".join(lines) + "\n"
