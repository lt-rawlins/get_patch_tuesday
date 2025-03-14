# Get Patch Tuesday

`get-patch-tuesday` is a Python script that retrieves the dates for Microsoft's Patch Tuesday updates.

## Features

- Fetch Patch Tuesday dates for a given year.
- Output dates in a user-friendly format.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/lt-rawlins/get_patch_tuesday.git
    ```
2. Navigate to the project directory:
    ```sh
    cd get_patch_tuesday
    ```
3. Install the required dependencies:
    ```sh
    pip install -e .
    ```

## Usage

**Show all patch Tuesdays for the current year:**

```sh
get-patch-tuesday
```

```
January 14 2025
February 11 2025
March 11 2025
April 8 2025
May 13 2025
June 10 2025
July 8 2025
August 12 2025
September 9 2025
October 14 2025
November 11 2025
December 9 2025
```

**Show all patch Tuesdays for a given year:**

```sh
get-patch-tuesday 2026
```

```
January 13 2026
February 10 2026
March 10 2026
April 14 2026
May 12 2026
June 9 2026
July 14 2026
August 11 2026
September 8 2026
October 13 2026
November 10 2026
December 8 2026
```

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE Version 3 License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

