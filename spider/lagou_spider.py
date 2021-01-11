import random
import time
import requests
import logging
from django.core.exceptions import ObjectDoesNotExist
from PersonalDjangoTutorial.settings import BASE_DIR
from .models import Position

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename=BASE_DIR / 'cache/log.log',
    filemode='a'
)


class Spider:
    def __init__(self, key_word):
        self.key_word = key_word
        self.USER_AGENTS = [
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
            "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
            "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
            "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        ]
        self.User_Agent = random.choice(self.USER_AGENTS)
        self.real_headers = {
            'Host': 'www.lagou.com',
            'Origin': 'https://www.lagou.com',
            'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
            'User-Agent': self.User_Agent,
        }
        self.headers = {'User-Agent': self.User_Agent}
        self.url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
        self.real_url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

    def exchange_header(self):
        self.User_Agent = random.choice(self.USER_AGENTS)
        self.real_headers = {
            'Host': 'www.lagou.com',
            'Origin': 'https://www.lagou.com',
            'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
            'User-Agent': self.User_Agent,
        }
        self.headers = {'User-Agent': self.User_Agent}

    def get_cookie(self):
        return requests.get(self.url, headers=self.headers).cookies

    def get_position_data(self, page):
        form_data = {'first': "false", 'pn': page, 'kd': self.key_word}
        while True:
            res = requests.post(self.real_url, headers=self.real_headers, data=form_data,
                                cookies=self.get_cookie()).json()
            try:
                return res['content']['positionResult']['result']
            except KeyError:
                self.exchange_header()
                time.sleep(40)

    def main(self):
        for i in range(1, 50, 5):
            for page in range(i, i + 5):
                position_data = self.get_position_data(str(page))
                if position_data:
                    for item in position_data:
                        try:
                            Position.objects.get(position_id=item['positionId'])
                        except ObjectDoesNotExist:
                            Position.objects.get_or_create(
                                position_id=item['positionId'],
                                position_name=item['positionName'],
                                company_full_name=item['companyFullName'],
                                # company_id=item['companyId'],
                                industry_field=item['industryField'] or '',
                                company_label_list='\\'.join(item['companyLabelList']),
                                first_type=item['firstType'],
                                second_type=item['secondType'],
                                third_type=item['thirdType'],
                                city=item['city'],
                                district=item['district'] or '',
                                salary=item['salary'],
                                work_year=item['workYear'],
                                job_nature=item['jobNature'],
                                education=item['education'],
                                create_time=item['createTime'],
                                skill_labels=item['skillLables'],
                                latitude=item['latitude'] or '',
                                longitude=item['longitude'] or '',
                            )
                            logging.debug(item)
                time.sleep(3)


if __name__ == '__main__':
    spider = Spider('python')
    spider.main()


