# A part of pdfrw (https://github.com/pmaupin/pdfrw)
# Copyright (C) 2006-2015 Patrick Maupin, Austin, Texas
# MIT license -- See LICENSE.txt for details

import pypdf2
from pdfwriter import PdfWriter
from pdfreader import PdfReader
from objects import (PdfObject, PdfName, PdfArray,
                      PdfDict, IndirectPdfDict, PdfString)
from tokens import PdfTokens
from errors import PdfParseError
from pagemerge import PageMerge

__version__ = '0.4'

# Add a tiny bit of compatibility to pyPdf

PdfFileReader = PdfReader
PdfFileWriter = PdfWriter

__all__ = """PdfWriter PdfReader PdfObject PdfName PdfArray
             PdfTokens PdfParseError PdfDict IndirectPdfDict
             PdfString PageMerge""".split()

class KineticPdf:

    def __init__(self):
        pass

    @staticmethod
    def update_pdf_form(input_pdf_path, output_pdf_path, new_values):

        reader = PdfReader(input_pdf_path)

        if '/AcroForm' in reader.Root:
            reader.Root.AcroForm.update(PdfDict(NeedAppearances=PdfObject('true')))

        # Iterate through each page and update form fields
        for page in reader.pages:
            annotations = page['/Annots']
            if annotations:
                for annotation in annotations:

                    if annotation['/Subtype'] == '/Widget':
                        for key in new_values:

                            if annotation['/T']:

                                field_name = annotation['/T'][1:-1]  # Remove parentheses around field name
                                if field_name == key:
                                    annotation.update(PdfDict(V=new_values[key]))  # Set new value
                                    annotation.update(PdfDict(AP=''))
                                    new_value = new_values[key]
                                    annotation.update(PdfDict(AS=PdfName(new_value)))

                                    annotation.update(PdfDict(V=new_value))

                                    if annotation['/FT'] == '/Btn' and '/AS' in annotation:
                                        new_value = new_values[key]
                                        print("X" + new_values[key])
                                        annotation.update(PdfDict(V=PdfName(new_value)))
                                        annotation.update(PdfDict(AS=PdfName(new_value)))
                                        annotation.update(PdfDict(AP=''))
                            else:
                                if annotation['/Parent']:
                                    parent = annotation['/Parent']
                                    if isinstance(parent, PdfDict) and '/T' in parent:
                                        my_name = parent['/T'][1:-1]
                                        if my_name == key:
                                            print('Not Update:' + new_values[key])
                                            new_value = new_values[key]
                                            annotation.update(
                                                PdfDict(V='{}'.format(new_value))
                                            )
                                            KineticPdf.set_radio_button_value(annotation, annotation['/Parent'], new_value)
                                            parent.update(PdfDict(V=new_values[key]))  # Set new value
                                            parent.update(PdfDict(AP=''))
                                            parent.update(PdfDict(AS=PdfName(new_value)))
                                            annotation.update(PdfDict(V=new_values[key]))  # Set new value
                                            annotation.update(PdfDict(AP=''))
                                            annotation.update(PdfDict(AS=PdfName(new_value)))

        PdfWriter().write(output_pdf_path, reader)

        return output_pdf_path

    @staticmethod
    def get_form_fields(infile):
        """
        Extract form fields and their values from a PDF.
        """
        form_fields = {}
        annotations = PdfReader(infile).Root.AcroForm.Fields
        for annotation in annotations:
            if annotation.FT == '/Tx':  # Field Type is Text
                key = annotation.T[1:-1]  # Remove parentheses around the key
                value = annotation.V[1:-1] if annotation.V else None  # Remove parentheses around the value
                form_fields[key] = value
            elif annotation.FT == '/Btn':  # Field Type is Button (Checkboxes and Radio buttons)
                key = annotation.T[1:-1]
                value = annotation.V
                form_fields[key] = value
            # Add more field types (like /Ch for choice fields) as needed
        return form_fields

    @staticmethod
    def get_pdf_metadata(infile):
        metadata = {}
        pdf = PdfReader(infile)
        info = pdf.Info
        if info:
            for key in info.keys():
                cleaned_key = key[1:]  # Remove '/' from the key
                value = info[key]
                if value:
                    # Remove starting and ending parentheses if present
                    if value.startswith('(') and value.endswith(')'):
                        value = value[1:-1]
                    # Process keywords
                    if cleaned_key == "Keywords":
                        metadata[cleaned_key] = [keyword.strip() for keyword in value.split(",")]
                    else:
                        metadata[cleaned_key] = value
                else:
                    metadata[cleaned_key] = None

            if 'Keywords' in metadata:
                keywords_list = metadata['Keywords']

                keywords_dict = {}
                for keyword in keywords_list:
                    key, value = keyword.split('=')
                    keywords_dict[key] = value

                metadata['keys'] = keywords_dict

        return metadata

    @staticmethod
    def set_radio_button_value(annotation, parent, desired_value):
        if annotation.get('/Parent') == parent:
            if '/' in desired_value:
                d = desired_value[1:]
            else:
                d = desired_value

            parent.update(PdfDict(V=PdfName(d)))
            parent.update(PdfDict(AS=PdfName(d)))
            if annotation['/AP']['/D']:
                if desired_value in annotation['/AP']['/D']:
                    annotation.update(PdfDict(V=PdfName('On')))
                    annotation.update(PdfDict(AS=PdfName(d)))
                else:
                    pass
                # annotation.update(pdfrw.PdfDict(AS=pdfrw.PdfName('/Off')))

    @staticmethod
    def extract_pdf_text(path):

        with open(path, 'rb') as file:
            results = []
            r = pypdf2.PdfReader(file)
            for i in range(0, len(r.pages)):
                text = r.pages[i].extract_text()
                results.append(text)
        return results

    @staticmethod
    def is_pdf_encrypted(pdf_path):
        with open(pdf_path, 'rb') as file:
            pdf_reader = pypdf2.PdfReader(file)
            return pdf_reader.is_encrypted
