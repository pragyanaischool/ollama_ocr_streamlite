import streamlit as st
import subprocess
import tempfile

st.title("Llama 3.2 Vision with Streamlit")

# Upload Image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

# User Prompt
user_prompt = st.text_area("Enter your prompt:", "Describe this image...")

if st.button("Run Llama Vision Model"):
    if uploaded_file:
        # Save the uploaded file to a temporary location
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
            temp_file.write(uploaded_file.read())
            image_path = temp_file.name

        try:
            # Run Ollama with the image and prompt
            command = ["ollama", "run", "llama3.2-vision", image_path, user_prompt]
            result = subprocess.run(command, text=True, capture_output=True)
            st.image(image_path, caption="Uploaded Image", use_column_width=True)
            st.write("### Output:")
            st.write(result.stdout)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please upload an image.")
