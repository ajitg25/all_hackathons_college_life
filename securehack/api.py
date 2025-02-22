import requests
import ssl
import socket
import whois
import re
from datetime import datetime
import os
from flask import Flask,render_template,request, flash,redirect,url_for
from werkzeug.utils import secure_filename 
from flask import jsonify
from waitress import serve
from flask_cors import CORS, cross_origin
import joblib
from pandas import json_normalize
import traceback
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.parse import urlparse
import urllib3
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
# from urllib3.exceptions import HTTPError, URLError


app = Flask(__name__)
CORS(app)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

model = joblib.load('RFFinal.pkl')
print ('Model loaded')
# model_columns = joblib.load("columns.pkl",mmap_mode='r') 


#IP address
def get_ip_address(url):
    try:
        ip_address = socket.gethostbyname(url)
        if ip_address is not None:
            return 1
            print("URL IP address:", ip_address)
        else:
            return -1
            print("No IP address available.")

        return ip_address
    except socket.gaierror:
        return -1
        return None
    
#check url length
def check_url_length(url):
    url_length = len(url)

    if url_length > 75:
        return -1
        print("len > 75")

    elif 54 < url_length < 75:
        return 0
        print("54 < len < 75")

    else:
        return 1
        print("len < 54")


def count_at(url):
    x = url.count("@")
    if(x):
        return -1
    return 1

def has_double_slash(url):
    pattern = r"//\Z"
    match = re.search(pattern, url)
    
    if(match is not None):
        return -1
    return 1

def count_hyphen(url):
    x = url.count("-")
    if(x):
        return -1
    return 1

def count_dot(url):
    x = url.count(".")
    if(x>=3):
        return -1
    if(x==2):
        return 0
    return 1

#ssl
def check_ssl_final_state(url):
    hostname = url.split('//')[1].split('/')[0] 
    port = 443 
    context = ssl.create_default_context()

    try:
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as secure_sock:
                cert = secure_sock.getpeercert()
                if 'https' not in url.lower() and 'http' not in cert['subjectAltName'][0][1].lower():
                    return -1
                    return "Not HTTP nor trusted"
                elif 'http' in url.lower() and 'http' in cert['subjectAltName'][0][1].lower():
                    return 0
                    return "HTTP and trusted"
                elif 'http' in url.lower() and 'http' not in cert['subjectAltName'][0][1].lower():
                    return 1
                    return "HTTP and not trusted"
    except Exception as e:
        return str(e)

def is_domain_expiry_within_1_year(domain):
    try:
        domain_info = whois.whois(domain)
        expiry_date = domain_info.expiration_date

        if isinstance(expiry_date, list):
            expiry_date = expiry_date[0]  # Take the first item if it's a list

        current_date = datetime.now()
        one_year_from_now = current_date + timedelta(days=365)
        
        if(expiry_date is not None and expiry_date <= one_year_from_now):
            return -1
        return 1
        return expiry_date is not None and expiry_date <= one_year_from_now
    except whois.parser.PywhoisError:
        return False



