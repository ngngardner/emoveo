"""Deduplication of pdf files."""

import time

import PyPDF2 as pdf
from beartype import beartype
from PyPDF2.pdf import PageObject

from emoveo.console import console


@beartype
def unique_pages(pages: list[PageObject]) -> list[PageObject]:
    """Return unique pages.

    Args:
        pages (list): List of pages.

    Returns:
        list: List of unique pages.
    """
    res = []
    page_contents = []

    start_time = time.time()
    for page in pages:
        page_content = page.extractText()
        if page_content not in page_contents:
            res.append(page)
            page_contents.append(page_content)

    diff = round(time.time() - start_time, 4)
    console.log('Time taken: {0}'.format(diff))

    return res


@ beartype
def set_pages(path: str, pages: list[PageObject]) -> None:
    """Set pages of output pdf file and write it.

    Args:
        path (str): Path to pdf file.
        pages (list): List of pages.
    """
    out_path=path.replace('.pdf', '_dedup.pdf')
    with open(out_path, 'wb') as fout:
        writer=pdf.PdfFileWriter()

        console.log('Number of pages before dedup: {0}'.format(len(pages)))
        pages=unique_pages(pages)
        console.log('Number of pages after dedup: {0}'.format(len(pages)))

        for page in pages:
            writer.addPage(page)

        console.log('Writing "{0}"'.format(out_path))
        writer.write(fout)


@ beartype
def dedup(path: str) -> None:
    """Deduplicate pdf files.

    Args:
        path (str): Path to pdf file.
    """
    console.log('Deduplicating "{0}"'.format(path))
    with open(path, 'rb') as fin:
        reader=pdf.PdfFileReader(fin)

        pages=[]
        for idx in range(reader.numPages):
            pages.append(reader.getPage(idx))

        set_pages(path, pages)
