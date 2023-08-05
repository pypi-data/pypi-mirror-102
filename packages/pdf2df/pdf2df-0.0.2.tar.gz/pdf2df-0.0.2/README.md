## Pdf2Df

This is a simple python package to create a dataframe with the text extracted from PDFs.

To install:

```
$ pip install pdf2df
```

### Get Started

To use the package, first import it:

```
from pdf2df import Pdf2df

sfd = Pdf2df(path, page=True, single_file=False)
df = sfd.get_text()
```

### Arguments

 - **path** (str) : Where the files are located. It could be a single file or a folder containing multiple pdf files
 - **page** (bool) : If True, the dataframe will contain each page of the pdf in a new row, if flase, all the text in the pdf will be in the same row.
 - **single_file** (bool) : This tell is method if the path is a folder containing multiple pdf files or a single pdf file.