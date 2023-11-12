### mailmail
이름을 **mailmail**라고 지었으며, 아웃룩의 이메일을 관리하는 도구입니다<br>
- 이것의 장점은 엑셀이나 Util과 연동하여 편의성을 더욱 증대하고있읍니다
- 기본적인 사용법이나 함수의 이름은 같은 형태를 따릅니다

아웃룩을 사용하기 쉽도록 하기위한 모듈이다.<br>
기본적으로 아웃룩은 폴더의 형태관리를 하고있다.<br>
또한 각 메일은 item이라는 객체로 관리가 된다<br>

#### 용어설명
    top folder: 제일위의 폴더
	item : 한개 메세지에 대한 정보와 메소드틀 갖고있는 클래스 객체

``` python
# -*- coding: utf-8 -*-
import mailmail
outlook = mailmail.mailmail()
#받은 편지함에서 최근의 10개 메일에 대한 정보들을 갖고오기
aaa = outlook.get_10_latest_mail_data_in_default_input_folder()
print (aaa)


#받은 편지함에서 최근의 교개를 메일 객체로 들려받는것
letters = outlook.get_latest_mail_items_at_input_mail_folder_obj(3)
print (letters)

#기본 폴더들이 어떤것이 있는지 알려 주는것
letter_box_all_name = outlook.get_all_default_folder_information()
print (letter_box_all_name)

#메일객체 1개에 대한 정보를 갖고오는 것
letter_information = outlook.get_all_information_for_one_mail(letters[0])
print (letter_information)

#한 메일객체에의 첨부 화일만 갖고오기
letter_attchments = outlook.get_attached_filename_all_for_one_mail(letters[0])
print (letter_attchments)

#플더 객체를 갖고오는 것
letter_box = outlook.get_mail_folder_obj_by_default_index_no(6)
print (letter_box)

#어떤 메일과 동일한 형식의 메일을 쓰기 위해서, 특정 메일의 정보를 갖고오는것
letter_information = outlook.get_one_mail_information (letters[0])
print (letter_information)

#오늘을 기준으로 몇일전후의 자료를 갖고올것인지
letter_by_day = outlook.get_mail_obj_in_mail_folder_obj_from_index_day(letter_box,2)
print(letter_by_day)

#날짜사이의 모든 메일 객체를 갖고오는 것
letter_between_day = outlook.get_mail_obj_in_mail_folder_obj_between_date(letter_box,"2023-10-23","2023-10-24")
print(letter_between_day)

#오늘 들어온 메일중 읽지 않은 메일
letters_today = outlook.get_new_mails_on_today_in_default_input_folder()
print(letters_today)

#새로운 메일 보내기
#혹시 그냥 발송될까봐 주석 처리함
#outlook.send_new_mail(to="", subject="", body="", attachments=None)

# 메일주소가 다른것만 갖고오기
letters_by_address = outlook.find_mail_items_in_input_folder_by_sender(letter_box, "lotte.net", False)
print(letters_by_address)


#메일을 만들어서, 임시 보관함으로 저장하기
#outlook.make _draft_ new_mail(**dic)
aaa = outlook.get_opened_mail_item()
	if aaa:
		bbb = outlook.get_one_mail_information(aaa)
		print(bbb)
outlook.reply_email(letters[0])


```


``` python
#-*- coding: utf-8 -*-
import mailmail
outlook = mailmail.mailmail()

#메일에 css를 적용해서, 테이블을 만들고 보내는 방법

body_top = """
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"> """

style_start ="""
<style type="text/css">
"""

style_1 ="""
table_id_1 {
	font-family: 맑은 고딕, Arial, Helvetica, sans-serif;
	background-color: #EEEEEE
	border-collapse: collapse;
	width: 100%;
	}

table td, table th {
	border: 1px solid #ddd;
	padding: 0рх 0рх;
}
table th{
	font-size: 15px;
	font-weight: bold;
	padding-top: 2px;
	padding-bottom: 2px
	text-align: left;
	background-color: #660000;
	color: white;
}
"""


style_end = """</style>"""

body_middle_start=""

body_bottom ="""
<br> <br> <br>
xython.co.kr
"""

tbe_title_data = ["업체명","PR번호", "요청납기","예상 납기일자", "납기소요일","수량", "비고"]
#여러자료증에서 원하는 y열들을 번호를 기준으로 갖고오는것
tbe_data =[
["aaa", "123", "2023-10-11", "2023-10-11", "90일", "1 set", ""],
["bbb", "456", "2023-10-12", "2023-10-12", "91일", "1 set", ""],
["ccc", "789", "2023-10-13", "2023-10-13", "92일", "1 set", ""],
]

doc_title = "업체 납기정보 공유건"
#htm로 테이블들의 자료를 만드는 것
input_text = "텍스트에 컬러를 넣는 방법"
text_html_1 = outlook.make_html_inline_text(input_text, True, 20, "red")
user_text_1 = "수고하십니다<br> <br>하기 구매요청 품목에 대한 TBE를 요청합니다<br> <br>구매품목 : 물건1 <br> <br>"
table_html = outlook.make_table("table_id_1", tbe_title_data, tbe_data)
body_top_all = body_top + style_start + style_1 +style_end
body_middle_all = body_middle_start + text_html_1 + user_text_1 + table_html +text_html_1
body_bottom_all = body_bottom

body_all = body_top_all + body_middle_all + body_bottom_all
#만든 자료들을 이용해서 outlook의 메일을 만드는것
aaa ={}
aaa["to"] = "abc@def.com"
aaa["subject"]= doc_title
aaa["cc"] = "rgb@rgb.com;"
outlook.make_draft_new_mail(to=aaa["to"],cc=aaa["cc"], subject=aaa["subject"], body=body_all)
```
