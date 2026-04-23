# Hi Dadi(grandma in Urdu), 
So I made an app that roasts you, basically it makes fun of you in a funny way, like a comedian would.
You can either describe yourself in text or upload a photo, and it will come up with a clever roast based on what it sees. You can even fire back and keep the roast battle going.
The AI doesn't just randomly insult you though. Before it replies, it checks a little knowledge base I built with tips on how to actually be funny, things like 'a good roast always has a kernel of truth' and 'be specific, not generic.' That way it stays clever instead of just being mean. 
I also added a safety layer so if anyone tries to trick it or say something harmful, it gets blocked before it even reaches the AI.
Here's what I used to build it:
Groq - the AI that writes the roasts and looks at your photos.
LangChain - connects all the pieces together.
Chroma - stores the comedy tips the AI reads before roasting you.
LangSmith - lets me monitor every AI call in real time, like a security camera for the app.
Streamlit - the actual website you open and click on.
