# Melon10

A small Python project that retrieves and displays the current Melon realtime music chart.

## Features

- Retrieves Melon's realtime chart using an unofficial endpoint.
- Configurable chart page size.
- Displays song rankings, titles, and credited artists.
- Shows ranking movement since the previous chart.
- Marks songs without a previous ranking with `*`.

## Requirements

- Python 3.13+
- `requests`

## Setup

Clone the repository:

```bash
git clone https://github.com/abascueomni/melon10.git
cd melon10
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Usage

Run the program:

```bash
python main.py
```

The current chart page size is configured in `main.py`.

## Example Output

```text
MELON REALTIME TOP 10
Chart: YYYY.MM.DD HH:MM

1. [—] Song Title — Artist
2. [↑ 3] Song Title — Artist
3. [↓ 2] Song Title — Artist
4. [*] New Song — Artist
```

## Data Source

This project retrieves chart data from an unofficial Melon mobile endpoint. The endpoint is not an officially supported public API and may change or become unavailable without notice.

This is a personal learning project and is not affiliated with Melon.

## Project Status

Initial implementation complete. Future development may include Spotify integration and automated playlist creation.