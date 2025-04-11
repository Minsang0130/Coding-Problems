def solution(chicken):
    coupons = chicken  # 주문한 치킨 수만큼 쿠폰이 발급됨.
    free_chicken = 0   # 받을 수 있는 서비스 치킨 수
    
    # 쿠폰이 10장 이상이면 교환 가능한 경우가 있음.
    while coupons >= 10:
        # 이번에 교환해서 받을 수 있는 서비스 치킨의 수
        service = coupons // 10
        free_chicken += service
        
        # 쿠폰을 교환한 후 남은 쿠폰과 서비스 치킨 발급으로 새로 획득한 쿠폰을 합침.
        coupons = coupons % 10 + service
        
    return free_chicken