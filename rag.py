from langchain_core.documents import Document

def build_roast_knowledge_base():
    roast_styles = [
        Document(page_content="Self-deprecating humour works best when it exaggerates a minor flaw into a catastrophe."),
        Document(page_content="Observational roasts point out something obviously true that the person never noticed about themselves."),
        Document(page_content="Timing roasts reference the person's age or life stage in an exaggerated way."),
        Document(page_content="Occupation roasts exaggerate the stereotype of someone's job or study field."),
        Document(page_content="A good roast always has a kernel of truth — pure fiction isn't funny."),
        Document(page_content="The best roasts are specific, not generic. Generic insults are lazy and unfunny."),
        Document(page_content="Roasts should punch at the situation, not at protected characteristics like race or disability."),
        Document(page_content="A clever roast makes the target laugh first before anyone else."),
        Document(page_content="Escalating roasts start mild and get progressively more savage with each exchange."),
        Document(page_content="The callback roast references something said earlier in the conversation for maximum impact."),
    ]
    return roast_styles

def get_roast_context(query: str, vectorstore=None) -> str:
    roast_styles = build_roast_knowledge_base()
    keywords = query.lower().split()
    relevant = []
    for doc in roast_styles:
        if any(k in doc.page_content.lower() for k in keywords):
            relevant.append(doc.page_content)
    if not relevant:
        relevant = [roast_styles[0].page_content, roast_styles[5].page_content]
    return "\n".join(relevant[:3])