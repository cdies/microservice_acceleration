import fastapi
import httpx
from scrapy.selector import Selector
import redis

api = fastapi.FastAPI()
redis = redis.Redis(host='redis', port=6379, db=0)

@api.get('/api/weather/{city}')
def weather(city: str) -> dict:
    # get cache from memory
    cache = redis.get(city)

    # check value from cache, if exists return it
    if cache is not None:
        return {'city':city, 'temperature':cache, 'source':'cache'}

    url = f'https://pogoda.mail.ru/prognoz/{city}/'

    with httpx.Client() as client:
        response = client.get(url)
        response.raise_for_status()

    selector = Selector(text=response.text)
    t = selector.xpath('//div[@class="information__content__temperature"]/text()').getall()[1].strip()

    # save cache in memory for 1 hour
    redis.set(city, t, ex=3600)

    return {'city':city, 'temperature':t, 'source':'pogoda.mail.ru'}
