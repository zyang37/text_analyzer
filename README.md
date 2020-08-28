# text_analyzer

## Goal
Develop a program that returns a abstractive summarization for given text, and ables to answer related questions
Purpose: Get familiar with Language modeling tools such as Huggingface, etc.

- Docker container
- Use Huggingface
- Test
- Develop functions
- May develope a UI


## Requirement
- PyQt5
- Transformer (Huggingface)

## Usage
    python3 text_analyzer3-1.py
- copy and paste text
- adjust length of the summary
- get a summary
- type in a question
- get the answer and a confidence score


## User Interface
<img src="samples/UI1.png" width="75%">

<img src="samples/UI2.png" width="75%">

## Future Work
- The program starts download OR update the correspond models, when clicking the "Summarize" and "Answer" buttons for the first time. This process is slow. The inference time is acceptable.

- Better UI design

- Embed with other NLP models
