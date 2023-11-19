import pytest
from src.utagmsengine.solver import Solver
from src.utagmsengine.dataclasses import Preference, Indifference, Criterion, Position


@pytest.fixture()
def performance_table_dict_dummy():
    return {
        'A': {'g1': 26.0, 'g2': 40.0, 'g3': 44.0},
        'B': {'g1': 2.0, 'g2': 2.0, 'g3': 68.0},
        'C': {'g1': 18.0, 'g2': 17.0, 'g3': 14.0},
        'D': {'g1': 35.0, 'g2': 62.0, 'g3': 25.0},
        'E': {'g1': -7.0, 'g2': 55.0, 'g3': 12.0},
        'F': {'g1': 25.0, 'g2': 30.0, 'g3': 12.0},
        'G': {'g1': 9.0, 'g2': 62.0, 'g3': 88.0},
        'H': {'g1': 0.0, 'g2': 24.0, 'g3': 73.0},
        'I': {'g1': 6.0, 'g2': 15.0, 'g3': 100.0},
        'J': {'g1': 16.0, 'g2': -9.0, 'g3': 0.0},
        'K': {'g1': 26.0, 'g2': 17.0, 'g3': 17.0},
        'L': {'g1': 62.0, 'g2': 43.0, 'g3': 0.0}
    }


@pytest.fixture()
def preferences_dummy():
    return [Preference(superior='G', inferior='F'), Preference(superior='F', inferior='E')]


@pytest.fixture()
def indifferences_dummy():
    return [Indifference(equal1='D', equal2='G')]


@pytest.fixture()
def criterions_dummy():
    return [Criterion(criterion_id='g1', gain=True, number_of_linear_segments=0), Criterion(criterion_id='g2', gain=True, number_of_linear_segments=0), Criterion(criterion_id='g3', gain=True, number_of_linear_segments=0)]


@pytest.fixture()
def predefined_criterions_dummy():
    return [Criterion(criterion_id='g1', gain=True, number_of_linear_segments=4), Criterion(criterion_id='g2', gain=True, number_of_linear_segments=4), Criterion(criterion_id='g3', gain=True, number_of_linear_segments=4)]


@pytest.fixture()
def positions_dummy():
    return [Position(alternative_id='A', worst_position=6, best_position=1)]


@pytest.fixture()
def hasse_diagram_dict_dummy():
    return {'A': ['F', 'K'], 'C': ['J'], 'D': ['G'], 'F': ['E', 'J'], 'G': ['B', 'D', 'F', 'H', 'K'], 'I': ['B'], 'K': ['C'], 'L': ['J'], 'B': [], 'E': [], 'H': [], 'J': []}


@pytest.fixture()
def representative_value_function_dict_dummy():
    return {'J': 0.0113, 'E': 0.1057, 'C': 0.1614, 'F': 0.2559, 'K': 0.3116, 'B': 0.3248, 'H': 0.3731, 'L': 0.374, 'A': 0.4617, 'D': 0.5233, 'G': 0.5233, 'I': 0.6325}


@pytest.fixture()
def criterion_functions_dummy():
    return {'g1': [(0.0, 0.00342706), (2.0, 0.00440622), (6.0, 0.00636454), (7.0, 0.0), (9.0, 0.00783327), (16.0, 0.0112603), (18.0, 0.0424458), (25.0, 0.151595), (26.0, 0.167187), (35.0, 0.307522), (39.0, 0.369893), (62.0, 0.369893)], 'g2': [(2.0, 0.0), (9.0, 0.0), (14.666666666666664, 0.0), (15.0, 5.79318e-05), (17.0, 0.000405522), (24.0, 0.00162209), (30.0, 0.00266486), (38.33333333333333, 0.00411316), (40.0, 0.00411316), (43.0, 0.00411316), (55.0, 0.00411316), (62.0, 0.00411316)], 'g3': [(0.0, 0.0), (12.0, 0.101619), (14.0, 0.118555), (17.0, 0.14396), (25.0, 0.211706), (33.33333333333333, 0.282275), (44.0, 0.290399), (66.66666666666666, 0.307663), (68.0, 0.320396), (73.0, 0.368146), (88.0, 0.511395), (100.0, 0.625994)]}


@pytest.fixture()
def predefined_hasse_diagram_dict_dummy():
    return {'A': ['F', 'K'], 'C': ['J'], 'D': ['G'], 'F': ['E', 'J'], 'G': ['B', 'D', 'F', 'H', 'K'], 'I': ['B'], 'K': ['C'], 'L': ['J'], 'B': [], 'E': [], 'H': [], 'J': []}


def test_get_hasse_diagram_dict(
        performance_table_dict_dummy,
        preferences_dummy,
        indifferences_dummy,
        criterions_dummy,
        positions_dummy,
        hasse_diagram_dict_dummy
):
    solver = Solver(show_logs=True)

    hasse_diagram_list = solver.get_hasse_diagram_dict(
        performance_table_dict_dummy,
        preferences_dummy,
        indifferences_dummy,
        criterions_dummy,
        #positions_dummy
    )

    assert hasse_diagram_list == hasse_diagram_dict_dummy


def test_get_representative_value_function_dict(
        performance_table_dict_dummy,
        preferences_dummy,
        indifferences_dummy,
        predefined_criterions_dummy,
        criterions_dummy,
        positions_dummy,
        representative_value_function_dict_dummy,
        criterion_functions_dummy
):
    solver = Solver(show_logs=True)

    representative_value_function_dict, criterion_functions, sampler_metrics = solver.get_representative_value_function_dict(
        performance_table_dict_dummy,
        preferences_dummy,
        indifferences_dummy,
        predefined_criterions_dummy,
        [],
        'files/polyrun-1.1.0-jar-with-dependencies.jar',
        '10'
    )

    assert representative_value_function_dict == representative_value_function_dict_dummy
    assert criterion_functions == criterion_functions_dummy


def test_predefined_get_hasse_diagram_dict(
        performance_table_dict_dummy,
        preferences_dummy,
        indifferences_dummy,
        predefined_criterions_dummy,
        positions_dummy,
        predefined_hasse_diagram_dict_dummy
):
    solver = Solver(show_logs=True)

    hasse_diagram_list = solver.get_hasse_diagram_dict(
        performance_table_dict_dummy,
        preferences_dummy,
        indifferences_dummy,
        predefined_criterions_dummy,
        positions_dummy
    )

    assert hasse_diagram_list == predefined_hasse_diagram_dict_dummy
