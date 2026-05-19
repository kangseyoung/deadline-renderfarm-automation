# 프로젝트 타임로그

이 문서는 졸업 프로젝트와 기술 논문을 준비하는 과정에서 진행한 개발 흐름을 공개용으로 정리한 타임라인입니다. 내부 경로, IP 주소, 자격 증명, 계정명, 라이선스 세부 정보, 원본 스크린샷은 공개 저장소에 맞지 않기 때문에 제외했습니다.

## 2025년 3월 - 초기 기획

### 2025-03-12 - 인프라 요구사항 조사

- 실습실 기반 렌더팜에 필요한 주요 요구사항을 정리했습니다.
- 네트워크 대역폭, 공유 스토리지, Worker PC 수, 메인 서버 사양을 검토했습니다.
- Worker 그룹 구성, 유휴 PC 활용, 렌더 큐 동작 방식을 고려했습니다.

### 2025-03-13 - 워크플로우 및 백엔드 구조 설계

- 예약부터 Deadline 제출까지 이어지는 전체 워크플로우 초안을 작성했습니다.
- 사용자, 예약, 렌더 상태를 저장하기 위한 MongoDB 컬렉션 구조를 계획했습니다.
- 초기 기술 스택으로 Python, PySide, MongoDB, Google Sheets, Google Apps Script, Flask, Deadline 도구를 선정했습니다.

### 2025-03-15 - 이전 파이프라인 도구 참고

- 이전에 만들었던 PySide/FFmpeg 기반 파이프라인 도구를 검토했습니다.
- 파일 선택, 경로 기반 메타데이터 추출, 명령어 생성, subprocess 진행률 처리 방식을 참고했습니다.
- 이후 렌더 제출 UI 설계에 해당 구조를 일부 반영했습니다.

### 2025-03-16 - Google OAuth 및 Calendar API 실험

- Flask 기반 Google 인증 흐름을 실험했습니다.
- route/callback 처리와 Google 서비스 연동 방식을 프로토타입으로 확인했습니다.
- 이후 예약 워크플로우는 Calendar보다 Google Sheets 중심으로 좁혔습니다.

### 2025-03-18 - Google Apps Script 예약 프로토타입

- Google Apps Script 기반 예약 시스템의 초기 프로토타입을 만들었습니다.
- 일자별 시트 생성, 시간 블록, PC 그룹 컬럼, 간단한 상호작용 흐름을 구성했습니다.
- 사용자용 예약 인터페이스의 첫 형태로 활용했습니다.

### 2025-03-19 - 피드백 반영

- 씬 파일을 NAS/공유 스토리지 기준으로 정리해야 한다는 피드백을 반영했습니다.
- Deadline API 조사와 제출 흐름 검증을 후속 과제로 정리했습니다.

## 2025년 4월 - 실습실 환경과 원격 관리

### 2025-03-31 - 실습실 PC 사양 조사

- 공개 가능한 범위에서 실습실 PC 규모와 Worker 활용 가능성을 정리했습니다.
- 현재 장비로 렌더팜을 구성할 수 있는지 대략적인 가능성을 검토했습니다.
- 무거운 렌더 작업을 위해 몇 대 단위로 Worker를 묶을지 고민했습니다.

### 2025-04-01 - 예약 데이터 동기화와 Headless Rendering 조사

- 예약 데이터와 렌더 시스템을 주기적으로 동기화하는 방식을 조사했습니다.
- Maya, Blender 및 관련 DCC 도구의 headless rendering 옵션을 검토했습니다.
- 도구별 batch rendering 동작 차이를 비교했습니다.

### 2025-04-02 - OpenSSH 및 Ansible 방향 검토

- Windows OpenSSH를 이용한 원격 Worker 관리 가능성을 조사했습니다.
- 수동 설정, 스크립트 기반 설정, Ansible 기반 오케스트레이션을 비교했습니다.
- 프로젝트 범위가 단순 UI 도구에서 인프라 운영 흐름으로 확장되었습니다.

### 2025-04-15 - Ansible 제어 계획

- WSL 기반 Ansible 컨트롤러로 Windows 실습실 PC를 관리하는 방안을 계획했습니다.
- 원격 접근, 안정적인 호스트 식별, 반복 가능한 설정 작업의 조건을 검토했습니다.
- 네트워크 안정성이 자동화의 선행 조건이라는 점을 확인했습니다.

### 2025-04-16 - NAS, 라이선스, 출력 경로 계획

- 입력 씬과 렌더 출력에 대한 공유 스토리지 규칙을 계획했습니다.
- Maya/Arnold 렌더링에 필요한 라이선스 서버 관련 요구사항을 조사했습니다.
- 분산 렌더링에서 로컬 경로를 피해야 하는 이유를 정리했습니다.

## 2025년 5월 - 라이선스와 NAS 연동

### 2025-05-14 - Autodesk/Arnold 네트워크 라이선스 조사

