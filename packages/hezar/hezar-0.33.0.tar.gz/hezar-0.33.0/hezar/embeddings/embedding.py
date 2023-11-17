import os
import tempfile
from typing import Dict, List, Union

from huggingface_hub import HfApi, hf_hub_download

from ..builders import build_embedding
from ..configs import EmbeddingConfig
from ..constants import (
    DEFAULT_EMBEDDING_CONFIG_FILE,
    DEFAULT_EMBEDDING_FILE,
    DEFAULT_EMBEDDING_SUBFOLDER,
    HEZAR_CACHE_DIR,
    Backends,
)
from ..utils import Logger, get_lib_version, verify_dependencies


logger = Logger(__name__)

# The below code is a workaround. Gensim's models have this limitation that the models can only be loaded using the same
# gensim & numpy version they were saved with.
REQUIRED_GENSIM_VERSION = "4.3.2"
REQUIRED_NUMPY_VERSION = "1.24"


# Check if the right combo of gensim/numpy versions are installed
def _verify_gensim_installation():
    if (
        not get_lib_version("numpy").startswith(REQUIRED_NUMPY_VERSION)
        or not get_lib_version("gensim").startswith(REQUIRED_GENSIM_VERSION)
    ):
        raise ImportError(
            f"The required Gensim version for this version of Hezar is currently {REQUIRED_GENSIM_VERSION} "
            f"and the required Numpy version for Gensim=={REQUIRED_GENSIM_VERSION} is {REQUIRED_NUMPY_VERSION}"
        )


class Embedding:
    """
    Base class for all embeddings.
    """

    required_backends: List[Union[str, Backends]] = []

    filename = DEFAULT_EMBEDDING_FILE
    vectors_filename = f"{filename}.wv.vectors.npy"
    config_filename = DEFAULT_EMBEDDING_CONFIG_FILE
    subfolder = DEFAULT_EMBEDDING_SUBFOLDER

    def __init__(self, config: EmbeddingConfig, embedding_file: str = None, vectors_file: str = None, **kwargs):
        verify_dependencies(self, self.required_backends)  # Check if all the required dependencies are installed
        _verify_gensim_installation()

        self.config = config.update(kwargs)
        self.model = self.from_file(embedding_file, vectors_file) if embedding_file else self.build()

    def build(self):
        raise NotImplementedError

    def from_file(self, embedding_path, vectors_path):
        raise NotImplementedError

    def __call__(self, inputs: Union[str, List[str]], **kwargs):
        if isinstance(inputs, str):
            inputs = [inputs]
        vectors = [self.word_vectors[w] for w in inputs]
        return vectors

    def train(
        self,
        dataset,
        epochs,
    ):
        raise NotImplementedError

    def word2index(self, word):
        return self.vocab.get(word, -1)

    def index2word(self, index):
        keyed_vocab = {v: k for k, v in self.vocab.items()}
        return keyed_vocab[index]

    def similarity(self, word1: str, word2: str):
        raise NotImplementedError

    def doesnt_match(self, words: List[str]):
        raise NotImplementedError

    def most_similar(self, word: str, top_n: int = 5):
        raise NotImplementedError

    def get_normed_vectors(self):
        raise NotImplementedError

    @classmethod
    def load(
        cls,
        hub_or_local_path,
        config_filename=None,
        embedding_file=None,
        vectors_file=None,
        subfolder=None,
        **kwargs,
    ) -> "Embedding":
        config_filename = config_filename or cls.config_filename
        embedding_file = embedding_file or cls.filename
        vectors_file = vectors_file or cls.vectors_filename
        subfolder = subfolder or cls.subfolder

        config = EmbeddingConfig.load(hub_or_local_path, filename=config_filename, subfolder=subfolder)

        if os.path.isdir(hub_or_local_path):
            embedding_path = os.path.join(hub_or_local_path, subfolder, embedding_file)
            vectors_path = os.path.join(hub_or_local_path, subfolder, vectors_file)
        else:
            embedding_path = hf_hub_download(
                hub_or_local_path,
                filename=embedding_file,
                subfolder=subfolder,
                cache_dir=HEZAR_CACHE_DIR,
                resume_download=True,
            )
            vectors_path = hf_hub_download(
                hub_or_local_path,
                filename=vectors_file,
                subfolder=subfolder,
                cache_dir=HEZAR_CACHE_DIR,
                resume_download=True,
            )

        embedding = build_embedding(
            config.name,
            config=config,
            embedding_file=embedding_path,
            vectors_file=vectors_path,
            **kwargs,
        )

        return embedding

    def save(
        self,
        path: Union[str, os.PathLike],
        filename: str = None,
        subfolder: str = None,
        save_config: bool = True,
        config_filename: str = None,
    ):
        raise NotImplementedError

    def push_to_hub(
        self,
        repo_id,
        commit_message=None,
        subfolder=None,
        filename=None,
        vectors_filename=None,
        config_filename=None,
        private=False,
    ):
        subfolder = subfolder or self.subfolder
        filename = filename or self.filename
        vectors_filename = vectors_filename or self.vectors_filename
        config_filename = config_filename or self.config_filename

        api = HfApi()
        # create remote repo
        api.create_repo(repo_id, exist_ok=True)
        # save to tmp and prepare for push
        cache_path = tempfile.mkdtemp()
        # save embedding model file
        embedding_save_dir = os.path.join(cache_path)
        os.makedirs(embedding_save_dir, exist_ok=True)

        if commit_message is None:
            commit_message = "Hezar: Upload embedding and config"

        self.save(embedding_save_dir, filename, subfolder=subfolder, save_config=False)

        self.config.push_to_hub(
            repo_id,
            config_filename,
            subfolder=subfolder,
            repo_type="model",
            private=private,
            commit_message=commit_message,
        )

        api.upload_file(
            repo_id=repo_id,
            path_or_fileobj=os.path.join(embedding_save_dir, subfolder, filename),
            repo_type="model",
            path_in_repo=f"{subfolder}/{filename}",
            commit_message=commit_message,
        )
        logger.log_upload_success(
            name=f"{self.__class__.__name__}(name={self.config.name})",
            target_path=f"{os.path.join(repo_id, subfolder, filename)}",
        )

        api.upload_file(
            repo_id=repo_id,
            path_or_fileobj=os.path.join(embedding_save_dir, subfolder, vectors_filename),
            repo_type="model",
            path_in_repo=f"{subfolder}/{vectors_filename}",
            commit_message=commit_message,
        )
        logger.log_upload_success(
            name=f"`{self.__class__.__name__}(name={self.config.name})`",
            target_path=f"`{os.path.join(repo_id, subfolder, vectors_filename)}`",
        )

    def torch_embedding(self):
        import torch

        weights = torch.FloatTensor(self.vectors)
        embedding_layer = torch.nn.Embedding.from_pretrained(weights)
        return embedding_layer

    @property
    def word_vectors(self):
        """
        Get key:value pairs of word:vector
        """
        raise NotImplementedError

    @property
    def vectors(self):
        """
        Get the all vectors array/tensor
        """
        raise NotImplementedError

    @property
    def vocab(self) -> Dict[str, int]:
        raise NotImplementedError
