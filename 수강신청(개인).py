# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 23:51:27 2018

@author: Shin
"""
import requests

idPwParams={'id':'',
            'pwd':''
}

header={'content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'User-tent-Type':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

s = requests.Session()
s.get("http://sugang.kongju.ac.kr")

loginURL = "http://sugang.kongju.ac.kr/login?attribute=loginChk"
r=s.post(loginURL,idPwParams)
data=r.json()

#Token 값 가져오기
token = data['token']

#Token 값 Dic에 넣기
idPwParams['token']=token


coreURL = "http://sugang.kongju.ac.kr/core?attribute=frame"
r=s.post(coreURL,idPwParams)


#수강신청 referer
#referer="http://sugang.kongju.ac.kr/sugang?attribute=sugangMain&token="+data['token']

#장바구니 referer
referer = "http://sugang.kongju.ac.kr/core?attribute=mainBasket&token="+data['token']


#Referer 값 추가(토큰 때문)
header['Referer']=referer


###Validation 값 받아오기###

#수강신청
#getValidateURL = "http://sugang.kongju.ac.kr/sugang?attribute=sugangMain&token="+data['token']

#장바구니
getValidateURL = "http://sugang.kongju.ac.kr/core?attribute=mainBasket&token"+data['token']
r=s.post(getValidateURL, idPwParams, headers=header)

###Parsing###
#a = ((r.text.split('data:{params:params,mode:mode,retake_yn:retake_yn,basket_yn:basket_yn,\'')[1].split('\'')))[0]
a = ((r.text.split('data:{params:params,mode:mode,retake_yn:retake_yn,\'')[1].split('\'')))[0]


#Vali 값 Dic에 추가
idPwParams[a]=a;

#수강신청 부분
#sustCdListJsonURL="http://sugang.kongju.ac.kr/core?attribute=sustCdListJson"
#r=s.post(sustCdListJsonURL,idPwParams,headers=header)

#수강신청부분
#sugangModeURL="http://sugang.kongju.ac.kr/sugang?attribute=sugangMode"

#장바구니 부분
basketModeURL = "http://sugang.kongju.ac.kr/core?attribute=basketMode"
idPwParams['params']=''
idPwParams['mode']='insert'

#r=s.post(sugangModeURL,idPwParams,headers=header)
r = s.post(basketModeURL, idPwParams,headers=header)
msg = r.json()

#print("sugangModeURL : " + r.text)
print("basketModeURL : " + r.text)
msg = msg['msg']

print(msg)
