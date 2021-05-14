import nmap3
import simplejson as json
from pygments import highlight, lexers, formatters


def nmap_scan(data,host):

    #scan tcp ports
    if 'tcp' in data:
        nmap = nmap3.NmapScanTechniques()
        result = nmap.nmap_tcp_scan(host)

    #scan udp ports
    elif 'udp' in data:
        nmap = nmap3.NmapScanTechniques()
        result = nmap.nmap_udp_scan(host)

    #scan top ports
    elif 'top port' in data:
        nmap = nmap3.Nmap()
        result = nmap.scan_top_ports(host)
    
    #scan for subdomains 
    elif 'subdomains' in data:
        nmap = nmap3.Nmap()
        result = nmap.nmap_dns_brute_script("domain")

    #scon for detect os
    elif 'os' in data:
        nmap = nmap3.Nmap()
        result = nmap.nmap_os_detection("your-host")

    #print in terminal with json format
    colored_json = highlight(json.dumps(result, indent=4, sort_keys=True), lexers.JsonLexer(), formatters.TerminalFormatter())
    print("\n\n", colored_json)

nmap_scan('os','localhost')
