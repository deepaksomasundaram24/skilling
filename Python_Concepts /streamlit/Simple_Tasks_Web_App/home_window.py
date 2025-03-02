import streamlit as st

st.title("Task Tracking WebApp")

def switch_page(page_name: str):
    from streamlit import _RerunData, _RerunException
    from streamlit.source_util import get_pages

    def standardize_name(name: str) -> str:
        return name.lower().replace("_", " ")
    
    page_name = standardize_name(page_name)

    pages = get_pages("home_window.py")  # OR whatever your main page is called

    for page_hash, config in pages.items():
        if standardize_name(config["page_name"]) == page_name:
            raise _RerunException(
                _RerunData(
                    page_script_hash=page_hash,
                    page_name=page_name,
                )
            )

    page_names = [standardize_name(config["page_name"]) for config in pages.values()]

    raise ValueError(f"Could not find page {page_name}. Must be one of {page_names}")

if st.button("Create Task"):
    st.switch_page("pages/1_create_task.py")

if st.button("Inprogress Task(s)"):
    st.switch_page("pages/2_inprogress_task.py")

if st.button("Completed Task(s)"):
    st.switch_page("pages/3_completed_task.py")