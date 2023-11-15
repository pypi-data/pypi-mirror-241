import ctypes
import os
import platform
import re
import subprocess
import sys
import tempfile
from collections import defaultdict
from functools import cache
import cv2
import numpy as np
from a_cv_imwrite_imread_plus import open_image_in_cv
from touchtouch import touch
import pandas as pd
from a_pandas_ex_apply_ignore_exceptions import pd_add_apply_ignore_exceptions
from multiprocca import start_multiprocessing
from multiprocca.proclauncher import MultiProcExecution
pd_add_apply_ignore_exceptions()
from lxml import etree, html
from ast import literal_eval


@cache
def get_short_path_name(long_name):
    try:
        if not iswindows:
            return long_name
        output_buf_size = 4096
        output_buf = ctypes.create_unicode_buffer(output_buf_size)
        _ = _GetShortPathNameW(long_name, output_buf, output_buf_size)
        return output_buf.value
    except Exception as e:
        sys.stderr.write(f"{e}\n")
        return long_name


iswindows = "win" in platform.platform().lower()
if iswindows:
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    startupinfo.wShowWindow = subprocess.SW_HIDE
    creationflags = subprocess.CREATE_NO_WINDOW
    invisibledict = {
        "startupinfo": startupinfo,
        "creationflags": creationflags,
        "start_new_session": True,
    }
    from ctypes import wintypes

    windll = ctypes.LibraryLoader(ctypes.WinDLL)
    kernel32 = windll.kernel32
    _GetShortPathNameW = kernel32.GetShortPathNameW
    _GetShortPathNameW.argtypes = [wintypes.LPCWSTR, wintypes.LPWSTR, wintypes.DWORD]
    _GetShortPathNameW.restype = wintypes.DWORD
else:
    invisibledict = {}



def get_tmpfile(suffix=".png"):
    tfp = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    filename = tfp.name
    filename = os.path.normpath(filename)
    tfp.close()
    touch(filename)
    return filename


