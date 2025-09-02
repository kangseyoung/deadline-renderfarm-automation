# gpclean - Maya Pipeline Tool

### ✨ 기능 요약
- 로그인 시스템
- 백엔드 연동
- 구글 시트 + MongoDB 통합
- Maya 자동 초기화 지원

---

### 💻 설치 방법

1. Git 클론

```bash
git clone https://github.com/kangseyoung/gp.git@test 
#현재 테스트 단계 이므로 테스트 브랜치를 다운로드해주세요 
> 📌 설치 전 꼭 확인하세요!

### 수정이 필요한 경로 (2곳):

1. **마야 스크립트 경로 (`maya_scripts_dir`)**
   - 기본값: `C:/Users/세영/OneDrive/문서/maya/2023/scripts/`
   - 마야 버전이나 OneDrive 아닌 사용자라면 `"Documents/maya/scripts/"`로 수정해야 합니다.

2. **깃 클론 위치 (`project_root`)**
   - 기본값: `D:/gitclonetest/gp/`
   - 본인이 깃 클론한 경로로 수정하세요.

---

예: 마야 2024 쓰고 있고, 깃 클론을 E드라이브에 했다면

```python
maya_scripts_dir = Path.home() / "Documents" / "maya" / "2024" / "scripts"
project_root = Path("E:/github/gp")

완벽해 세영! 그거까지 알려줘야 설치하고 바로 사용자 등록할 수 있지 😊
아래처럼 README.md나 설치 가이드에 딱 한 줄로 요약하면 돼.

---

### 🔐 사용자 등록 방법 (학번 + 비밀번호)

사용자 인증은 다음 파일에서 등록할 수 있습니다:

gpclean/backend/authDB/auth_hashed_pw.py

makefile
복사
편집

이 파일 안의 `make_dictionary()` 함수에 있는 `auth_dict`에  
학번(ID)과 비밀번호를 추가하면 됩니다.

예시:
```python
auth_dict = {
    "20231234": "1234",   # 학번: 비밀번호
    "20235678": "5678"
}
🔒 비밀번호는 실행 시 자동으로 SHA-256 해시로 암호화됩니다.
평문 입력만 하면 됩니다!


---

### 📄 구글 시트 연동 설정 방법

1. [Google Cloud Console](https://console.cloud.google.com/)에서 서비스 계정을 생성하고  
   Google Sheets API 및 Drive API 사용 설정 후 JSON 키 파일을 다운받습니다.
# 테스트중 
# 노션링크 
https://www.notion.so/google_credit-json-21e6d5f533c08031a40acf9fb432a616


2. 해당 JSON 키 파일을 아래 경로에 저장하거나, 본인 경로에 맞게 수정하세요:

C:/Users/세영/OneDrive/Desktop/google_creds/google_creds.json

3. `auth_hashed_pw.py` 또는 `sheet_controller.py` 등에서 다음 부분을 수정:

```python
creds = ServiceAccountCredentials.from_json_keyfile_name(
    "C:/Users/세영/OneDrive/Desktop/google_creds/google_creds.json", scope
)