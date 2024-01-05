

import streamlit as st
import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyCGwtv94hX3XGsTzJ57h3zU_zLE-0M4Vgk"

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def generate_javascript_code(task_description):
    template = f"""
        {task_description}

        Write JavaScript code to achieve the task described above.
    """
    response = model.generate_content(template)
    javascript_code = response.text
    javascript_code = javascript_code.replace("```javascript", "").rstrip("```")
    return javascript_code

def main():
    st.set_page_config(page_title="SQL Query Generator", page_icon="🚀")
    st.markdown(
        """
            <div style="text-align:center;">
                <h1>JavaScript Code Generator</h1>
                <h3>I can generate JavaScript codes for you!</h3>
            </div>
        """,
        unsafe_allow_html=True,
    )

    task_description = st.text_area("Describe the Program:")

    submit = st.button("Generate JavaScript Code")

    if submit:
        with st.spinner("Generating JavaScript Code..."):
            javascript_code = generate_javascript_code(task_description)

            with st.container():
                st.success("JavaScript Code Generated! Here is your code:")
                st.code(javascript_code, language="javascript")

if __name__ == "__main__":
    main()