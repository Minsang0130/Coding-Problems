def solution(id_pw, db):
    user, password = id_pw
    
    # 회원 정보 데이터베이스(db)를 순회하며 아이디 비교
    for record in db:
        db_user, db_pw = record
        if db_user == user:
            # 아이디가 일치하면 패스워드도 비교합니다.
            if db_pw == password:
                return "login"
            else:
                return "wrong pw"
    
    # db에 해당 아이디가 없으면 "fail" 반환
    return "fail"