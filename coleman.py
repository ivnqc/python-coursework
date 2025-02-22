import cs50
import re

def main():
    # Get input text from the user
    text = cs50.get_string("Text: ")

    if text:
        # Calculate the number of letters, sentences, and words
        letter_count = count_letters(text)
        sentence_count = count_sentences(text)
        word_count = count_words(text)

        # Calculate the Coleman-Liau index
        index = calculate_coleman_liau_index(letter_count, sentence_count, word_count)

        # Determine and print the readability grade
        print(get_readability_grade(index))

def count_letters(text):
    """Count the number of letters in the text."""
    return len(re.findall('[a-zA-Z]', text))

def count_sentences(text):
    """Count the number of sentences in the text."""
    return len(re.findall('[.!?]', text))

def count_words(text):
    """Count the number of words in the text."""
    return len(text.split())

def calculate_coleman_liau_index(letter_count, sentence_count, word_count):
    """Calculate the Coleman-Liau Index."""
    L = (letter_count / word_count) * 100  # Average letters per 100 words
    S = (sentence_count / word_count) * 100  # Average sentences per 100 words
    return 0.0588 * L - 0.296 * S - 15.8

def get_readability_grade(index):
    """Determine the readability grade based on the Coleman-Liau Index."""
    if index < 1:
        return "Before Grade 1"
    elif 1 <= index < 16:
        return f"Grade {round(index)}"
    else:
        return "Grade 16+"

if __name__ == "__main__":
    main()
