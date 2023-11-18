#
# Kinetic PDF - 2023
#    Updates and wrapper around PDF handling functions updated for 2023.
#    Copyright 2023 - Kinetic Seas Inc, Chicago Illinois
#    Edward Honour, Joseph Lehman
#
#    Includes functions from pdfrw (https://github.com/pmaupin/pdfrw)
#           Copyright (C) 2006-2015 Patrick Maupin, Austin, Texas
#           MIT license -- See LICENSE.txt for details
#           pdfrw functions were the best for reading and writing Forms in PDF.
#
#           pdfrw has not been updated in years, so we included the
#           functions to make whatever changes necessary.
#
#    Includes functions from PyPDF2
#    PyPDF2 functions were the best for reading text from PDFs and
#           checking if a PDF is encrypyted.
#
#           PyPDF2 is deprecated, so we included the functions to make
#           whatever changes necessary.
#
#           Documentation: <URL coming soon>
#           FAQ: <http://mstamy2.github.io/PyPDF2/FAQ.html>
#           PyPI: <https://pypi.python.org/pypi/PyPDF2>
#           GitHub: <https://github.com/mstamy2/PyPDF2>
#           Homepage: <http://mstamy2.github.io/PyPDF2/>
#
#    PikePDF is a dependency and used to decrypt PDFs.
#           pikepdf is a Python library for reading and writing PDF files.
#
#           PikePDF is actively maintained so we DID not include thier
#           functions in this library.

from .pypdf2 import *                                       # Import PyPDF2 Functions.
from .pdfwriter import PdfWriter                            # Import pdfrw implementation of PdfWriter.
from .pdfreader import PdfReader                            # Import pdfrw implementation of PdfReader.
from .objects import (PdfObject, PdfName, PdfArray,
                      PdfDict, IndirectPdfDict, PdfString)
