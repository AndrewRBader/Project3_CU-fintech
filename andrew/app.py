import streamlit as st
# Import the setup form component
from setup_form import setup_form

# Define the dashboard tab
def dashboard():
    st.write("This is the dashboard tab")

# Define the execution tab
def execution():
    st.write("This is the execution tab")

# Define the main function
def main():
    st.set_page_config(page_title="Will-Asset Token App")
    st.title("Will-Asset Token App")

    # Create a tab menu
    tabs = ["Form to set up", "Dashboard", "Execution"]
    current_tab = st.sidebar.radio("Select a tab", tabs)

    # Display the appropriate tab
    if current_tab == "Form to set up":
        setup_form()
    elif current_tab == "Dashboard":
        dashboard()
    else:
        execution()

# Call the main function to run the app
if __name__ == "__main__":
    main()
