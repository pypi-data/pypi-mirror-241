[![coverage report](https://gitlab.com/nobodyinperson/hledger-utils/badges/main/coverage.svg)](https://gitlab.com/nobodyinperson/hledger-utils/-/commits/main)
[![pipeline status](https://gitlab.com/nobodyinperson/hledger-utils/badges/main/pipeline.svg)](https://gitlab.com/nobodyinperson/hledger-utils/-/commits/main)
[![REUSE status](https://api.reuse.software/badge/gitlab.com/nobodyinperson/hledger-utils)](https://api.reuse.software/info/gitlab.com/nobodyinperson/hledger-utils)
[![PyPI version](https://badge.fury.io/py/hledger-utils.svg)](https://badge.fury.io/py/hledger-utils)
[![Downloads](https://static.pepy.tech/badge/hledger-utils)](https://pepy.tech/project/hledger-utils)

#  🛠️ `hledger` Utilities

This Python package extends [`hledger`](https://hledger.org) the [plaintextaccounting](https://plaintextaccounting.org) tool with some utilities.
 
## ✨ Features Added to `hledger`

### `hledger edit ...`: 📝 Editing `hledger` Transactions in your `$EDITOR`

```bash
# Opens your EDITOR (or VISUAL) with only transactions in € that have a Berlin tag
# You can modify them as usual, if you save and quit the editor, the changes will be
# applied to the appropriate files
hledger edit cur:€ tag:location=Berlin

# Opens your EDITOR with all transactions
hledger edit

# If you don't have LEDGER_FILE set, you need to specify a journal file as usual:
hledger edit -f journal.hledger

# More examples and explanations:
hledger edit --help
```

This should work with pretty much any hledger query, just substitute `hledger balance` or `hledger register` etc. with 'hledger edit'. This is a neat way of quickly editing transactions you were just inspecting.

🎥 Check this screencast below to see `hledger edit` in action:

[![asciicast](https://asciinema.org/a/549559.svg)](https://asciinema.org/a/549559)

### `hledger plot ...`: 📈 Plotting charts of hledger queries

```bash
# Open an interactive line chart of your assets with forecast (if available) and also save it as PNG
hledger plot -- balance  ^Assets --daily --exchange=USD --historical --forecast -o assets.png

# Help, examples and configuration options (renaming, inverting, summing, styling, etc..)
hledger plot --help
```

📈 Example plot:

![hledger plot](https://gitlab.com/nobodyinperson/hledger-utils/-/raw/main/doc/hledger-plot.png)

Note: Currently, only the `balance` command output can be plotted. `hledger-plot` has many options, check them out with `hledger-plot --help`, most notably:

- `--sum`ming and `--mean`ing columns by regex
- `--multiply`ing a column with a factor
- Filtering columns with `--drop` and `--only` regexes
- `--resample`ing to a different interval, e.g. 10 days with `--resample 10d`
- adding `--trend`s to (specific time periods of) columns and show slope in legend at configurable interval
- grouping e.g. by quarter with `--groupby quarter` to compare quarters
- `--style`ing depending on the account name

Consider converting your amounts to one currency (e.g. `-X€`) and using `--historical`. `--stacked --barplot`s are also available.

See [the `doc/` folder](https://gitlab.com/nobodyinperson/hledger-utils/-/tree/main/doc) for examples of `hledger-plot`.

## 📦 Installation

```bash
# Install this package from PyPI:
pipx install hledger-utils

# Install the latest development version:
pipx install git+https://gitlab.com/nobodyinperson/hledger-utils

# Install from the repository root
git clone https://gitlab.com/nobodyinperson/hledger-utils
cd hledger-utils
pipx install .
```

The previous commands will install `hledger-edit` and `hledger-plot` to `~/.local/bin/` by default. Make sure that directory is in your `PATH`.


This package is also available in the AUR as [`hledger-utils`](https://aur.archlinux.org/packages/hledger-utils) (latest release) and [`hledger-utils-git`](https://aur.archlinux.org/packages/hledger-utils-git) (development version).

## 📝 Changelog

Version tags (`v*`) are annotated with a summary of changes. You can view them for example [on GitLab](https://gitlab.com/nobodyinperson/hledger-utils/-/tags) or from the repository with this command:

```bash
git tag -l 'v*' -n99 --sort=-version:refname --format='%(color:green)%(refname:strip=2)%(color:yellow) (%(color:cyan)%(creatordate:format:%a %b %d %Y)%(color:yellow))%0a%(color:magenta)==========================%0a%0a%(color:yellow)%(contents:subject)%(color:normal)%0a%0a%(contents:body)'
```
