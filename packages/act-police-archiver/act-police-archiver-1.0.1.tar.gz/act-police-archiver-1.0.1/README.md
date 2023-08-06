# ACT Police Media Release Archiver

A tool I've made to keep archives of ACT Policing's Media Releases.

---

PyPI: [https://pypi.org/project/act-police-archiver/](https://pypi.org/project/act-police-archiver/)

## Setup

### With pip

```sh
pip3 install act-police-archiver
```

### Manual

Install `poetry`:

```sh
pip3 install poetry
```

Update dependencies:

```sh
poetry update
```

## Usage

### Run as a script

To export all media releases to a specific directory (e.g your Desktop), run this command:

```sh
poetry run py -m act_police_archiver -o /path/to/desktop
```

This will start downloading every media release on ACT Police's website.

To download a specific release, run this command:

```sh
poetry run py -m act_police_archiver -o /path/to/desktop -p <url of media release>
```

### Import code

You can also import the code as a module if you want to access specific functions like this:

```py
import act_police_archiver

# Example:
act_police_archiver.scrape_release('someurl', '/path/to/folder')
```