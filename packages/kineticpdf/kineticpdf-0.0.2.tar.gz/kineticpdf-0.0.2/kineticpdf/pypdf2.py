import warnings

from pdf2._encryption import PasswordType
from pdf2._merger import PdfFileMerger, PdfMerger
from pdf2._page import PageObject, Transformation
from pdf2._reader import DocumentInformation, PdfFileReader, PdfReader
from pdf2._version import __version__
from pdf2._writer import PdfFileWriter, PdfWriter
from pdf2.pagerange import PageRange, parse_filename_page_ranges
from pdf2.papersizes import PaperSize

__all__ = [
    "__version__",
    "PageRange",
    "PaperSize",
    "DocumentInformation",
    "parse_filename_page_ranges",
    "PdfFileMerger",  # will be removed in PyPDF2 3.0.0; use PdfMerger instead
    "PdfFileReader",  # will be removed in PyPDF2 3.0.0; use PdfReader instead
    "PdfFileWriter",  # will be removed in PyPDF2 3.0.0; use PdfWriter instead
    "PdfMerger",
    "PdfReader",
    "PdfWriter",
    "Transformation",
    "PageObject",
    "PasswordType",
]
