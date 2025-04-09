from google import genai
from google.genai import types
import base64
from vertexai.vision_models import ImageGenerationModel
import time
from google.genai.types import GenerateVideosConfig, Image
import os
import vertexai

def generate_answer(query):
    client = genai.Client(
      vertexai=True,
      project="fresh-span-400217",
      location="us-central1",
    )


    model = "gemini-2.0-flash-001"
    contents = [
    types.Content(
        role="user",
        parts=[
            types.Part.from_text(text=f"""{query}""")
                ]
            )
        ]
    generate_content_config = types.GenerateContentConfig(
        temperature = 1,
        top_p = 0.95,
        max_output_tokens = 8192,
        response_modalities = ["TEXT"],
        safety_settings = [types.SafetySetting(
              category="HARM_CATEGORY_HATE_SPEECH",
              threshold="OFF"
            ),types.SafetySetting(
              category="HARM_CATEGORY_DANGEROUS_CONTENT",
              threshold="OFF"
            ),types.SafetySetting(
              category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
              threshold="OFF"
            ),types.SafetySetting(
              category="HARM_CATEGORY_HARASSMENT",
              threshold="OFF"
            )
        ],
    )
    text_result = ""

    for chunk in client.models.generate_content_stream(
    model = model,
    contents = contents,
    config = generate_content_config,
    ):
        print(chunk.text, end="")
        text_result+=chunk.text
    return text_result

def generate_image(user_query):

    model = ImageGenerationModel.from_pretrained("imagen-3.0-generate-002")
    print(user_query)
    images = model.generate_images(
        prompt=user_query,
        number_of_images=1,
        aspect_ratio="1:1",
        safety_filter_level="block_few",
        person_generation="allow_all",
    )

    image_bytes = images[0]._image_bytes
    base64_encoded = base64.b64encode(image_bytes).decode("utf-8")
    print(type(base64_encoded))
    print(f"Created output image using {len(image_bytes)} bytes")

    return base64_encoded

