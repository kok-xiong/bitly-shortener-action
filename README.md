# Bitly URL Shortener

## Usage

Input bitly developer token and long URL to output short URL.

## Example usage (workflow in .github/workflows)

```yaml
name: Bitly Shortener
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@master

      - name: Set up Python 3.7
        uses: actions/setup-python@v1
        with:
          python-version: "3.7"

      - name: Bitly shortener
        id: shortener
        uses: kok-xiong/test-actions@master
        with:
          bitlyToken: ${{ secrets.BITLY_TOKEN }}
          longURL: https://github.com/${{ github.repository }}/commit/${{ github.sha }}

      - name: outputs
        run: echo "${{ steps.shortener.outputs.shortURL }}" / https://github.com/${{ github.repository }}/commit/${{ github.sha }}
```

Other examples of workflows in .github/workflows:
- https://github.com/kok-xiong/test-actions/blob/master/.github/workflows/python.yml - Send Bitly shortened URL to Telegram.

## Inputs

| Input                                             | Description                                        |
|------------------------------------------------------|-----------------------------------------------|
| `bitlyToken`  | Mandatory Bitly developer token (put in secrets of repository settings)    |
| `longURL`  | Mandatory long URL (example: Github commit URL)    |

## Outputs

| Output                                             | Description                                        |
|------------------------------------------------------|-----------------------------------------------|
| `shortURL`  | Short URL output (returns 'https://bit.ly/2U7tDCX')    |
