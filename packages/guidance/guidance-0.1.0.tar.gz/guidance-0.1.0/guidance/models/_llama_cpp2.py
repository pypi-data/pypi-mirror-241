import os
from pathlib import Path
import multiprocessing
from itertools import takewhile
import operator

import numpy as np

from ._model import Chat
from ._local import Local

try:
    # TODO: can we eliminate the torch requirement for llama.cpp by using numpy in the caller instead?
    import torch
    is_torch = True
except ImportError:
    is_torch = False

try:
    import llama_cpp
    is_llama_cpp = True
except ImportError:
    is_llama_cpp = False

class LlamaCpp2(Local):
    def __init__(self, model=None, tokenizer=None, echo=True, caching=True, temperature=0.0, **kwargs):
        if not is_torch:
            raise Exception("Please install PyTorch in order to use guidance.models.LlamaCpp!")

        if not is_llama_cpp:
            raise Exception("Please install llama-cpp-python with `pip install llama-cpp-python` in order to use guidance.models.LlamaCpp!")

        if isinstance(model, Path):
            model = str(model)
        if model is None or isinstance(model, str) and len(model.strip()) == 0:
            model = os.environ.get("LLAMA_CPP_MODEL", "")
            if len(model.strip()) == 0:
                try:
                    with open(os.path.expanduser('~/.llama_cpp_model'), 'r') as file:
                        model = file.read().replace('\n', '')
                except:
                    pass
                if len(model.strip()) == 0:
                    raise ValueError("If model is None then a model file must be specified in either the LLAMA_CPP_MODEL environment variable or in the ~/.llama_cpp_model file.")

        if isinstance(model, str):
            self.model = model
            if "n_threads" not in kwargs:
                kwargs["n_threads"] = multiprocessing.cpu_count()
            self.model_obj = llama_cpp.Llama(model_path=model, **kwargs)
        elif isinstance(model, llama_cpp.Llama):
            self.model = model.__class__.__name__
            self.model_obj = model
        else:
            raise TypeError("model must be None, a file path string, or a llama_cpp.Llama object.")

        if tokenizer is None:
            tokenizer = llama_cpp.LlamaTokenizer(self.model_obj)
        elif not isinstance(tokenizer, llama_cpp.LlamaTokenizer):
            raise TypeError("tokenizer must be None or a llama_cpp.LlamaTokenizer object.")
        self._orig_tokenizer = tokenizer

        #self._n_threads = multiprocessing.cpu_count()
        self._n_vocab = tokenizer.llama.n_vocab()
        self.caching = caching
        self.temperature = temperature

        super().__init__(
            [bytes(tokenizer.decode([i]), encoding="utf8") for i in range(self._n_vocab)],
            tokenizer.llama.token_bos(),
            tokenizer.llama.token_eos(),
            echo=echo
        )

        self._cache_state["cache_token_ids"] = []

    def _get_logits(self, token_ids):
        '''Computes the logits for the given token state.
        
        This overrides a method from the LocalEngine class that is used to get
        inference results from the model.
        '''

        if len(token_ids) == 0:
            raise ValueError("token_ids must contain some tokens.")

        cache_token_ids = self._cache_state["cache_token_ids"]
        num_cached = sum(takewhile(operator.truth, map(operator.eq, token_ids, cache_token_ids)))
        if num_cached == len(token_ids):
            if num_cached == len(cache_token_ids):
                return self._cache_state["logits"]
            # llama_cpp doesn't like it when we pass in 0 new tokens, so re-input one
            num_cached = num_cached - 1 
        self._cache_state["cache_token_ids"] = token_ids.copy()
        token_ids = np.array(token_ids[num_cached:], dtype=np.int32)
        token_ids = (llama_cpp.llama_token * len(token_ids))(*token_ids)
        llama_cpp.llama_eval(self.model_obj.ctx, token_ids, len(token_ids), num_cached)#, self._n_threads)
        logits = llama_cpp.llama_get_logits(self.model_obj.ctx)
        logits = np.ctypeslib.as_array(logits, shape=(self._n_vocab,))
        logits = torch.from_numpy(logits)
        self._cache_state["logits"] = logits
        return logits
    
class LlamaCppChat(LlamaCpp, Chat):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
