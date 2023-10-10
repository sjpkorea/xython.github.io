# -*- coding: utf-8 -*-
import basic_data  # xython 모듈

import win32com.client  # pywin32의 모듈
import win32  # pywin32의 모듈
import scolor

class ganada:


	def __init__(self, file_name=""):
		# 공통으로 사용할 변수들을 설정하는 것이다
		self.base_data = basic_data.basic_data()
		self.color = scolor.scolor()
		self.var = self.base_data.vars  # 패키지내에서 공통으로 사용되는 변수

		self.var_word = {}  # 워드용으로 공통으로 사용되는 변수들
		self.enum_word = {}  # 워드용으로 enum으로 사용되는 변수들
		self.obj_word = {}  # 객체를 사용하기 위해서 사용하는것

		self.data_enum_word()
		self.data_var_word()

		# 워드를 실행시킵니다
		self.word_program = win32com.client.dynamic.Dispatch('Word.Application')
		self.word_program.Visible = 1

		self.check_file(file_name)

	def check_content_name(self, input_name):
		"""
		어떤 기준으로 할것인지를 확인하는 것
		content로 사용되는 단어들을 이것저것 사용하여도 적용이 가능하도록 만든것

		:param input_name:
		:return:
		"""
		type_dic = {"line": "line", "줄": "line", "한줄": "line", "라인": "line",
		            "paragraph": "paragraph", "패러그래프": "paragraph", "문단": "paragraph", "para": "paragraph",
		            "word": "word", "단어": "word", "워드": "word",
		            "sentence": "sentence", "문장": "sentence",
		            }
		result = type_dic[input_name]
		return result

	def check_file(self, file_name=""):
		"""
		만약 오픈된 워드가 하나도 없으면,새로운 빈 워드를 만든다

		:param file_name: 입력한 화일 이름
		:return:
		"""
		if file_name == "":
			# 만약 오픈된 워드가 하나도 없으면,새로운 빈 워드를 만든다
			try:
				self.active_word_file = self.word_program.ActiveDocument
			except:
				self.word_program.Documents.Add()
				self.active_word_file = self.word_program.ActiveDocument
		elif file_name == "new":
			self.word_program.Documents.Add()
			self.active_word_file = self.word_program.ActiveDocument

		else:
			self.word_program.Documents.Open(file_name)
			self.active_word_file = self.word_program.ActiveDocument
			self.word_program.ActiveDocument.ActiveWindow.View.Type = 3
		self.selection = self.word_program.Selection

	def check_selection(self):
		"""
		선택한 영역을 객체로 만들어서 돌려준다
		영역이 선택된 영역이 없다면, selection은 현재 cursor가 가르키고있는 위치를 가르킨다

		:return:
		"""
		self.var_word["selection"] = self.word_program.Selection
		return self.var_word["selection"]

	def close(self):
		"""
		현재 활성화된 문서를 닫는다

		:return:
		"""
		self.active_word_file.Close()

	def close_all_without_saving(self):
		"""
		현재 활성화된 문서를 저장하지 않고 그냥 닫는다

		:return:
		"""
		for one in self.word_program.Documents:
			one.Close(SaveChanges=False)

	def count_character_nos_in_selection(self):
		"""
		선택된영역의 글자수를 갖고온다

		:return:
		"""
		result = self.word_program.Selection.Characters.Count
		return result

	def count_file_nos_in_document(self):
		"""
		현재 열려져있는 워드화일의 모든 걋수를 갖고온다

		:return:
		"""
		result = self.word_program.Documents.Count
		return result

	def count_paragraph_nos_in_document(self):
		"""
		현재 활성화된 워드의 모든 문단수 갖고온다
		형태적인 분류 : active_document(화일) > sentence(문장) > word(한 단어) > character(한글자)
		의미적인 분류 : active_document(화일) > paragraph(문단) > line(줄) > word(한 단어) > character(한글자)
		sentence : 표현이 완결된 단위, 그 자체로 하나의 서술된 문장이 되는 것
		paragraph : 줄바꿈이 이루어지기 전까지의 자료


		:return:
		"""
		result = self.active_word_file.Paragraphs.Count
		return result

	def count_paragraph_nos_in_selection(self):
		"""
		현재 선택되어진 영역에서의 모든 문단수
		형태적인 분류 : active_document(화일) > sentence(문장) > word(한 단어) > character(한글자)
		의미적인 분류 : active_document(화일) > paragraph(문단) > line(줄) > word(한 단어) > character(한글자)
		sentence : 표현이 완결된 단위, 그 자체로 하나의 서술된 문장이 되는 것
		paragraph : 줄바꿈이 이루어지기 전까지의 자료


		:return:
		"""
		result = self.selection.Paragraphs.Count
		return result

	def count_table_nos_in_document(self):
		"""
		현재 워드화일안의 테이블의 총 갯수

		:return:
		"""
		result = self.active_word_file.Tables.Count
		return result

	def count_word_nos_in_document(self):
		"""
		현재 워드화일안의 총단어숫자

		:return:
		"""
		result = len(str(self.read_all_text_in_document()).split())
		return result

	def cut_selection(self):
		"""
		선택한 영역 잘라내기

		:return:
		"""
		self.word_program.Selection.Cut()

	def data_enum_word(self):
		"""
		워드에서 사용되는 자주 사용하는 enum모음
		전부 소문자 이다

		:return:
		"""
		self.enum_word["wdCell"] = 12,
		self.enum_word["wdColumn"] = 9,
		self.enum_word["wdRow"] = 10,
		self.enum_word["wdTable"] = 15,
		self.enum_word["wdCharacte"] = 1
		self.enum_word["wdWord"] = 2
		self.enum_word["wdCharacterFormatting"] = 13
		self.enum_word["wdItem"] = 16
		self.enum_word["wdLine"] = 5  # 라인
		self.enum_word["wdSentence"] = 3  # 글을쓰다가 .까지의 영역
		self.enum_word["wdParagraph"] = 4  # 문단
		self.enum_word["wdParagraphFormatting"] = 14
		self.enum_word["wdScreen"] = 7
		self.enum_word["wdSection"] = 8  # 임의적으로 구역을 나누는것
		self.enum_word["wdStory"] = 6
		self.enum_word["wdWindow"] = 11

		self.enum_word["wdGoToAbsolute"] = 1  # An absolute position.
		self.enum_word["wdGoToFirst"] = 1  # The first instance of the specified object.
		self.enum_word["wdGoToLast"] = -1  # The last instance of the specified object.
		self.enum_word["wdGoToNext"] = 2  # The next instance of the specified object.
		self.enum_word["wdGoToPrevious"] = 3  # The previous instance of the specified object.
		self.enum_word["wdGoToRelative"] = 2  # A position relative to the current position.
		self.enum_word["wdGoToBookmark"] = -1  # A bookmark.
		self.enum_word["wdGoToComment"] = 6  # A comment.
		self.enum_word["wdGoToEndnote"] = 5  # An endnote.
		self.enum_word["wdGoToEquation"] = 10  # An equation.
		self.enum_word["wdGoToField"] = 7  # A field.
		self.enum_word["wdGoToFootnote"] = 4  # A footnote.
		self.enum_word["wdGoToGrammaticalError"] = 14  # A grammatical error.
		self.enum_word["wdGoToGraphic"] = 8  # A graphic.
		self.enum_word["wdGoToHeading"] = 11  # A heading.
		self.enum_word["wdGoToLine"] = 3  # A line.
		self.enum_word["wdGoToObject"] = 9  # An object.
		self.enum_word["wdGoToPage"] = 1  # A page.
		self.enum_word["wdGoToPercent"] = 12  # A percent.
		self.enum_word["wdGoToProofreadingError"] = 15  # A proofreading error.
		self.enum_word["wdGoToSection"] = 0  # A section.
		self.enum_word["wdGoToSpellingError"] = 13  # A spelling error.
		self.enum_word["wdGoToTable"] = 2  # A table.

	def data_for_cursor(self):
		"""
		현재 커서가 위치한곳의 정보 (커서의 시작위치, 끝위치)
		가끔 사용을 하다보면, 정확히 어디인지 모를때가 많아, 사용하기 쉽도록 커서의 위치를 모두 만들도록 하자

		:return:
		"""
		self.var_word["cursor_start"] = self.selection.Range.Start
		self.var_word["cursor_end"] = self.selection.Range.End

	def data_for_file(self):
		"""
		현재 워드화일안에 대한 정보들

		:return:
		"""
		self.var_word["current_page_start_no"] = self.word_program.Selection.Range.Information(1)
		self.var_word["current_page_end_no"] = self.word_program.Selection.Range.Information(3)
		self.var_word["page_total"] = self.word_program.Selection.Range.Information(4)
		self.var_word["cap_on_off"] = self.word_program.Selection.Range.Information(21)
		self.var_word["num_on_off"] = self.word_program.Selection.Range.Information(22)
		self.var_word["current_line_index"] = self.word_program.Selection.Range.Information(10)
		self.var_word["zoom"] = self.word_program.Selection.Range.Information(19)
		self.var_word["file_name"] = self.active_word_file.Name
		self.var_word["file_fullname"] = self.active_word_file.FullName
		self.var_word["file_path"] = self.active_word_file.Path
		self.var_word["paragraph_nos"] = self.active_word_file.Paragraphs.Count
		self.var_word["file_nos"] = self.word_program.Documents.Count
		self.var_word["table_nos"] = self.active_word_file.Tables.Count

		self.data_for_selection()
		return self.var_word

	def data_for_selection(self):
		"""
		현재 selection에 대한 정보들

		:return:
		"""
		self.var_word["start_page_no_for_selection"] = self.word_program.Selection.Range.Information(1)
		self.var_word["end_page_no_for_selection"] = self.word_program.Selection.Range.Information(3)
		self.var_word["start_line_no_for_selection"] = self.word_program.Selection.Range.Information(10)
		self.var_word["end_line_no_for_selection"] = self.read_line_no_at_end_of_selection()
		self.var_word["word_nos_in_selection"] = self.selection.Words.Count
		self.var_word["start_word_no_in_selection"] = self.get_line_no_at_start_of_selection()
		self.var_word["character_nos_for_selection"] = self.selection.Characters.Count
		self.var_word["line_nos_for_selection"] = self.selection.Lines.Count
		self.var_word["start_character_no_in_selection"] = self.selection.Start
		self.var_word["end_no_character_in_selection"] = self.selection.End
		self.var_word["start_paragraph_no_for_selection"] = self.read_paragraph_no_at_start_of_selection()
		self.var_word["paragraph_nos_for_selection"] = self.selection.Paragraphs.Count

		self.var_word["selection"] = {}
		self.var_word["selection"]["start_page_no"] = self.word_program.Selection.Range.Information(1)
		self.var_word["selection"]["end_page_no"] = self.word_program.Selection.Range.Information(3)
		self.var_word["selection"]["start_line_no"] = self.word_program.Selection.Range.Information(10)
		self.var_word["selection"]["end_line_no"] = self.read_line_no_at_end_of_selection()
		self.var_word["selection"]["start_word_no"] = self.get_line_no_at_start_of_selection()
		self.var_word["selection"]["start_character_no"] = self.selection.Start
		self.var_word["selection"]["end_character_no"] = self.selection.End
		self.var_word["selection"]["start_paragraph_no"] = self.read_paragraph_no_at_start_of_selection()

		self.var_word["selection"]["character_nos"] = self.selection.Characters.Count
		self.var_word["selection"]["word_nos"] = self.selection.Words.Count
		self.var_word["selection"]["line_nos"] = self.selection.Lines.Count
		self.var_word["selection"]["paragraph_nos"] = self.selection.Paragraphs.Count

		return self.var_word

	def data_for_table(self):
		"""
		현재 워드화일안의 테이블들의 갯수들

		:return:
		"""
		self.var_word["table_nos"] = self.active_word_file.Tables.Count
		return self.var_word

	def data_var_word(self):
		"""
		보통 라인이나 색들의 일반적인 변수들에대한 enum을 넣어서 공통적으로 사용하기 위한 것이다

		:return:
		"""
		self.var_word["line"] = {}
		self.var_word["line"]["-."] = 5
		self.var_word["line"]["-.."] = 6
		self.var_word["line"]["."] = 2
		self.var_word["line"]["="] = 7
		self.var_word["line"]["-"] = 1

		self.var_word["color_index"] = {}
		self.var_word["color_index"]["red"] = 6
		self.var_word["color_index"]["bla"] = 1
		self.var_word["color_index"]["blu"] = 2
		self.var_word["color_index"]["basic"] = 0
		self.var_word["color_index"][""] = 0
		self.var_word["color_index"]["gra"] = 16
		self.var_word["color_index"]["gre"] = 11
		self.var_word["color_index"]["pin"] = 5
		self.var_word["color_index"]["vio"] = 12
		self.var_word["color_index"]["whi"] = 8
		self.var_word["color_index"]["yel"] = 7

		self.var_word["color_24bit"] = {}
		self.var_word["color_24bit"]["aqu"] = 13421619
		self.var_word["color_24bit"][""] = -16777216
		self.var_word["color_24bit"]["bla"] = 0
		self.var_word["color_24bit"]["blu"] = 16711680
		self.var_word["color_24bit"]["bro"] = 13209
		self.var_word["color_24bit"]["gre"] = 32768
		self.var_word["color_24bit"]["ind"] = 10040115
		self.var_word["color_24bit"]["ora"] = 26367
		self.var_word["color_24bit"]["pin"] = 16711935
		self.var_word["color_24bit"]["red"] = 255
		self.var_word["color_24bit"]["vio"] = 8388736
		self.var_word["color_24bit"]["whi"] = 16777215
		self.var_word["color_24bit"]["yel"] = 65535

		self.var_word["line_width"] = {}
		self.var_word["line_width"]["yel"] = 7
		self.var_word["line_width"]["25"] = 2
		self.var_word["line_width"]["50"] = 4
		self.var_word["line_width"]["75"] = 6
		self.var_word["line_width"]["100"] = 8
		self.var_word["line_width"]["150"] = 12
		self.var_word["line_width"]["225"] = 18
		self.var_word["line_width"]["300"] = 24
		self.var_word["line_width"]["450"] = 36
		self.var_word["line_width"]["600"] = 48

		self.var_word["line_width"]["---"] = 2
		self.var_word["line_width"]["--"] = 4
		self.var_word["line_width"]["-"] = 6
		self.var_word["line_width"]["basic"] = 8
		self.var_word["line_width"][""] = 8
		self.var_word["line_width"]["+"] = 12
		self.var_word["line_width"]["++"] = 18
		self.var_word["line_width"]["+++"] = 24
		self.var_word["line_width"]["++++"] = 36
		self.var_word["line_width"]["+++++"] = 48

	def delete_line_by_no(self, input_line_no=1):
		"""
		현재 워드화일안의 전체문서중 라인번호로 삭제

		:param input_line_no: 라인번호
		:return:
		"""
		self.select_nth_line_from_begin(input_line_no)
		self.word_program.Selection.range.Text = ""

	def delete_paragraph_by_no(self, input_no=1):
		"""
		현재 워드화일안의 문단번호로 삭제
		형태적인 분류 : active_document(화일) > sentence(문장) > word(한 단어) > character(한글자)
		의미적인 분류 : active_document(화일) > paragraph(문단) > line(줄) > word(한 단어) > character(한글자)
		sentence : 표현이 완결된 단위, 그 자체로 하나의 서술된 문장이 되는 것
		paragraph : 줄바꿈이 이루어지기 전까지의 자료


		:param input_no: 문단번호
		:return:
		"""
		self.select_nth_paragraph_from_begin(input_no)
		self.word_program.Selection.range.Text = ""

	def delete_selection(self):
		"""
		선택한 영역을 삭제

		:return:
		"""
		self.word_program.Selection.Delete()


	def delete_xline_in_table(self, table_obj, x_position, x_nos):
		"""
		현재 워드화일안의 테이블객체에서 가로행 번호를 이용하여 가로행을 삭제

		:param table_obj: 테이블 객제
		:param x_position: 가로행의 시작번호
		:param x_nos: 삭제한 가로행의 갯수
		:return:
		테이블의 가로행을 삭제
		"""
		for no in range(x_nos):
			table_obj.Rows(x_position).Delete()

	def delete_yline_in_table(self, table_obj, y_position, y_nos):
		"""
		현재 워드화일안의 테이블객체에서 세로행 번호를 이용하여 세로행을 삭제

		:param table_obj:  테이블 객제
		:param y_position:  세로행의 시작번호
		:param y_nos: 삭제한 세로행의 갯수
		:return:
		"""
		for no in range(y_nos):
			table_obj.Columns(y_position).Delete()

	def draw_borderline_in_selection(self):
		"""
		선택영역의 와곽선 그리기

		:return:
		"""
		self.selection.Font.Borders(1).LineStyle = 7  # wdLineStyleDouble	7
		self.selection.Font.Borders(1).LineWidth = 6  # wdLineWidth075pt	6
		self.selection.Font.Borders(1).ColorIndex = 7  # 7 :yellow

	def draw_line_color_for_table(self, table_obj, inside_color="bla", outside_color="bla"):
		"""
		테이블의 선을 색칠하기

		:param table_obj:  테이블 객제
		:param inside_color: 안쪽 색이름
		:param outside_color: 바깥쪽 색이름
		:return:
		"""
		table_obj.Borders.InsideColorIndex = self.var_word["color_index"][inside_color]
		table_obj.Borders.OutsideColorIndex = self.var_word["color_index"][outside_color]



	def draw_line_style_for_table(self, table_obj, inside_line="-", outside_line="-"):
		"""
		테이블 선의 모양을 선정

		:param table_obj:  테이블 객제
		:param inside_line: 안쪽선의 모양
		:param outside_line: 바깥쪽 선의 모양
		:return:
		"""
		table_obj.Borders.InsideLineStyle = self.var_word["line"][inside_line]
		table_obj.Borders.OutsideLineStyle = self.var_word["line"][outside_line]



	def insert_table_at_cursor(self, x_no, y_no):
		"""
		커서위치에 테이블삽입

		:param x_no:
		:param y_no:
		:return:
		"""
		self.obj_word["active_table"] = self.active_word_file.Tables.Add(self.selection.Range, x_no, y_no)
		self.draw_line_style_for_table(self.obj_word["active_table"])
		return self.obj_word["active_table"]



	def draw_outline_in_selection(self):
		"""
		선택한 영역의 외곽선을  wdToggle스타일로 그리기

		:return:
		"""
		self.selection.Font.Outline = 9999998  # wdToggle

	def draw_outside_border_in_selection(self, line_style=1, line_color="blu", line_width="+"):
		"""
		선택영역의 외곽선을 그리기

		:param line_style: 선의 스타일을 선택
		:param line_color: 선의 색을 선택
		:param line_width: 선의 두께를 선택
		:return:
		"""
		self.selection.Borders.OutsideLineStyle = line_style
		self.selection.Borders.OutsideLineWidth = self.var_word["line_width"][line_width]
		self.selection.Borders.OutsideColor = self.var_word["color_24bit"][line_color]

	def draw_strikethrough_in_selection(self):
		"""
		선택한 영역에 취소선을 적용

		:return:
		"""
		self.selection.Font.StrikeThrough = True

	def draw_underline_in_selection(self):
		"""
		선택한 영역에 언더라인을 적용

		:return:
		"""
		self.selection.Font.Underline = 1  # wdUnderlineSingle = 1, A single line

	def get_all_chacters_no_for_document(self):
		para_nums_total = self.active_word_file.Paragraphs.Count
		end = self.active_word_file.Paragraphs(para_nums_total).Range.End
		return end

	def get_file_name(self):
		"""
		현재 활성화된 워드화일의 이름

		:return:
		"""

		result = self.word_program.ActiveDocument.Name
		return result

	def get_file_name_all(self):
		"""
		현재 열려있는 모든 문서의 이름을 돌려준다

		:return:
		"""
		doc_no = self.word_program.Documents.Count
		result = []
		for no in range(doc_no):
			result.append(self.word_program.Documents(no + 1).Name)
		return result

	def get_line_no_at_start_of_selection(self):
		"""
		현재 활성화된 워드화일에서 선택된영역에서 제일 첫번째 라인의 글자들
		wdFirstCharacterLineNumber : 10

		:return:
		"""
		result = self.selection.Range.Information(10)
		return result

	def get_list1d_by_style_for_document(self):
		"""
		전체 문서에서 스타일이 표준이외의것만 을 기준으로 하나로 만들어서 돌려주는것

		:return:
		"""
		result = []
		story_all = []
		action_no = 0

		para_nums_total = self.active_word_file.Paragraphs.Count
		start = ""
		style_name = ""
		title = ""
		for para in self.active_word_file.Paragraphs:
			story_or_title = para.Range.Text
			style = para.Style.NameLocal

			if style == "표준":
				story_all.append(story_or_title)
			else:
				if start == "":
					if story_all == []:
						story_all = [[]]
					result.append(["무제", "제목", story_all])
					story_all = []
					start = "no"
					style_name = style
					title = story_or_title
				else:
					result.append([title, style_name, story_all])
					style_name = style
					title = story_or_title
					start = "no"
					story_all = []

			print(style, action_no, "/", para_nums_total, action_no / para_nums_total * 100, "%")
			action_no = action_no + 1

		return result

	def get_paragraph_index_at_start_of_selection(self):
		"""
		현재 화성화된 문서에서 선택된 영역의 첫번째 문단이 전체문서중 몇번째 문단인 돌려준다
		형태적인 분류 : active_document(화일) > sentence(문장) > word(한 단어) > character(한글자)
		의미적인 분류 : active_document(화일) > paragraph(문단) > line(줄) > word(한 단어) > character(한글자)
		sentence : 표현이 완결된 단위, 그 자체로 하나의 서술된 문장이 되는 것
		paragraph : 줄바꿈이 이루어지기 전까지의 자료


		:return:
		"""
		result = self.word_program.Selection.Range.Information(10)
		return result

	def get_paragraph_object_all(self):
		"""
		현재 화성화된 문서 모든 문단객체를 돌려준다
		형태적인 분류 : active_document(화일) > sentence(문장) > word(한 단어) > character(한글자)
		의미적인 분류 : active_document(화일) > paragraph(문단) > line(줄) > word(한 단어) > character(한글자)
		sentence : 표현이 완결된 단위, 그 자체로 하나의 서술된 문장이 되는 것
		paragraph : 줄바꿈이 이루어지기 전까지의 자료


		:return:
		"""
		self.obj_word["paragraphs"] = self.active_word_file.Paragraphs
		return self.obj_word["paragraphs"]

	def get_paragraph_object_by_index(self, input_para_no):
		"""
		현재 화성화된 워드에서 문단번호로 문단객체를 갖고온다

		:param input_para_no: 문단번호
		:return:
		"""
		self.obj_word["index_paragraph"] = self.active_word_file.Paragraphs(input_para_no)
		return self.obj_word["index_paragraph"]

	def get_strat_chacacter_no_for_selection(self):
		"""
		현재 화성화된 워드에서 선택된 영역의 첫번째 글자가 전체 글자에서의 몇번째 글자번호인지 갖고오는 것
		선택된것이 없을때는 현재 커서가 대신한다

		:return:
		"""
		result = self.word_program.Selection.Characters.Count
		return result

	def get_style_name_all(self):
		"""
		현재 화성화된 워드 화일안의 모든 스타일을 돌려준다

		:return:
		"""
		result = []
		stylecount = self.active_word_file.Styles.Count
		for i in range(1, stylecount + 1):
			styleObject = self.active_word_file.Styles(i)
			result.append(styleObject.NameLocal)
		return result

	def get_table_obj_all(self):
		"""
		현재 화성화된 워드 화일안의 모든 테이블객체를 돌려준다
		테이블 객체란 테이블에대한 모든 정보를 갖고있는 클래스의 인스턴스이다

		:return:
		"""
		self.obj_word["tables"] = self.active_word_file.Tables
		return self.obj_word["tables"]


	def get_table_obj_by_index(self, input_table_no=1):
		"""
		현재 화성화된 워드 화일안의 테이블 번호로 테비블 객체를 갖고오는 것

		:param input_table_no: 테이블 번호
		:return:
		"""
		self.obj_word["index_table"] = self.active_word_file.Tables(input_table_no)
		return self.obj_word["index_table"]

	def get_table_obj_by_table_no(self, input_table_no):
		"""
		현재 화성화된 워드 화일안의 테이블 번호로 테비블 객체를 갖고오는 것
		:param input_table_no: 테이블 번호
		:return:
		"""
		table_obj = self.active_word_file.Tables(input_table_no)
		self.obj_word["active_table"] = table_obj
		return table_obj

	def get_text_for_current_paragraph(self, input_no=1):
		"""
		현재 커서가 있는 문단을 선택해서, 그 문단 전체의 text를 돌려준다
		형태적인 분류 : active_document(화일) > sentence(문장) > word(한 단어) > character(한글자)
		의미적인 분류 : active_document(화일) > paragraph(문단) > line(줄) > word(한 단어) > character(한글자)
		sentence : 표현이 완결된 단위, 그 자체로 하나의 서술된 문장이 되는 것
		paragraph : 줄바꿈이 이루어지기 전까지의 자료


		:param input_no:
		:return:
		"""
		self.selection.GoTo(What=4, Which=1, Count=input_no)
		result = self.word_program.Selection.range.Text
		return result

	def get_xy_for_selection(self):
		"""
		선택된 영역의 위치시작과 끝의 번호값을 갖고온다

		:return:
		"""
		x = self.word_program.Selection.Start
		y = self.word_program.Selection.End
		return [x, y]

	def history(self):
		"""
		
		:return: 
		"""

		result = """
		2023-10-09 : 전반적으로 바꿈, github에 문서화를 위해서 xythonn에 들어있는 대부분의 모듈을 정리함
		
		"""
		
		return result

	def insert_header(self):
		"""
		헤더를 삽입

		:return:
		"""
		for section in self.active_word_file.Sections:
			# header를 하나씩 설정할수는 없다
			section.Headers(1).PageNumbers.Add(PageNumberAlignment=2, FirstPage=True)
			section.Headers(1).PageNumbers.ShowFirstPageNumber = True
			section.Headers(1).PageNumbers.RestartNumberingAtSection = True
			section.Headers(1).PageNumbers.StartingNumber = 1

	def insert_header_new(self):
		"""
		헤더를 삽입

		:return:
		"""
		page_no = 0
		for section in self.active_word_file.Sections:
			section.Headers(1).Range.Fields.Update()
			headersCollection = section.Headers
			for header in headersCollection:
				header.Range.Fields.Update()
				page_no = page_no + 111
				# print("헤더", page_no)
				aaa = header.Range
				aaa.Select()
				header.Range.Text = "헤더 : " + str(page_no)
				# aaa.Font.Bold = True
				# aaa.ParagraphFormat.Alignment = 1
				new_table = self.active_word_file.Tables.Add(Range=aaa, NumRows=1, NumColumns=3, DefaultTableBehavior=0,
				                                        AutoFitBehavior=0)
				new_table.Cell(1, 3).range.ParagraphFormat.Alignment = 0
				new_table.Cell(1, 3).range.Text = "헤더 : " + str(page_no)

		for section in self.active_word_file.Sections:
			HeaderTablesCount = section.Headers(1).Range.Tables.Count
			FooterTablesCount = section.Footers(1).Range.Tables.Count

			for index in range(HeaderTablesCount):
				HeaderTable = section.Headers(1).Range.Tables(index + 1)
				HeaderTable.Cell(1, 1).Range.Text = index

	def insert_many_xline_in_table(self, table_obj, x_position, x_nos):
		"""
		테이블객체의 테이블에 가로행을 추가하는 것 (아랫부분에 추가)

		:param table_obj:  테이블 객제
		:param x_position: 가로행의 시작 번호
		:param x_nos:  몇라인을 추가할것인지 설정
		:return:
		"""
		table_obj.Rows(x_position).Select()
		self.selection.InsertRowsBelow(x_nos)

	def insert_many_yline_in_table(self, table_obj, y_position, y_nos):
		"""
		테이블객체의 테이블에 세로행을 추가하는 것 (오른쪽에 추가)

		:param table_obj:  테이블 객제
		:param y_position: 세로행의 시작 번호
		:param y_nos: 몇라인을 추가할것인지 설정
		:return:
		"""
		table_obj.Columns(y_position).Select()
		self.selection.InsertColumnsRight(y_nos)

	def insert_new_line_at_end_of_selection(self):
		"""
		현재 커서의 위치에 줄바꿈문자를 넣어서 새로운 문단을 만드는 것이다

		:return:
		"""
		self.word_program.Selection.InsertAfter("\r\n")

	def insert_new_para_with_properties(self, input_text, size=14, font="Arial", align="right", bold=True,
	                                    input_color="red", style="표준"):
		"""
		선택한 위치에 글을 쓴다
		형태적인 분류 : active_document(화일) > sentence(문장) > word(한 단어) > character(한글자)
		의미적인 분류 : active_document(화일) > paragraph(문단) > line(줄) > word(한 단어) > character(한글자)
		sentence : 표현이 완결된 단위, 그 자체로 하나의 서술된 문장이 되는 것
		paragraph : 줄바꿈이 이루어지기 전까지의 자료


		wdAlignParagraphCenter	1	Center-aligned.
		wdAlignParagraphJustify	3	Fully justified.
		wdAlignParagraphLeft	0	Left-aligned.
		wdAlignParagraphRight	2	Right-aligned.

		:param input_text:
		:param size:
		:param font:
		:param align:
		:param bold:
		:param input_color:
		:param style:
		:return:
		"""

		temp_value = self.color.change_scolor_to_rgb(input_color)
		rgb_int = self.color.change_rgb_to_rgbint(temp_value)

		self.word_program.Selection.InsertAfter(input_text + "\r\n")
		para_no = self.read_paragraph_no_at_start_of_selection()
		self.select_paragraph_by_no(para_no - 1)

		self.selection.Style = style
		self.selection.Range.Font.Name = font
		self.selection.Range.Font.Bold = bold
		self.selection.Range.Font.Size = size
		self.selection.Font.TextColor.RGB = rgb_int
		self.active_word_file.Paragraphs(para_no - 1).Alignment = 2

	def insert_no_colored_table_at_cursor(self, x_no, y_no):
		"""
		커서위치에 테이블삽입
		단, 선의 색이 없는 것을 적용해서 문서를 넣어서 사용하는 것을 만드는 것이다

		:param x_no:
		:param y_no:
		:return:
		"""
		self.obj_word["active_table"] = self.active_word_file.Tables.Add(self.selection.Range, x_no, y_no)
		self.obj_word["active_table"].Borders.LineStyle = 0  # wdLineStyleNone =0
		return self.obj_word["active_table"]

	def insert_one_xline_at_end_of_table(self, table_obj):
		"""
		테이블에 가로행을 추가하는것 (아랫부분에 추가)

		:param table_obj:  테이블 객제
		:return:
		"""
		total_row = table_obj.Rows.Count
		table_obj.Rows(total_row).Select()
		self.selection.InsertRowsBelow(1)

	def insert_picture_at_cursor(self, file_full_name, size_w, size_h):
		"""
		커서위치에 그림삽입

		:param file_full_name:
		:param size_w:
		:param size_h:
		:return:
		"""
		current_pic = self.word_program.Selection.range.InlineShapes.AddPicture(file_full_name)
		current_pic.Height = size_h
		current_pic.Width = size_w

	def insert_table_at_end_of_paragraph(self, para_no, table_xy=[5, 5]):
		"""
		*** 없애도 되는 것
		선택한 문단뒤에 테이블을 만든다
		형태적인 분류 : active_document(화일) > sentence(문장) > word(한 단어) > character(한글자)
		의미적인 분류 : active_document(화일) > paragraph(문단) > line(줄) > word(한 단어) > character(한글자)
		sentence : 표현이 완결된 단위, 그 자체로 하나의 서술된 문장이 되는 것
		paragraph : 줄바꿈이 이루어지기 전까지의 자료


		:param para_no:
		:param table_xy:
		:return:
		"""
		myrange = self.active_word_file.Paragraphs(para_no).Range
		mytable = self.active_word_file.Tables.Add(myrange, table_xy[0], table_xy[1])
		mytable.AutoFormat(36)

	def insert_text_at_end_of_selection(self, input_text="aaaaaaaa"):
		"""
		선택한 영역의 제일 뒷부분에 text값을 값을 넣것

		:param input_text: 입력값
		:return:
		"""
		self.selection.InsertAfetr(input_text)

	def insert_text_at_start_of_selection(self, input_text="aaaaaaaa"):
		"""
		선택한 영역의 제일 앞부분에 text값을 값을 넣것

		:param input_text: 입력값
		:return:
		"""
		self.selection.InsertBefore(input_text)

	def make_table_obj(self, row_line_no=3, col_line_no=3):
		"""
		기본적인 형태의 테이블 객체를 만든다

		:param row_line_no:
		:param col_line_no:
		:return:
		"""

		new_table = self.active_word_file.Tables.Add(Range=self.selection.Range, NumRows=row_line_no, NumColumns=col_line_no,
		                                        DefaultTableBehavior=0, AutoFitBehavior=0)
		new_table.Cell(1, 3).range.ParagraphFormat.Alignment = 0

		# tableToChange.Borders(wdBorderTop).LineStyle = wdLineStyleNone
		# tableToChange.Borders(wdBorderLeft).LineStyle = wdLineStyleNone
		# tableToChange.Borders(wdBorderBottom).LineStyle = wdLineStyleNone
		# tableToChange.Borders(wdBorderRight).LineStyle = wdLineStyleNone
		# tableToChange.Borders(wdBorderVertical).LineStyle = wdLineStyleNone
		# tableToChange.Borders(wdBorderDiagonalDown).LineStyle = wdLineStyleNone
		# tableToChange.Borders(wdBorderDiagonalUp).LineStyle = wdLineStyleNone
		return new_table

	def merge_entire_xline_at_table(self, table_obj, start_x):
		"""
		선택된 가로줄을 전부 병합시키는것

		:param table_obj:  테이블 객제
		:param start_x: 가로줄번호
		:return:
		"""
		count_y = table_obj.Columns.Count
		count_x = table_obj.Rows.Count
		print(count_x, count_y)
		table_obj.Cell(start_x, 1).Merge(MergeTo=table_obj.Cell(start_x, count_y))

	def merge_entire_yline_at_table(self, table_obj, start_y):
		"""
		선택된 세로줄을 전부 병합시키는것

		:param table_obj:  테이블 객제
		:param start_y: 세로줄번호
		:return:
		"""
		count_y = table_obj.Columns.Count
		count_x = table_obj.Rows.Count
		print(count_x, count_y)
		table_obj.Cell(1, start_y).Merge(MergeTo=table_obj.Cell(count_x, start_y))

	def merge_selection_area_in_table(self, table_obj, xyxy):
		"""
		테이블의 가로와 세로번호까지의 영역을 병합

		:param table_obj:  테이블 객제
		:param xyxy: [가로시작, 세로시작, 가로끝, 세로끝]
		:return:
		"""
		my_range = self.active_word_file.Range(Start=table_obj.Cell(xyxy[0], xyxy[1]).Range.Start,
		                                  End=table_obj.Cell(xyxy[2], xyxy[3]).Range.End)
		my_range.Select()
		self.selection.Cells.Merge()

	def merge_xyxy_at_table(self, table_obj, xyxy):
		"""
		시작지점에서 몇개를 병합할것인지

		:param table_obj:  테이블 객제
		:param start_x:
		:param start_y:
		:param x_len:
		:param y_len:
		:return:
		"""
		table_obj.Cell(xyxy[0], xyxy[1]).Merge(MergeTo=table_obj.Cell(xyxy[2], xyxy[3]))

	def move_cursor_by_index(self, x_char=1):
		"""
		문서의 맨처음에서 n번째 글자로 커서를 이동

		:param x_char: 번호
		:return:
		"""
		self.active_word_file.Range(x_char, x_char).Select()

	def move_cursor_from_end_of_selection(self, input_index):
		"""
		현재 선택한영역에서 n번째 문자뒤로 커서를 옮기는것

		:param input_index: 번호
		:return:
		"""
		y = self.selection.Range.End

		# 읽을때는 range를 사용하고, 쓸때는 사용하지 않는다
		self.selection.Start = y + input_index
		self.selection.End = y + input_index
		self.selection.Select()
		result = self.selection.Range.Start
		print("이동전 위치 =>", y, "이동후 위치 =>", result)
		return result

	def move_cursor_to_end_of_document(self):
		"""
		문서의 끝으로 커서를 이동
		맨마지막에 글자를 추가하거나 할때 사용한다

		:return:
		"""
		self.selection.EndKey(Unit=6)

	def move_cursor_to_end_of_selection(self):
		"""
		선택영역의 끝으로 커서를 이동

		:return:
		"""
		y = self.selection.Range.End
		self.active_word_file.Range(y, y).Select()

	# self.selection.MoveEnd = 8
	def move_cursor_to_n_line_from_selection(self, input_no=1):
		"""
		선택된 라인에서 몇번째 라인뒤로 이동하는 것 (라인을 기준으로 이동)
		계속해서 사용하면 기본으로 1로 설정이 되어있어서, 한줄씩 내려갈수 있다

		:param input_no:
		:return:
		"""
		self.word_program.Selection.MoveRight(Unit=3, Count=input_no)

	def move_cursor_to_next_nth_character(self, input_no=1):
		"""
		현재 커서에서 글자수로 n번째 뒤로 이동 (글자를 기준으로 이동)

		:param input_no:
		:return:
		"""
		y_char = self.selection.End  # y_char : 영역을 기준으로 문서에서 처음부터 문자를 기준으로 (x_char, y_char)로 나타냄
		self.active_word_file.Range(y_char + input_no, y_char + input_no).Select()

	def move_cursor_to_next_nth_line(self, input_no):
		"""
		선택된 커서를 기준으로 몇번째 라인뒤로 이동하는 것 (라인을 기준으로 이동)
		마이너스값을 넣으면 앞으로 이동한다

		:param input_no:
		:return:
		몇줄 뒤로 이동
		"""
		self.select_next_n_line_from_selection(input_no)
		self.selection.MoveLeft()

	def move_cursor_to_next_nth_paragraph(self, input_no):
		"""
		몇줄 뒤로 이동 (라인을 기준으로 이동)
		마이너스값을 넣으면 앞으로 이동한다

		:param input_no:
		:return:
		"""
		self.select_next_n_paragraphs_from_selection(input_no)
		self.selection.MoveLeft()

	def move_cursor_to_next_nth_word(self, input_no):
		"""
		현재커서의 위치를 기준으로 몇번째 단어 뒤로 이동 (단어를 기준으로 이동)
		마이너스값을 넣으면 앞으로 이동한다

		:param input_no:
		:return:
		"""
		self.select_next_n_words_from_selection(input_no)
		self.selection.MoveLeft()

	def move_cursor_to_previous_nth_character(self, input_no):
		"""
		현재커서의 위치에서 n번째 이전 단어로 커서 이동

		:param input_no:
		:return:
		"""
		self.move_cursor_to_next_nth_character(-1 * input_no)

	def move_cursor_to_previous_nth_line(self, input_no):
		"""
		현재커서의 위치에서 1줄 이전으로 커서 이동

		:param input_no:
		:return:
		"""
		self.move_cursor_to_next_nth_line(-1 * input_no)

	def move_cursor_to_previous_nth_paragraph(self, input_no):
		"""
		현재커서의 위치에서 1줄 이전으로 커서 이동

		:param input_no:
		:return:
		"""
		self.move_cursor_to_next_nth_paragraph(-1 * input_no)

	def move_cursor_to_previous_nth_word(self, input_no):
		"""
		현재커서의 위치에서 n번째 이전 단어로 커서 이동

		:param input_no:
		:return:
		"""
		self.move_cursor_to_next_nth_word(-1 * input_no)

	def move_cursor_to_start_of_document(self):
		"""
		활성화된 워드화일의 처음으로 커서를 이동

		:return:
		"""
		self.move_cursor_by_index(0)

	def move_cursor_to_start_of_line_no(self, input_no=1):
		"""
		원하는 순서의 라인의 첫번째 위치로 이동

		:param input_no:
		:return:
		"""
		self.selection.GoTo(What=3, Which=1, Count=input_no)
		result = self.word_program.Selection.range.Text
		return result

	def move_cursor_to_start_of_selection(self):
		"""
		선택한 영역의 처음으로 커서를 이동

		:return:
		"""
		x = self.selection.Range.Start
		self.active_word_file.Range(x, x).Select()

	def new_document(self):
		"""
		새 문서를 하나더 만듦

		:return:
		"""
		self.word_program.Documents.Add()

	def paint_border_in_selection(self, input_color):
		"""
		선택영역의 외곽선을 그리기

		:param input_color: 색이름
		:return:
		"""
		self.selection.Font.Borders.Color = self.var_word["color_24bit"][input_color]

	def paint_color_for_cell_in_table(self, table_obj, xy, color_index="red"):
		"""
		테이블객체의 가로세로번호의 셀의 배경색을 색칠하기

		:param table_obj:  테이블 객제
		:param xy:
		:param color_index:
		:return:
		"""
		table_obj.Cell(xy[0], xy[1]).Shading.BackgroundPatternColor = self.var_word["color_24bit"][color_index]

	def paint_highlight_from_char_no1_to_char_no2(self, input_no1, input_no2, input_color = "blu"):
		"""
		선택영역의 글자들의 배경을 하이라이트를 설정

		:param input_color:
		:return:
		"""
		my_range = self.active_word_file.Range(Start=input_no1, End=input_no2)
		my_range.HighlightColorIndex = self.var_word["color_index"][input_color]

	def paint_highlight_in_selection(self, input_color):
		"""
		선택영역의 글자들의 배경을 하이라이트를 설정

		:param input_color:
		:return:
		"""
		self.selection.Range.HighlightColorIndex = self.var_word["color_index"][input_color]



	def paint_shading_background_in_selection(self, input_color):
		"""
		선택영역의 배경색의 음영설정

		:param input_color:
		:return:
		"""
		self.selection.Font.Shading.BackgroundPatternColor = self.var_word["color_24bit"][input_color]


	def paint_shading_foreground_in_selection(self, input_color):
		"""
		선택영역의 foreground의 음영설정

		:param input_color:
		:return:
		"""
		self.selection.Font.Shading.ForegroundPatternColor = self.var_word["color_24bit"][input_color]

	def paste_selection(self):
		"""
		선택영역에 붙여넣기

		:return:
		"""
		self.word_program.Selection.Paste()

	def quit(self):
		"""

		:return:
		워드 프로그램 종료하기
		"""
		self.word_program.Quit()

	def read_all_text_in_document(self):
		"""
		현재 문서에서 모든 텍스트만 돌려준다

		:return:
		"""
		result = self.active_word_file.Range().Text
		return result

	def read_bookmark_list(self):
		"""
		북마크의 리스트를 돌려준다

		:return:
		"""
		result = []
		for bookmark in self.active_word_file.Bookmarks:
			bookmark_name = bookmark.Name
			my_range = self.active_word_file.Bookmarks(bookmark.Name).Range
			my_range_text = my_range.Text
			start_no = my_range.Start
			end_no = my_range.End
			temp = [bookmark_name, start_no, end_no, my_range_text]
			result.append(temp)
		return result

	def read_cursor_position(self):
		"""
		현재 커서의 위치를 돌려준다
		영역이 선택되지 않으면 selection은 cursor를 가르킨다
		기본적으로 시작점을 나타내도록 한다

		:return:
		"""
		result = self.selection.Range.Start
		print("현재 커서의 시작 위치는 ==> ", result)
		return result

	def read_font_size_in_selection(self):
		"""
		선택한 영역의 폰트 크기

		:return:
		"""
		result = self.selection.Font.Size
		return result

	def read_line_no_at_end_of_selection(self):
		"""
		선택한 영역의 마지막 줄번호

		:return:
		"""
		pos2 = self.selection.Range.End
		last_no = self.word_program.Selection.Range.Information(10)
		count = self.selection.Words.Count
		result = last_no - count + 1
		return result

	def read_line_no_at_start_of_selection(self):
		"""
		선택영역의 첫글자가 있는 전체 워드에서의 줄번호

		:return:
		"""
		result = self.word_program.Selection.Range.Information(10)
		return result

	def read_paragraph_no_at_end_of_selection(self):
		"""
		선택영역에서 마지막 문단번호
		형태적인 분류 : active_document(화일) > sentence(문장) > word(한 단어) > character(한글자)
		의미적인 분류 : active_document(화일) > paragraph(문단) > line(줄) > word(한 단어) > character(한글자)
		sentence : 표현이 완결된 단위, 그 자체로 하나의 서술된 문장이 되는 것
		paragraph : 줄바꿈이 이루어지기 전까지의 자료


		:return:
		"""
		start_para_no = self.read_paragraph_no_at_start_of_selection()
		count_para = self.selection.Paragraphs.Count
		result = start_para_no + count_para - 1
		return result

	def read_paragraph_no_at_start_of_selection(self):
		"""
		선택영역의 첫번째 문장이 전체 워드화일의 문장중 몇번째 문장번호인지 알려주는 것
		형태적인 분류 : active_document(화일) > sentence(문장) > word(한 단어) > character(한글자)
		의미적인 분류 : active_document(화일) > paragraph(문단) > line(줄) > word(한 단어) > character(한글자)
		sentence : 표현이 완결된 단위, 그 자체로 하나의 서술된 문장이 되는 것
		paragraph : 줄바꿈이 이루어지기 전까지의 자료

		:return:
		"""

		pos2 = self.selection.Range.End
		myrange = self.active_word_file.Range(Start=0, End=pos2)
		result = myrange.Paragraphs.Count + 1
		return result

	def read_selection(self):
		"""
		현재 커서가 위치한곳의 뒷글자 하나를 나타낸다
		선택한 영역이 떨어져있으면 하나로 인식

		:return:
		"""
		rng_obj = self.word_program.Selection
		# 선택한것중 제일 나중에 선택된것을 갖는다
		print("제일 나중에 선택된것은 ==> ", rng_obj.Text)
		ddd = self.word_program.Selection.Characters
		print("aaa ==> ", ddd.Count, ddd(1).Item)

		# 커서를 한줄 이동시킨다
		# rng_obj.MoveDown()

		# 선택한것중 제일 나중에 선택된것을 갖는다
		print("제일 나중에 선택된것은 ==> ", rng_obj.Text)

		paras_obj = rng_obj.Paragraphs
		# 선택한 영역안의 파라그래프의 숫자
		print("선택한 문장의 갯수 ==> ", paras_obj.Count)

		for no in range(paras_obj.Count):
			new_rng_obj = rng_obj.Paragraphs(no + 1).Range
			print("첫번째 ==> ", new_rng_obj)

		for one in rng_obj.Paragraphs:
			print("번호", one)
			self.word_program.Selection.Start = one.Range.Start
			self.word_program.Selection.End = one.Range.End
			print("제일 나중에 선택된것은 ==> ", self.word_program.Selection.Text)

		for one in range(paras_obj.Count):
			print(paras_obj(one + 1))
		rng_1_obj = paras_obj(1)
		print(rng_obj, rng_obj.Start, rng_obj.End, paras_obj.Count, rng_1_obj)

	def read_text_between_para_1_to_para_2(self, para1_index, para2_index):
		"""
		선택한 2개의 문단 번호 사이의 글을 돌려준다

		:param para1_index:
		:param para2_index:
		:return:
		"""
		start = self.active_word_file.Paragraphs(para1_index).Range.Start
		end = self.active_word_file.Paragraphs(para2_index).Range.End
		result = self.active_word_file.Range(start, end).Text
		return result

	def read_text_for_current_paragraph(self):
		"""
		현재 커서가 있는 문단의 전체 text를 돌려줍니다
		형태적인 분류 : active_document(화일) > sentence(문장) > word(한 단어) > character(한글자)
		의미적인 분류 : active_document(화일) > paragraph(문단) > line(줄) > word(한 단어) > character(한글자)
		sentence : 표현이 완결된 단위, 그 자체로 하나의 서술된 문장이 되는 것
		paragraph : 줄바꿈이 이루어지기 전까지의 자료


		:return:
		"""
		current_para_index = self.word_program.Selection.Range.Information(10)
		result = self.word_program.Selection.Paragraphs(current_para_index).Range.Text
		return result

	def read_text_for_paragraph_index(self, input_no):
		"""
		paragraph 번호에 따라서 해당하는 paragraph의 text 를 갖고오는것
		형태적인 분류 : active_document(화일) > sentence(문장) > word(한 단어) > character(한글자)
		의미적인 분류 : active_document(화일) > paragraph(문단) > line(줄) > word(한 단어) > character(한글자)
		sentence : 표현이 완결된 단위, 그 자체로 하나의 서술된 문장이 되는 것
		paragraph : 줄바꿈이 이루어지기 전까지의 자료


		:param input_no:
		:return:
		"""
		aaa = self.active_word_file.Paragraphs(input_no)
		result = aaa.Range.Text
		return result

	def read_text_for_range(self):
		"""
		range영역의 text를 갖고온다

		:return:
		"""
		result = self.active_word_file.Range().Text
		return result

	def read_text_from_begin_of_paragraph_by_len(self, input_index, x, length):
		"""
		선택된 문단에서 몇번째의 글을 선택하는 것
		일정 영역의 자료를 갖고오는 3
		paragraph를 선택한다, 없으면 맨처음부터
		형태적인 분류 : active_document(화일) > sentence(문장) > word(한 단어) > character(한글자)
		의미적인 분류 : active_document(화일) > paragraph(문단) > line(줄) > word(한 단어) > character(한글자)
		sentence : 표현이 완결된 단위, 그 자체로 하나의 서술된 문장이 되는 것
		paragraph : 줄바꿈이 이루어지기 전까지의 자료


		:param input_index:
		:param x:
		:param length:
		:return:
		"""
		paragraph = self.active_word_file.Paragraphs(input_index)
		# 맨앞에서 몇번째부터, 얼마의 길이를 선택할지를 선정
		x_no = paragraph.Range.Start + x - 1
		y_no = paragraph.Range.Start + x + length - 1
		result = self.active_word_file.Range(x_no, y_no).Text
		return result

	def read_text_from_index1_to_index2(self, index_1, index_2):
		"""
		활성화된 워드화일의 문자번호 사이의 글자를 갖고온다

		:param index_1:
		:param index_2:
		:return:
		"""
		result = self.active_word_file.Range(index_1, index_2).Text
		return result

	def read_text_from_x_to_y(self, x, y):
		"""
		활성화된 워드화일의 문자번호 사이의 글자를 갖고온다
		화일의 글자수를 기준으로 text를 읽어오는 것

		:param x:
		:param y:
		:return:
		"""
		result = self.active_word_file.Range(x, y).Text

	def read_text_in_selection(self):
		"""
		선택된 영역의 text를 갖고오는 것

		:return:
		"""
		result = self.word_program.Selection.range.Text
		return result

	def read_text_in_table_by_xy(self, table_index, lxly):
		"""
		테이블객체에서 가로세로번호의 셀의 text값을 갖고온다

		:param table_index:
		:param lxly:
		:return:
		"""
		table = self.active_word_file.Tables(table_index)
		result = table.Cell(Row=lxly[0], Column=lxly[1]).Range.Text
		# str문자들은 맨 마지막에 끝이라는 문자가 자동으로 들어가서, 이것을 없애야 표현이 잘된다
		return result[:-1]

	def read_word_no_at_end_of_selection(self):
		"""
		선택한 영역에서 제일 마지막 단어의 번호

		:return:
		"""
		pos2 = self.selection.Range.End
		myrange = self.active_word_file.Range(Start=0, End=pos2)
		result = myrange.Words.Count + 1
		return result

	def read_word_no_at_start_of_selection(self):
		"""
		선택한 영역에서 제일 첫번째 단어의 번호

		:return:
		"""
		pos2 = self.selection.Range.End
		myrange = self.active_word_file.Range(Start=0, End=pos2)
		result = myrange.Words.Count + 1
		return result

	def release_selection(self):
		"""
		커서를 selection의 맨 끝을 기준으로 옮겨서 해제한것

		:return:
		"""
		self.selection.Collapse(0)

	def change_selection_to_input_text(self, after_text):
		"""
		selection한 영역을 바꾸는 것

		:param after_text: 바꿀 문자
		:return:
		"""

		self.selection.Range.Text = after_text

	def replace_all(self, before_text, after_text):
		"""
		워드화일에서 한번에 원하는 글자를 바꾸는 것

		:param before_text: 찾을 문자
		:param after_text: 바꿀 문자
		:return:
		"""
		# aaa.Find.Execute(찾을단어, False, False, False, False, False, 앞쪽으로검색, 1, True, 바꿀문자, 전체변경/Replace)
		aaa = self.active_word_file.Range(Start=0, End=self.active_word_file.Characters.Count)
		aaa.Find.Execute(before_text, False, False, False, False, False, True, 1, True, after_text, 2)


	def replace_all_1(self, before_text, after_text):
		"""
		원하는 문자를 한번에 모두 바꾸는 것

		:param before_text: 찾을 문자
		:param after_text: 바꿀 문자
		:return:
		"""
		self.active_word_file.Content.Find.Text = before_text
		self.active_word_file.Content.Replacement.Text = after_text
		self.active_word_file.Content.Find.Execute(Replace=self.enum_word["wdReplaceAll"], Forward=True)

	def replace_all_with_color(self, input_text, after, color_name="red"):
		"""
		화일안의 모든 문자를 바꾸고 색칠하기

		:param input_text:
		:param after:
		:param color_name:
		:return:
		"""

		self.release_selection()
		# 이것이 없으면, 커서이후부터 찾는다
		self.move_cursor_to_start_of_document()
		result = []
		temp_value = self.color.change_scolor_to_rgb(color_name)
		rgb_int = self.color.change_rgb_to_rgbint(temp_value)

		while self.selection.Find.Execute(input_text):
			self.selection.Range.Font.Italic = True
			self.selection.Range.Font.TextColor.RGB = rgb_int
			self.selection.Range.HighlightColorIndex = 7  # 7번은 노랑, 6번은 빨강

			start_no = self.selection.Range.Start
			end_no = start_no + len(input_text)
			self.selection.Range.Text = after

	def replace_all_with_color_from_selection_to_end(self, input_text, after, color_name="red"):
		"""
		현재위치 이후의 모든것을 변경

		:param input_text:
		:param after:
		:param color_name:
		:return:
		"""
		self.release_selection()
		# 이것이 없으면, 커서이후부터 찾는다
		#self.move_cursor_to_start_of_document()
		result = []
		temp_value = self.color.change_scolor_to_rgb(color_name)
		rgb_int = self.color.change_rgb_to_rgbint(temp_value)

		while self.selection.Find.Execute(input_text):
			self.selection.Range.Font.Italic = True
			self.selection.Range.Font.TextColor.RGB = rgb_int
			self.selection.Range.HighlightColorIndex = 7  # 7번은 노랑, 6번은 빨강

			start_no = self.selection.Range.Start
			end_no = start_no + len(input_text)
			self.selection.Range.Text = after

	def replace_one_time_from_selection(self, before, after):
		"""
		전체가 아니고 제일 처음의 것만 바꾸는것

		:param before:
		:param after:
		:return:
		"""
		self.enum_word["wdReplaceOne"] = 1  # Replace the first occurrence encountered.
		aaa = self.active_word_file.Range(Start=0, End=self.active_word_file.Characters.Count)
		aaa.Find.Execute(before, False, False, False, False, False, True, 1, True, after, 1)

	def replace_text_for_selection(self, input_value):
		"""
		선택한 영역안에서 에서만 글자를 변경하는 것

		:param input_value:
		:return:
		"""
		self.word_program.Selection.Delete()
		self.word_program.Selection.InsertBefore(input_value)

	def save(self, file_name=""):
		"""
		화일 저장하기

		:param file_name:
		:return:
		"""
		if file_name == "":
			self.active_word_file.Save()
		else:
			self.active_word_file.SaveAs(file_name)

	def save_as(self, file_name):
		"""
		다른이름으로 화일을 저장

		:param file_name:
		:return:
		"""
		self.active_word_file.SaveAs(file_name)

	def save_as_pdf(self, file_name):
		"""
		pdf로 저장

		:param file_name:
		:return:
		"""
		self.active_word_file.SaveAs(file_name, FileFormat=2)

	def search_all_with_color_and_return_position(self, input_text):
		"""
		전체 화일에서 입력글자를 찾아서 색깔을 넣기

		:param input_text:
		:return:
		"""
		result = []
		while self.selection.Find.Execute(input_text):
			self.selection.Range.Font.Italic = True
			self.selection.Range.Font.Color = 255
			self.selection.Range.HighlightColorIndex = 11
			start_no = self.selection.Range.Start
			end_no = start_no + len(input_text)
			temp = [start_no, end_no, self.selection.Range.Text]
			result.append(temp)
		return result

	def search_first_text_from_cursor(self, input_text):
		"""
		현재 위치에서 찾는것을 입력하면, 바로 다음것을 선택하는 것
		search를 사용할것인지 find를 사용할것인지 정해보자
		replace

		:param input_text:
		:return:
		"""
		result = []
		if self.selection.Find.Execute(input_text):
			self.selection.Range.Font.Italic = True
			self.selection.Range.Font.Color = 255
			self.selection.Range.HighlightColorIndex = 11
			start_no = self.selection.Range.Start
			end_no = start_no + len(input_text)
			temp = [start_no, end_no, self.selection.Range.Text]
			result.append(temp)

		return result

	def select_all_chacters(self):
		"""
		영역을 선택하는 것
		맨앞에서 몇번째부터，얼마의 길이를 선택할지를 선정
		"""
		no_char = self.get_all_chacters_no_for_document()
		self.select_chacters_from_no_to_length(0, no_char - 1)

	def select_all_text(self):
		"""
		모든 문서를 선택하는 것

		:return:
		"""
		self.selection = self.active_word_file.Selection.WholeStory

	def select_bookmark(self, bookmark_name):
		"""
		북마크의 이름을 기준으로 그 영역을 선택하는 것

		:param bookmark_name:
		:return:
		"""
		my_range = self.active_word_file.Bookmarks(bookmark_name).Range
		my_range.Select()

	def select_by_range(self):
		"""
		range 객체의 일정부분을 영역으로 선택

		:return:
		"""
		self.selection = self.active_word_file.Range(0, 0)

	def select_chacters_from_no_to_length(self, x, lengh):
		"""
		영역을 선택하는 것
		맨앞에서 몇번째부터，얼마의 길이를 선택할지를 선정

		:param x:
		:param lengh:
		:return:
		"""
		self.active_word_file.Range(x, x + lengh).Select()




	def select_current_line(self):
		"""
		현재 위치에서 줄의 끝까지 선택

		:return:
		"""
		self.selection.Expand(self.enum_word["wdSentence"])

	def select_current_paragraph(self):
		"""
		현재 위치의 문단을 선택

		:return:
		"""
		self.selection.Expand(self.enum_word["wdParagraph"])

	def select_current_sentence(self):
		"""
		현재 위치에서 줄의 처음까지

		:return:
		"""
		self.selection.Expand(self.enum_word["wdSentence"])

	def select_file_by_name(self, input_name):
		"""
		현재 open된 문서중 이름으로 active문서로 활성화 시키기

		:param input_name:
		:return:
		"""
		self.active_word_file = self.word_program.Documents(input_name)
		self.active_word_file.Activate()

	def select_from_index1_to_index2_by_character_from_selection(self, index1, index2):
		"""
		맨앞에서 몇번째 글자를 선택하는 것

		:param index1:
		:param index2:
		:return:
		"""
		self.active_word_file.Selection.Start = index1
		self.active_word_file.Selection.End = index2
		self.active_word_file.Range.Select()

	def select_line_by_line_no_from_cursor(self, line_no):
		"""
		현재 커서부터 n번째 라인 선택

		:param line_no:
		:return:
		"""
		self.selection.MoveDown(Unit=self.enum_word["wdLine"], Count=line_no)
		self.selection.Expand(self.enum_word["wdLine"])

	def select_multi_line_from_selection(self, line_no_start=1, line_len=3):
		"""
		전체 문서에서 줄수로 선택하는것

		:param line_no_start:
		:param line_len:
		:return:
		"""
		self.select_multi_selection_basic(line_no_start, line_len, "line")

	def select_multi_paragraph_from_selection(self, line_no_start=1, line_len=3):
		"""
		전체 문서에서 줄수로 선택하는것

		:param line_no_start:
		:param line_len:
		:return:
		"""

		self.select_multi_selection_basic(line_no_start, line_len, "paragraph")

	def select_multi_selection_basic(self, line_no_start=1, line_len=3, input_content="line"):
		"""
		전체 문서에서 줄수로 선택하는것

		:param line_no_start:
		:param line_len:
		:param input_content:
		:return:
		"""
		# 어떤 종류인지를 파악하는것
		if input_content == "word":
			content_type = self.enum_word["wdWord"]
		elif input_content == "sentence":
			content_type = self.enum_word["wdSentence"]
		elif input_content == "line":
			content_type = self.enum_word["wdLine"]
		elif input_content == "paragraph":
			content_type = self.enum_word["wdParagraph"]

		# 현재 selction위치를 저장한다
		x = self.selection.Range.Start
		y = self.selection.Range.End

		# 시작점의 위치를 얻어낸다
		self.selection.MoveDown(Unit=content_type, Count=line_no_start)
		self.selection.Expand(content_type)
		x_start = self.selection.Range.Start

		# 원래위치로 이동한다
		self.active_word_file.Range(x, y).Select()
		# 마지막위치로 이동한다
		self.selection.MoveDown(Unit=content_type, Count=line_no_start + line_len)
		self.selection.Expand(content_type)

		y_end = self.selection.Range.End
		self.active_word_file.Range(x_start, y_end).Select()

	def select_multi_sentence_from_selection(self, line_no_start=1, line_len=3):
		"""
		전체 문서에서 줄수로 선택하는것

		:param line_no_start: 라인의 시작 번호
		:param line_len:
		:return:
		"""
		self.select_multi_selection_basic(line_no_start, line_len, "sentence")

	def select_multi_word_from_selection(self, line_no_start=1, line_len=3):
		"""
		전체 문서에서 줄수로 선택하는것

		:param line_no_start: 라인의 시작 번호
		:param line_len:
		:return:
		"""
		self.select_multi_selection_basic(line_no_start, line_len, "word")

	def select_n_more_word_from_selection(self, input_no):
		"""
		현재 위치에서 단어하나를 추가해서 선택하는것

		:param input_no:
		:return:
		"""
		self.selection.MoveDown(Unit=self.enum_word["wdWord"], Count=input_no)
		self.selection.Expand(self.enum_word["wdWord"])

	def select_next_basic(self, input_type, input_count=1, expand_type=1):
		"""
		기본적인 형태로 사용이 가능하도록 만든것

		:param input_type:
		:param input_count:
		:param expand_type:
		:return:
		"""
		checked_input_type = self.check_content_name(input_type)
		type_dic = {"line": 5, "paragraph": 4, "word": 2, "sentence": 3, }
		try:
			self.selection.MoveDown(Unit=type_dic[checked_input_type], Count=input_count)
		except:
			self.selection.MoveRight(Unit=type_dic[checked_input_type], Count=input_count)
		self.selection.Expand(expand_type)

	def select_next_line_from_selection(self):
		"""
		다음 줄로 이동하는 것

		:return:
		"""
		self.selection.MoveRight(Unit=self.enum_word["wdLine"], Count=1)
		self.selection.Expand(self.enum_word["wdLine"])

	def select_next_n_chacter_from_selection(self, input_no):
		"""
		현재 선택한 영역의 뒤로, n번째 글자를 선택하는 것

		:param input_no:
		:return:
		"""
		start_no = self.selection.Range.Start
		self.active_word_file.Range(start_no, start_no + input_no).Select()

	def select_next_n_line_from_cursor(self, line_no):
		"""
		전체 문서에서 줄수로 선택하는것

		:param line_no:
		:return:
		"""
		self.selection.MoveDown(Unit=self.enum_word["wdLine"], Count=line_no)
		self.selection.Expand(self.enum_word["wdLine"])

	def select_next_n_line_from_selection(self, line_no=1):
		"""
		전체 문서에서 줄수로 선택하는것
		self.selection.Start = 1

		:param line_no:
		:return:
		"""
		self.selection.MoveDown(Unit=self.enum_word["wdLine"], Count=line_no)
		self.selection.Expand(self.enum_word["wdLine"])

	def select_next_n_paragraphs_from_selection(self, input_no):
		"""
		현재 위치에서 몇개단어 뒤까지 선택하는것

		형태적인 분류 : active_document(화일) > sentence(문장) > word(한 단어) > character(한글자)
		의미적인 분류 : active_document(화일) > paragraph(문단) > line(줄) > word(한 단어) > character(한글자)
		sentence : 표현이 완결된 단위, 그 자체로 하나의 서술된 문장이 되는 것
		paragraph : 줄바꿈이 이루어지기 전까지의 자료

		:param input_no:
		:return:
		"""
		self.selection.MoveDown(Unit=self.enum_word["wdParagraph"], Count=input_no)
		self.selection.Expand(self.enum_word["wdParagraph"])

	def select_next_n_sentence_from_selection(self, input_no):
		"""
		현재 선택한 영역의 뒤로, n번째 문장을 선택하는 것

		형태적인 분류 : active_document(화일) > sentence(문장) > word(한 단어) > character(한글자)
		의미적인 분류 : active_document(화일) > paragraph(문단) > line(줄) > word(한 단어) > character(한글자)
		sentence : 표현이 완결된 단위, 그 자체로 하나의 서술된 문장이 되는 것
		paragraph : 줄바꿈이 이루어지기 전까지의 자료

		:param input_no:
		:return:
		"""
		self.selection.MoveDown(Unit=self.enum_word["wdSentence"], Count=input_no)
		self.selection.Expand(self.enum_word["wdSentence"])

	def select_next_n_words_from_selection(self, input_no):
		"""
		현재 선택한 영역의 뒤로, n번째 단어를 선택하는 것

		:param input_no:
		:return:
		"""
		self.selection.MoveRight(Unit=self.enum_word["wdWord"], Count=input_no)
		self.selection.Expand(self.enum_word["wdWord"])

	def select_next_paragraph_from_selection(self):
		"""
		현재 선택한 영역의 뒤로, 바로뒤의 paragraph를 선택하는 것
		형태적인 분류 : active_document(화일) > sentence(문장) > word(한 단어) > character(한글자)
		의미적인 분류 : active_document(화일) > paragraph(문단) > line(줄) > word(한 단어) > character(한글자)
		sentence : 표현이 완결된 단위, 그 자체로 하나의 서술된 문장이 되는 것
		paragraph : 줄바꿈이 이루어지기 전까지의 자료


		:return:
		"""
		self.selection.MoveDown(Unit=self.enum_word["wdParagraph"], Count=1)
		self.selection.Expand(self.enum_word["wdParagraph"])

	def select_next_sentence_from_selection(self):
		"""
		현재 선택한 영역의 뒤로, 바로뒤의 sentence를 선택하는 것

		:return:
		"""
		self.selection.MoveRight(Unit=self.enum_word["wdSentence"], Count=1)
		self.selection.Expand(self.enum_word["wdSentence"])

	def select_next_word_from_selection(self):
		"""
		현재 선택한 영역의 뒤로, 바로뒤의 단어를 선택하는 것

		:return:
		"""
		self.selection.MoveDown(Unit=self.enum_word["wdWord"], Count=1)
		self.selection.Expand(self.enum_word["wdWord"])

	def select_nth_line_from_begin(self, line_no):
		"""
		문서의 처음부터 원하는 n번째 라인을 선택

		:param line_no:
		:return:
		"""
		self.move_cursor_by_index(0)
		self.selection.MoveDown(Unit=self.enum_word["wdLine"], Count=line_no)
		self.selection.Expand(self.enum_word["wdLine"])

	def select_nth_line_from_cursor(self, line_no):
		"""
		문서의 처음부터 원하는 n번째 라인을 선택

		:param line_no:
		:return:
		"""
		self.selection.MoveDown(Unit=self.enum_word["wdLine"], Count=line_no)
		self.selection.Expand(self.enum_word["wdLine"])

	def select_nth_paragraph_from_begin(self, input_no):
		"""
		문서의 처음부터 원하는 n번째 라인을 선택

		:param input_no:
		:return:
		"""
		self.move_cursor_by_index(0)
		self.selection.MoveDown(Unit=self.enum_word["wdParagraph"], Count=input_no)
		self.selection.Expand(self.enum_word["wdParagraph"])

	def select_nth_paragraph_from_cursor(self, input_no=1):
		"""
		현재 커서의 위치를 기준으로 n번째 문단을 선택

		:param input_no:
		:return:
		"""
		my_range = self.active_word_file.Paragraphs(input_no).Range
		my_range.Select()
		result = self.word_program.Selection.range.Text
		return result

	def select_next_one_word_from_selection(self):
		"""
		현재 선택한 영역의 바로뒤의 단어를 선택하는것

		:return:
		"""
		self.selection.Expand(self.enum_word["wdWord"])

	def select_some_char_in_paragraphs(self, para_no, y, length):
		"""
		문단 번호로 문단 전체의 영역을 선택하는 것
		paragraph 를 선택한다, 없으면 맨처음부터

		:param para_no:
		:param y:
		:param length:
		:return:
		"""
		paragraph = self.active_word_file.Paragraphs(para_no)
		# 맨앞에서 몇번째부터，얼마의 길이를 선택할지를 선정
		x = paragraph.Range.Start + y - 1
		y = paragraph.Range.Start + y + length - 1
		self.var_word["new_range"] = self.active_word_file.Range(x, y).Select()

	def select_previous_basic(self, input_type, input_count=1, expand_type=1):
		"""
		입력형태에 따라서 영역을 선택하는것
		기본적인 형태로 사용이 가능하도록 만든것

		:param input_type:
		:param input_count:
		:param expand_type:
		:return:
		"""
		checked_input_type = self.check_content_name(input_type)
		type_dic = {"line": 5, "paragraph": 4, "word": 2, "sentence": 3, }
		try:
			self.selection.MoveUp(Unit=type_dic[checked_input_type], Count=input_count)
		except:
			self.selection.MoveLeft(Unit=type_dic[checked_input_type], Count=input_count)
		self.selection.Expand(expand_type)

	def select_previous_line_from_selection(self):
		"""
		현재 선택된 영역을 기준으로 전 줄로 이동하는 것

		:return:
		"""
		self.selection.MoveLeft(Unit=self.enum_word["wdLine"], Count=1)
		self.selection.Expand(self.enum_word["wdLine"])

	def select_previous_n_line_from_selection(self, input_line=1):
		"""
		현재 선택된 영역을 기준으로 앞으로 n번째 줄을 선택

		:param input_line:
		:return:
		"""
		self.selection.MoveLeft(Unit=self.enum_word["wdLine"], Count=input_line)
		self.selection.Expand(self.enum_word["wdLine"])

	def select_previous_n_paragraph_from_selection(self, input_no):
		"""
		현재 선택된 영역을 기준으로 n번째 문장을 선택하는 것

		:param input_no:
		:return:
		"""
		self.selection.MoveUp(Unit=self.enum_word["wdParagraph"], Count=input_no)
		self.selection.Expand(self.enum_word["wdParagraph"])

	def select_previous_n_sentence_from_selection(self, input_no):
		"""
		현재 선택된 영역을 기준으로 전 센텐스로 이동하는 것

		:param input_no:
		:return:
		"""
		self.selection.MoveLeft(Unit=self.enum_word["wdSentence"], Count=input_no)
		self.selection.Expand(self.enum_word["wdSentence"])

	def select_previous_n_word_from_selection(self, input_no):
		"""
		현재 선택된 영역을 기준으로 전체 문서에서 줄수로 선택하는것

		:param input_no:
		:return:
		"""
		self.selection.MoveUp(Unit=self.enum_word["wdWord"], Count=input_no)
		self.selection.Expand(self.enum_word["wdWord"])

	def select_previous_paragraph_from_selection(self):
		"""
		현재 선택된 영역을 기준으로 전체 문서에서 줄수로 선택하는것

		:return:
		"""
		self.selection.MoveUp(Unit=self.enum_word["wdParagraph"], Count=1)
		self.selection.Expand(self.enum_word["wdParagraph"])

	def select_previous_sentence_from_selection(self):
		"""
		현재 선택된 영역을 기준으로 전 센텐스로 이동하는 것

		:return:
		"""
		self.selection.MoveLeft(Unit=self.enum_word["wdSentence"], Count=1)
		self.selection.Expand(self.enum_word["wdSentence"])

	def select_previous_word_from_selection(self):
		"""
		현재 선택된 영역을 기준으로 전체 문서에서 줄수로 선택하는것

		:return:
		"""
		self.selection.MoveUp(Unit=self.enum_word["wdWord"], Count=1)
		self.selection.Expand(self.enum_word["wdWord"])

	def select_some_character_in_line(self, line_no, start_no, count_no):
		"""
		전체 문서에서 몇번째 라인의 앞에서 a~b까지의 글자를 선택하는 것

		:param line_no: 줄번호
		:param start_no: 글자의 시작번호
		:param count_no: 글자의 갯수
		:return:
		"""
		self.selection.GoTo(What=3, Which=line_no, Count=count_no)
		self.selection.Move(Unit=count_no)
		result = self.word_program.Selection.range.Text
		return result

	def select_table_by_index(self, table_index):
		"""
		테이블 번호로 테이블을 선택

		:param table_index:
		:return:
		"""
		self.word_program.Tables(table_index).Select()

	def select_one_word_by_no(self, input_no=1):
		"""
		전체 문서에서 몇번째 단어를 선택하는것

		:param input_no:
		:return:
		"""
		self.active_word_file.Words(input_no).Select()
		result = self.word_program.Selection.range.Text
		return result

	def select_char_nos_from_cursor(self, x, length):
		"""
		현재커서의 위치에서 몇번째 문자로 에서부터 선택시작

		:param x: 시작점
		:param length: 시작점에서부터 몇개를 선택할것 인지
		:return:
		"""
		self.word_program.Selection.Start = x
		self.word_program.Selection.End = x + length - 1

	def select_xy_cell_in_table(self, table_index, table_xy, x, lengh):
		"""
		테이블안의 셀안의 값을 선택하는 방법

		:param table_index:
		:param table_xy:
		:param x:
		:param lengh:
		:return:
		"""
		table = self.active_word_file.Tables(table_index)
		range = table.Cell(table_xy[0], table_xy[1]).Range.Characters(x)
		range.End = table.Cell(table_xy[0], table_xy[1]).Range.Characters(x + lengh - 1).End
		range.Select()

	def set_active_document(self):
		"""
		현재 활성화된 문서를 기본 문서로 설정

		:return:
		"""
		self.active_word_file = self.word_program.ActiveDocument

	def set_backgroundcolor_in_selection(self):
		"""
		배경색넣기
		#	16764057	wdColorPaleBlue	Pale blue color
		#	16711935	wdColorPink	Pink color
		#	6697881	wdColorPlum	Plum color
		#	255	wdColorRed	Red color
		#	13408767	wdColorRose	Rose color
		#	6723891	wdColorSeaGreen	Sea green color
		#	16763904	wdColorSkyBlue	Sky blue color
		#	10079487	wdColorTan	Tan color
		#	8421376	wdColorTeal	Teal color
		#	16776960	wdColorTurquoise	Turquoise color
		#	8388736	wdColorViolet	Violet color
		#	16777215	wdColorWhite	White color
		#	65535	wdColorYellow	Yellow color

		:return:
		"""

		self.selection.Font.Shading.ForegroundPatternColor = 255
		self.selection.Font.Shading.BackgroundPatternColor = 255

	def set_bookmark_at_range(self, input_range, bookmark_name):
		"""
		북마크를 영역으로 설정

		:param input_range:
		:param bookmark_name:
		:return:
		"""
		input_range.Bookmarks.Add(Name=bookmark_name)

	def set_bookmark_by_xy(self, xy, bookmark_name):
		"""
		북마크를 이름으로 설정

		:param xy:
		:param bookmark_name:
		:return:
		"""
		my_range = self.set_range_obj_by_xy(xy)
		my_range.Bookmarks.Add(Name=bookmark_name)

	def set_bottom_margin(self, input_value=20):
		"""
		페이지의 아래 마진을 설정

		:param input_value:
		:return:
		"""
		self.active_word_file.PageSetup.BottomMargin = input_value

	def set_bottom_margin_for_page(self, input_value=20):
		"""
		페이지셋업 : 아래쪽 띄우기

		:param input_value:
		:return:
		"""
		self.active_word_file.PageSetup.BottomMargin = input_value

	def set_font_bold_in_selection(self):
		"""
		두껍게

		:return:
		"""
		self.selection.Font.Bold = True

	def set_font_color_in_selection(self, input_color="red"):
		"""
		선택한것의 폰트 크기

		:param input_color:
		:return:
		"""
		dic_color = {"bla": 1, "blu": 2, "gre": 11, "red": 6, "yel": 7, "gra": 15, "pin": 5, "whi": 8}
		self.selection.Font.ColorIndex = dic_color[str(input_color).lower()]

	def set_font_color_in_selection_by_scolor(self, input_color="red"):
		"""
		선택한것의 폰트 크기

		:param input_color:
		:return:
		"""
		temp_value = self.color.change_scolor_to_rgb(input_color)
		rgb_int = self.color.change_rgb_to_rgbint(temp_value)
		self.selection.Font.TextColor.RGB = rgb_int

	def set_font_name_for_selection(self, input_no="Georgia"):
		"""
		선택영역에 폰트를 설정

		:param input_no:
		:return:
		"""
		self.selection.Font.Name = input_no

	def set_font_name_for_table(self, input_no="Georgia"):
		"""
		테이블의 폰트이름을 설정

		:param input_no:
		:return:
		"""
		self.word_program.table(input_no).Font.Name = input_no

	def set_font_name_for_xy_cell_in_table(self, table_index, cell_index, input_no="Georgia"):
		"""
		테이블의 xy의 폰트를 설정

		:param table_index:
		:param cell_index:
		:param input_no:
		:return:
		"""
		table = self.word_program.Tables(table_index)
		table(cell_index).Font.Name = input_no

	def set_font_size_down_for_selection(self):
		"""
		선택한것의 폰트를 한단계 내리기

		:return:
		"""
		self.selection.Font.Shrink()

	def set_font_size_for_selection(self, input_no=10):
		"""
		선택한것의 폰트 크기

		:param input_no:
		:return:
		"""
		self.selection.Font.Size = input_no

	def set_font_size_for_table(self, table_index, font_size=10):
		"""
		표에 대한 글자크기를 설정

		:param table_index:
		:param font_size:
		:return:
		"""
		table = self.active_word_file.Tables(table_index)
		table.Font.Size = font_size

	def set_font_size_up_for_selection(self):
		"""
		선택한것의 폰트를 한단계 올린다

		:return:
		"""
		self.selection.Font.Grow()

	def set_left_margin(self, input_value=20):
		"""
		왼쪽 띄우기

		:param input_value:
		:return:
		"""
		self.active_word_file.PageSetup.LeftMargin = input_value

	def set_left_margin_for_page(self, input_value=20):
		"""
		페이지셋업 : 왼쪽 띄우기

		:param input_value:
		:return:
		"""
		self.active_word_file.PageSetup.LeftMargin = input_value

	def set_line_width_for_table(self, table_obj, inside_width="", outside_width=""):
		"""
		테이블의 선두께

		:param table_obj:  테이블 객제
		:param inside_width:
		:param outside_width:
		:return:
		"""
		table_obj.Borders.InsideLineWidth = self.var_word["line_width"][inside_width]
		table_obj.Borders.OutsideLineWidth = self.var_word["line_width"][outside_width]

	def set_orientation_for_page(self, input_value=20):
		"""
		페이지의 회전을 설정

		:param input_value:
		:return:
		"""
		self.active_word_file.PageSetup.Orientation = input_value

	def set_orientation_for_page_setup(self, input_value=20):
		"""
		페이지의 회전을 설정

		:param input_value:
		:return:
		"""
		self.active_word_file.PageSetup.Orientation = input_value

	def set_range_obj_from_letter_no1_to_letter_no2(self, start_no, end_no):
		"""
		영역 선택

		:param start_no:
		:param end_no:
		:return:
		"""
		my_range = self.active_word_file.Range(start_no, end_no)
		return my_range


	def set_range_obj_by_xy(self, xy_list):
		"""
		글자의 위치로 range객체를 만드는것
		북마크등을 하기위한것

		:param xy_list: [시작위치, 끝위치]
		:return:
		"""
		my_range = self.active_word_file.Range(Start=xy_list[0], End=xy_list[1])
		return my_range


	def set_right_margin_for_page(self, input_value=20):
		"""
		페이지셋업 : 오른쪽 띄우기

		:param input_value:
		:return:
		"""
		self.active_word_file.PageSetup.RightMargin = input_value

	def set_style_for_selection(self, input_no="제목 1"):
		"""
		스타일 지정하는 코드

		:param input_no:
		:return:
		"""
		self.selection.Style = self.active_word_file.Styles(input_no)

	def set_top_margin_for_page(self, input_value=20):
		"""
		페이지셋업 : 위쪽 띄우기

		:param input_value:
		:return:
		"""
		self.active_word_file.PageSetup.TopMargin = input_value

	def split_all_file_by_style_name_as_list2d(self):
		"""
		전체 문서를 스타일이 다른것을 기준으로 분리하는 것

		:return:
		"""
		result = []
		story_all = []

		start = ""
		style_name = ""
		title = ""
		for para in self.active_word_file.Paragraphs:
			story_or_title = para.Range.Text
			style = para.Style.NameLocal

			if style == "표준":
				story_all.append(story_or_title)
			else:
				if start == "":
					if story_all == []:
						story_all = [[]]
					result.append(["무제", "제목", story_all])
					story_all = []
					start = "no"
					style_name = style
					title = story_or_title
				else:
					result.append([title, style_name, story_all])
					style_name = style
					title = story_or_title
					start = "no"
					story_all = []

		return result

	def terms(self):
		result =	"""
		*** 용어설명
		active_document(화일) > paragraph(문단) > sentence(문장) > word(한 단어) > character(한글자)
		active_document : 현재 선택된 워드문서, word라는 단어가 두가지 이름으로 사용되기때문에, file로 통일시킴
		paragraph : 줄바꿈이 이루어지기 전까지의 자료
		line : 한줄
		word : 공백으로 구분된 단어 (다른의미 : 프로그램이름과 혼동을 피하기위해 file이라는 이름으로 사용)
		character : 글자 1개
		content : 라인, 문단, 단어들을 총괄적으로 뜻하는것, 항목이라고 설명하는것이 좋을듯...

		bookmark : 책갈피
		range : 임의적으로 설정할수가 있으며,word밑에 range가 설정이 되고
				select를 하면 selection밑에 자동으로 range객체가 설정된다

		형태적인 분류 : active_document(화일) > sentence(문장) > word(한 단어) > character(한글자)
		의미적인 분류 : active_document(화일) > paragraph(문단) > line(줄) > word(한 단어) > character(한글자)
		sentence : 표현이 완결된 단위, 그 자체로 하나의 서술된 문장이 되는 것
		paragraph : 줄바꿈이 이루어지기 전까지의 자료

		x_char : 첫문자에서부터 번호째
		x_word : 처음에서부터의 단어순번째
		x_para : 처음에서부터의 문단의 순번째
		x_line : 처음에서부터의 줄의 순번째
		x_sel : 선택된 첫

		xy_s : selection의 처음과 끝위치
		x_len : x는 시작위치, l은 길이
		x_sel : selection의 시작점
		y_sel : selection의 끝점

		nth : 맨처음부터 몇번째의 의미

		MS워드를 사용하기 쉽게하기위해 만든 모듈입니다,
		차후에는 다른 Libero및 한글의 연동또한 만들 예정입니다

		기본적으로 적용되는 selection은 제외한다

		"""
		return result

	def unmerge_for_table(self, table_obj, start_x, start_y):
		"""
		워드는 unmerge가 없으며, 셀분할로 만들어야 한다

		:param table_obj:  테이블 객제
		:param start_x:
		:param start_y:
		:return:
		"""
		count_y = table_obj.Columns.Count
		count_x = table_obj.Rows.Count

	# Selection.Cells.Split(NumRows := 1, NumColumns := 2, MergeBeforeSplit := True)

	def write_end_doc(self, input_text="커서 뒤에 삽입되었어요"):
		"""
		화일의 제일 뒤에 글자 추가

		:param input_text:
		:return:
		"""
		import time
		paragraph_num = self.active_word_file.Paragraphs.Count

		# 워드화일의 제일 끝으로 이동한다
		len_text = len(input_text)
		current_pos = self.active_word_file.Characters.Count  # 커서의 현재위치 확인
		print("최초번호", current_pos)
		title_start_no = current_pos
		title_end_no = current_pos + len(input_text)

		self.selection.Start = current_pos
		self.selection.InsertAfter("\r\n")
		self.selection.InsertAfter(input_text)
		time.sleep(2)

		current_pos = self.active_word_file.Characters.Count  # 커서의 현재위치 확인
		print("한줄바꾸기 번호", current_pos)
		self.selection.Start = current_pos
		self.selection.InsertAfter("\r\n")
		# self.selection.InsertBreak()
		self.selection.Style = self.active_word_file.Styles("표준")  # 스타일 지정하는 코드
		time.sleep(2)

		current_pos = self.active_word_file.Characters.Count  # 커서의 현재위치 확인
		print("마지막글 번호", current_pos)
		self.selection.Start = current_pos
		self.selection.InsertAfter(input_text)
		self.selection.InsertAfter("\r\n")
		self.selection.End = current_pos + len(input_text)
		self.selection.Style = self.active_word_file.Styles("표준")  # 스타일 지정하는 코드
		time.sleep(2)

		self.selection.Start = title_start_no
		self.selection.End = title_end_no
		self.selection.Style = self.active_word_file.Styles("제목")  # 스타일 지정하는 코드

	def write_list2d_with_style(self, input_list2d):
		"""
		[['050630\r', '제목', '\\n\x0c']] ==> [제목, 제목의 스타일이름, 내용]
		위와같은 형태의 자료를 새로운 워드를 오픈해서 작성하는것

		:param input_list2d:
		:return:
		"""
		total_len = len(input_list2d)
		for index, list1d in enumerate(input_list2d):
			print("완료된 %는 ==> ", index / total_len * 100)
			title = str(list1d[0]).strip()
			style_name = str(list1d[1])
			text_data_old = list1d[2]
			text_data = ""

			for index, one in enumerate(text_data_old):
				text_data = text_data + one

			# 스타일이 있는 제목 부분을 나타내는 코드
			cursor = self.active_word_file.Characters.Count  # 워드의 가장 뒷쪽으로 커서위치를 설정
			self.selection.Start = cursor
			self.selection.End = cursor + len(title)
			self.selection.InsertAfter(title)
			self.selection.Style = self.active_word_file.Styles(style_name)  # 스타일 지정하는 코드

			# 스타일이 없는 부분을 표준으로 설정해서 나타내는 코드
			self.selection.InsertAfter("\r\n")
			cursor = self.active_word_file.Characters.Count  # 커서의 현재위치 확인
			self.selection.Start = cursor
			self.selection.InsertAfter(text_data)
			self.selection.End = cursor + len(text_data)
			self.selection.Style = self.active_word_file.Styles("표준")  # 스타일 지정하는 코드
			self.selection.InsertAfter("\r\n")

	def write_styled_text_at_end_of_document(self, input_text, style_name):
		"""
		맨뒤에 글쓰기

		:param input_text:
		:param style_name:
		:return:
		"""
		self.move_cursor_to_end_of_document()
		self.active_word_file.Content.InsertAfter(input_text + "\r\n")
		self.selection.Start = currentPosition = self.selection.Range.Start
		self.selection.End = self.selection.Start + len(input_text)
		self.selection.Style = self.active_word_file.Styles(style_name)  # 스타일 지정하는 코드

	def write_text_as_list1d_for_each_paragraph(self):
		"""
		모든 paragraph를 리스트로 만들어서 돌려주는 것

		:return:
		"""
		result = []
		para_nums = self.active_word_file.Paragraphs.Count
		for no in range(1, para_nums + 1):
			result.append(self.active_word_file.Paragraphs(no).Range.Text)
		return result

	def write_text_at_cursor_to_right_with_space(self, input_text):
		"""
		현재의 위치에 앞에 공백을 넣고 글자를 추가하는것

		:param input_text:
		:return:
		"""
		self.selection.InsertAfter(" " + str(input_text))

	def write_text_at_end_for_selection(self, input_text):
		"""
		선택한것의 뒤에 글씨넣기

		:param input_text:
		:return:
		"""
		self.selection.InsertAfter(input_text)

	def write_text_at_end_of_cursor(self, input_value):
		"""
		선택한것의 뒤에 글씨넣기

		:param input_value:
		:return:
		"""
		self.selection.InsertAfter(input_value)

	def write_text_at_end_of_word_document(self, input_text):
		"""
		문서의 제일 뒷부분에 글을 넣는것

		:param input_text:
		:return:
		"""
		self.active_word_file.Content.InsertAfter(input_text)

	def write_text_at_left_for_selection(self, input_text):
		"""
		선택한것의 앞에 글씨넣기

		:param input_text:
		:return:
		"""
		self.word_program.Selection.InsertBefore(input_text)

	def write_text_at_line_no(self, input_no, input_text=""):
		"""
		현재 커서의 위치중 첫번째 라인에 새로운 라인을 넣는 다

		:param input_no:
		:param input_text:
		:return:
		"""
		self.move_cursor_by_index(0)
		self.selection.MoveDown(Unit=5, Count=input_no)
		self.write_text_at_start_of_cursor(input_text)

	def write_text_at_nth_cell_in_table(self, table_index, input_no=1, input_text=""):
		"""
		테이블의 n번째 셀에 값넣기

		:param table_index:
		:param input_no:
		:param input_text:
		:return:
		"""
		table = self.active_word_file.Tables(table_index)
		table(input_no).Range.Text = input_text

	def write_text_at_start_of_cursor(self, input_value):
		"""
		*** 보관용
		선택한것의 뒤에 글씨넣기

		:param input_value:
		:return:
		"""
		self.selection.InsertBefore(input_value)

	def write_text_at_start_of_selection(self, input_text):
		"""
		선택영역의 뒷부분에 글쓰기

		:param input_text:
		:return:
		"""
		self.selection.InsertBefore(input_text)

	def write_text_at_xy_cell_in_table(self, input_table_no, xy, input_text):
		"""
		테이블의 셀 위치에 값넣기

		:param input_table_no:
		:param xy:
		:param input_text:
		:return:
		"""
		self.active_word_file.Tables(input_table_no).Cell(int(xy[0]), int(xy[1])).Range.Text = str(input_text)

	def write_text_in_table_by_xy(self, table_index="", xy="", input_text=""):
		"""
		테이블의 셀에 글씨 입력하기

		:param table_index:
		:param xy:
		:param input_text:
		:return:
		"""
		table = self.active_word_file.Tables(table_index)
		table.Cell(xy[0], xy[1]).Range.Text = input_text

	def write_text_with_new_line_at_end_of_document(self, input_text):
		"""
		맨뒤에 글쓰기

		:param input_text:
		:return:
		"""
		self.active_word_file.Content.InsertAfter(input_text + "\r\n")

	def write_value_at_end_of_para_no(self, para_no=1, input_text="hfs1234234234;lmk"):
		"""
		문단의 번호로 선택된 문단의 제일 뒷부분에 글을 넣는것

		:param para_no:
		:param input_text:
		:return:
		"""
		self.active_word_file.Paragraphs(para_no).Content.InsertAfter(input_text)

	def zzz_fstring(self):
		"""
		매번 혼돈되는 f-format에 대해서 간단히 적어 본다

		:return:
		"""
		result = """
		{변수이름:공백이 있을때 0으로 체우기<(왼쪽정렬)10.2f(총 10자리중 소숫점이하 2자리}
		{var_int:0<10.2f}
		{:>10}	전체 10칸, 공백을 앞에
		{:#>10}	전체 10칸, 공백대신에 #을 앞에
		{:<10}	전체 10칸, 공백을 뒤에
		{:^10}	전체 10칸, 공백을 앞뒤에
		{:.10f}	소수점 10까지 표시
		{:,}	천단위 쉼표 표시
		{1:>10}	두번째[1] 오는 변수의 전체 10칸, 공백을 앞에

		"""
		print(result)
		return result
