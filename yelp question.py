def solution(trendy_businesses, favorite_businesses):
    result = []

    trendy_ind = 0
    fav_ind = 0

    while trendy_ind < len(trendy_businesses) and fav_ind < len(favorite_businesses):
        if trendy_businesses[trendy_ind]["num_reviews"] > favorite_businesses[fav_ind]["num_reviews"]:
            result.append(trendy_businesses[trendy_ind])
            trendy_ind += 1
        else:
            result.append(favorite_businesses[fav_ind])
            fav_ind += 1
    
    if trendy_ind < len(trendy_businesses):
        result += trendy_businesses[trendy_ind:]
    else:
        result += favorite_businesses[fav_ind:]
    
    return result
