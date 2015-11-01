from general import *
from domain_name import *
from ip_address import *
import nmap as nmap1
from robots_txt import *
from pythonwhois import get_whois
from pprint import pformat

ROOT_DIR = 'companies'
create_dir(ROOT_DIR)


def gather_info(name, url):
    domain_name = get_domain_name(url)
    ip_address = get_ip_address(domain_name)
    nmap = nmap1.PortScanner()
    nmap = nmap.scan(ip_address)
    try:
        robots_txt = get_robots_txt(url)
    except urllib.error.HTTPError:
        robots_txt = ''
    whois = get_whois(domain_name)
    create_report(name, url, domain_name, nmap, robots_txt, whois)


def create_report(name, full_url, domain_name, nmap, robots_txt, whois):
    project_dir = ROOT_DIR + '/' + name
    create_dir(project_dir)
    write_file(project_dir + '/full_url.txt', full_url)
    write_file(project_dir + '/domain_name.txt', domain_name)
    write_file(project_dir + '/nmap.txt', pformat(nmap))
    write_file(project_dir + '/robots.txt', robots_txt)
    write_file(project_dir + '/whois.txt', pformat(whois))

gather_info("marcin", 'http://www.marcin.matlacz.eu')

