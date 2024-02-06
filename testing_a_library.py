
from pdf2image import convert_from_path


if __name__ == "__main__":

    pdf_file = r"C:\Nitanshus_Work\Projects\Project-Resume-ATS-System-Early-Roles\Documents\Nitanshu_Joshi_Resume.pdf"

    # incase of Linux we don't have to provide the popper_path parameter
    images = convert_from_path(pdf_file)#, poppler_path=r"poppler-0.68.0_x86\poppler-0.68.0\bin")

    for i in range(len(images)):
        # Save pages as images in the pdf
        images[i].save(f'image_{i+1}.png', 'PNG')