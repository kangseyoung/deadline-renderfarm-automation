from dataclasses import dataclass
from typing import Dict, Optional, List

@dataclass
class SceneInfo:
    dcc: str                 # "maya" | "blender"
    scene_file: str          # UNC
    project_root: Optional[str] = None
    render_layers: Optional[List[str]] = None
    camera: Optional[str] = None

@dataclass
class RenderSettings:
    renderer: str
    version: str
    frame_start: int = 1
    frame_end: int = 1
    frame_step: int = 1
    image_prefix: str = "<Scene>/<RenderLayer>/<Camera>"
    output_ext: str = "exr"
    output_dir: Optional[str] = None  # UNC
    extra: Optional[Dict[str, str]] = None

@dataclass
class JobSpec:
    name: str
    comment: str = ""
    priority: int = 50
    chunk_size: int = 1
    pool: str = "none"
    group: str = "none"
    env: Optional[Dict[str, str]] = None
