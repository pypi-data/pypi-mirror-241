import qualtop_llmapi
from qualtop_llmapi.models.loading import load_embedder

from typing import List, Union
from fastapi import APIRouter

from pydantic import BaseModel, Field

### This should follow https://github.com/openai/openai-openapi/blob/master/openapi.yaml

class EmbeddingRequest(BaseModel):
    model: str = Field(
        "mistral-7b-instruct-v0.1.Q4_0.gguf", description="The model to generate an embedding from."
    )
    input: Union[str, List[str], List[int], List[List[int]]] = Field(
        ..., description="Input text to embed, encoded as a string or array of tokens."
    )


class EmbeddingUsage(BaseModel):
    prompt_tokens: int = 0
    total_tokens: int = 0


class Embedding(BaseModel):
    index: int = 0
    object: str = "embedding"
    embedding: List[float]


class EmbeddingResponse(BaseModel):
    object: str = "list"
    model: str
    data: List[Embedding]
    usage: EmbeddingUsage


router = APIRouter(prefix="/embeddings", tags=["Embedding Endpoints"])

def get_embedding(data: EmbeddingRequest) -> EmbeddingResponse:
    """
    Calculates the embedding for the given input using a specified model.

    Args:
        data (EmbeddingRequest): An EmbeddingRequest object containing the input data
        and model name.

    Returns:
        EmbeddingResponse: An EmbeddingResponse object encapsulating the calculated embedding,
        usage info, and the model name. 
        (1536 components for openai models)
        (384 for BERT embeddings)
    """
    embedder = qualtop_llmapi.embedder
    if isinstance(data.input, list):
        embedding_list = []
        for i, txt in enumerate(data.input):
            embedding = embedder.embed_query(txt)
            embedding_list.append(Embedding(index=i, embedding=embedding))
    else:
        embedding = embedder.embed(data.input)
        embedding_list = [Embedding(embedding=embedding)]

    return EmbeddingResponse(
        data=embedding_list, usage=EmbeddingUsage(), model=data.model
    )


@router.post("/", response_model=EmbeddingResponse)
def embeddings(data: EmbeddingRequest):
    """
    Creates an embedder with the specified model
    """
    # LOAD EMBEDDING MODEL
    if not qualtop_llmapi.embedder:
        qualtop_llmapi.embedder = load_embedder(data.model)
        qualtop_llmapi.selected_embedder = data.model
    else:
        if qualtop_llmapi.selected_embedder != data.model:
            del qualtop_llmapi.embedder
            qualtop_llmapi.embedder = load_embedder(data.model)
            qualtop_llmapi.selected_embedder = data.model
    return get_embedding(data)
