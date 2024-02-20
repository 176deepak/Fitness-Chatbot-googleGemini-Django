# load the required modules
import re
import os
import google.generativeai as genai


# function for handle the images
def input_image_setup(uploaded_file):
    # Read the file into bytes
    with open(uploaded_file, 'rb') as file:
        bytes_data = file.read()

    # Get the mime type of the file
    mime_type = 'image/' + uploaded_file.split('.')[-1]

    image_parts = [
        {
            "mime_type": mime_type,
            "data": bytes_data
        }
    ]
    return image_parts


def reformat_response(response):
    # cleaned text
    text = re.sub(r"\*", "", response.text)
    return text


def ask_to_bot(query:str, image=None) -> str:

    # configure the API KEY 
    genai.configure(api_key = "REPLACE_WITH_YOUR_API_KEY")

    if image is None:
        # input prompt for general fitness bot
        gen_input_prompt = """
            Hey, you're a fitness trainer. You lead, instruct, motivate, and help individuals or groups achieve their fitness goals through customized exercise and nutrition plans. You provide advice to people on how to care for their body's health based on their body weight, body type, and fitness goals.
        """
        # load the LLM Model "Gemini-Pro"
        llm_model = genai.GenerativeModel('gemini-pro')
        # pass or asks the user's problem to fitness bot
        response = llm_model.generate_content([gen_input_prompt, query])
        text = reformat_response(response=response)
        # chat format
        chat = f"YOU:\n{query}\n\nBOT:\n{text}"
        # return the bot response to user
        return chat
    
    elif image is not None:
        # personalized input prompt
        per_input_prompt = """
            Hey, you're a fitness trainer. You lead, instruct, motivate, and help individuals achieve their fitness goals through customized exercise and nutrition plans. Where, You make a diet plan for and give strict advice on how to care for their body's health based on provided full body photo of individual, their body weight, body type, and fitness goals.
        """
        # get the image data
        img_folder = r"media\userImage"
        img_path = os.path.join(img_folder, image)
        image_data=input_image_setup(img_path)
        # load the LLM Model "Gemini-Pro"
        llm_model = genai.GenerativeModel('gemini-pro-vision')
        # pass or asks the user's problem to fitness bot
        response = llm_model.generate_content([per_input_prompt,image_data[0], query])
        text = reformat_response(response=response)
        # chat format
        chat = f"YOU:\n{query}\n\nBOT:\n{text}"
        # return the bot response to user
        return chat