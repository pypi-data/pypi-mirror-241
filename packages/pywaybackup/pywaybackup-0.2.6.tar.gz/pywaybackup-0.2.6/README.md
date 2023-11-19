# archive wayback downloader

![Version](https://img.shields.io/badge/Version-0.2.6-blue)
![Release](https://img.shields.io/badge/Release-alpha-red)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Downloading archived web pages from the [Wayback Machine](https://archive.org/web/).

Internet-archive is a nice source for several OSINT-information. This script is a work in progress to query and fetch archived web pages.

This project is not intended to get fast results. Moreover it is a tool to get a lot of data over a long period of time.

## Limitations

The wayback-machine does refuse connections over public access if the query rate is too high. So for now there seems no possibility to implement a multi-threaded download. As soon as a connection is refused, the script will wait and retry the query. Existing projects seem to ignore this limitation and just rush through the queries. This resulted in a lot of missing files and probably missing knowledge about the target.

Timeout seems to be about 2.5 minutes per 20 downloads.

## Installation

### Pip

1. Install the package <br>
   ```pip install pywaybackup```
2. Run the script <br>
   ```waybackup -h```

### Manual

1. Clone the repository <br>
   ```git clone https://github.com/bitdruid/waybackup.git```
2. Install requirements <br>
   ```pip install -r requirements.txt```
3. Run the script <br>
   ```python waybackup.py -h```

## Usage

This script allows you to download content from the Wayback Machine (archive.org). You can use it to download either the latest version or all versions of web page snapshots within a specified range.

### Basic Command

`python script_name.py [-h] [-v] -u URL {-c | -f} [-l] [-r RANGE] [-o OUTPUT] [--retry-failed [RETRY_FAILED]]`


### Arguments

- `-h`, `--help`: Show the help message and exit.
- `-v`, `--version`: Show the script's version.

#### Required Arguments

- `-u URL`, `--url URL`: The URL of the web page to download. This argument is required.

#### Mode Selection (Choose One)

- `-c`, `--current`: Download the latest version of each file snapshot. This option is mutually exclusive with `-f/--full`.
- `-f`, `--full`: Download snapshots of all timestamps. This option is mutually exclusive with `-c/--current`.

#### Optional Arguments

- `-l`, `--list`: Only print the snapshots available within the specified range. Does not download the snapshots.
- `-r RANGE`, `--range RANGE`: Specify the range in years for which to search and download snapshots.
- `-o OUTPUT`, `--output OUTPUT`: The folder where downloaded files will be saved.

#### Special Features

- `--retry-failed [RETRY_FAILED]`: Retry failed downloads. You can specify the number of retry attempts as an integer. If no number is provided, the script will keep retrying indefinitely.

### Examples

Download latest snapshot of all files:<br>
`waybackup -u http://example.com -c`

Download latest snapshot of all files with retries:<br>
`waybackup -u http://example.com -c --retry-failed 3`

Download all snapshots sorted per timestamp with a specified range:<br>
`waybackup -u http://example.com -f -r 5`

Download all snapshots sorted per timestamp with a specified range and save to a specified folder:<br>
`waybackup -u http://example.com -f -r 5 -o /home/user/Downloads/snapshots`

List available snapshots per timestamp without downloading:<br>
`waybackup -u http://example.com -f -l`

## Contributing

I'm always happy for some feature requests to improve the usability of this script.
Feel free to give suggestions and report issues. Project is still far from being perfect.