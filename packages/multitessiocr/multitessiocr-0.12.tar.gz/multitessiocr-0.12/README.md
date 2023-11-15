# Performs a very fast OCR on a list of images (file path, url, base64, bytes, numpy, PIL ...) using Tesseract and returns the recognized text, its coordinates, and line-based word grouping in a DataFrame.

## Tested against Windows 10 / Python 3.11 / Anaconda

### pip install multitessiocr


```python
from multitessiocr import tesser_ocr

piclist = [
    r"C:\screeeni\35.png",
    r"C:\Users\hansc\Downloads\2023-11-12 00_48_43-.png",
    r"C:\Users\hansc\Downloads\WhatsApp Image 2023-09-19 at 12.03.41 PM.jpeg",
    r"C:\Users\hansc\Downloads\WhatsApp Image 2023-09-19 at 11.06.46 AM.jpeg",
    r"C:\Users\hansc\Downloads\WhatsApp Image 2023-09-19 at 11.06.33 AM.jpeg",
    r"C:\Users\hansc\Downloads\WhatsApp Image 2023-09-19 at 11.06.22 AM.jpeg",
    r"C:\Users\hansc\Downloads\WhatsApp Image 2023-09-19 at 12.03.42 PM.jpeg",
]

df = tesser_ocr(
    piclist=piclist,
    tesser_path=r"C:\Program Files\Tesseract-OCR\tesseract.exe",
    add_after_tesseract_path="",
    add_at_the_end="-l eng+por --psm 3",
    processes=5,
    chunks=5,
    print_stdout=False,
    print_stderr=True,
)

#         aa_text  aa_start_x  aa_start_y  aa_end_x  aa_end_y aa_object aa_type  aa_element_index  aa_page  aa_index aa_language aa_parents aa_all_children aa_direct_children aa_tag  aa_x_size  aa_x_descenders  aa_x_ascenders  aa_x_wconf  aa_baseline_1  aa_baseline_2  aa_document_index  aa_width  aa_height  aa_area  aa_center_x  aa_center_y
# 7  Ameta-markup         802         318       922       335      word    word                 1        1         3        <NA>     (4, 5)              ()                 ()   span       <NA>             <NA>            <NA>        77.0           <NA>           <NA>                  0       120         17     2040          862          326
# 8     language,         933         321      1001       335      word    word                 1        1         4        <NA>     (4, 5)              ()                 ()   span       <NA>             <NA>            <NA>        96.0           <NA>           <NA>                  0        68         14      952          967          328
# 9          used        1014         318      1050       331      word    word                 1        1         5        <NA>     (4, 5)              ()                 ()   span       <NA>             <NA>            <NA>        96.0           <NA>           <NA>                  0        36         13      468         1032          324


    Perform OCR on a list of images using Tesseract.

    Parameters:
    - piclist (list): List of image file paths.
    - tesser_path (str): Path to the Tesseract executable.
    - add_after_tesseract_path (str): Additional parameters to add after the Tesseract path.
    - add_at_the_end (str): Additional parameters to add at the end of Tesseract command.
    - processes (int): Number of parallel processes for image processing.
    - chunks (int): Number of chunks to divide the image list for parallel processing.
    - print_stdout (bool): Whether to print standard output during execution.
    - print_stderr (bool): Whether to print standard error during execution.

    Returns:
    - pd.DataFrame: A DataFrame containing parsed OCR results.

```