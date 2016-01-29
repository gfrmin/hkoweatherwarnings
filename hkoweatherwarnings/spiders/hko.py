# -*- coding: utf-8 -*-
import scrapy
from hkoweatherwarnings.items import warningItem
from datetime import date
from dateutil.rrule import rrule, DAILY

class HkoSpider(scrapy.Spider):
    name = "hko"
    allowed_domains = ["hko.gov.hk"]

    startdate = date(1946, 1, 1)
    enddate = date(2016, 1, 1)
    datestocrawl = rrule(DAILY, dtstart=startdate, until=enddate)
    start_urls = map(lambda dt: "http://www.hko.gov.hk/cgi-bin/climat/warndb_ea.pl?start_ym=" + dt.strftime("%Y%m%d"), datestocrawl)

    def parse(self, response):
        warningstables = response.css("td td:nth-child(2) table")
        if warningstables != []:
            for warningstable in warningstables:
                warningsrows = warningstable.css("tr")[2:]
                for warningsrow in warningsrows:
                    warningstds = map(lambda td: td.css("::text").extract()[-1], warningsrow.css("td")[1:])
                    warning = warningItem()
                    warning['warningdate'] = response.css("h1").css("::text").extract()[0]
                    warning['warning'] = warningstds[0]
                    warning['issuetime'] = warningstds[1]
                    warning['issuedate'] = warningstds[2]
                    warning['canceltime'] = warningstds[3]
                    if len(warningstds) == 5:
                        warning['canceldate'] = warningstds[4]
                    yield warning
