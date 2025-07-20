# Django Ollama Chat App

This Django project showcases the power of building local AI-powered chat applications using the Ollama library and Meta's Llama 3 model 

[Accompanying post with additional info here](https://scoutapm.com/blog/building-ai-with-ollama-and-django)

**Key Features**

* **Local AI :**  Leverages Ollama to run the Llama 3 model locally
* **Django Framework:** Built on the Django web framework
* **Real-time Streaming:**  Chat interface displays AI responses as they are generated
* **Open Source:**  Fully open-source code, allowing you to explore, modify, and extend the project to your liking

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/scoutapp/ollama-django
   cd ollama-django

2. **Install Dependencies:**
   ```bash
   chmod +x install.sh
   ./install.sh

3. **Run Ollama Chat:**
   ```bash
   chmod +x run.sh
   ./run.sh
   ```
   > use --install flag will check and install dependencies (if needed) before running

**Chat Away:** Open your browser and visit http://localhost:8000/ or http://localhost:8000/chat/ to start chatting with your AI

[//]: # (**Project Structure**)
[//]: # (chat/: Contains the Django app for the chat interface and Ollama interaction.)
[//]: # (templates/: HTML template for the chat interface.)
[//]: # (requirements.txt: Lists the project dependencies.)

**Future Enhancements**

Frontend refactoring: frontend written by a backend dev + ChatGPT. \
Reduced Latency: Optimization techniques to minimize response delays. \
Multimodal AI: Exploration of combining text with images and audio. 

[//]: # (Additional Models: Integration of other Ollama-supported models.)

**Contributing**

Contributions are welcome! Feel free to open issues, submit pull requests, or share your feedback to help improve this project.

**Acknowledgements**

[Ollama](https://ollama.com/download): For providing a powerful library for local AI model execution.

[Django](https://www.djangoproject.com): For the excellent web development framework.

[//]: # ([Llama 3]&#40;https://llama.meta.com/llama3&#41;: The open-source AI model that powers this chat app.)
