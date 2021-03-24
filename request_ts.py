import requests
from bs4 import BeautifulSoup as bs
import datetime
import os.path
from os import path

def get_soup(JWT, link):
    User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    Accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    Sec_Fetch_Site = 'same-origin'
    Sec_Fetch_Mode = 'navigate'
    Sec_Fetch_User = '?1'
    Sec_Fetch_Dest = 'document'
    Accept_Language = 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7'
    # JWT = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2MTYyODE1NjcsInByb3BlcnRpZXMiOnsic2FsdCI6IjQ3OWNkYTE4MWEwYzRiNWJmNzAyZTBiYThjYjllZTY3IiwiaGFzaCI6IjAwMDA2ODUwNjg1MDY4NTBmYzhmYTY3ZmYyZDM2ZjlhIiwibG9naW5JZCI6MTUxMzgxLCJsb3dSZXMiOmZhbHNlLCJtb2JpbGVPcHRpbWl6YXRpb25zIjpmYWxzZSwidmlsbGFnZVBlcnNwZWN0aXZlIjoicGVyc3BlY3RpdmVSZXNvdXJjZXMiLCJ1dWlkIjoiODU0ZmE4MDAtNmM0Ny0xMWViLTE5MDQtMDEwMDAwMDAwNTg2IiwicHciOiJkMDFmMmFhYzk4MWY0Y2E0ZjgyYzE0ZWU4N2JhOTk4YTYwZGUwOWIyIn19.QAqbXWzwQAjELIuJ6LjbURNqcW0ZSW62YUWFVuWZteq4ug1pXFYmpXekk66H4AcI3TPjATWJbdZvhwKu0ENrEqRUyaS9_wZmYxbdRNCljWxpzUlyQ24extTM9I5nTh0ExZqXhfEUt3HX7V3OIVmez6IyHEpo18n30Xad2YRt94GMxxJFCq890a8ETpW-LavCUCFSgAReAL8bCPrGdk_rhepdrGdI8fQloaTKNtOH83VWVk191MhE-TgXFReAsBNLlopG7JSn71S36XOtiwU6WvorIPw0ZmasjiOOPik2q6y9WPCv53U4X8hRCC5rHS4QrUnXpi0F7bTAMN_WvSkfVw'
    cmpconsentx17155 = 'CPDWsgGPDWsgGAfSDBPLBSCgAP_AAH_AAAigHbpd5D_NTXFBcXx5SvtkOYwV1-QUA2QCCBCBAyAFAAGQ8LQCk0AisASABCgCIQAAohIBAAAEHEkEAEEQQABEAAGoAASEgAAIICBEEBEBACJQAAoKAAAQAAAAAAABKQAAmEDQA8bqBGAAIIAwQAgAgIABCAAAQAAASB26XeQ_zU1xQXF8eUr7ZDmMFdfkFANkAggQgQMgBQABkPC0ApNAIrAEgAQoAiEAAKISAQAABBxJBABBEEAARAABqAAEhIAACCAgRBARAQAiUAAKCgAAEAAAAAAAASkAAJhA0APG6gRgACCAMEAIAICAAQgAAEAAAEgAAA'
    cmpcvcx17155 = '__c6491_c6487_s914_s94_s40_s1052_s64_c6011_c6137_s1469_c6494_s65_c8227_s23_s69_s1100_c6489_s123_s1473_s7_s1433_c6085_c7306_s312_s1_s26_s135_s1104_s1409_s905_s46_s24_s37_s14_c6490_s1475_s1442_c6488_s282_c6486_s11_c6136_s898_c6138_s49_s971_c6135_c5973_s34_c6446_c6493_s77_c7475_s261_c6492_s1078_s3_c6495_s30_U__'
    cmpcpcx17155 = '__51_52_53_54_55__'

    cookies = {'JWT':JWT,
               'cmpconsentx17155': cmpconsentx17155,
               'cmpcvcx17155':cmpcvcx17155,
               'cmpcpcx17155':cmpcpcx17155}

    headers = {'User-Agent': User_Agent,
              'Accept':Accept,
              'Sec-Fetch-Dest':Sec_Fetch_Dest,
              'Accept-Language':Accept_Language,
              }


    r = requests.get(link, cookies=cookies, headers=headers)
    print(r.cookies.get_dict())
    # print('\n', r.text)

    soup = bs(r.text, 'html.parser')
    return soup

