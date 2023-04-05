from get_plan import get_plan


def test_should_return_expected_goals_with_rounding():
    goals = get_plan(500, 3, 50)

    assert goals == [750, 1125, 1687]


def test_should_return_expected_goals_without_rounding():
    goals = get_plan(100, 4, 100)

    assert goals == [200, 400, 800, 1600]


def test_should_return_zeros_when_current_production_is_0():
    goals = get_plan(0, 4, 30)

    assert goals == [0, 0, 0, 0]


def test_should_return_fixed_goals_when_percent_is_0():
    goals = get_plan(100, 3, 0)

    assert goals == [100, 100, 100]


def test_should_return_empty_list_when_month_is_0():
    goals = get_plan(250, 0, 50)

    assert goals == []