from .tokens import PdfTokens
from .errors import PdfParseError
from .pagemerge import PageMerge
import os
import copy

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

    #
    # fill_pdf_form: reads a PDF from the filesystem, applies new values,
    #                and writes output file.
    #
    @staticmethod
    def fill_pdf_form(input_pdf_path, output_pdf_path, new_values):

        field_update_count = 0
        fields_updated = []

        # EH: new_values must be a dict or return error.
        if isinstance(new_values, dict):
            fields_missing = copy.deepcopy(new_values)
        else:
            error_code = "8001"
            error_msg = "New Values must be a dictionary."
            return {"error_code": error_code, "error_msg": error_msg, "data": {}}

        # EH: Output path must not be blank.
        if output_pdf_path == "":
            error_code = "8002"
            error_msg = "Output file path must not be blank."
            return {"error_code": error_code, "error_msg": error_msg, "data": {}}
        else:
            output_dir = os.path.dirname(output_pdf_path)
            if not os.path.exists(output_dir):
                os.makedirs(output_dir, exist_ok=True)

        # EH: Input path must not be blank.
        if input_pdf_path == "":
            error_code = "8002"
            error_msg = "Input PDF Path must not be blank."
            return {"error_code": error_code, "error_msg": error_msg, "data": {}}
        else:
            # Test input file exists.
            if os.path.exists(input_pdf_path):
                # Test if file is encrypted
                if KineticPdf.is_pdf_encrypted(input_pdf_path):
                    error_code = "8005"
                    error_msg = "Cannot fill a password protected PDF: " + str(input_pdf_path)
                    return {"error_code": error_code, "error_msg": error_msg, "data": {}}

                try:
                    # Attempt the read.
                    reader = PdfReader(input_pdf_path)
                except:
                    error_code = "8003"
                    error_msg = "Error Opening File: " + str(input_pdf_path)
                    return {"error_code": error_code, "error_msg": error_msg, "data": {}}

            else:
                error_code = "8003"
                error_msg = "Input file path does not exist: " + str(input_pdf_path)
                return {"error_code": error_code, "error_msg": error_msg, "data": {}}

        #
        # EH: If you don't set NeedsAppearances, updated forms may not appear
        # on different viewers, like Adobe Acrobat Pro.
        #
        if '/AcroForm' in reader.Root:
            reader.Root.AcroForm.update(PdfDict(NeedAppearances=PdfObject('true')))
        else:
            error_code = "8000"
            error_msg = "No Form in this PDF"
            return {"error_code": error_code, "error_msg": error_msg, "data": {}}

        #
        # EH: Iterate through each page and update form fields.  There are different
        # ways to process pages and annotations, but this seems to be the cleanest and
        # most stable.
        #
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
                                    field_update_count += 1
                                    f = {key: new_values[key], "type": "annotation"}
                                    fields_updated.append(f)
                                    tmp = copy.deepcopy(fields_missing)
                                    if key in tmp:
                                        del fields_missing[key]
                                    
                                    if annotation['/FT'] == '/Btn' and '/AS' in annotation:
                                        new_value = new_values[key]
                                        annotation.update(PdfDict(V=PdfName(new_value)))
                                        annotation.update(PdfDict(AS=PdfName(new_value)))
                                        annotation.update(PdfDict(AP=''))
                            else:
                                if annotation['/Parent']:
                                    parent = annotation['/Parent']
                                    if isinstance(parent, PdfDict) and '/T' in parent:
                                        my_name = parent['/T'][1:-1]
                                        if my_name == key:
                                            field_update_count += 1
                                            tmp = copy.deepcopy(fields_missing)
                                            if key in tmp:
                                                del fields_missing[key]

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
                                            f = {key: new_values[key], "type": "parent"}
                                            fields_updated.append(f)

        PdfWriter().write(output_pdf_path, reader)

        data = {"output_file_name": output_pdf_path, "field_count": str(field_update_count), "fields_updated": fields_updated, "fields_not_updated": fields_missing}
        output = {"error_code": "0", "error_msg": "", "data": data}

        return output

    @staticmethod
    def get_pdf_form(input_pdf_path):

        # EH: Input path must not be blank.
        if input_pdf_path == "":
            error_code = "8002"
            error_msg = "Input PDF Path must not be blank."
            return {"error_code": error_code, "error_msg": error_msg, "data": {}}
        else:
            # Test input file exists.
            if os.path.exists(input_pdf_path):

                # Test if file is encrypted
                if KineticPdf.is_pdf_encrypted(input_pdf_path):
                    error_code = "8004"
                    error_msg = "Cannot read a password protected PDF: " + str(input_pdf_path)
                    return {"error_code": error_code, "error_msg": error_msg, "data": {}}

                try:
                    # Attempt the read.
                    annotations = PdfReader(input_pdf_path).Root.AcroForm.Fields
                except:
                    error_code = "8003"
                    error_msg = "Error Opening File: " + str(input_pdf_path)
                    return {"error_code": error_code, "error_msg": error_msg, "data": {}}
            else:
                error_code = "8003"
                error_msg = "Input file path does not exist: " + str(input_pdf_path)
                return {"error_code": error_code, "error_msg": error_msg, "data": {}}

        form_fields = {}
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

        output = {"error_code": "0", "error_msg": "", "data": form_fields}
        return output

    @staticmethod
    def get_pdf_metadata(input_pdf_path, clean=True):

        # EH: Input path must not be blank.
        if input_pdf_path == "":
            error_code = "8002"
            error_msg = "Input PDF Path must not be blank."
            return {"error_code": error_code, "error_msg": error_msg, "data": {}}
        else:
            # Test input file exists.
            if os.path.exists(input_pdf_path):

                # Test if file is encrypted
                if KineticPdf.is_pdf_encrypted(input_pdf_path):
                    error_code = "8004"
                    error_msg = "Cannot read a password protected PDF: " + str(input_pdf_path)
                    return {"error_code": error_code, "error_msg": error_msg, "data": {}}

                try:
                    # Attempt the read.
                    pdf = PdfReader(input_pdf_path)
                except:
                    error_code = "8003"
                    error_msg = "Error Opening File: " + str(input_pdf_path)
                    return {"error_code": error_code, "error_msg": error_msg, "data": {}}
            else:
                error_code = "8003"
                error_msg = "Input file path does not exist: " + str(input_pdf_path)
                return {"error_code": error_code, "error_msg": error_msg, "data": {}}

        metadata = {}
        info = pdf.Info
        if info:
            for key in info.keys():
                if clean:
                    cleaned_key = key[1:]  # Remove '/' from the key
                else:
                    cleaned_key = key

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

            # if 'Keywords' in metadata:
            #    keywords_list = metadata['Keywords']

            #    keywords_dict = {}
            #    for keyword in keywords_list:
            #        key, value = keyword.split('=')
            #        keywords_dict[key] = value

            #    metadata['keys'] = keywords_dict

        output = {"error_code": "0", "error_msg": "", "data": form_fields}
        return output

    # Radio Buttons are always an issue.
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
    def get_pdf_text(input_pdf_path):

        # EH: Input path must not be blank.
        if input_pdf_path == "":
            error_code = "8002"
            error_msg = "Input PDF Path must not be blank."
            return {"error_code": error_code, "error_msg": error_msg, "data": {}}
        else:
            # Test input file exists.
            if os.path.exists(input_pdf_path):

                # Test if file is encrypted
                if KineticPdf.is_pdf_encrypted(input_pdf_path):
                    error_code = "8004"
                    error_msg = "Cannot read a password protected PDF: " + str(input_pdf_path)
                    return {"error_code": error_code, "error_msg": error_msg, "data": {}}

                try:
                    # Attempt the read.
                    with open(input_pdf_path, 'rb') as file:
                        results = []
                        r = pypdf2.PdfReader(file)
                        for i in range(0, len(r.pages)):
                            text = r.pages[i].extract_text()
                            results.append(text)
                except:
                    error_code = "8003"
                    error_msg = "Error Opening File: " + str(input_pdf_path)
                    return {"error_code": error_code, "error_msg": error_msg, "data": {}}
            else:
                error_code = "8003"
                error_msg = "Input file path does not exist: " + str(input_pdf_path)
                return {"error_code": error_code, "error_msg": error_msg, "data": {}}

        output = {"error_code": "0", "error_msg": "", "data": results}
        return output

    @staticmethod
    def is_pdf_encrypted(pdf_path):
        with open(pdf_path, 'rb') as file:
            pdf_reader = pypdf2.PdfReader(file)
            return pdf_reader.is_encrypted
