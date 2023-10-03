import pytesseract
from PIL import Image
class OCR:
    def process_image(self, image_path):
        '''
        Process the given image and extract text using OCR.
        Args:
            image_path (str): The path to the image file.
        Returns:
            str: The extracted text from the image.
        '''
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text