import streamlit as st
import base64

def main_web() -> None:
    """ Args: no any
        (this function helps to present widest section of webpage, It initialize four buttons
        of basic information about project and developer contact details)
        Return: None"""
    st.header("Check your password strength", divider='rainbow')
    st.markdown("<h3 style='font-size: 24px;'>Project and Developer information</h3>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)  
    with  col1.expander(label='Project information'): 
        text = """ 
            ### Project Goal:
            Predict password strength (strong, medium, weak) based on data

            ##### Data Source:
            User registration data (passwords) from Facebook APIs

            ##### Use Case:
            Determine the strength level of a password entered during user registration

            ##### Model Creation Process:
            - Breaking password
            - Fetching count of numbers, characters, special symbols, UPPER case letters, lower case letters
            - Creating dataframe of fetched data
            - Model trained (Logistic Regression)
            - Score: 99.9% (test score)
            - Calibrating model performance
            """
        st.markdown(text)

    with  col2.expander(label='Contact details'): 
        contacts_info = """
        Contacts:
        - **Name:** Vijay Dipak Takbhate
        - **Email:** [vijaytakbhate20@gmail.com](mailto:vijaytakbhate20@gmail.com)

        Work Profiles:
        - **LinkedIn:** [Vijay Takbhate](https://www.linkedin.com/in/vijay-takbhate-b9231a236/)
        - **Github:** [vijaytakbhate2002](https://github.com/vijaytakbhate2002/Microsoft-Machine-Failure-Detection.git)
        - **Kaggle:** [vijay20213](https://www.kaggle.com/vijay20213)
        """
        st.markdown(contacts_info)

    with  st.expander(label='Resume'):
        pdf_file_path = "static\\Vijay_Takbhate_LaTeX.pdf"
        def read_pdf_file(pdf_file_path):
            with open(pdf_file_path, "rb") as file:
                pdf_contents = file.read()
            return base64.b64encode(pdf_contents).decode("utf-8")

        encoded_pdf = read_pdf_file(pdf_file_path)
        st.markdown(f'<embed src="data:application/pdf;base64,{encoded_pdf}" width="700" height="1000"></embed>', unsafe_allow_html=True)


if __name__ == '__main__':
    main_web()