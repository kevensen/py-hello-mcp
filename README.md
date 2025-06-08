# py-hello-mcp

This is a basic agent to be used with the Google ADK.  It is an example of how to use an agent with a streaming HTTP tool server.

## How to Run

First setup your Python environment in a clean folder

```
python3 -m venv .venv
```
Then install the Google ADK
```
pip install google-adk
```
In the simple folder, create a `.env` file that contains the following
```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=<key>
``` 
The `GOOGLE_API_KEY` can be obtained from the [Google AI Studio](https://aistudio.google.com/apikey).

Then, from the `py-hello-mcp` folder run
```
adk web
```