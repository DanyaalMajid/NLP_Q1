import streamlit as st
import nltk
from nltk import ngrams
from nltk.tokenize import word_tokenize

nltk.download('punkt')

# Function to generate n-grams
def generate_ngrams(text, n):
    tokens = word_tokenize(text)
    n_grams = list(ngrams(tokens, n))
    return n_grams

# Streamlit app
def main():
    st.title("N-gram Generator")

    # User input for text
    user_text = st.text_area("Enter some text:")

    # Choose n-gram option
    n_gram_options = ["Bigram", "Trigram", "Custom N-gram"]
    selected_option = st.selectbox("Choose N-gram option:", n_gram_options)

    if selected_option == "Bigram":
        n_value = 2
    elif selected_option == "Trigram":
        n_value = 3
    else:
        n_value = st.number_input("Enter the value of N:", min_value=1, step=1)

    # Generate n-grams
    if user_text:
        n_grams = generate_ngrams(user_text, n_value)

        # Display n-grams and their count
        st.header(f"{selected_option} ({n_value}-grams):")
        for i, gram in enumerate(n_grams):
            st.text(f"{i + 1}. {' '.join(gram)}")

        st.info(f"Total {selected_option.lower()}s: {len(n_grams)}")

if __name__ == "__main__":
    main()

