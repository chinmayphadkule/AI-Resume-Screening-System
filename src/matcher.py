from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_match_score(resume, job_desc):
    embeddings = model.encode([resume, job_desc])
    score = cosine_similarity([embeddings[0]], [embeddings[1]])
    return score[0][0]