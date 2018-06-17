def solution(total_money, total_damage, costs, damages):
    # write your code in Python 3.6
    
    dmg_cost_dict = {}
    
    for i in range(len(costs)):
        for dmg, cost in dmg_cost_dict.items():
            subtotal_dmg = dmg + damages[i]
            subtotal_cost = cost + costs[i]
            if subtotal_dmg >= total_damage and subtotal_cost <= total_money:
                return True
            if subtotal_dmg < total_damage and subtotal_cost < total_money:
                if subtotal_dmg not in dmg_cost_dict:
                    dmg_cost_dict[subtotal_dmg] = subtotal_cost
                else:
                    dmg_cost_dict[subtotal_dmg] = subtotal_cost if subtotal_cost < dmg_cost_dict[subtotal_dmg] else dmg_cost_dict[subtotal_dmg]

        if damages[i] >= total_damage and costs[i] <= total_money:
            return True
        else:
            dmg_cost_dict[damages[i]] = costs[i]
        
    return False
        
                
    