def solution(enroll, referral, seller, amount):
    tooth = {"center": ["center", 0]}
    for i, name in enumerate(referral):
        if name == '-':
            tooth[enroll[i]] = ["center", 0]
        else:
            tooth[enroll[i]] = [name, 0]
    
    for i, person in enumerate(seller):
        price = amount[i] * 100
        curr_person = person
        while price >= 1:
            tooth[curr_person][1] += price - price // 10
            price = price // 10
            curr_person = tooth[curr_person][0]
    
    ans = []
    for key, value in tooth.items():
        if key != 'center':
            ans.append(value[1])
    
    return ans