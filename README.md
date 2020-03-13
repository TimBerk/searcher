# Search-program

Console search-program

## Installation

```console
git clone https://github.com/TimBerk/searcher
python install setup.py
cd dist
pip install searcher-0.1-py3-none-any.whl
```

## Usage

```console
# Help of the programm
searcher -h
usage: searcher [-h] [-r [RECURSE [RECURSE ...]]] [-d RECURSE_DEEP]
                [-f FORMAT]
                request {google,rambler,bing,yahoo} count

# Search first 5 phrase "IT 2020" in Google.com
searcher "IT 2020" google 5
IT-Events: https://it-events.com/
Кем работать в IT в 2020 году — список перспективных ...: https://rb.ru/opinion/kem-rabotat-v-it/
город IT: увидимся осенью 2020 года!: https://gorod.it/
Международные выставки ИТ/IT digital электронной ...: https://worldexpo.pro/sector/it-it-digital-elektronnaya-kommerciya
ИТ конференции и мероприятия ИТ в 2020 году - ICT2go: https://ict2go.ru/events/
```

You can use 4 different search site as Google, Rambler, Bing and Yahoo.  
Also  you can output searched data in 3 way:
- console
- json file
- csv file
