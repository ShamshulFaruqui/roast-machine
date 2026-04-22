import os
from dotenv import load_dotenv
load_dotenv()

# LangSmith tracing
os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2", "true")
os.environ["LANGCHAIN_ENDPOINT"] = os.getenv("LANGCHAIN_ENDPOINT", "https://api.smith.langchain.com")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY", "")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT", "RoastMachine")

import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from rag import build_roast_knowledge_base, get_roast_context
from guardrails import check_input, check_roast_output


load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)

vectorstore = build_roast_knowledge_base()

def roast_text(user_input: str, chat_history: list) -> str:
    input_check = check_input(user_input)
    if not input_check["safe"]:
        return input_check["message"]

    context = get_roast_context(user_input, vectorstore)

    history_str = "\n".join([
        f"User: {msg['user']}\nAI: {msg['ai']}"
        for msg in chat_history[-3:]
    ])

    prompt = ChatPromptTemplate.from_template("""
You are a witty, savage roast comedian. Your job is to roast the user 
based on what they tell you about themselves.

Use these comedic principles to guide your roast:
{context}

Previous exchanges (use these for callbacks):
{history}

Roast this person based on: {input}

Rules:
- Be clever and specific, not generic
- Maximum 3 sentences
- End with a mic drop one-liner
- Never attack protected characteristics
- Stay funny, not cruel
""")

    chain = prompt | llm | StrOutputParser()
    roast = chain.invoke({
        "context": context,
        "history": history_str,
        "input": user_input
    })

    output_check = check_roast_output(roast)
    if not output_check["safe"]:
        return output_check["message"]

    return roast

def roast_image(image_description: str) -> str:
    input_check = check_input(image_description)
    if not input_check["safe"]:
        return input_check["message"]

    context = get_roast_context(image_description, vectorstore)

    prompt = ChatPromptTemplate.from_template("""
You are a witty roast comedian. Roast the person based on this 
image description:

Comedic principles:
{context}

Image description: {input}

Rules:
- Be clever and specific
- Maximum 3 sentences
- End with a mic drop one-liner
- Never attack protected characteristics
""")

    chain = prompt | llm | StrOutputParser()
    roast = chain.invoke({"context": context, "input": image_description})

    output_check = check_roast_output(roast)
    if not output_check["safe"]:
        return output_check["message"]

    return roast