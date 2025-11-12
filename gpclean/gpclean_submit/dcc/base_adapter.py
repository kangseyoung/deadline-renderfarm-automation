from abc import ABC, abstractmethod
from ..core.types import SceneInfo, RenderSettings

class DCCAdapter(ABC):
    @abstractmethod
    def gather_scene_info(self) -> SceneInfo: ...
    @abstractmethod
    def gather_render_settings(self) -> RenderSettings: ...
    @abstractmethod
    def validate(self) -> None: ...
