"""
This module contains simple function for test
"""

from recognition import Recognition


class ImageRecognition:
    """
    A class for image recognition that extracts text from an image using the Recognition class.

    Attributes:
        - image_path (str): The path to the image for text recognition.
        - language (str): The language for text recognition (default is 'eng' for English).

    Methods:
        - __init__(self, image_path, language='eng'): Initializes the ImageRecognition class 
            with the provided image path and language.
        - get_text_from_photo(self): Retrieves text from the image using text recognition.
    """

    def __init__(self, image_path, language='eng') -> None:
        """
        Initializes the ImageRecognition class with the provided image path and language.

        Args:
            - image_path (str): The path to the image for text recognition.
            - language (str): The language for text recognition (default is 'eng' for English).
        """
        self.image_path = image_path
        self.language = language

    def get_text_from_photo(self):
        """
        Retrieves text from the image using text recognition.

        Returns:
            - extracted_text (str): The extracted text from the image.
        """
        recognition = Recognition(self.image_path)
        extracted_text = recognition.process_text_extraction(self.language)
        return extracted_text
    

if __name__ == '__main__':
    pass
    # print(ImageRecognition('src/image_recognition_demo_test/edit.jpg', 'eng').get_text_from_photo())
