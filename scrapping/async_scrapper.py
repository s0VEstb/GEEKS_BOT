# import httpx
# import asyncio
# from parsel import Selector
# from config import bot
# from database import db
# from aiogram import Dispatcher, types
#
#
# class AsyncAnimeScrapper:
#     START_URL = "https://www.imdb.com"
#     URL = "https://www.imdb.com/list/ls058654847/?st_dt=&mode=detail&page={page}&sort=list_order,asc"
#     HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:122.0) Gecko/20100101 Firefox/122.0",
#                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
#                "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
#                "Accept-Encoding": "gzip, deflate, br"
#                }
#     LINK_XPATH = '//h3[@class="lister-item-header"]/a/@href'
#
#     async def async_generator(self, limit):
#         for i in range(1, limit + 1):
#             yield i
#
#     async def get_pages(self):
#         async with httpx.AsyncClient(headers=self.HEADERS) as client:
#             response = await client.get(url=self.URL)
#             print("response-url: ", response.url)
#
#             res = await self.scrape_url(response=response)
#             return res
#
#     async def scrape_url(self, response):
#         tree = Selector(text=response.text)
#         links = tree.xpath(self.LINK_XPATH).extract()
#         #for link in links:
#             #print(self.START_URL + link)
#         return links
#
#
# async def anime_call(call: types.CallbackQuery):
#     datab = db.Database()
#     scraper = AsyncAnimeScrapper()
#     data = await scraper.get_pages()
#
#     for link in data[:5]:
#         datab.sql_insert_anime_link(link=link)
#         await bot.send_message(
#             chat_id=call.from_user.id,
#             text=scraper.START_URL + link
#         )
#
# def register_anime_scrapper(dp: Dispatcher):
#     dp.register_callback_query_handler(anime_call,
#                                        lambda call: call.data == "anime")
#
#
#
# if __name__ == '__main__':
#     scraper = AsyncAnimeScrapper()
#     asyncio.run(scraper.get_pages())
#
#
#
#
