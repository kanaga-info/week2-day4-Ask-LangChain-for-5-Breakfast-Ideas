from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Reads OPENAI_API_KEY from your .env file (or from your exported terminal environment variable)
load_dotenv()

# 1. Initialize the model (default temperature lets you observe variation between runs)
llm = ChatOpenAI(model="gpt-4o-mini")

# 2. Define "healthy" clearly and pin the exact output format
prompt = (
    "Give me exactly 5 healthy Indian breakfast ideas that are high in protein and fiber, "
    "minimally processed, and not deep-fried. "
    "Format strictly as a numbered list from 1 to 5, one line per idea, with no preamble, "
    "no descriptions, and no closing text."
)

# 3. Invoke the model
reply = llm.invoke(prompt)

# 4. Print ONLY the text string (try print(reply) once first to see the full AIMessage object!)
print(reply.content)