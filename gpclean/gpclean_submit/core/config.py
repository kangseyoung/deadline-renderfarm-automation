from dataclasses import dataclass

@dataclass
class SubmitConfig:
    deadlinecommand: str = r"C:\Program Files\Thinkbox\Deadline10\bin\deadlinecommand.exe"  # 절대경로 지정 가능
    default_pool: str = "none"
    default_group: str = "none"
    default_priority: int = 50
    default_chunk_size: int = 1
