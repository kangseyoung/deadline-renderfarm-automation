import os
from dataclasses import dataclass

@dataclass
class SubmitConfig:
    deadlinecommand: str = os.getenv(
        "DEADLINE_COMMAND",
        "/path/to/deadlinecommand",
    )
    default_pool: str = os.getenv("DEADLINE_DEFAULT_POOL", "none")
    default_group: str = os.getenv("DEADLINE_DEFAULT_GROUP", "none")
    default_priority: int = int(os.getenv("DEADLINE_DEFAULT_PRIORITY", "50"))
    default_chunk_size: int = int(os.getenv("DEADLINE_DEFAULT_CHUNK_SIZE", "1"))
