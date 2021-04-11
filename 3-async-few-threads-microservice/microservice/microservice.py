import fastapi
import httpx
from scrapy.selector import Selector

api = fastapi.FastAPI()

@api.get('/api/weather/{city}')
async def weather(city: str):
    url = f'https://pogoda.mail.ru/prognoz/{city}/'

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()

    selector = Selector(text=response.text)
    t = selector.xpath('//div[@class="information__content__temperature"]/text()').getall()[1].strip()

    return {'city':city, 'temperature':t, 'source':'pogoda.mail.ru'}


