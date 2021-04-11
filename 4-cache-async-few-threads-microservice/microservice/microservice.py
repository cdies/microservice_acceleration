import fastapi
import httpx
from scrapy.selector import Selector
import aioredis

api = fastapi.FastAPI()

@api.get('/api/weather/{city}')
async def weather(city: str):
    redis = await aioredis.create_redis(address=('redis', 6379))
    cache = await redis.get(city)

    if cache is not None:
        return {'city':city, 'temperature':cache, 'source':'cache'}

    url = f'https://pogoda.mail.ru/prognoz/{city}/'

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()

    selector = Selector(text=response.text)
    t = selector.xpath('//div[@class="information__content__temperature"]/text()').getall()[1].strip()

    await redis.set(city, t, expire=3600)

    return {'city':city, 'temperature':t, 'source':'pogoda.mail.ru'}


