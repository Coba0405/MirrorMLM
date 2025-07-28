# 活動費（イベント参加費、セールス費、交通費を計算）
def calc_monthly_activity_cost(area: str, invite_per_month: int) -> int:
    event_cost = 0
    sales_cost = 0
    move_cost = 0
    activity_cost_monthly = 0
    # 辞書の作成
    AREA_COST = {
        'city_center': {"event":6000, "sales_unit":1000, "move_unit":500},
        'local_city': {"event":5000, "sales_unit":1000, "move_unit":300},
        'local_town': {"event":4000, "sales_unit":900, "move_unit":200}
    }
    cost = AREA_COST.get(area)


    if area not in AREA_COST:
        return 0
    if not cost:
        return 0
    # フロントから地域を取得しその地域によって「イベント活動費」を算出する
    if area == 'city_center':
        event_cost = AREA_COST[area]["event"]
    elif area == 'local_city':
        event_cost = AREA_COST[area]["event"]
    elif area == 'local_town':
        event_cost = AREA_COST[area]["event"]
    activity_cost_monthly += event_cost

    # フロントからで地域と勧誘人数(invite_per_month)の両方を取得できた時、「販促活動費」を算出する
    if area == 'city_center':
        sales_cost = AREA_COST[area]["sales_unit"] * invite_per_month
    elif area == 'local_city':
        sales_cost = AREA_COST[area]["sales_unit"] * invite_per_month
    elif area == 'local_town':
        sales_cost = AREA_COST[area]["sales_unit"] * invite_per_month
    activity_cost_monthly += sales_cost

    # フロントからで地域と勧誘人数(invite_per_month)の両方を取得できた時、「交通費」を算出する
    if area == 'city_center':
        move_cost = AREA_COST[area]["move_unit"] * invite_per_month
    elif area == 'local_city':
        move_cost = AREA_COST[area]["move_unit"] * invite_per_month
    elif area == 'local_town':
        move_cost = AREA_COST[area]["move_unit"] * invite_per_month
    activity_cost_monthly += move_cost

    # event_cost + sales_cost + move_cost の合計額をclass TotalCostのactivity_costに加算する
    return activity_cost_monthly