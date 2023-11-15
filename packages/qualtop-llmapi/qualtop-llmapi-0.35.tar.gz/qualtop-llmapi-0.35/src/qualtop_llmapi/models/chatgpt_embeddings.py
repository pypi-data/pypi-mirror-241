# -*- coding:utf-8 -*-
import os
import openai
import pickle
import tiktoken

import qualtop_llmapi

from gpt4all import Embed4All

from datetime import datetime

import argparse

from scipy import spatial

import pandas as pd

# models
EMBEDDING_MODEL = "text-embedding-ada-002"
GPT_MODEL = "gpt-3.5-turbo"
BATCH_SIZE = 1000  # you can submit up to 2048 embedding inputs per request

# search function
def strings_ranked_by_relatedness(query, 
                                  df, 
                                  relatedness_fn=lambda x, y: 1 - spatial.distance.cosine(x, y),
                                  top_n=100):
    """Returns a list of strings and relatednesses, sorted from most related to least."""

    query_embedding = Embed4All().embed(query)
    strings_and_relatednesses = [
        (row["text"], relatedness_fn(query_embedding, row["embedding"]))
        for i, row in df.iterrows()
    ]
    strings_and_relatednesses.sort(key=lambda x: x[1], reverse=True)
    strings, relatednesses = zip(*strings_and_relatednesses)
    return strings[:top_n], relatednesses[:top_n]

def num_tokens(text, model):
    """Return the number of tokens in a string."""
    if "llama" in model or "mistral" in model:
        encoding = tiktoken.get_encoding("gpt2")
    else:
        encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))

def create_message_with_context(query, df, model, token_budget, prompt):
    """Return a message for GPT, with relevant source texts pulled from a dataframe."""

    if "llama" in model or "mistral" in model:
        token_budget_error = 100
    else:
        token_budget_error = 0
    strings, relatednesses = strings_ranked_by_relatedness(query, df)
    selected_articles = []
    for string in strings:
        new_article = f'{string}'
        possible_prompt = prompt.format(
                context="\n".join(selected_articles + [new_article]), 
                question=query
                )
        total_tokens = num_tokens(possible_prompt, 
                                  model=model)
        total_tokens += token_budget_error
        if total_tokens > token_budget:
            break
        else:
            selected_articles.append(new_article)
    final_prompt = prompt.format(
            context="\n".join(selected_articles), 
            question=query
            )
    return final_prompt 
