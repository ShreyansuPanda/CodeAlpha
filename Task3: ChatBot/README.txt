# CodeAlpha Task 3: AI ChatBot Using Google Gemini

This project is a simple AI chatbot using the Google Gemini API. It is capable of understanding and responding to user queries about the weather, time, or other topics. The chatbot, named Phoenix, interacts with users through both text and voice input.

##Video Tutorial: https://www.linkedin.com/posts/shreyansu-panda-5a9854276_ai-chatbot-geminiapi-activity-7164166780939067392-ths-?utm_source=share&utm_medium=member_desktop

## Features

- **AI Conversations**: Uses Google Gemini to generate AI-based responses to user queries.
- **Weather Information**: Provides real-time weather updates for a specified city using the Yahoo Weather API.
- **IP Address Lookup**: Retrieves the IP address of a given host.
- **Voice Recognition**: Supports speech-to-text functionality to allow users to interact with the bot via voice commands.
- **Function Calling**: Dynamically calls functions based on user requests, such as fetching weather details or IP addresses.

## Tools Used

- **Python 3.x**: Primary programming language for development.
- **Flask**: Web framework used for the backend server.
- **Google Gemini API**: Powers the AI chatbot's conversation capabilities.
- **SpeechRecognition**: Python library for voice recognition.
- **Yahoo Weather API**: Provides weather information.
- **Requests**: Python library used to make HTTP requests to APIs.

## Requirements

- Python 3.x
- Flask
- requests
- SpeechRecognition
- Google Gemini API Key
- Yahoo Weather API Key

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/ai-chatbot-google-gemini.git
    ```
   
2. **Navigate to the project directory**:
    ```bash
    cd ai-chatbot-google-gemini
    ```

3. **Install required packages**:
    ```bash
    pip install Flask requests SpeechRecognition
    ```

4. **Set up API keys**:
    - Obtain a Google Gemini API key and a Yahoo Weather API key.
    - Add these keys to the `config.py` file in the project directory.

## Usage

1. **Run the Flask application**:
    ```bash
    python Flask.py
    ```
   
2. **Access the application**:
   - Open your web browser and navigate to `http://localhost:5000`.
   - Use the input field to type queries, or speak directly if using the voice input option.

3. **Available functionalities**:
   - **Text Input**: Enter queries such as "What's the weather in New York?" or "Find the IP address of google.com."
   - **Voice Input**: Choose to speak your question for the bot to respond.

## Project Structure

AI ChatBot Using Google Gemini/
│
├── Flask.py # Flask server handling requests and routing
├── PhoneixAi.py # Main chatbot logic using Google Gemini API
├── agent.py # Handles conversation flow and function calls
├── mic_text.py # Voice recognition logic
├── temp_city.py # Functions for weather and IP lookups
├── config.py # Contains API keys and configuration
└── README.md # Project documentation


## Functions

### Flask.py
- **process_message_func1**: Receives user messages and returns responses from the chatbot.
- **index**: Renders the main HTML template for the web interface.

### PhoneixAi.py
- **Talk_with_ai**: Interacts with Google Gemini to process user input and generate responses.

### agent.py
- **run_conversation**: Manages the conversation flow, including making function calls based on user requests.

### mic_text.py
- **mic1**: Captures and processes voice input from the user.

### temp_city.py
- **temp_city**: Fetches and returns weather details for a specified city.
- **get_ip**: Retrieves the IP address of a specified host.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to submit a pull request.

## License

This project is licensed under the MIT License.


