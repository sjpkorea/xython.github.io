### ganada
#### ganada의 용어 설명
워드를 좀더 쉽게 사용하기 위한 방법이다. 기본적으로 워드는 전반적인 사용은 직접 다루는 것이 편하기 때문에, 엑셀의 자료를 잘 갖고와서 
특정한 곳에 변경을 하거나 집어 넣는 부분에 촛점을 맞추었다

|       용어        | 설명       |
|:---------------:|----------|
|     형태적인 분류     | active_document(화일) > sentence(문장) > word(한 단어) > character(한글자) |                       
|     의미적인 분류     | active_document(화일) > paragraph(문단) > line(줄) > word(한 단어) > character(한글자) |              
| active_document | 현재 선택된 워드문서, word라는 단어가 두가지 이름으로 사용되기때문에, file로 통일시킴 |                           
|    paragraph    | 줄바꿈이 이루어지기 전까지의 자료 |                   
|      line       | 한줄       |            
|      word       | 공백으로 구분된 단어 (다른의미 : 프로그램이름과 혼동을 피하기위해 file이라는 이름으로 사용) |                                 
|    character    | 글자 1개    |            
|     content     | 라인, 문단, 단어들을 총괄적으로 뜻하는것, 항목이라고 설명하는것이 좋을듯... |                              
|    bookmark     | 책갈피      |            
|      range      | 임의적으로 설정할수가 있으며,word밑에 range가 설정이 되고, select를 하면 selection밑에 자동으로 range객체가 설정된다 |            
|    sentence     | 표현이 완결된 단위, 그 자체로 하나의 서술된 문장이 되는 것 |         
|    paragraph    | 줄바꿈이 이루어지기 전까지의 자료 |         
|                 | MS워드를 사용하기 쉽게하기위해 만든 모듈입니다, |            
|                 | 차후에는 다른 Libero및 한글의 연동또한 만들 예정입니다 |              
|                 | 기본적으로 적용되는 selection은 제외한다 |         


``` python
# -*- coding: utf-8 -*-
import ganada

word = ganada.ganada()
input_text = "가나다"
#워드의 테이블 1번의 가로 2, 세로 3의 위치에 값을 넣는것
word.write_text_in_table_by_xy("table_1", [2,3], input_text)
```


``` python
# -*- coding: utf-8 -*-
import pcell
excel = pcell.pcell()
import ganada
word = ganada.ganada()
#현재 열린문서의 모든 글자를 삭제한다
word.select_all()
word.delete_selection()
text ="""님의 침묵
한용운
님은 갔습니다. 아아, 사랑하는 나의 님은 갔습니다.
푸른 산빛을 깨치고 단풍나무 숲을 향하여 난 작은 길을 걸어서, 차마 떨치고 갔습니다.
황금의 꽃같이 굳고 빛나던 옛 맹세는 차디찬 티끌이 되어서 한숨의 미풍에 날아갔습니다.
날카로운 첫 키스의 추억은 나의 운명의 지침을 돌려놓고, 뒷걸음쳐서 사라졌습니다.
나는 향기로운 님의 말소리에 귀먹고, 꽃다운 님의 얼굴에 눈멀었습니다.
사랑도 사람의 일이라, 만날 때에 미리 떠날 것을 염려하고 경계하지 아니한 것은 아니지만,
이별은 뜻밖의 일이 되고, 놀란 가슴은 새로운 슬픔에 터집니다.
그러나 이별을 쓸데없는 눈물의 원천을[1] 만들고 마는 것은 스스로 사랑을 깨치는 것인 줄 아는 까닭에,
걷잡을 수 없는 슬픔의 힘을 옮겨서 새 희망의 정수박이에 들어부었습니다.
우리는 만날 때에 떠날 것을 염려하는 것과 같이 떠날 때에 다시 만날 것을 믿습니다.
아아, 님은 갔지마는 나는 님을 보내지 아니하였습니다.
제 곡조를 못 이기는 사랑의 노래는 님의 침묵을 휩싸고 돕니다.
"""
#위의 글을 쓰는것
word.write_text_at_end_of_word_document(text)

#바꾸기
word.replace_all("님", "니이이임")
r_sawcarp = word.search_all_with_color_and_return_position("니이이임")

#맨마지막으로 커서를 이동
word.move_cursor_to_end_of_document()

#검정색 선의 테이블을 만든다
word.make_table_obj_with_black_line(5,7)

#테이블에 글을 쓰기
word.write_text_at_xy_cell_in_table(1, [2,2], "2,2번째 셀입니다")

#문서의 맨마지막에 글을  쓰기
word.move_cursor_to_end_of_document()
word.write_text_at_end_of_word_document("테스트용으로 넣은것")

#검정색 선의 테이블을 만든다
word.move_cursor_to_end_of_document()
word.make_table_obj_with_black_line(5,7)

#커서를 처음으로 이동
word.move_cursor_to_start_of_document()

#3번째 라인을 선택
word.select_line_by_line_no_from_cursor(4)
word.paint_border_in_selection("red")

#한재 라인의 2번째 뒤의 라인을 선택
word.select_line_by_line_no_from_cursor(2)
word.paint_border_in_selection("blu")
word.select_all()
#정규표현식으로 글자를 찾아서 변경하기
aaa = word.replace_in_document_by_jfsql("[숫자:1~ 2],[숫자:1~2]", "777777777777")

#2번째 테이블의 3번째 셀부터, 리스트의 값을 순차적으로 집어 넣기
input_list1d = ["1번","2번","3번","4번","5번","6번","7번","8번"]
for index, one_value in enumerate(input_list1d):
	word.select_xy_cell_in_table(2, [1, 3+index])
	word.write_text_at_end_of_cursor(one_value)

#헤더에 페이지를 넣는것
word.set_page_no_at_header("xython.co.kr",1)

#사진 넣기
word.insert_picture_at_cursor("D:\\test_폴더\\다운로드.jpg",100,100)

#pdf로 출력하기
word.print_as_pdf("D:\\aaa.pdf")

word.move_cursor_to_end_of_document()

#글자를 넣으면서 색과 크기를 지정
word.write_text_in_selection_with_color_size_bold("dasdasdadasda", "blu", 20, False)

#선택영역의 배경색을 지정
word.paint_background_color_in_selection("pin90")


```
