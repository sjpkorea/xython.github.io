### pcell
엑셀을 좀더 쉽게 사용하기 위하여 만든 것입니다
어떤 것보다 엑셀 그자체로 할수가 있다면, 그것만큼 편하고 좋은것은 없겠지요<br>
그런데, 이것을 사용하기 시작한 이유중의 하나는, 어느정도 이상의 매크로 기능을 VBA로 하기위해서는, 상당한 고수의 능룍이 필요합니다
생각이상으로 조금만 고급의 긴으을 하기위해서는 독단적인 VBA를 알아야 한다는 것이지요<br>

그래서 아래와 같은 이유로 이것을 사용하는 것입니다
- VBA는 엑셀의 매크로 기능 이외에는 사용할곳이 없다
- VBA의 고급기능을 하기 위해선, 상당히 높은 차원의 능력이 필요하다
- 파이썬은 배우기가 쉽고 확장성이 큽니다
- 생각 이상으로 문서자동화에서 사용하는 기능은 그리 엄청나게 많지 않다는 것입니다
- 함수형태로 만들어서 좀더 쉽게 사용이 가능합니다

-각 메소드는 각각 별도의 내용으로 사용합니다

#### 변경 기록
	엑셀을 컨트롤 할수있는 모듈
	2023-03-02 : 전반적으로 이름을 수정함
	2023-05-09 : 이름과 부족한 것을 추가함
	2023-10-21 : 비슷한것들을 삭제하고 하나씩만 남기도록 하였다

	add : 기존것에 추가하는 것
	insert : 새로운 뭔가를 만드는 것
	new : 어떤 객체를 하나 만들때 사용

#### 예제
``` python
# -*- coding: utf-8 -*-
import pcell, ganada,scolor, pynal
excel = pcell.pcell()
word = ganada.ganada()
color = scolor.scolor()
sigan = pynal.pynal()

# read range value in activesheet
# 현재시트에 영역안의 값을 갖고오는 것
list_2d = excel.read_value_in_range("", [1,1,5,5])

# write text in current cursor
# 현재 커서위치에 글씨를 쓰는것
word.write_text_at_begin_of_cursor("write text ")

# change the rgb color from easy
# 색을 쉽게 rgb로 바꿔주는것
rgb_list = color.change_scolor_to_rgb("red++")

# get today style
today = sigan.get_today_as_yyyy_mm_dd_style()

#현재 선택된 영역을 돌려주는 것
#return된값은 r_rsa의 형태로 하도록 한다
# 만약 같은 값이 있을때는, 1,2등의 숫자를 붙이도록 한다
r_rsa= excel.read_selection_address()
print(r_rsa)
#[3,3,7,7]을 선택하도록 하자
range_1 = [3,3,7,7]

excel.select_range("", range_1)
#선택한 영역에 빨간색을 열흐게 칠해보자

excel.paint_range_by_scolor("", range_1, "red95")
#선택한 영역에 숫자를 쓰도록 하자
for x in range(3,7+1):
	for y in range(3, 7+ 1):
		excel.write_value_in_cell("", [x,y], "셀 :"+str(x)+", "+str(y))


#선택한 영역에 기본선의 형태로 설정된 선을 굿도록 하자
excel.draw_line_in_range_as_basic("", range_1)
#엑셀의 값을 이동시킨다
range_2 = [1,1, 5,5]
excel.move_range("", range_1, "", range_2)

#영역을 복사하기
excel.copy_range("", range_2)
range_3 = [6,1]
excel.paste_range("", range_3)

#선택된영역의 3번째 마다 값을 삭제
excel. delete_value_in_range_by_step("", [1,2,10,3], 3)

#빈셀을 위의 것으로 체우기
excel.write_uppercell_value_in_emptycell_in_range("", [1,2,10,2])#수정 필요, 여러줄일때 오류

#정규표현식을 사용하는 방법
import jfinder
myre = jfinder.jfinder()
r_rvir = excel.read_value_in_range("", [1,5,10,5])
re_sql= ":([숫자:1~1])(,)"
for index, list_1d in enumerate(r_rvir):
	r_sabj = myre.search_all_by_jf_sql(re_sql, list_1d[0])
	print(r_sabj)
	excel.write_value_in_cell("", [index+20, 1], list_1d[0])
	excel.write_value_in_cell("", [index+20, 2], r_sabj)
	excel.write_value_in_cell("", [index+20, 3], str(r_sabj))

#excel.delete_empty._sheet #이 함수가 없어짐, 빈 시트 삭제하기
#영역의 픽셀값을 갖고온다
r_cxtp = excel.change_xyxy_to_pxyxy([1,1,7,7])
print(r_cxtp)

#현재 선택한 영역의 라인의 모든 값을 읽어온다
excel.select_cell("", [3,3])
r_raia = excel.read_address_in_activecell()
r_rvx = excel.read_value_in_xline("", [r_raia[0],r_raia[0]])
#print(r_rvx)

#여러개의 단어를 한번에 변경하자
change_words = [["3,4", "삼점사"], ["5,5", "5점5"]]
excel.replace_many_word_in_range("", [1,1, 10,6] ,change_words) #x,y,가 잘못됨, 수정 필요

#시트이름바꾸기
r_ran = excel.read_activesheet_name()
all_sheet_name = excel.read_all_sheet_name()
if r_ran != "Sheet1l" and not r_ran in all_sheet_name:
	excel. change_sheet_name(r_ran, "Sheet1")

#새로운시트를 추가
excel.insert_sheet_with_name("새로운시트")

#기존의 시트로 돌아오기
excel.select_sheet("Sheet1")

#선택영역에 왼쪽에 글자를 추가하는 것
excel.add_text_in_range_at_left("", [1,2,4,4], "추가-")

#사진하나 추가하기
picture_path = ""
if picture_path != "":
	excel.insert_picture_with_same_size_of_input_range("", [17,1,20,4], picture_path)
```
