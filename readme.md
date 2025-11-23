# BG3 XML Dialogue Label Maker

## This is a WIP!! It will get easier to use over time. But it's scuffed rn as I find time to finetune it.

### Current Script features:
- Given a loca index and the lsx dialogue file, it will add the human-readable text to the lsx file above the tagtext!
- It comes with the English loca, flags, and tags already databased
- If you would rather work with subtitles in another language, you can also extract that loca file and use the build_indices script to use that instead

### Future goals:
- Handle switching between multiple loca_dbs?? (for ppl writing custom dialogues) without having to re-index or keep editing the py file
- And/or a way to expand the existing dbs with your new lines, flags, and tags.
- Make GUI better
- Error handling

## How to use:

### Windows:
[Download the latest release](https://github.com/kelocena/bg3-xml-label-maker/releases). Unzip the file and run the exe in the extracted folder.

PLEASE ONLY SELECT **.LSX** FILES IN SINGLE FILE SELECTION. I HAVEN'T ADDED PROPER ERROR HANDLING YET.

### Any OS:
You will need to either clone the repo or download the ZIP of the codebase to use it.
- Global requirement: Python 3 => https://wiki.python.org/moin/BeginnersGuide/Download
- Strong recommendation: Pipenv => https://pipenv.pypa.io/en/latest/installation.html

Short version: Pipenv allows you to manage different versions of various dependencies across multiple projects on the same machine.

### Setup
- Unzip/navigate to where you cloned the project.
- Open a terminal at that location.
- Run `pipenv shell`
- Run `pipenv install` to install the project dependecies.

All commands listed below assume you are running them in the pipenv shell!!
### Making an index
- Edit the file path to point to the loca you want to index in the file `build_indices.py`
- Run `python3 build_indices.py` in the pipenv shell

### Adding labels to your LSX
- Run `python3 .\app\index.py` in the pipenv shell
- This should open the GUI app :)