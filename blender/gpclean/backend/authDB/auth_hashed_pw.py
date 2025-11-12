# hashlib: 비밀번호를 해시화하기 위한 표준 라이브러리
import hashlib

# pymongo: MongoDB에 연결하고 작업하기 위한 라이브러리
from pymongo import MongoClient

# 비밀번호를 SHA-256 알고리즘으로 해시하는 함수
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# MongoDB 연결 설정
client = MongoClient("mongodb://localhost:27017")  # 필요시 URI 변경
db = client["student_db"]        # 데이터베이스 이름
collection = db["auth_collection"]          # 컬렉션 이름

# MongoDB에 새로운 학생의 학번과 해시된 비밀번호를 저장하는 함수
def add_students_to_mongo():
    auth_dict = make_dictionary()

    for student_id, plain_password in auth_dict.items():
        if check_registered_user(student_id):
            print(f" 이미 존재하는 학번입니다: {student_id}")
            continue  # 다음 사용자로 넘어감

        hashed_pw = hash_password(plain_password)

        # MongoDB에 삽입
        collection.insert_one({
            "student_id": student_id,
            "password_hash": hashed_pw
        })

        print(f"ReplaceA {student_id} 등록 완료!")

# 등록할 학번과 비밀번호 딕셔너리 생성
def make_dictionary():
    auth_dict = {
        "C123000": "1234",
        "C123400": "0000",
        "C123450": "hi23423"
    }
    return auth_dict

# MongoDB에서 해당 학번이 이미 있는지 확인
def check_registered_user(student_id):
    return collection.find_one({"student_id": student_id}) is not None

# 실행
add_students_to_mongo()

################################################################################
# mongosh 명령어 요약
"""
1. mongosh
    Connecting to: mongodb://127.0.0.1:27017/

2. show dbs #데이터베이스 목록보기

3. use student_db 데이터베이스 선택하기

4. show collections 컬렉션이름 확인하기

5. db.getCollection("auth").find()
   db["auth"].find().pretty() 
   #컬렉션 접근하기 컬렉션이름 바꿈
6.  컬렉션 이름 바꾸기
    use admin
    db.adminCommand({
    renameCollection: "student_db.auth",
    to: "student_db.auth_collection"
    })
7. 확인
    use student_db
    show collections
    db.auth_collection.find().pretty()



"""
###########################################################################
# 출력
"""
admin> use student_db
switched to db student_db
student_db> show collections
auth_collection
student_db> db.auth_collection.find().pretty()
[
  {
    _id: ObjectId('68514fcbb81ba211e54157d8'),
    student_id: 'C123000',
    password_hash: '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4'
  },
  {
    _id: ObjectId('68514fcbb81ba211e54157d9'),
    student_id: 'C123400',
    password_hash: '9af15b336e6a9619928537df30b2e6a2376569fcf9d7e773eccede65606529a0'
  },
  {
    _id: ObjectId('68514fcbb81ba211e54157da'),
    student_id: 'C123450',
    password_hash: 'e74bfd169dd34c1bf669cc113bd02ba0fce42d774826177b53b6f1e53f2fd47e'
  }

"""