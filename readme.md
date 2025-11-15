# BG3 XML Dialogue Label Maker

## This is a WIP!! It will get easier to use over time. Especially once it has GUI lol. But it's scuffed rn as I find time to finetune it.

### Current features:
- Given a loca index and the lsx dialogue file, it will add the human-readable text to the lsx file above the tagtext!
- It comes with the English loca already databased
- If you would rather work with subtitles in another language, you can also extract that loca file and use the create_loca_db script to use that instead

### Future goals:
- A GUI
- Ability to label multiple files at once (i.e. pass it a folder)
- Ability to index and label flags and tags
- Handle switching between multiple loca_dbs (for ppl writing custom dialogues) without having to re-index or keep editing the py file

## How to use:
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
- Edit the file path to point to the loca/flag/tag list you want to index in the file `build_indices.py`
    - Note the path is relative!
- Run `python3 build_indices.py` in the pipenv shell

### Adding labels to your LSX
- Edit `label_maker.py` to change the file paths and names where indicated (search `EDIT`)
- Run `python3 label_maker.py` in the pipenv shell
