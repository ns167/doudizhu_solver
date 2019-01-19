import numpy
import random



#3-13为3-K，A=14,2=15，小王=16，大王=17
#type:单=0,双=1,三带一=2，三带二=3，四带二单=4，四带两对=5，炸弹=1000
def solution(target,type,handCard):
    
    #返回可以出牌的组合


def hand_out(me_pokers, enemy_pokers, last_hand, cache):
    if not me_pokers:
        # 我全部过牌，直接获胜
        return True
    if not enemy_pokers:
        # 对手全部过牌，我失败
        return False
    # 获取我当前可以出的所有手牌组合，包括过牌
    all_hands = get_all_hands(me_pokers)
    # 遍历我的所有出牌组合，进行模拟出牌
    for hand in all_hands:
        # 如果上一轮对手出了牌，则这一轮我必须要出比对手更大的牌 或者 对手上一轮选择过牌，那么我只需出任意牌，但是不能过牌
        if (last_hand and can_comb2_beat_comb1(last_hand, hand)) or (not last_hand and hand['type'] != COMB_TYPE.PASS):
            # 模拟对手出牌，如果对手不能取胜，则我必胜
            if not hand_out(enemy_pokers, make_hand(me_pokers, hand), hand, cache):
                return True
        # 如果上一轮对手出了牌，但我这一轮选择过牌
        elif last_hand and hand['type'] == COMB_TYPE.PASS:
            # 模拟对手出牌，如果对手不能取胜，则我必胜
            if not hand_out(enemy_pokers, me_pokers, None, cache):
                return True
    # 如果之前的所有出牌组合均不能必胜，则我必败
    return False





    


class card(object):
    def __init__(self,card=''):
        self.card=card
        self.num=int(card)
        



class player(object):
    def __init__(self):
        self.handCard=[]





if __name__ == '__main__':
    allCard=[]
    
    for i in range(3,16):
        for j in range(4):
            a1=card(str(i))
            allCard.append(a1)

    a1=card(str(16))
    allCard.append(a1)
    a1=card(str(17))
    allCard.append(a1)

    
    print('总共',len(allCard),'张牌')


##    for  i in range (len(allCard)):
##        print(allCard[i].card)

    random.shuffle(allCard)
##    for  i in range (len(allCard)):
##        print(allCard[i].card)




    p1=player()
    p2=player()
    p3=player()



    for i in range(0,17):
        p1.handCard.append(allCard[i].card)
    for i in range(17,34):
        p2.handCard.append(allCard[i].card)
    for i in range(34,54):
        p3.handCard.append(allCard[i].card)


    listShow=[]
    for i in range (len(p1.handCard)):
        listShow.append(int(p1.handCard[i]))
    print('p1手牌数:',str(len(p1.handCard)))
    listShow.sort()
    
    print(listShow)
        
    













        


        