def get_favicon_domain(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    favicon_tag = soup.find('link', rel='icon')
    if favicon_tag is None:
        return -1

    favicon_url = favicon_tag.get('href')
    favicon_domain = urljoin(url, favicon_url).split('/')[2]
    
    a = url.split('/')
    if(favicon_domain in a):
        return 1
    return -1


def check_https(url):
    if("http" in url.lower()):
        return -1
    return 1


#request
def check_request_url(url):
    url_length = len(url)
    threshold = len(url) * 0.22  # 22% threshold

    if url_length > threshold:
        return -1
        print("Request URL > 61%")

    elif threshold <= url_length <= (threshold * 0.61):
        return 0
        print("22% <= Request URL <= 61%")

    else:
        return 1
        print("Request URL < 22%")

#anchor_url
def check_url_of_anchor(anchor_url):
    url_length = len(anchor_url)
    threshold = len(anchor_url) * 0.22  # 22% threshold

    if url_length > threshold:
        return -1
        print("anchor_url > 61%")

    elif threshold <= url_length <= (threshold * 0.61):
        return 0
        print("22% <= anchor_url <= 61%")

    else:
        return 1
        print("anchor_url < 22%")


#SFH
def check_sfh(url):
    try:
        response = requests.get(url)
        csp_header = response.headers.get('Content-Security-Policy', '')

        # Check for empty SFH
        if not csp_header:
            return -1
            print("Empty SFH: Server-Side Forwarding (SFH) is not implemented.")

        # Check for SFH pointing to a different domain
        elif "'none'" in csp_header or "'self'" in csp_header:
            return 0
            print("SFH for Different Domain: Server-Side Forwarding (SFH) is implemented, but allows loading content from a different domain.")

        # Check for valid SFH
        elif 'frame-ancestors' in csp_header:
            return 1
            print("Valid SFH: Server-Side Forwarding (SFH) protection mechanism is likely implemented.")
        
        else:
            return -1
            print("Unknown SFH configuration.")

    except requests.exceptions.RequestException:
        return -1


def check_form_processing(url):
    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')
    form = soup.find('form')

    if form is None:
        return 1

    action = form.get('action')
    method = form.get('method')

    if action and action.startswith('mailto:'):
        return -1
        print("Form data is being sent via email.")
    if action and action.startswith('mail:'):
        return -1

    if method and method.lower() == 'post':
        return 1
        print("Form data is being sent using the HTTP POST method.")
        # Further analysis of the server-side code may be required to check for email processing.
    return 1
    print("Form processing method could not be determined.")



def abnormal_url(url):
    parsed_url = urlparse(url)
    if(bool(parsed_url.hostname)):
        return 1
    return -1

def count_redirects(url):
    try:
        count = 0
        while True:
            response = requests.get(url, allow_redirects=False)
            if not response.is_redirect:
                break
            count += 1
            if(count>=2):
                return 0
            url = response.headers['Location']
        return 1
    except:
        return 0
        print("Invalid URL or unable to resolve IP address.")
    return 1


#pop up
def analyze_link_behavior(url):
    response = requests.get(url)
    if response.status_code == 200:
        content_type = response.headers.get('content-type', '')
        if 'html' in content_type:
            html_content = response.text
            if 'oncontextmenu="return false;"' in html_content:
                return -1
                print("Right click Disabled and pop-up")
            else:
                return 1
                print("No pop-up")
        else:
            return 1
            print("No pop-up")
    else:
        return 0
        print("Right click with alert")

def iframe(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return -1

    soup = BeautifulSoup(response.content, 'html.parser')
    ad_tags = soup.find_all(['iframe'])  # Adjust the list of HTML elements as per your requirements

    ad_count = len(ad_tags)
    if(ad_count==0):
        return 1
    return -1

#domain age
def calculate_domain_age(url):
    try:
        domain = whois.whois(url)
        creation_date = domain.creation_date

        if isinstance(creation_date, list):
            creation_date = creation_date[0]

        current_date = datetime.now()
        domain_age = (current_date - creation_date).days

        if domain_age is not None:
            if domain_age < 365:
                return -1
                print("Age of domain: < 1 year")
        else:
                return 1
                print("Age of domain: > 1 year")

    except Exception as e:
        return 1
        print("Error fetching domain age:", str(e))

    return 0

def check_dns_record(url):
    try:
        hostname = url.split('//')[-1].split('/')[0]
        ip_address = socket.gethostbyname(hostname)
        return 1
    except socket.gaierror:
        return -1
    return 1

def count_inbound_links(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        links = soup.find_all("a", href=url)
        if(len(links))<5:
            return 1
        return -1
    except:
        return -1

# Example usage
url = "https://github.com/nayan911/securehack"

IP_add= get_ip_address(url)
url_len = check_url_length(url)
at = count_at(url)
slash = has_double_slash(url)
hyphen = count_hyphen(url)
dot = count_dot(url)
ssl_final = check_ssl_final_state(url)
domain_expiry = is_domain_expiry_within_1_year(url)
favicon_domain = get_favicon_domain(url)
httpsSecu = check_https(url)
request_url = check_request_url(url)
anchor = check_url_of_anchor(url)
sfh = check_sfh(url)
mailtoo = check_form_processing(url)
abnormal = abnormal_url(url)
redirec = count_redirects(url)
linkBehav = analyze_link_behavior(url)
ifram = iframe(url)
domain_age = calculate_domain_age(url)
dns_record = check_dns_record(url)
inbound_links = count_inbound_links(url)

print(IP_add,url_len,at,slash,hyphen,dot,ssl_final,domain_expiry,favicon_domain,httpsSecu,request_url,anchor,sfh,mailtoo,abnormal,redirec,linkBehav,ifram,domain_age,dns_record,inbound_links)
# query = [sfh,pop_up,ssl_final_state,request_url,url_of_anchor,url_length,domain_age,ip_address,web_traffic]
# prediction = model.predict([query])
# testy = model.predict([[1,0,1,1,0,0,0,1,1]])
# print(testy)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        if model:
            try:
                url = request.json['link']

                IP_add= get_ip_address(url)
                url_len = check_url_length(url)
                at = count_at(url)
                slash = has_double_slash(url)
                hyphen = count_hyphen(url)
                dot = count_dot(url)
                ssl_final = check_ssl_final_state(url)
                domain_expiry = is_domain_expiry_within_1_year(url)
                favicon_domain = get_favicon_domain(url)
                httpsSecu = check_https(url)
                request_url = check_request_url(url)
                anchor = check_url_of_anchor(url)
                sfh = check_sfh(url)
                mailtoo = check_form_processing(url)
                abnormal = abnormal_url(url)
                redirec = count_redirects(url)
                linkBehav = analyze_link_behavior(url)
                ifram = iframe(url)
                domain_age = calculate_domain_age(url)
                dns_record = check_dns_record(url)
                inbound_links = count_inbound_links(url)

                # query = pd.get_dummies(pd.DataFrame({'sfh': [sfh],pop_up': [pop_up],'ssl_final_state': [ssl_final_state],'request_url': [request_url],'url_of_anchor': [url_of_anchor],'url_length': [url_length],'domain_age': [domain_age],'ip_address': [ip_address]}))
                # query = query.reindex(columns=model_columns, fill_value=0)
                print(IP_add,url_len,at,slash,hyphen,dot,ssl_final,domain_expiry,favicon_domain,httpsSecu,request_url,anchor,sfh,mailtoo,abnormal,redirec,linkBehav,ifram,domain_age,dns_record,inbound_links)
                query = [IP_add,url_len,at,slash,hyphen,dot,ssl_final,domain_expiry,favicon_domain,httpsSecu,request_url,anchor,sfh,mailtoo,abnormal,redirec,linkBehav,ifram,domain_age,dns_record,inbound_links]

                prediction = model.predict([query])
                print(prediction)
                return jsonify({'prediction': str(prediction)})
            except:
                return jsonify({'trace': traceback.format_exc()})
        else:
            print ('Train the model first')
            return ('No model here to use')
    else:
        "server running, no parameters recieved"

@app.route('/')
def home():
    return "Hello"


#if __name__  == "__main__":
#    app.run(host=os.getenv('IP', '0.0.0.0'), 
#    port=int(os.getenv('PORT', 8889)), debug=True) #any code changes automatic refresh due to debug being True
    
if __name__ == "__main__":
    serve(app, host='0.0.0.0',port=8889,threads=2)