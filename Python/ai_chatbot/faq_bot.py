"""Simple FAQ chatbot using TF-IDF similarity."""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


faq_pairs = [
("How do I reset my password?", "To reset your password, go to /reset and follow instructions."),
("What are your hours?", "We operate 9am-6pm Monday to Friday."),
("How to contact support?", "Email support@example.com or call +1-555-000.")
]


questions = [q for q, a in faq_pairs]
answers = [a for q, a in faq_pairs]


vec = TfidfVectorizer().fit_transform(questions)




def answer(question):
qv = TfidfVectorizer().fit(questions).transform([question])
# Use the original vectorizer for fair comparison
qv = vec.transform([question]) if hasattr(vec, 'shape') else vec
sims = linear_kernel(qv, vec).flatten()
idx = sims.argmax()
return answers[idx], sims[idx]




if __name__ == '__main__':
print('FAQ bot (type "exit" to quit)')
while True:
q = input('\nYou: ')
if q.strip().lower() in ('exit', 'quit'):
break
ans, score = answer(q)
print(f'Bot (score {score:.2f}): {ans}')
