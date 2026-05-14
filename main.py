import streamlit as st
import validators
from rag import process_urls, generate_answer

# Add Open Graph metadata
st.markdown(
    """
    <meta property="og:title" content="Real Estate Research Tool">
    <meta property="og:description" content="A tool to answer real estate questions using provided URLs.">
    """,
    unsafe_allow_html=True
)

st.title("🏠 Real Estate Research Tool")

# Predefined URLs
PREDEFINED_URLS = {
    "Zillow (Market Trends)": "https://www.zillow.com/research/data/",
    "Realtor.com (News)": "https://www.realtor.com/news/real-estate-news/",
    "Redfin (Market Insights)": "https://www.redfin.com/news/",
    "Investopedia (Real Estate)": "https://www.investopedia.com/mortgage-4427715"
}

# Initialize session state
if "urls_processed" not in st.session_state:
    st.session_state.urls_processed = False
if "last_urls" not in st.session_state:
    st.session_state.last_urls = []
if "selected_predefined_urls" not in st.session_state:
    st.session_state.selected_predefined_urls = []

# Sidebar for URL input
st.sidebar.header("📎 Provide Website URLs")
st.sidebar.markdown("**Quick Start**: Select predefined URLs to test the app instantly! 🚀")
selected_urls = st.sidebar.multiselect(
    "🔗 Predefined URLs (select one or more)",
    options=list(PREDEFINED_URLS.keys()),
    default=st.session_state.selected_predefined_urls,
    help="Choose these to quickly test the app with reliable sources!"
)

# Expander for custom URL inputs
with st.sidebar.expander("🔗 Enter Custom Website Links", expanded=False):
    st.markdown("**Paste your website links here!** 🌐 Add up to 3 custom URLs to search for answers.")
    url1 = st.text_input("URL 1", value=st.session_state.last_urls[0] if len(st.session_state.last_urls) > 0 else "", key="url1")
    url2 = st.text_input("URL 2", value=st.session_state.last_urls[1] if len(st.session_state.last_urls) > 1 else "", key="url2")
    url3 = st.text_input("URL 3", value=st.session_state.last_urls[2] if len(st.session_state.last_urls) > 2 else "", key="url3")

# Expander with vibrant guidance
with st.expander("ℹ️ How This Tool Helps You!", expanded=True):
    st.markdown("""
    **Your Real Estate Assistant!** 🏡 I answer questions using the websites you provide. Here’s the scoop:

    **It Rocks When** ✅
    - Sites have clear, text-based info (e.g., mortgage rates 💰, current or historical).
    - *Examples*: "What’s the 30-year rate today?" or "What was it on March 20, 2025?"

    **It Struggles When** 🚫
    - Info is missing, in images 🖼️, tables, or behind logins 🔒.
    - Sites like CNBC block access 🌐⛔.

    **Pro Tips** 💡
    - Try the predefined URLs above to test instantly! 🔗
    - Use text-rich, public websites 📝.
    - Expand the sidebar section to add custom links! 🌐
    - Process URLs before asking questions! 🚀
    """)

# Process URLs button
process_url_button = st.sidebar.button("🔄 Process URLs")
if process_url_button:
    # Combine predefined and custom URLs
    urls = [PREDEFINED_URLS[url] for url in selected_urls] + [url for url in (url1, url2, url3) if url.strip()]
    if not urls:
        st.error("🚨 Please provide at least one URL (predefined or custom)!")
    else:
        # Validate URLs
        invalid_urls = [url for url in urls if not validators.url(url)]
        if invalid_urls:
            st.error(f"🚫 Invalid URLs: {', '.join(invalid_urls)}")
        else:
            with st.spinner("🌐 Processing URLs..."):
                try:
                    for status in process_urls(urls):
                        st.info(status)
                    st.session_state.urls_processed = True
                    st.session_state.last_urls = [url for url in (url1, url2, url3) if url.strip()]
                    st.session_state.selected_predefined_urls = selected_urls
                    st.success("🎉 URLs processed successfully!")
                except Exception as e:
                    st.error(f"😓 Error processing URLs: {str(e)}")

# Query input
query = st.text_input(
    "💬 Ask Your Real Estate Question",
    disabled=not st.session_state.urls_processed,
    placeholder="E.g., 'What’s the current 30-year mortgage rate?'"
)
if query:
    with st.spinner("🤖 Generating Answer..."):
        try:
            answer, sources = generate_answer(query)
            st.header("📝 Answer:")
            st.write(answer)

            if sources:
                st.subheader("🔗 Sources:")
                for source in sources.split("\n"):
                    st.write(source)
        except Exception as e:
            st.error(f"😓 Error generating answer: {str(e)}")
