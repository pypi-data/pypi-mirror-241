from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-mpnet-base-v2')
model = AutoModel.from_pretrained('sentence-transformers/all-mpnet-base-v2')
import torch
import numpy as np

def get_dense_vector(text):
    data = text.split(' ')
    if len(data)>1:
        inputs = tokenizer(text,padding=True, truncation=True, return_tensors="pt")
        with torch.no_grad():
            outputs = model(**inputs)
            embeddings = outputs.last_hidden_state
        dense_vector = torch.mean(embeddings, dim=1)
        dense_vector = dense_vector.tolist()
        dense_vector = dense_vector[0]
        return dense_vector
    else:
        if len(data[0]) > 1:
            inputs = tokenizer(text,padding=True, truncation=True, return_tensors="pt")
            with torch.no_grad():
                outputs = model(**inputs)
                embeddings = outputs.last_hidden_state
            dense_vector = torch.mean(embeddings, dim=1)
            dense_vector = dense_vector.tolist()
            dense_vector = dense_vector[0]
            return dense_vector
        else:
            num_dimensions = 768
            default_value = 1e-10
            dense_vector = np.full(num_dimensions, default_value)
            dense_vector = dense_vector.tolist()
            return dense_vector