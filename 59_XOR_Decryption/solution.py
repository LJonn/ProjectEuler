import itertools
import string


def is_chart_ascii(value):
    return ord(value) < 128


common_english_words = ["the", "be", "and", "of", "a", "in", "to", "have",
                        "it", "I", "that", "for", "you", "he", "with", "on",
                        "do", "say", "this", "they", "at", "but", "we", "his",
                        "from", "not", "by", "she", "or", "as", "what", "go",
                        "their", "can", "who", "get", "if", "would", "her",
                        "all", "my", "make", "about", "know", "will", "as",
                        "up", "one", "time", "has", "been", "there", "year",
                        "so", "think", "when", "which", "them", "some", "me",
                        "people", "take", "out", "into", "just", "see", "him",
                        "your", "come", "could", "now", "than", "like", "other",
                        "how", "then", "its", "our", "two", "more", "these",
                        "want", "way", "look", "first", "also", "new",
                        "because", "day", "use", "no", "man", "find", "here",
                        "thing", "give", "many", "well", "only", "those",
                        "tell", "very", "even", "back", "any", "good", "woman",
                        "through", "us", "life", "child", "there", "work",
                        "down", "may", "after", "should", "call", "world",
                        "over", "school", "still", "try", "last", "ask",
                        "need", "too", "feel", "three", "state", "never", "become",
                        "between", "high", "really", "something", "most", "another",
                        "much", "family", "leave", "put", "old", "while", "mean", "keep",
                        "student", "why", "let", "great", "same", "big", "group", "begin",
                        "seem", "country", "help", "talk", "where", "turn", "problem", "every",
                        "start", "hand", "might", "American", "show", "part", "about", "against",
                        "place", "over", "such", "again", "case", "run", "however", "believe",
                        "own", "buy", "plan", "believe", "provide", "stand", "oh", "cost", "help",
                        "lose", "send", "most", "provide", "serve", "begin", "fall", "follow",
                        "left", "local", "mean", "meet", "present", "seem", "talk", "teach",
                        "tell", "work", "call", "ask", "believe", "break", "bring", "buy",
                        "change", "come", "cut", "do", "fall", "get", "give", "go", "hold",
                        "keep", "know", "lead", "leave", "let", "lie", "like", "live", "look",
                        "make", "play", "put", "read", "run", "say", "see", "seem", "set", "show",
                        "sit", "stand", "take", "talk", "tell", "think", "try", "turn", "use",
                        "want", "work", "ask", "be", "become", "begin", "call", "come", "could",
                        "do", "feel", "find", "get", "give", "go", "have", "hear", "help", "keep",
                        "know", "leave", "like", "live", "look", "make", "may", "mean", "might",
                        "move", "need", "play", "put", "run", "say", "see", "seem", "should",
                        "show", "start", "take", "talk", "tell", "think", "try", "turn", "use",
                        "want", "will", "work"]


with open("./cipher.txt", 'r') as file:
    secret_bytes = file.read()
secret_bytes = [int(num) for num in secret_bytes.split(",")]

alphabet_lowercase = string.ascii_lowercase
permutations_of_alphabet = itertools.permutations(alphabet_lowercase, 3)

answer = dict()

for secret_guess in permutations_of_alphabet:
    contains_english = 0
    decrypted = ""
    for i, secret_byte in enumerate(secret_bytes):
        letter = chr(secret_byte ^ ord(secret_guess[i % 3]))
        decrypted += letter
        if letter == " ":
            if decrypted.split()[-1] in common_english_words:
                contains_english += 1
    if contains_english > 10:
        answer[contains_english] = [secret_guess, decrypted]

ascii_sum = 0
max_key = max(answer, key=lambda k: int(k))
for letter in answer[max_key][1]:
    ascii_sum += ord(letter)
print(ascii_sum, answer[max_key][0], answer[max_key][0])
