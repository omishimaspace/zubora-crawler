TAG=0.1
REPO=zubora
SPIDER_NAME=
DOMAIN=
URL=
CMD=docker run --rm -it -v `pwd`/zubora_crawler:/usr/src/app zubora:0.1
SCRAPY=${CMD} scrapy

build:
	docker build -t ${REPO}:${TAG} .

shell:
	${CMD} /bin/sh

spider:
	${SCRAPY} genspider ${SPIDER_NAME} ${DOMAIN}

scrapyshell:
	${SCRAPY} shell ${URL}

run:
	${SCRAPY} runspider zubora_crawler/spiders/${SPIDER_NAME}.py


