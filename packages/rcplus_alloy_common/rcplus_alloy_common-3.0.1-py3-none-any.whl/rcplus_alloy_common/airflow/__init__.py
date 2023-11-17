from dataclasses import dataclass, field


@dataclass
class DagRunEventMessage:
    dag_id: str
    dag_run_id: str | None = None
    logical_date: str | None = None
    conf: dict = field(default_factory=dict)
    note: str | None = None
