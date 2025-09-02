from .core.logger import setup_logging
from .core.preflight import run_common_checks
from .core.job_builder import build_job_info, build_plugin_info
from .core.deadline import submit
from .core.types import JobSpec
from .core.config import SubmitConfig

# 어댑터는 필요 시 지연 임포트
def _adapter_for(dcc: str):
    d = dcc.lower()
    if d == "maya":
        from .dcc.maya_adapter import MayaAdapter
        return MayaAdapter()
    elif d == "blender":
        from .dcc.blender_adapter import BlenderAdapter
        return BlenderAdapter()
    else:
        raise ValueError(f"Unknown DCC: {dcc}")

def submit_job(dcc: str, name: str, **kwargs):
    log = setup_logging()
    cfg = kwargs.get("config", SubmitConfig())
    adapter = _adapter_for(dcc)
    adapter.validate()
    scene = adapter.gather_scene_info()
    rend  = adapter.gather_render_settings()
    run_common_checks(scene, rend)

    spec = JobSpec(
        name=name,
        comment=kwargs.get("comment", ""),
        priority=kwargs.get("priority", cfg.default_priority),
        chunk_size=kwargs.get("chunk_size", cfg.default_chunk_size),
        pool=kwargs.get("pool", cfg.default_pool),
        group=kwargs.get("group", cfg.default_group),
        env=kwargs.get("env")
    )
    job_info = build_job_info(scene, rend, spec)
    plugin_info = build_plugin_info(scene, rend)

    ok, out, err = submit(job_info, plugin_info, deadlinecommand=cfg.deadlinecommand)
    if ok:
        log.info("Deadline 제출 성공")
        log.info(out.strip())
    else:
        log.error("Deadline 제출 실패")
        if err: log.error(err.strip())
        if out: log.error(out.strip())
    return ok, out, err
