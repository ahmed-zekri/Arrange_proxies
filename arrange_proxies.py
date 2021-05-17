import os
import sys

from proxy_checker import ProxyChecker

if __name__ == '__main__':
    formatted_proxies = ''
    checker = ProxyChecker()
    with open('file.txt', 'r') as file:
        file_content = file.read()
        proxies = file_content.split(',')
        proxies = [str(proxies[i]).strip().replace('http://', '').replace('@', ':').replace("'", '') for i in
                   range(len(proxies))]

        for _, proxy in enumerate(proxies):
            proxy = proxy.split(':')
            if len(proxy) < 4:
                print(f'invalid line {_ + 1}')
                sys.exit(0)
            formatted_proxies += f'{proxy[2]}:{proxy[3]}:{proxy[0]}:{proxy[1]}\n'
            # print(checker.check_proxy(f'{proxy[2]}:{proxy[3]}', user=proxy[0],
            #                           password=proxy[1]))
    if not os.path.exists('file_formatted.txt'):
        os.mkdir('file_formatted.txt')
    with open('file_formatted.txt', 'w') as file_write:
        file_write.write(formatted_proxies)