- Autodesk Network License Manager와 Arnold 라이선스 동작을 조사했습니다.
- 방화벽, 호스트 이름 해석, 환경 변수 설정이 운영상 중요한 요소라는 점을 확인했습니다.
- 공개 문서에서는 반드시 placeholder로 처리해야 하는 민감 영역으로 분류했습니다.

### 2025-05-21 - UI 및 데이터 흐름 정리

- PySide UI 구조와 데이터 흐름을 다시 정리했습니다.
- UI 표시 로직과 controller/data access 로직을 분리했습니다.
- 예약 데이터가 렌더 제출 동작과 어떻게 연결되어야 하는지 명확히 했습니다.

### 2025-05-28 - NAS 이슈 정리

- 공유 스토리지 설계와 관련된 이슈를 정리하고 NAS 방향을 확정했습니다.
- 씬 입력과 렌더 출력이 일관된 공유 경로를 사용해야 한다는 점을 재확인했습니다.
- 우선 Maya와 Blender 연동에 집중하기로 했습니다.

## 2025년 6월 - 원격 설정, UI, DB, 패키징

### 2025-06-08 - Ansible 및 Docker 테스트

- Worker 설정과 환경 격리를 위해 Ansible과 Docker 아이디어를 테스트했습니다.
- Windows 실습실 관리에는 호스트/네트워크 준비가 먼저 필요하다는 점을 확인했습니다.
- Docker/Ansible은 최종 배포의 핵심보다는 설계 참고와 실험 결과로 남겼습니다.

### 2025-06-11 - 고정 IP 및 원격 접근 이슈

- 고정 주소와 원격 접근 관련 문제를 조사했습니다.
- 안정적인 주소 체계, 호스트 이름 기반 접근, 네트워크 관리 개선 방향을 검토했습니다.
- 네트워크 일관성을 운영 리스크로 분류했습니다.

### 2025-06-20 - MongoDB 및 Google Sheets 연동

- 예약 데이터 형식과 MongoDB 저장 구조를 연결했습니다.
- Google Sheets와 백엔드 데이터 동기화 개념을 테스트했습니다.
- 렌더 상태와 예약 상태를 추적하는 흐름을 정리했습니다.

### 2025-06-21 - 설정 및 보안 계획

- 환경 변수와 샘플 설정 파일을 이용한 config 관리 방식을 계획했습니다.
- 개발 중 민감 파일이 포함되었을 때 GitHub Push Protection이 동작하는 과정을 확인했습니다.
- credentials, tokens, passwords, internal IPs는 커밋하지 않는 원칙을 정리했습니다.

### 2025-06-24 - 프로젝트 패키징과 로그인 흐름

- Python 프로젝트 구조를 더 명확한 패키지 형태로 정리했습니다.
- 로그인 흐름과 관련된 UI 및 백엔드 연결을 구성했습니다.
- 공개 가능한 저장소 구조에 맞춰 GitHub 정리를 시작했습니다.

### 2025-06-25 - DCC 도구 연동 계획

- Maya, Blender, 향후 DCC adapter가 렌더 작업을 제출하는 구조를 계획했습니다.
- UI 설정과 Deadline 제출 로직 사이의 adapter 경계를 정의했습니다.
- 첫 동작 경로는 Maya와 Blender 중심으로 우선순위를 잡았습니다.

### 2025-06-26 - Maya 배포 방향

- Maya 쪽 배포와 startup 동작을 준비했습니다.
- Windows 환경에서 예약 실행 또는 유지보수 자동화 가능성을 검토했습니다.
- Maya 스크립트가 전체 제출 흐름과 어떻게 연결되는지 점검했습니다.

## 2025년 8월 - Deadline Worker와 도구 연동

### 2025-08-06 - Docker 기반 Deadline Worker 설계

- Docker 기반 Deadline Worker 구성을 실험적으로 검토했습니다.
- 컨테이너 기반 구성과 Windows 실습실 환경의 현실적인 제약을 비교했습니다.
- 최종 구현 증거라기보다는 설계 참고 자료로 정리했습니다.

### 2025-08-07 - Blender 연동 완료

- Blender 중심의 제출 경로를 구성했습니다.
- Blender 씬/렌더 설정을 프로젝트 제출 구조와 연결했습니다.
- Blender 실행 경로와 공유 스토리지 접근이 일관되어야 한다는 점을 확인했습니다.

### 2025-08-23 - Deadline Worker 운영 설계

- Deadline Worker의 pools, groups, limits, chunk size, concurrent tasks 동작을 조사했습니다.
- 실습실 스케줄링과 리소스 제어를 위한 Worker 관리 아이디어를 문서화했습니다.
- 모니터링과 트러블슈팅이 핵심 운영 요소임을 확인했습니다.

## 2025년 9월 - Deadline 보안과 제출 도구

### 2025-09-01 - Deadline 인증서 구조 조사

