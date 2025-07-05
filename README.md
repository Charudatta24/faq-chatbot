# AI Chatbot for FAQs
A smart, visually appealing chatbot that answers Frequently Asked Questions (FAQs) using Google's Gemini 2.0 Flash model and Streamlit. This project combines the power of generative AI with a sleek UI to deliver fast, accurate responses in real time.
##  Project Overview

This chatbot allows users to input any frequently asked question, processes it through Gemini 2.0 Flash, and responds with a natural-language answer. It features:

-  Gemini 2.0 Flash API integration
-  Animated and modern user interface (Streamlit)
-  Real-time response generation
-  Modular code with separate logic and UI files
  ##  Demo UI Features

- Gradient background with animated title
- Personalized developer tag
- Typing animation for chatbot header
- Loader animation while the answer is being generated
- Custom-styled buttons and layout

## 📁 File Structure

├── app.py               # Main Streamlit application
├── ai_generator.py      # Contains Gemini API call logic
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation

Install dependencies

pip install -r requirements.txt

Run the app

streamlit run app.py

 How It Works
User Input: The user enters a question in the text box.
API Call: The question is sent to get_gemini_response() which connects to the Gemini model.
Response Generation: The model generates a natural-language answer.
UI Display: The response is shown in an animated, styled interface.
 Screenshots
 ![image](https://github.com/user-attachments/assets/4f61f4ee-ae84-4338-ba7f-a65d219ae34e)

 Author
 Pesala Govinda Charu Datta
