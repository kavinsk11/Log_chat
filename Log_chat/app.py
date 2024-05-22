import streamlit as st

# Define pages
PAGES = {
    "Home": "home",
    "View Conversation": "view_conversation"
}

# Add sidebar for navigation
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

# Load the selected page module
page = PAGES[selection]
module = __import__(page)

# Run the selected page's main function
module.main()
