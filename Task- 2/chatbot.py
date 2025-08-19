import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from preprocess import preprocess

class FAQChatbot:
    def __init__(self, faq_file: str):
        # Load FAQs
        with open(faq_file, "r") as f:
            self.faqs = json.load(f)

        # Store questions & answers
        self.questions = list(self.faqs.keys())
        self.answers = list(self.faqs.values())

        # Preprocess all questions
        processed_questions = [preprocess(q) for q in self.questions]

        # Build vectorizer
        self.vectorizer = TfidfVectorizer()
        self.vectors = self.vectorizer.fit_transform(processed_questions)

    def get_answer(self, user_input: str) -> str:
        """
        Return the best matching FAQ answer.
        """
        user_processed = preprocess(user_input)
        user_vector = self.vectorizer.transform([user_processed])
        similarity = cosine_similarity(user_vector, self.vectors)
        best_match_idx = similarity.argmax()
        return self.answers[best_match_idx]
