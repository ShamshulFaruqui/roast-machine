import streamlit as st
import os
from dotenv import load_dotenv
from roaster import roast_text, roast_image
from guardrails import check_input

load_dotenv()

st.set_page_config(
    page_title="AI Roast Machine 🔥",
    page_icon="🔥",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
    .main { padding: 2rem; }
    .roast-header {
        text-align: center;
        padding: 2rem 0 1rem 0;
    }
    .roast-title {
        font-size: 20rem;
        font-weight: 800;
        background: linear-gradient(135deg, #ff6b35, #f7c59f);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
    }
    .roast-subtitle {
        color: #888;
        font-size: 1.1rem;
        margin-top: 0.5rem;
    }
    .roast-result {
        background: linear-gradient(135deg, #1a0a00, #2d1500);
        border: 1px solid #ff6b35;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        font-size: 1.1rem;
        line-height: 1.6;
        color: #f7c59f;
    }
    .stat-box {
        background: #1a1a2e;
        border: 1px solid #333;
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
    }
    .stat-number {
        font-size: 2rem;
        font-weight: 800;
        color: #ff6b35;
    }
    .stat-label {
        color: #888;
        font-size: 0.85rem;
    }
    .badge {
        display: inline-block;
        background: #ff6b3520;
        border: 1px solid #ff6b35;
        color: #ff6b35;
        padding: 0.2rem 0.7rem;
        border-radius: 20px;
        font-size: 0.8rem;
        margin: 0.2rem;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="roast-header">
    <p style="font-size:4rem; font-weight:800; background: linear-gradient(135deg, #ff6b35, #f7c59f); -webkit-background-clip:text; -webkit-text-fill-color:transparent; margin:0;">🔥 AI Roast Machine</p>
    <p class="roast-subtitle">Too polite AI? Not here. Get roasted — if you dare.</p>
    <span class="badge">Powered by Groq</span>
    <span class="badge">RAG-enhanced</span>
    <span class="badge">Guardrails Active</span>
    <span class="badge">LangSmith Traced</span>
</div>
""", unsafe_allow_html=True)

st.divider()

# Session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "injection_attempts" not in st.session_state:
    st.session_state.injection_attempts = 0
if "total_roasts" not in st.session_state:
    st.session_state.total_roasts = 0

# Stats row
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"""
    <div class="stat-box">
        <div class="stat-number">{st.session_state.total_roasts}</div>
        <div class="stat-label">Roasts Delivered</div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown(f"""
    <div class="stat-box">
        <div class="stat-number">{st.session_state.injection_attempts}</div>
        <div class="stat-label">Injections Blocked</div>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown(f"""
    <div class="stat-box">
        <div class="stat-number">{len(st.session_state.chat_history)}</div>
        <div class="stat-label">Exchanges</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

tab1, tab2 = st.tabs(["🗣 Roast Me (Text)", "📸 Roast My Photo"])

# --- TEXT TAB ---
with tab1:
    st.subheader("Tell me something about yourself")
    user_input = st.text_area(
        "The more you say, the harder I roast...",
        height=120,
        placeholder="e.g. I'm a 22 year old computer science student who drinks too much coffee and hasn't slept properly in 3 years..."
    )

    if st.button("🔥 Roast Me", type="primary", use_container_width=True):
        if user_input.strip() == "":
            st.warning("Say something first — I can't roast thin air.")
        else:
            with st.spinner("Sharpening my words..."):
                check = check_input(user_input)
                if not check["safe"] and check["reason"] == "prompt_injection":
                    st.session_state.injection_attempts += 1
                response = roast_text(user_input, st.session_state.chat_history)
                st.session_state.chat_history.append({
                    "user": user_input,
                    "ai": response
                })
                st.session_state.total_roasts += 1
                st.rerun()

    if st.session_state.chat_history:
        latest = st.session_state.chat_history[-1]
        st.markdown(f'<div class="roast-result">🔥 {latest["ai"]}</div>', unsafe_allow_html=True)

        st.divider()
        st.subheader("💬 Full Roast History")
        for exchange in st.session_state.chat_history:
            st.chat_message("user").write(exchange["user"])
            st.chat_message("assistant").write(exchange["ai"])

        st.divider()
        st.subheader("🎤 Fire Back")
        comeback = st.text_input("Think you can roast better?", placeholder="Give it your best shot...")
        if st.button("🎤 Fire Back", use_container_width=True):
            if comeback.strip():
                with st.spinner("Preparing counter-roast..."):
                    counter = roast_text(
                        f"The user is trying to roast me back by saying: {comeback}. Defend yourself then roast them harder.",
                        st.session_state.chat_history
                    )
                st.session_state.chat_history.append({
                    "user": comeback,
                    "ai": counter
                })
                st.session_state.total_roasts += 1
                st.rerun()

# --- PHOTO TAB ---
with tab2:
    st.subheader("Upload a photo — I'll roast what I see")
    st.caption("Powered by Groq Vision — no image is safe.")
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        from PIL import Image
        import base64
        import io
        from groq import Groq

        image = Image.open(uploaded_file)
        col1, col2 = st.columns([1, 1])
        with col1:
            st.image(image, caption="Your soon-to-be-roasted photo", width=300)
        with col2:
            st.markdown("### Ready to be roasted?")
            st.markdown("Our AI will analyse your photo and deliver a personalised roast based on what it sees.")
            if st.button("🔥 Roast This Photo", type="primary", use_container_width=True):
                with st.spinner("Analysing your photo..."):
                    img_bytes = io.BytesIO()
                    image.save(img_bytes, format="PNG")
                    img_bytes.seek(0)
                    img_base64 = base64.b64encode(img_bytes.read()).decode("utf-8")

                    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
                    vision_response = client.chat.completions.create(
                        model="meta-llama/llama-4-scout-17b-16e-instruct",
                        messages=[
                            {
                                "role": "user",
                                "content": [
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": f"data:image/png;base64,{img_base64}"
                                        }
                                    },
                                    {
                                        "type": "text",
                                        "text": "Describe this image in detail — what does the person look like, what are they wearing, what is in the background, what is their vibe?"
                                    }
                                ]
                            }
                        ]
                    )
                    image_description = vision_response.choices[0].message.content
                    roast = roast_image(image_description)
                    st.session_state.total_roasts += 1

                st.markdown(f'<div class="roast-result">🔥 {roast}</div>', unsafe_allow_html=True)

# --- GUARDRAIL LOG ---
st.divider()
with st.expander("🛡 Guardrail & Safety Log"):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-number">{st.session_state.injection_attempts}</div>
            <div class="stat-label">Prompt Injection Attempts Blocked</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="stat-box">
            <div class="stat-number">✅</div>
            <div class="stat-label">Guardrails Active</div>
        </div>
        """, unsafe_allow_html=True)
    st.caption("All inputs are screened for prompt injection and harmful content before reaching the AI. All outputs are screened before reaching you.")