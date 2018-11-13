# Logo-Extractor
Crawler which extracts logos from websites

## Cloning Crawler

```
git clone git@github.com:Isabek/Logo-Extractor.git ~/projects/Logo-Extractor
```

## Installation 

### Virtual Environment 

Install [virtualenv](https://virtualenv.pypa.io/en/latest/installation/) and create virtual environment for crawler.

```
cd ~/projects/Logo-Extractor
```

```
virtualenv -p python3 venv
```

### Install Dependencies

```
pip install -r requirements.txt
```

## Install Chrome driver

You can download Chrome driver [here](http://chromedriver.chromium.org/home) and install it.

If you use Ubuntu you can install like this:

```
wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
sudo chown ${USER}:${GROUP} /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver
```

Run chrome headless driver

```
chromedriver --url-base=/wd/hub
```

## Usage

```
scrapy runspider spider.py -a input_file_path=logo-extraction.txt -o result.json
```

```input_file_path``` - localtion of file which contains websites

```o``` - output file

Format should be as shown below

```
Webpage Url,Logo Url
http://ground-truth-data.s3-website-us-east-1.amazonaws.com/autoglassforyou.com,http://ground-truth-data.s3-website-us-east-1.amazonaws.com/autoglassforyou.com/images/logo-change.gif
```

## Checker

Crawler writes results to json file. Example: ```result.json```. 

If you want to check how accuracy of extracted logos run next command

```
python checker.py -actual logo-extraction.txt -json result.json
```
