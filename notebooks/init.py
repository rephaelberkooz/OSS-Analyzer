import marimo

__generated_with = "0.14.13"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import pandas as pd

    import sh

    import os

    from dotenv import load_dotenv
    return load_dotenv, os, sh


@app.cell
def _(load_dotenv, os):
    load_dotenv()


    whisper_repo_path = os.getenv("WHISPER_FOLDER_ROOT")
    return (whisper_repo_path,)


@app.cell
def _(sh, whisper_repo_path):
    # https://git-scm.com/book/en/v2/Git-Internals-Git-Objects

    sh.cd(whisper_repo_path)
    sh.ls()
    return


if __name__ == "__main__":
    app.run()
