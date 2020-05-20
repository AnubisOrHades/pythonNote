import os
import time
import m3u8
import requests
from glob import iglob
from natsort import natsorted
from urllib.parse import urljoin
from dataclasses import dataclass
from concurrent.futures import ThreadPoolExecutor
from fake_useragent import UserAgent


@dataclass
class DownLoadM3U8:
    m3u8_url: str
    file_name: str
    path: str = r"."
    max_workers: int = 10

    def __post_init__(self):
        self.headers = {
            'User-Agent': UserAgent().chrome, }
        self.thread_pool = ThreadPoolExecutor(max_workers=self.max_workers)

    def get_ts_url(self):
        m3u8_obj = m3u8.load(self.m3u8_url, headers=self.headers)
        base_uri = m3u8_obj.base_uri

        for seg in m3u8_obj.segments:
            yield urljoin(base_uri, seg.uri)

    def download_single_ts(self, urlinfo):
        url, ts_name = urlinfo
        try:
            down_name = "{}\\{}".format(self.path, ts_name)
            if os.path.isfile(down_name):
                return None
            res = requests.get(url, headers=self.headers)
            with open(down_name, 'wb') as fp:
                fp.write(res.content)
        except Exception as e:
            print("Error:{}".format(e))
        else:
            pass
        finally:
            print(url)

    def download_all_ts(self):
        ts_urls = self.get_ts_url()
        for index, ts_url in enumerate(ts_urls):
            self.thread_pool.submit(self.download_single_ts, [ts_url, f'{index}.ts'])
        self.thread_pool.shutdown()

    def run(self):
        self.download_all_ts()
        ts_path = r'{}\*.ts'.format(M3U8.path)
        new_path = r"{}\{}".format(M3U8.path, M3U8.file_name)
        print(new_path)
        with open(new_path, 'wb') as fn:
            for ts in natsorted(iglob(ts_path)):
                with open(ts, 'rb') as ft:
                    scline = ft.read()
                    fn.write(scline)
        for ts in iglob(ts_path):
            os.remove(ts)


if __name__ == '__main__':
    start = time.time()
    m3u8_url = 'http://aa.kk400500.com/20200116/BBVZwZdC/438kb/hls/index.m3u8'
    down_path = r'D:'
    file_name = "亚洲自慰在公共hd上.mp4"

    M3U8 = DownLoadM3U8(m3u8_url, path=down_path, file_name=file_name)
    M3U8.run()

    end = time.time()
    print('耗时:', end - start)
