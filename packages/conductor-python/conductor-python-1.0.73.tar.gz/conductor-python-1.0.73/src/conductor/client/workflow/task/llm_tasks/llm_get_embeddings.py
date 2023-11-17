from conductor.client.workflow.task.task import TaskInterface
from conductor.client.workflow.task.task_type import TaskType
from typing import Any, Dict, List
from typing_extensions import Self


class LlmGetEmbeddings(TaskInterface):
    def __init__(self, task_name: str, task_ref_name: str, vector_db: str, namespace: str, index: str, embeddings: List[int]) -> Self:
        super().__init__(
            task_name=task_name,
            task_reference_name=task_ref_name,
            task_type=TaskType.LLM_GET_EMBEDDINGS,
            input_parameters={
                "vectorDB": vector_db,
                "namespace": namespace,
                "index": index,
                "embeddings": embeddings
            }
        )
