# Number Test

## Boilerplate package with example numerical tests.

[![status: experimental](https://github.com/GIScience/badges/raw/master/status/experimental.svg)](https://github.com/GIScience/badges#experimental)
![build: status](https://github.com/StephenRicher/number_test/actions/workflows/tests.yaml/badge.svg)

## Table of contents

* [Features](#features)
* [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)

## Features

A brief description of the projects primary features.

## Installation

Installation is possible via `pip` as shown below.

Unix/macOS
```bash
python3 -m pip install number_test
```

Windows
```bash
py -m pip install number_test
```

#### Alternative Install Methods (optional)

<details>
  <summary><strong>1. Install within a Virtual Environment</strong></summary>

<details>
  <summary><strong>Unix/macOS</strong></summary>

```bash
python -m venv number_test
source number_test/bin/activate
python3 -m pip install number_test
```
</details>

<details>
  <summary><strong>Windows</strong></summary>

```bash
py -m venv number_test
number_test/Scripts/Activate.ps1
py -m pip install number_test
```

If running scripts is disabled on your system then run the following command before activating your environment.

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
</details>
</details>

<details>
<summary><strong>2. Install within a Docker container</strong></summary>

See [here](./docker/README.md) for detailed guidance.

</details>

## Usage

```console
stephen@pc:$ number_test --help
usage: number_test [-h] [--version] [--verbose] Commands ...

Boilerplate package with example numerical tests.

optional arguments:
  -h, --help  show this help message and exit
  --version   show program's version number and exit
  --verbose   verbose logging for debugging

required commands:

  Commands    Description:
    prime     Check if a number is prime.
    fib       Check if a number is part of the fibonacci sequence.

Stephen Richer, (stephen.richer@proton.me)
```

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create.
Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

See [CONTRIBUTING.md](./CONTRIBUTING.md) for detailed guidance.

## License

Distributed under the MIT License. _See [LICENSE](./LICENSE) for more information._

### Contact

If you have any other questions please contact the author, [Stephen Richer](mailto:stephen.richer@proton.me?subject=[GitHub]%20number_test).
