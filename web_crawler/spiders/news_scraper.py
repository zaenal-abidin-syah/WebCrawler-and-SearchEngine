import scrapy
import csv
import string

class NewsSpider(scrapy.Spider):
  name = "NewsScraper"
  
  start_urls = [
      "https://health.okezone.com",
      "https://health.okezone.com/sehatterkini",
      "https://health.okezone.com/hidupsehat",
      "https://health.okezone.com/medicalcheckup",
      "https://edukasi.okezone.com",
      "https://edukasi.okezone.com/sekolah",
      "https://edukasi.okezone.com/kampus",
      "https://sports.okezone.com",
      "https://bola.okezone.com",
      "https://sports.okezone.com/f1",
      "https://sports.okezone.com/motogp",
      "https://sports.okezone.com/netting",
      "https://sports.okezone.com/basket",
      "https://sports.okezone.com/sportlain",
      "https://travel.okezone.com",
      "https://travel.okezone.com/infowisata",
      "https://travel.okezone.com/destinasi",
      "https://travel.okezone.com/jalan-jalan",
      "https://travel.okezone.com/wisatakuliner"
      "https://indeks.kompas.com/?site=health",
      "https://indeks.kompas.com/?site=edukasi",
      "https://indeks.kompas.com/?site=bola",
      "https://indeks.kompas.com/?site=travel",
      "https://www.detik.com/edu",
      "https://www.detik.com/edu/sekolah",
      "https://www.detik.com/edu/edutainment",
      "https://www.detik.com/edu/beasiswa",
      "https://www.detik.com/edu/perguruan-tinggi",
      "https://health.detik.com",
      "https://health.detik.com/berita-detikhealth",
      "https://health.detik.com/diet",
      "https://health.detik.com/konsultasi",
      "https://health.detik.com/penyakit",
      "https://health.detik.com/kebugaran",
      "https://sport.detik.com",
      "https://sport.detik.com/moto-gp",
      "https://sport.detik.com/raket",
      "https://sport.detik.com/f1",
      "https://sport.detik.com/basket",
      "https://sport.detik.com/sepakbola",
      "https://sport.detik.com/sport-lain",
      "https://travel.detik.com",
      "https://travel.detik.com/travel-news",
      "https://travel.detik.com/destinations",
      "https://travel.detik.com/dtravelers",
      "https://travel.detik.com/travel-tips",
      "https://travel.detik.com/penginapan",
      ]

  def parse(self, response):

    # ambil link link berita
    article_links = self.getArticleLink(response)
    
    for link in article_links:
      yield scrapy.Request(link, callback=self.parse_article)

  def getArticleLink(self, response):
    if 'okezone.com' in response.url:
      if 'travel.okezone.com' in response.url:
        return response.css('a.desc-text::attr(href)').extract()
      else:
        return response.css('a.gabreaking::attr(href)').extract()
    elif 'kompas.com' in response.url:
    # buat kompas dll
      return response.css('a.article-link::attr(href)').extract()
      # pass
    elif 'detik.com' in response.url:
      print('crawling url = ', response.url)
      return response.css('.media__text .media__title a[dtr-act="artikel"]::attr(href)').extract()

  def parseOkezone(self, response, url):
    if 'travel.okezone.com' in url:
      judul = self.remove_text(response.css('.title-article h1::text').get())
      waktu = response.css('.journalist span::text').get()
      waktu = waktu.replace('Jurnalis', '')
      waktu = waktu.replace(',', '')
      # waktu = waktu.replace('"', '')
      waktu = waktu[2::]
      kelas = 'pariwisata'
    else:
      judul = self.remove_text(response.css('div.title h1::text').get())
      if 'health.okezone.com' in url:
        waktu = response.css('.tanggal::text').get()
        kelas = 'kesehatan'
      else:
        waktu = response.css('.namerep b::text').get()
        if 'edukasi.okezone.com' in url:
          kelas = 'pendidikan'
        elif 'bola.okezone.com' in url or 'sports.okezone' in url:
          kelas = 'olahraga'
        else:
          return None    
    konten = self.remove_text(' '.join(response.css('p').xpath('string()').getall()))
    return judul, konten, waktu, kelas

  def parseKompas(self, response, url):
    judul = self.remove_text(response.css('h1.read__title::text').get())
    waktu = response.css("div.read__time::text").get()
    waktu = waktu[3:]
    waktu = waktu.replace(',', '')
    konten = self.remove_text(' '.join(response.css('div.read__content p').xpath('string()').getall()))
    kelas = response.css('li.breadcrumb__item:nth-child(2) span::text').get()
    if 'health.kompas.com' in url:
      kelas = 'kesehatan'
    elif 'bola.kompas.com' in url:
      kelas = 'olahraga'
    elif 'kompas.com/edu' in url:
      kelas = 'pendidikan'
    elif 'travel.kompas.com' in url:
      kelas = 'pariwisata'
    else:
      return None
    return judul, konten, waktu, kelas

  def parseDetik(self, response, url):
    if 'travel.detik.com/highlight' in url or 'travel.detik.com/escapes-uncovered' in url:
      return None
    judul = self.remove_text(response.css('h1.detail__title::text').get())
    waktu = response.css('div.detail__date::text').get()
    waktu = waktu.replace(',', '')
    konten = self.remove_text(' '.join(response.css('div.detail__body-text p').xpath('string()').getall()))
    if 'health.detik.com' in url:
      kelas = 'kesehatan'
    elif 'sport.detik.com' in url:
      kelas = 'olahraga'
    elif 'detik.com/edu' in url:
      kelas = 'pendidikan'
    elif 'travel.detik.com' in url:
      kelas = 'pariwisata'
    else:
      return None 
    return judul, konten, waktu, kelas

  def parse_article(self, response):   
      url = response.url   
      if 'okezone.com' in url:
        result = self.parseOkezone(response, url)
        if result:
          judul, konten, waktu, kelas = self.parseOkezone(response, url)
        else:
          return None
      elif 'kompas.com' in url:
        # result
        result = self.parseKompas(response, url)
        if result:
          judul, konten, waktu, kelas = self.parseKompas(response, url)
        else:
          return None
      elif 'detik.com' in url:
        result = self.parseDetik(response, url)
        if result:
          judul, konten, waktu, kelas = self.parseDetik(response, url)
        else:
          return None

      # Menyimpan data ke dalam file CSV
      with open('news.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONE)
        # Menulis baris data
        if file.tell() == 0:
            # Menulis nama kolom jika file masih kosong
            writer.writerow(['Judul', 'Waktu', 'URL', 'Kelas', 'Konten'])
        writer.writerow([judul, waktu, url, kelas, konten.strip()])

  def remove_text(self, text):
      # Membuat tabel translasi untuk menghapus tanda baca
      text = text.replace('\n', ' ')
      text = text.replace('\t', ' ')
      text = text.replace(',', '')

      translator = str.maketrans('', '', string.punctuation)
      
      # Menghapus tanda baca dari teks menggunakan tabel translasi
      text = text.translate(translator)
      
      # Menghapus karakter whitespace ekstra
      text = ' '.join(text.split())
      
      return text