def start_tesser(ini, tesseractcommand, txtresults, txtout, files2delete, **kwargs):
    r"""
    Execute Tesseract OCR on an image and parse the results.

    Parameters:
    - ini (int): The document index.
    - tesseractcommand (str): The Tesseract OCR command.
    - txtresults (str): The path to the OCR results file in hOCR format.
    - txtout (str): The path to the temporary text output file.
    - files2delete (tuple): Tuple of file paths to be deleted after processing.
    - **kwargs: Additional keyword arguments for subprocess.run.

    Returns:
    - pd.DataFrame: A DataFrame containing parsed OCR results.
    """
    try:
        exec ("""
import os
import sys
import platform
# import re
import subprocess
import tempfile
from collections import defaultdict
from functools import cache
import numpy as np
import pandas as pd
from a_pandas_ex_apply_ignore_exceptions import pd_add_apply_ignore_exceptions
pd_add_apply_ignore_exceptions()
from lxml import etree, html
from ast import literal_eval        
        """, globals())

        idcounter = 0
        iswindows = "win" in platform.platform().lower()
        if iswindows:
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            startupinfo.wShowWindow = subprocess.SW_HIDE
            creationflags = subprocess.CREATE_NO_WINDOW
            invisibledict = {
                "startupinfo": startupinfo,
                "creationflags": creationflags,
                "start_new_session": True,
            }
        else:
            invisibledict = {}

        def fia(el, h):
            nonlocal idcounter
            elhash = hash(el)
            if elhash not in newids:
                newids[elhash] = int(idcounter)
                idcounter += 1
            if elhash not in allitems:
                allitems[elhash] = el
            if not hasattr(el, "getchildren"):
                method = el.iter
            else:
                method = el.getchildren
            for j in method():
                fia(j, h + (elhash,))
                allparents[hash(j)].update(h)
                allparentschildren[elhash].add(hash(j))

        kwargs.update(invisibledict)
        subprocess.run(tesseractcommand, **kwargs)
        with open(txtresults + ".hocr", mode="r", encoding="utf-8") as f:
            data = f.read()
        files2delete = list(files2delete)
        files2delete.extend([txtout, txtresults, txtresults + ".hocr"])

        allitems = {}
        allparents = defaultdict(set)
        allparentschildren = defaultdict(set)

        newids = {}
        tree = html.fromstring(data.encode())
        fia(tree, ())
        allparents = {k: frozenset(v) for k, v in allparents.items()}
        allparentschildren = {k: frozenset(v) for k, v in allparentschildren.items()}
        df = pd.DataFrame(pd.Series(allitems))
        df["aa_element_id"] = df.index.__array__().copy()
        df["aa_parents"] = df.index.map(allparents)
        allchildren = defaultdict(set)
        for k, v in allparents.items():
            for vv in v:
                allchildren[vv].add(k)
        allchildren2 = {}
        for k in allchildren:
            allchildren2[k] = frozenset(allchildren[k])
        df["aa_all_children"] = df.index.map(allchildren2)
        df["aa_direct_children"] = df.index.map(allparentschildren)
        df["aa_tag"] = df[0].ds_apply_ignore(pd.NA, lambda q: q.tag)

        def parse_text(h):
            try:
                tco = "\n".join(([str(x.text_content()) for x in h])).strip()
                if not tco:
                    return etree.tostring(
                        h, method="text", encoding="unicode", with_tail=True
                    ).strip()
                return tco
            except Exception:
                try:
                    return etree.tostring(
                        h, method="text", encoding="unicode", with_tail=True
                    ).strip()
                except Exception:
                    return ""

        df["aa_text"] = df[0].ds_apply_ignore(pd.NA, lambda q: parse_text(q))
        df["aa_items"] = df[0].ds_apply_ignore(
            ((None, None),), lambda q: tuple(q.items())
        )
        mava = df.aa_items.apply(len).max()
        dfitems = df.aa_items.apply(
            lambda x: x + tuple(([pd.NA] * (mava - len(x))))
        ).apply(pd.Series)

        dfitems.columns = ["tesser_" + str(x) for x in dfitems.columns]
        df = df.merge(dfitems, right_index=True, left_index=True)
        df.reset_index(drop=True, inplace=True)
        for t in [x for x in df.columns if str(x).startswith("tesser_")]:
            df[t] = df[t].ds_apply_ignore(pd.NA, lambda q: q[1])
        df.tesser_0 = df.tesser_0.str.split("_").str[-1]
        splitind = df.loc[~df[df.columns[-1]].isna()].index.__array__()
        spli = np.array_split(df, splitind)[1:]
        df = pd.concat(
            [x.assign(aa_element_index=i) for i, x in enumerate(spli)],
            ignore_index=True,
        )
        df = pd.concat(
            [
                df,
                df.tesser_1.str.split("_")
                .apply(pd.Series)[[0, 1, 2]]
                .rename(columns={0: "aa_type", 1: "aa_page", 2: "aa_index"}),
            ],
            axis=1,
        )
        df.rename(columns={"tesser_0": "aa_object"}, inplace=True)
        df.drop(columns="tesser_1", inplace=True)
        df.tesser_2 = df.tesser_2.str.strip()
        df["aa_language"] = df.tesser_2.str.extract(r"^(?P<aa_language>[^\s]+)$")
        df["tessertemp"] = df.tesser_2 + " " + df.tesser_3.fillna("")
        df = pd.concat(
            [
                df,
                df["tessertemp"]
                .str.extractall(
                    r"bbox\s+(?P<start_x>\d+)\s+(?P<start_y>\d+)\s+(?P<end_x>\d+)\s+(?P<end_y>\d+)\s*"
                )
                .reset_index(drop=True)
                .astype("Int64"),
            ],
            axis=1,
        )
        df.tessertemp = df.tessertemp.str.split(";").str[1:]
        tmpd = []
        _ = df.ds_apply_ignore(
            pd.NA,
            lambda q: pd.NA
            if not tmpd.append(
                [q.name, [x.strip().split(maxsplit=1) for x in q.tessertemp]]
            )
            else pd.NA,
            axis=1,
        )

        @cache
        def astli(x):
            try:
                return literal_eval(x)
            except Exception:
                return x

        for i, t in tmpd:
            if t:
                for tt in t:
                    df.at[i, f"aa_{tt[0]}"] = astli(tt[1])
        missing = object()
        baselines = df.aa_baseline.str.extractall(
            r"^(?P<aa_baseline_1>[^\s]+)\s+(?P<aa_baseline_2>[^\s]+)"
        ).reset_index()
        bale = baselines.level_0.__array__()
        df.loc[bale, "aa_baseline_1"] = baselines["aa_baseline_1"].astype("Float64")
        df.loc[bale, "aa_baseline_2"] = baselines["aa_baseline_2"].astype("Float64")
        df.reset_index(drop=True, inplace=True)
        lookupdict1 = df.aa_element_id.to_dict()
        lookupdict2 = {v: k for k, v in lookupdict1.items()}
        df.aa_parents = df.aa_parents.ds_apply_ignore(
            (),
            lambda x: tuple(
                sorted(
                    list(
                        (
                            q
                            for q in (set((lookupdict2.get(y, missing) for y in x)))
                            if q is not missing
                        )
                    )
                )
            ),
        )
        df.aa_all_children = df.aa_all_children.ds_apply_ignore(
            (),
            lambda x: tuple(
                sorted(
                    list(
                        (
                            q
                            for q in (set((lookupdict2.get(y, missing) for y in x)))
                            if q is not missing
                        )
                    )
                )
            ),
        )
        df.aa_direct_children = df.aa_direct_children.ds_apply_ignore(
            (),
            lambda x: tuple(
                sorted(
                    list(
                        (
                            q
                            for q in (set((lookupdict2.get(y, missing) for y in x)))
                            if q is not missing
                        )
                    )
                )
            ),
        )
        df.drop(
            columns=[
                0,
                "aa_element_id",
                "aa_items",
                "tesser_2",
                "tesser_3",
                "tessertemp",
                "aa_baseline",
            ],
            inplace=True,
        )

        for f in files2delete:
            try:
                os.remove(f)
            except Exception:
                continue

        df = (
            df[
                [
                    "aa_text",
                    "start_x",
                    "start_y",
                    "end_x",
                    "end_y",
                    "aa_object",
                    "aa_type",
                    "aa_element_index",
                    "aa_page",
                    "aa_index",
                    "aa_language",
                    "aa_parents",
                    "aa_all_children",
                    "aa_direct_children",
                    "aa_tag",
                    "aa_x_size",
                    "aa_x_descenders",
                    "aa_x_ascenders",
                    "aa_x_wconf",
                    "aa_baseline_1",
                    "aa_baseline_2",
                ]
            ]
            .astype(
                {
                    "aa_text": "string",
                    "start_x": np.int32,
                    "start_y": np.int32,
                    "end_x": np.int32,
                    "end_y": np.int32,
                    "aa_object": "string",
                    "aa_type": "string",
                    "aa_element_index": np.int32,
                    "aa_page": np.int32,
                    "aa_index": np.int32,
                    "aa_language": "string",
                    "aa_parents": object,
                    "aa_all_children": object,
                    "aa_direct_children": object,
                    "aa_tag": "string",
                    "aa_x_size": "Float64",
                    "aa_x_descenders": "Float64",
                    "aa_x_ascenders": "Float64",
                    "aa_x_wconf": "Float64",
                    "aa_baseline_1": "Float64",
                    "aa_baseline_2": "Float64",
                }
            )
            .assign(aa_document_index=ini)
        )

        df["aa_width"] = df.end_x - df.start_x
        df["aa_height"] = df.end_y - df.start_y
        df["aa_area"] = df.aa_width * df.aa_height
        df["aa_center_x"] = df.start_x + (df.aa_width // 2)
        df["aa_center_y"] = df.start_y + (df.aa_height // 2)
        df.columns = [
            f"aa_{x}" if not str(x).startswith("aa_") else x for x in df.columns
        ]
        return df
    except Exception as e:
        sys.stderr.write(f"{e}\n")
        sys.stderr.flush()
        return pd.DataFrame()


def tesser_ocr(
    piclist,
    tesser_path=r"C:\Program Files\Tesseract-OCR\tesseract.exe",
    add_after_tesseract_path="",
    add_at_the_end="-l eng+por --psm 3",
    processes=5,
    chunks=1,
    print_stdout=False,
    print_stderr=True,

):
    r"""
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
    """
    allcommands = []
    tesseractpath = get_short_path_name(tesser_path)
    for ini, pi in enumerate(piclist):
        tmpfile = get_tmpfile(suffix=".png")
        loadedimg = open_image_in_cv(pi, channels_in_output=4)
        cv2.imwrite(tmpfile, loadedimg)

        txtout = get_tmpfile(suffix=".txt")
        txtresults = get_tmpfile(suffix=".txt")
        files2delete = [tmpfile]
        with open(txtout, mode="w", encoding="utf-8") as f:
            f.write(tmpfile)

        tesseractcommand = rf"""{tesseractpath} {add_after_tesseract_path} {txtout} {txtresults} hocr {add_at_the_end}"""
        tesseractcommand = re.sub(r" +", " ", tesseractcommand)
        allcommands.append(
            (ini, tesseractcommand, txtresults, txtout, tuple(files2delete))
        )
    f = [
        MultiProcExecution(fu=start_tesser, args=x, kwargstuple=()) for x in allcommands
    ]
    formatted_results, raw_data = start_multiprocessing(
        it=f,
        usecache=True,
        processes=processes,
        chunks=chunks,
        print_stdout=print_stdout,
        print_stderr=print_stderr,
    )
    return pd.concat([x[1] for x in formatted_results.items()], ignore_index=True)


