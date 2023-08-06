""" Pseudonymize a PDF by replacing text """
import pdf_redactor


def pseudonymize(input, output, direct_replace=[]):
    """ Pseudonymize a PDF by replacing text """
    options = pdf_redactor.RedactorOptions()
    options.input_stream = input
    options.output_stream = output
    options.content_filters = direct_replace
    pdf_redactor.redactor(options)
