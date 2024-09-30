from aqt import mw, gui_hooks
from aqt.utils import showInfo
from .eng_to_ipa import convert

# 발음 기호를 추가하는 함수
def add_pronunciation(note):
    field_name = "Front"  # 발음을 추출할 필드 이름
    pronunciation_field_name = "Pronunciation"  # 발음 기호를 저장할 필드

    if field_name in note and pronunciation_field_name in note:
        text = note[field_name]
        if text.strip():  # 필드가 비어 있지 않은 경우에만 처리
            pronunciation = convert(text)
            note[pronunciation_field_name] = pronunciation
            note.flush()  # 변경사항 저장

# 노트가 추가된 후 호출되는 함수
def on_add_cards_did_add_note(note, card_id):
    add_pronunciation(note)
    # 노트가 이미 추가된 후이므로, 변경 사항을 업데이트해야 합니다.
    mw.col.update_note(note)

# 기존 노트가 편집기에서 열릴 때 호출되는 함수
def on_editor_did_load_note(editor):
    note = editor.note
    add_pronunciation(note)
    mw.col.update_note(note)  # 변경 사항 업데이트

# 후크 연결: 노트 추가 시 자동으로 발음 기호 추가
gui_hooks.add_cards_did_add_note.append(on_add_cards_did_add_note)

# 후크 연결: 기존 노트를 편집기에서 열 때 자동으로 발음 기호 추가
gui_hooks.editor_did_load_note.append(on_editor_did_load_note)