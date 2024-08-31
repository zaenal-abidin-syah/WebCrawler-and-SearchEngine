import scrapy
import csv

class DoujinSpider(scrapy.Spider):
    name = "DoujinSpider"
    start_urls = [
      'https://doujindesu.tv/series/',
      ]

    def parse(self, response):
        # Mendapatkan daftar tautan artikel
        article_links = response.css('entries entry a::attr(href)').extract()
        for link in article_links:
            yield scrapy.Request(link, callback=self.parse_article)

    def parse_article(self, response):
      print('response = ',response)
        # judul = response.css('h1.read__title::text').get()
        # waktu = response.css('div.read__time::text').get()
        # url = response.url
        # konten = response.css('div.read__content').xpath('string()').get()
        # kelas = response.css('li.breadcrumb__item:nth-child(2) span::text').get()

        # # Menyimpan data ke dalam file CSV
        # with open('hasil_scrap1.csv', 'a', newline='', encoding='utf-8') as file:
        #     writer = csv.writer(file)
        #     # Menulis baris data
        #     if file.tell() == 0:
        #         # Menulis nama kolom jika file masih kosong
        #         writer.writerow(['Judul', 'Waktu', 'URL', 'Kelas', 'Konten'])
        #     writer.writerow([judul, waktu, url, kelas, konten.strip()])