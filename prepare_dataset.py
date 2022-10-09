#!/usr/bin/env python
from zipfile import PyZipFile
from pathlib import Path
import os
import shutil
from pypinyin import pinyin, Style
import pypinyin

import click
from tqdm import tqdm

@click.command()
@click.option("--input-dir", type=Path,
              help="Path to esd dataset in zip.")
@click.option("--output-dir", type=Path, default="trimmed",
              help="outdir")
def main(input_dir: Path, output_dir: Path) -> None:
    
    output_dir.mkdir(exist_ok=True, parents=True)

    for audio_path in  tqdm(list(input_dir.rglob("*.wav"))):
        text_path = audio_path.parent / (audio_path.stem + ".txt")
        with open(text_path) as fil:
            text = fil.read()
        translite = to_translite(text)
        lab_path = output_dir / (audio_path.stem + ".lab")
        with open(lab_path, 'w') as fil:
            fil.write(translite)
        audio_path.rename(output_dir / audio_path.name)
    
    shutil.rmtree(input_dir)

def to_translite(text: str) -> str:
    translite = ""
    for i, sym in enumerate(text):
        if i == len(text) - 1:
            translite += pinyin(sym, style=Style.TONE3, neutral_tone_with_five=True)[0][0]
        else:
            translite += pinyin(sym, style=Style.TONE3, neutral_tone_with_five=True)[0][0] + " "
    return translite


if __name__ == "__main__":
    main()


