# Nike Scraper Bot

## Overview

This project is a Discord bot designed to fetch and display Nike product information based on SKU codes provided by users in a specific channel. The bot uses the `requests` library to scrape data from Nike's website and the `discord.py` library to interact with Discord.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Weeshsh/DC-check-stock-nike.git
   ```
2. Navigate to the project directory:
   ```bash
   cd DC-check-stock-nike
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Create a `config.py` file in the project directory with the following content:

```python
CHANNEL = 'your_channel_name'
TOKEN = 'your_discord_bot_token'
SIZES = ['list', 'of', 'sizes']
```

Replace `'your_channel_name'`, `'your_discord_bot_token'`, and `['list', 'of', 'sizes']` with your actual channel name, Discord bot token, and sizes list.

## Usage

Run the bot:
```bash
python main.py
```

In the specified Discord channel, users can use the command `$nike <SKU>` to fetch and display information about the Nike product with the given SKU.

## Files

- `main.py`: The main bot script that handles Discord events and commands.
- `nike.py`: The script that scrapes Nike product data.
- `config.py`: Configuration file for storing channel name, Discord token, and sizes.

## Example Command

```
$nike DV0834-101
```

If you have any questions or need further assistance, feel free to contact the project maintainers.
