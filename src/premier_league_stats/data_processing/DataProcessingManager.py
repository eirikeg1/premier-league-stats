class DataProcessingManager:
    def __init__(self, data):
        self.raw_data = data
        self.tokenized_data = None
        self.vectorized_data = None
    
    def clean_data(self, cleaning_method="default"):
        pass
    
    def tokenize_data(self, tokenization_method="default"):
        pass
    
    def vectorize_data(self, vectorization_method="default"):
        pass
    