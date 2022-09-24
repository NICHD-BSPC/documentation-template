This repository shows how to set up, write, build, and publish documentation on
GitHub Pages using GitHub Actions.

Once set up, on every push to GitHub, your docs will be built in a temporary space using GitHub Actions. 
Your built docs will be uploaded as an artifact, which means that if you're on
a pull request you can inspect the results.

Docs will be published only from the the `main` branch, and will be publicly
available at `USER`.github.io/`PROJECT`.

For details, see the automatically-built documentation at
https://nichd-bspc.github.io/documentation-template, which is itself built
using these methods.