def save_image(JWT, link, name, time, ddate):

    cookies ={}
    User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    Accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    Sec_Fetch_Site = 'same-origin'
    Sec_Fetch_Mode = 'navigate'
    Sec_Fetch_User = '?1'
    Sec_Fetch_Dest = 'document'
    Accept_Language = 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7'
    #JWT = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2MTYyODE1NjcsInByb3BlcnRpZXMiOnsic2FsdCI6IjQ3OWNkYTE4MWEwYzRiNWJmNzAyZTBiYThjYjllZTY3IiwiaGFzaCI6IjAwMDA2ODUwNjg1MDY4NTBmYzhmYTY3ZmYyZDM2ZjlhIiwibG9naW5JZCI6MTUxMzgxLCJsb3dSZXMiOmZhbHNlLCJtb2JpbGVPcHRpbWl6YXRpb25zIjpmYWxzZSwidmlsbGFnZVBlcnNwZWN0aXZlIjoicGVyc3BlY3RpdmVSZXNvdXJjZXMiLCJ1dWlkIjoiODU0ZmE4MDAtNmM0Ny0xMWViLTE5MDQtMDEwMDAwMDAwNTg2IiwicHciOiJkMDFmMmFhYzk4MWY0Y2E0ZjgyYzE0ZWU4N2JhOTk4YTYwZGUwOWIyIn19.QAqbXWzwQAjELIuJ6LjbURNqcW0ZSW62YUWFVuWZteq4ug1pXFYmpXekk66H4AcI3TPjATWJbdZvhwKu0ENrEqRUyaS9_wZmYxbdRNCljWxpzUlyQ24extTM9I5nTh0ExZqXhfEUt3HX7V3OIVmez6IyHEpo18n30Xad2YRt94GMxxJFCq890a8ETpW-LavCUCFSgAReAL8bCPrGdk_rhepdrGdI8fQloaTKNtOH83VWVk191MhE-TgXFReAsBNLlopG7JSn71S36XOtiwU6WvorIPw0ZmasjiOOPik2q6y9WPCv53U4X8hRCC5rHS4QrUnXpi0F7bTAMN_WvSkfVw'
    cmpconsentx17155 = 'CPDWsgGPDWsgGAfSDBPLBSCgAP_AAH_AAAigHbpd5D_NTXFBcXx5SvtkOYwV1-QUA2QCCBCBAyAFAAGQ8LQCk0AisASABCgCIQAAohIBAAAEHEkEAEEQQABEAAGoAASEgAAIICBEEBEBACJQAAoKAAAQAAAAAAABKQAAmEDQA8bqBGAAIIAwQAgAgIABCAAAQAAASB26XeQ_zU1xQXF8eUr7ZDmMFdfkFANkAggQgQMgBQABkPC0ApNAIrAEgAQoAiEAAKISAQAABBxJBABBEEAARAABqAAEhIAACCAgRBARAQAiUAAKCgAAEAAAAAAAASkAAJhA0APG6gRgACCAMEAIAICAAQgAAEAAAEgAAA'
    cmpcvcx17155 = '__c6491_c6487_s914_s94_s40_s1052_s64_c6011_c6137_s1469_c6494_s65_c8227_s23_s69_s1100_c6489_s123_s1473_s7_s1433_c6085_c7306_s312_s1_s26_s135_s1104_s1409_s905_s46_s24_s37_s14_c6490_s1475_s1442_c6488_s282_c6486_s11_c6136_s898_c6138_s49_s971_c6135_c5973_s34_c6446_c6493_s77_c7475_s261_c6492_s1078_s3_c6495_s30_U__'
    cmpcpcx17155 = '__51_52_53_54_55__'

    cookies = {'JWT': JWT,
               'cmpconsentx17155': cmpconsentx17155,
               'cmpcvcx17155': cmpcvcx17155,
               'cmpcpcx17155': cmpcpcx17155}

    headers = {'User-Agent': User_Agent,
               'Accept': Accept,
               'Sec-Fetch-Dest': Sec_Fetch_Dest,
               'Accept-Language': Accept_Language,
               }

    r = requests.get(link, cookies=cookies, headers=headers)
    # print(r.cookies.get_dict())
    # print('\n', r.text)

    time = str(time)
    time = time[11:19]
    # link = 'picture_at_'+time+'.png'
    # file = open(link, 'wb')
    # file.write(r.content)

    soup = bs(r.text, 'html.parser')

    link = '/var/www/html/image/'+str(ddate)+'/'+name+'_'+time+'.png'
    sprawdz = '/var/www/html/image/'+str(ddate)
    if (path.exists(sprawdz)):
        file = open(link, 'wb')
        file.write(r.content)
        file.close()
    else:
        os.mkdir(sprawdz)
        file = open(link, 'wb')
        file.write(r.content)
        file.close()

#link = 'https://ts4.travian.pl//hero/body/3400de05e903d0075a1ba30fb90b72178b1301006700000007002500410058006400.png'

#save_image(link, 'lukas84')