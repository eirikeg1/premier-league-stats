from abc import ABC, abstractmethod

class DataProcessingManager(ABC):
    """
    Abstract base class for data processing managers.
    
    This class provides a blueprint for data processing managers that can be extended for different API endpoints,
    such as the Fantasy Premier League events endpoint.
    
    This includes some commonly used tools like tokenizers.
    """
    def __init__(self, data, base_tokenizer=None):
        self.raw_data = data
        self.tokenized_data = None
        self.vectorized_data = None
        self.base_tokenizer = base_tokenizer # TODO: Add default tokenizer
    
    @abstractmethod
    def clean_data(self, cleaning_method="default"):
        pass
    
    @abstractmethod
    def tokenize_data(self, tokenization_method="default"):
        pass
    
    @abstractmethod
    def vectorize_data(self, vectorization_method="default"):
        pass
    