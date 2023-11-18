import os

import logging
import time
from typing import Dict, List

import pandas as pd

from fastapi import APIRouter, Depends, Response, Security, status
from pydantic import BaseModel, Field

from langchain.prompts import ChatPromptTemplate
from langchain.schema.messages import SystemMessage, HumanMessage, AIMessage

import qualtop_llmapi
import qualtop_llmapi.models.loading as loading
import qualtop_llmapi.models.single_prompt as single_prompt
import qualtop_llmapi.models.rag as rag
import qualtop_llmapi.models.rag_sql as rag_sql
from qualtop_llmapi.models.chatgpt_embeddings import num_tokens

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

### This should follow https://github.com/openai/openai-openapi/blob/master/openapi.yaml
class ChatCompletionMessage(BaseModel):
    role: str
    content: str


class ChatCompletionRequest(BaseModel):
    model: str = Field(..., description='The model to generate a completion from.')
    messages: List[ChatCompletionMessage] = Field(..., description='The model to generate a completion from.')


class ChatCompletionChoice(BaseModel):
    message: ChatCompletionMessage
    index: int
    finish_reason: str


class ChatCompletionUsage(BaseModel):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class ChatCompletionResponse(BaseModel):
    id: str
    object: str = 'text_completion'
    created: int
    model: str
    choices: List[ChatCompletionChoice]
    usage: ChatCompletionUsage


router = APIRouter(prefix="/chat", tags=["Completions Endpoints"])

# Message formatting for LangChain
def format_messages(messages):
    formatted_messages = []
    for message in messages:
        formatted_messages.append((message['role'], message["content"]))
    formatted_messages.append(("assistant", ""))
    return ChatPromptTemplate.from_messages(formatted_messages)

@router.post("/completions", response_model=ChatCompletionResponse)
async def chat_completion(request: ChatCompletionRequest):
    '''
    Completes a LLM model response.
    '''
    req_dict = request.dict()
    messages = req_dict["messages"]
    formatted_messages = format_messages(messages)
    model_name = req_dict["model"]

    # Load model
    if not qualtop_llmapi.llm:
        try:
            qualtop_llmapi.llm = loading.load_model(model_name)
            qualtop_llmapi.selected_model = model_name
        except FileNotFoundError as e:
            qualtop_llmapi.llm = loading.load_model("mistral-7b")
            qualtop_llmapi.selected_model = "mistral-7b"
    elif qualtop_llmapi.selected_model != model_name:
        del qualtop_llmapi.llm 
        try:
            qualtop_llmapi.llm = loading.load_model(model_name)
            qualtop_llmapi.selected_model = model_name
        except FileNotFoundError as e:
            qualtop_llmapi.llm = loading.load_model("mistral-7b")
            qualtop_llmapi.selected_model = "mistral-7b"
    
    try:
        if "single" in model_name:
            answer = rag.ask(messages, 
                             qualtop_llmapi.llm,
                             "single")
        elif "collection" in model_name:
            answer = rag.ask(messages, qualtop_llmapi.llm, "collection")
        elif "code" in model_name:
            answer = single_prompt.ask_manual(messages, 
                                              qualtop_llmapi.llm)
        elif "gentera" in model_name:
            answer = rag_sql.ask(messages, 
                                 qualtop_llmapi.llm)
        else:
            answer = single_prompt.ask_manual(messages, 
                                              qualtop_llmapi.llm)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, 
                            detail="Model not found.")

    choices = [ChatCompletionChoice(message=ChatCompletionMessage(role="assistant",
                                                                  content=answer),
                                    index=0,
                                    finish_reason="stop")]
   
    # Get measures
    # TODO: RETURN THIS IN RESPONSE OF THE MODEL
    prompt_tokens = 0
    completion_tokens = 0
    total_tokens = prompt_tokens + completion_tokens

    return ChatCompletionResponse(
        id="chatcmpl-abc123",
        object="chat.completion",
        created=int(time.time()),
        model=request.model,
        choices=choices,
        usage={'prompt_tokens': prompt_tokens, 
               'completion_tokens': completion_tokens, 
               'total_tokens': total_tokens},
    )
