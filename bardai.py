from bardapi import BardCookies
import datetime

cookie_dict = {
    "__Secure-1PSID" : "cwjytGK5uAobiCPWWW3-phxKH6fhr52Z1K4y2PWAwwB6FGgpAQZ9XGpKrvYyHLzc_w5u-Q.",
"__Secure-1PSIDTS" : "sidts-CjIBNiGH7mhK5aG9eXfXBwdWVHq4SOEj0R-fuZION5SJmT7lIyrUSa9CVGAH2NdY3zubehAA",
"__Secure-1PSIDCC" : "ACA-OxNM9UgkooiUHnP0II7vjlS7xDfXC4del8NVev6d-24itRn_mZO0ak1NLH1tSFvVseYhaj0"
}
bard = BardCookies(cookie_dict=cookie_dict)

def split_and_save_paragraphs(data, filename):
    paragraphs = data.split('\n\n')
    with open(filename, 'w') as file:
        file.write(data)
    data = paragraphs[:2]
    separator = ', '
    joined_string = separator.join(data)
    return joined_string

# Main Execution

while True:
    Question = input("Enter The Query : ")
    RealQuestion = str(Question)
    results = bard.get_answer(RealQuestion)['content']
    current_datetime = datetime.datetime.now()
    formatted_time = current_datetime.strftime("%H%M%S")
    filenamedate = str(formatted_time) + str(".txt")
    filenamedate = "DataBase//" + filenamedate
    print(split_and_save_paragraphs(results, filename=filenamedate))
