import pandas as pd
import csv
from io import BytesIO, StringIO



DOCUMENT_TEMPLATE = '''<p style="font-size:10pt;line-height:1.2;font-family:돋움체;color:rgb(0, 0, 0);margin-top:0px;margin-bottom:0px;">
글쓰기 동아리 애자일쓰다 {month}월 {times}주차 활동비 지급 요청드립니다.<br />아래와 같이 기안을 작성하오니, 내용 확인 후 재가 부탁드립니다.</p>
<p style="line-height:1.2;font-size:10pt;font-family:돋움체;color:rgb(0, 0, 0);margin-top:0px;margin-bottom:0px;"><span style="font-size:10pt;">&nbsp; &nbsp; &nbsp;&nbsp;</span></p>
<p style="margin-left:40px;line-height:1.2;font-size:10pt;font-family:돋움체;color:rgb(0, 0, 0);margin-top:0px;margin-bottom:0px;">
<span style="font-size:10pt;">- 아 래 -</span></p>
<ol style="font-family:굴림;font-size:12px;margin-top:12px;margin-bottom:12px;padding-left:40px;">
	<li style="font-size:10pt;line-height:1.2;font-family:돋움체;color:rgb(0, 0, 0);margin-top:0px;margin-bottom:0px;"><strong>일시 :</strong>&nbsp;{term}</li>
	<li style="font-size:10pt;line-height:1.2;font-family:돋움체;color:rgb(0, 0, 0);margin-top:0px;margin-bottom:0px;"><strong>장소 :</strong>&nbsp;온라인</li>
	<li style="font-size:10pt;line-height:1.2;font-family:돋움체;color:rgb(0, 0, 0);margin-top:0px;margin-bottom:0px;"><strong>인원 :</strong>&nbsp;{people}</li>
	<li style="font-size:10pt;line-height:1.2;font-family:돋움체;color:rgb(0, 0, 0);margin-top:0px;margin-bottom:0px;"><strong>내용 :</strong>&nbsp;2주 1회 글쓰기 시행</li>
	<li style="font-size:10pt;line-height:1.2;font-family:돋움체;color:rgb(0, 0, 0);margin-top:0px;margin-bottom:0px;"><strong>활동비 :</strong>&nbsp;{activityExpense}원</li>
	<li style="font-size:10pt;line-height:1.2;font-family:돋움체;color:rgb(0, 0, 0);margin-top:0px;margin-bottom:0px;"><b>첨부</b>&nbsp;: 아래 노션 관리 데이터 베이스 캡처 첨부 및 링크 첨부</li>
	<li style="font-size:10pt;line-height:1.2;font-family:돋움체;color:rgb(0, 0, 0);margin-top:0px;margin-bottom:0px;"><a href="{notion_link}" target="_blank" style="color:blue;cursor:pointer;">{notion_link}</a></li>
	<li style="font-size:10pt;line-height:1.2;font-family:돋움체;color:rgb(0, 0, 0);margin-top:0px;margin-bottom:0px;">{img}</li>
</ol>'''



# csv 파일 전처리
def preprocess_for_document(file_bytes):
    # 데이터 읽어오기
    csv_data = StringIO(file_bytes.decode('utf-8'))
    reader = csv.DictReader(csv_data)
    records = pd.DataFrame(reader)

    # 청구서 작성에 필요한 변수
    month = ''
    times = ''
    term = ''
    people = ''
    activityExpense = ''
    notion_link = ''
    img = ''

    pass 

# 보고서 작성
def write_document(info_dict : dict) : 
    pass