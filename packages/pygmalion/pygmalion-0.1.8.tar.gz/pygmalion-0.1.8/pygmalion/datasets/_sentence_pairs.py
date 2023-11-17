import pathlib
from pygmalion.utilities._download import download


def sentence_pairs(directory: str):
    """
    downloads the modified en-fr 'Tatoeba' dataset from OPUS
    in the given directory
    """
    download(pathlib.Path(directory) / "sentence_pairs.csv.gz",
             "https://drive.google.com/file/d/1RmBm7qwTn-UlSsaWM-6K8eXk8QnZVC5x/view?usp=share_link")
