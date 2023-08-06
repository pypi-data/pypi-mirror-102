from fpdf import FPDF


class MyPdf(object):
    def __init__():
        pass

    def gen_pdf(image_list, path):
        pdf = FPDF()
        for image in image_list:
            pdf.add_page()
            pdf.image(image, 0, 0, 800, 600)
        pdf.output(path, "F")