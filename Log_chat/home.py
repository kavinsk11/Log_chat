import streamlit as st

def main():
    st.title('AI Chat Box')

    # Sidebar for dark mode
    st.sidebar.title('Settings')
    dark_mode = st.sidebar.checkbox('Dark Mode', value=True)

    # Apply dark mode if selected
    if dark_mode:
        st.markdown("""
            <style>
            .main {
                background-color: #1e1e1e;
                color: #ffffff;
            }
            </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
            .main {
                background-color: #ffffff;
                color: #000000;
            }
            </style>
        """, unsafe_allow_html=True)

    st.subheader('Enter Conversation Details')
    # Create input fields for Conversation ID and Store ID
    conversation_id = st.text_input('Conversation ID:')
    store_id = st.text_input('Store ID:')

    # Create an "Enter" button
    if st.button('Enter'):
        if conversation_id and store_id:
            # Set the URL with query parameters
            st.experimental_set_query_params(conversation_id=conversation_id, store_id=store_id)
            # Redirect to the "View Conversation" page
            st.experimental_rerun()

# Run the main Streamlit app
if __name__ == "__main__":
    main()
