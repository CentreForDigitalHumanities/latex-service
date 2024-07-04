[![DOI](https://zenodo.org/badge/686339559.svg)](https://zenodo.org/doi/10.5281/zenodo.10571416)
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

# LaTeX Service

LaTeX Service contains everything needed to create a small containerised Flask server with a `latexmk` and `texlive` installation. It is used in combination with [Spindle Server](https://github.com/UUDigitalHumanitieslab/spindle-server) as a dependency of [ParsePort](https://github.com/UUDigitalHumanitieslab/parseport).

## Contents

This repository uses `texlive-latex-extra`, which includes an extensive set of additional packages needed for the [ParsePort](https://github.com/UUDigitalHumanitieslab/parseport). There are, however, several other `texlive` packages out there. (An overview and discussion can be found [here](https://tex.stackexchange.com/questions/245982/differences-between-texlive-packages-in-linux).) These packages vary greatly in size and a choice for one or another could drastically impact the size of the image.

## Prerequisites

A host machine with Docker installed.

## Usage

1. Build an image with `docker build -t latex-service:latest .`

2. Run a container and expose a port with `docker run -d -p 32769:5000 --name latex-service latex-service`

3. Send a request with a `.tex` string as its body to 5000.

4. The response should contain the PDF in byte string format.

## Clean up

The LaTeX compiler creates auxiliary files with a uniquely created ID in the name, which are not automatically removed. For production use, it is recommended that you periodically clean up these files. You can do this by running `docker exec -it latex-service /bin/bash` and then running `latexmk -C` (for the auxiliary files) followed by `rm *.tex` for the source files. If you have `cron` on the server, you may want to add the job in `Crontab`, which performs this cleanup once a day. Make sure to change the name of the container name in the command above if it is named differently on your system.

## Licence

LaTeX Service is shared under a BSD 3-Clause licence. See [LICENSE](./LICENSE) for more information.

## Citation

If you wish to cite this repository, please use the metadata provided in our [CITATION.cff file](./CITATION.cff).

## Contact

For questions, small feature suggestions, and bug reports, feel free to [create an issue](https://github.com/UUDigitalHumanitieslab/latex-service/issues/new). If you do not have a Github account, you can also [contact the Centre for Digital Humanities](https://cdh.uu.nl/contact/).