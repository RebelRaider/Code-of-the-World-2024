from llama_cpp import Llama
from loguru import logger

from ml.SETTINGS import LLM_PATH

logger.debug("Init the LLM model")
llm_model = Llama(
    model_path=LLM_PATH,
    n_gpu_layers=-1,
    n_batch=512,
    n_ctx=4096,
    n_parts=1,
)