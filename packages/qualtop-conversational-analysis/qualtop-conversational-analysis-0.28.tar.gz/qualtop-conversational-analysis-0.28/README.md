# Conversational analysis based on communication with the OpenAI API (regardless of the API Base)

Implementation of several methods for communication with the OpenAI API, embedding-based retrieval and data preparation

## Getting Started

Can be installed directly with pip (a `setup.py` file is provided, if needed).

Notably the module contains the `ChatGPTMemory` class, which enables communication with the OpenAI API (through the ChatCompletion endpoint) while managing conversation memory.

### Data preparation modules

This project was not originally intended for production. A lot of the scripts contained here are mainly for data preparation (to demonstrate different use cases). However, some functions are being used by both the [qualtop-llmapi](https://github.com/QOPA-LLM/qualtop-llmapi) and the QOPA-LLM [demo](https://github.com/QOPA-LLM/qualtop_llm_frontend) sides of the project.

In the future, this module should be replaced by a communication module. Also, any existent calculation functions should be passed to the server.
