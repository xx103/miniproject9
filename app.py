import streamlit as st
from transformers import pipeline

# Initialize the model
generator = pipeline('text-generation', model='gpt2')

# Streamlit app
def main():
    # App title and introduction
    st.title('GPT-2 Chatbot')
    st.write('This chatbot uses the GPT-2 model from Hugging Face to generate responses.')

    # User input
    user_input = st.text_input('Say something to the chatbot:')

    # Generate response when there's user input
    if user_input:
        with st.spinner('Thinking...'):
            responses = generator(user_input, max_length=50)
            response = responses[0]['generated_text']
        st.write(response)

    # Footer
    st.caption('Created with Streamlit and Hugging Face Transformers')

# Run the app
if __name__ == '__main__':
    main()
