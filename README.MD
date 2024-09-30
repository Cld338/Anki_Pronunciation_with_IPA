# Anki Pronunciation with IPA

Anki Pronunciation with IPA는 Anki에서 노트를 추가하거나 편집할 때 자동으로 IPA 발음 기호를 추가하는 애드온입니다. "Front" 필드에 입력된 텍스트를 발음 기호로 변환하여 "Pronunciation" 필드에 저장합니다. 기존 노트와 새 노트 모두 호환됩니다.

## 주요 기능

- 새 노트가 생성될 때 자동으로 IPA 발음 기호를 추가합니다.
- 기존 노트를 편집기에서 열면 발음 기호를 자동으로 업데이트합니다.
- "Front" 필드의 텍스트를 기반으로 발음 기호를 생성하고, "Pronunciation" 필드에 저장합니다.
- 발음 기호 생성이 자동으로 백그라운드에서 처리됩니다.

## 설치 방법

### 1. 수동 설치

1. 이 저장소를 다운로드하고 압축을 풉니다.
2. `anki_pronunciation_with_ipa` 폴더를 Anki 애드온 디렉토리에 복사합니다:

   - Windows: `C:\Users\<사용자 이름>\AppData\Roaming\Anki2\addons21\`
   - macOS: `~/Library/Application Support/Anki2/addons21/`
   - Linux: `~/.local/share/Anki2/addons21/`

3. Anki를 재시작하여 애드온을 활성화합니다.

### 2. Anki 애드온 매니저를 통한 설치 (가능한 경우)

1. Anki를 엽니다.
2. 상단 메뉴에서 `도구` -> `애드온`을 선택합니다.
3. `애드온 가져오기` 버튼을 클릭하고 애드온 코드를 입력합니다 (AnkiWeb에 게시된 경우).
4. Anki를 재시작합니다.

## Usage

애드온이 설치되면, 노트를 추가하거나 편집할 때 자동으로 IPA 발음 기호가 추가됩니다.

### For New Notes

1. 새로운 노트를 추가할 때 "Front" 필드에 텍스트를 입력합니다.
2. 애드온이 "Front" 필드의 내용을 기반으로 자동으로 발음 기호를 생성하여 "Pronunciation" 필드에 저장합니다.

### For Existing Notes

1. 기존 노트를 편집기에서 엽니다.
2. "Pronunciation" 필드가 있으면, 애드온이 자동으로 발음 기호를 추가합니다.

## Fields Configuration

- **"Front"**: 텍스트가 입력되는 필드입니다. 이 필드의 내용을 기반으로 발음 기호가 생성됩니다.
- **"Pronunciation"**: 발음 기호가 저장되는 필드입니다. 노트 타입에 이 필드가 있어야 하며, 없는 경우 수동으로 추가해야 할 수 있습니다.

## Example

- **"Front" 필드 입력**: "Hello"
- **"Pronunciation" 필드 출력**: /həˈloʊ/

## Notes

- 이 애드온을 사용하려면 노트 타입에 "Front"와 "Pronunciation" 필드가 있어야 합니다. 필드가 없으면 노트 타입을 수정해야 합니다.
- 발음 기호는 자동으로 추가되며, 수동으로 트리거할 필요가 없습니다.

## Contributing

이 애드온에 기여하고 싶다면 다음 절차를 따르세요:

1. 이 저장소를 포크합니다.
2. 새로운 브랜치를 만들어 기능이나 버그 수정을 진행합니다.
3. 변경 사항을 커밋한 후 명확한 설명을 작성합니다.
4. 풀 리퀘스트를 제출합니다.

코드 스타일을 준수하고 관련 테스트를 통과했는지 확인해주세요.

## LICENSE

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 [LICENSE](./LICENSE) 파일을 참조하세요.

## CREDIT

- [eng_to_ipa](https://github.com/mphilli/English-to-IPA) - 영어 텍스트를 IPA 발음 기호로 변환하는 라이브러리.