- Deadline certificate와 client connection 개념을 조사했습니다.
- Worker 설정 과정에서 인증서를 배포하거나 참조하는 방식을 검토했습니다.
- 인증서 파일과 private key는 공개 저장소에 포함하지 않는 것으로 정리했습니다.

### 2025-09-02 - Deadline Submitter 코드 구조

- DCC adapter, job settings, Deadline command generation을 기준으로 제출 코드를 정리했습니다.
- UI에서 씬/렌더 설정을 일관되게 수집할 수 있도록 구조를 다듬었습니다.
- UI, adapter, submission 책임을 분리해 유지보수성을 높였습니다.

### 2025-09-10 - Deadline Client 권한 이슈

- Windows Worker 환경에서 Deadline client/worker 폴더 권한 문제를 확인했습니다.
- 일반 실습실 사용자와 공유 계정이 설정 경로에 접근해야 하는 범위를 검토했습니다.
- 공유 PC에서 Worker 실행을 안정화하기 위한 운영 이슈로 정리했습니다.

### 2025-09-17 - Worker / Monitor 상태 확인

- Deadline 관련 화면과 설정 확인 기록을 검토했습니다.
- 내부 스크린샷을 공개하지 않고 검증 목적만 요약했습니다.
- 경로, 장비명, 서버 값이 보이는 스크린샷은 redaction 전까지 비공개로 유지해야 한다고 정리했습니다.

## 2025년 10월 - Worker 설정과 최종 운영

### 2025-10-11 - 네트워크 라이선스 서버 계획

- 네트워크 라이선스 환경의 표준 설정 과정을 정리했습니다.
- 방화벽, 호스트 이름, 환경 변수, 로그 모니터링 관련 사항을 검토했습니다.
- 계정, serial, product key, host, server 세부값은 공개 버전에서 제거했습니다.

### 2025-10-13 - Deadline Worker 설정 매뉴얼

- 여러 대의 Worker를 반복적으로 설정하기 위한 체크리스트를 작성했습니다.
- 공유 repository 접근, Worker 설치, 방화벽 접근, 인증서, 라이선스 관련 환경 변수, 재시작 절차를 정리했습니다.
- 실제 네트워크 경로와 credential처럼 보이는 값은 공개 저장소에서 제외했습니다.

### 2025-10-20 - 시각 자료 기반 환경 확인

- 렌더팜 설정 중 확인한 시각 자료를 정리했습니다.
- 원본 내부 스크린샷 대신 어떤 목적의 확인이었는지만 요약했습니다.
- 향후 스크린샷을 올릴 경우 반드시 민감 정보 블러 처리가 필요하다고 정리했습니다.

### 2025-10-29 - 최종 렌더팜 운영 이슈

- 실제 실습실 운영 중 발견된 문제를 추적했습니다.
- 경로 차이, 장비별 실패, 팀 커뮤니케이션 공백, 하드웨어 지원 필요 사항을 정리했습니다.
- 프로젝트가 프로토타입을 넘어 실제 운영과 트러블슈팅 단계로 이동했다는 점을 확인했습니다.

## 주요 기술 작업

- 실제 실습실 환경을 기준으로 한 render farm workflow 설계.
- Deadline, NAS/shared storage, MongoDB, Google Sheets, PySide, Flask, Ansible, Docker, Maya, Blender 조사.
- 예약 데이터와 렌더 상태 데이터 흐름 설계.
- Maya/Blender workflow를 위한 Deadline submitter 구조 설계.
- Worker grouping, monitoring, permissions, troubleshooting 계획.
- 공개 문서화와 security redaction 정책 정리.

## 배운 점

- 렌더팜 개발은 단순 UI나 job submission만의 문제가 아니라 인프라 작업에 가깝습니다.
- 분산 렌더링을 안정적으로 만들려면 shared path 표준화가 먼저 필요합니다.
- 수동 설정은 규모가 커질수록 유지하기 어렵기 때문에 Worker setup은 반복 가능해야 합니다.
- License handling은 렌더팜 운영의 핵심 의존성입니다.
- 렌더 제출 UI만으로는 부족하고, database logic, scheduling logic, path validation, worker monitoring, error reporting이 함께 필요합니다.
- 실제 운영에서는 프로토타입 단계에서 예측하기 어려운 문제가 드러납니다.

## 공개 저장소 안전 체크리스트

- 실제 IP 주소, UNC/NAS 경로, host name, 학번, 계정명, 이메일 주소는 제거해야 합니다.
- password, token, API key, OAuth secret, product key, serial, certificate, private key는 커밋하면 안 됩니다.
- screenshot에 경로, 장비명, 사용자, 로그, license 관련 정보가 보이면 블러 처리하거나 제외해야 합니다.
- 공개 예시는 `<nas-server-ip>`, `<internal-path>`, `<license-server-ip>`, `<student-id>`, `<secret>` 같은 placeholder를 사용해야 합니다.
- 민감한 프로젝트 자료를 공개하기 전에는 Git history까지 확인해야 합니다.
