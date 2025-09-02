# UI 버튼에서 호출할 간단한 진입점
from ..cli import submit_job

def on_click_send_to_deadline(dcc: str, job_name: str, **kwargs):
    return submit_job(dcc=dcc, name=job_name, **kwargs)
