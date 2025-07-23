def distribute_pv(
        purchaser_id: str,
        total_pv: float,
        members: dict,
        *,
        max_depth: int = 2
    ):
    """
    購入者を含め最大 max_depth 階層まで PV をフルコピー
    """
    distribution = {}
    current = purchaser_id
    depth = 0

    while current is not None and depth <= max_depth:
        distribution[current] = round(
            distribution.get(current, 0) + total_pv, 2
        )
        current = members.get(current, {}).get("parent")
        depth += 1

    return distribution