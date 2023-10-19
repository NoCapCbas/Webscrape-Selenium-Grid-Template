link to blog:
https://medium.com/dev-genius/docker-python-selenium-the-quickest-way-to-start-web-scraping-6c47248c69c3

### Build container
'bash
docker build -t webscrape_example .
'

### Run container 
'bash 
docker run -d -p 4444:4444 -p 7900:7900 --shm-size="2g" my_custom_selenium_chrome


'
