# genshin-builds

## What this is

This is a CLI that aims to scrape
[Genshin Impact Helper Team's Character Builds](https://docs.google.com/spreadsheets/d/1gNxZ2xab1J6o1TuNVWMeLOZ7TPOqrsf3SshP5DLvKzI/htmlview#)
in hopes of escaping the horrible UX of a spreadsheet

## Requirements

- [uv](https://docs.astral.sh/uv/getting-started/installation/) (I keep my installation at latest so not sure what would be the minimum supported uv version)

## How to use this?

> [!WARNING]
>
> This section will be updated in the future based on how the project progresses

1. Clone this repo

   ```sh
   git clone https://github.com/Van-sh/genshin-builds
   ```

2. Install dependencies

   ```sh
   uv sync
   ```

## Contributing
>
> [!WARNING]
>
> This section will be updated in the future based on how the project progresses

If you are looking to make a PR, make sure you have made an issue first!

1. Clone this repo

   ```sh
   git clone https://github.com/Van-sh/genshin-builds
   ```

2. Install dependencies including the test group which installs unittest-parallel for running the tests concurrently

   ```sh
   uv sync
   ```

3. Get local copies of the build sheet's html

   ```sh
   uv run poe setup:files
   ```
