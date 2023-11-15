def create_baller(id_baller,name,value):
    """
    function that creates a baller based on its integer id_baller, name string and float value
    :param id_baller: int
    :param name: str
    :param value: float
    :return: a baller with the id id_baller the name name and the value value
    """
    return {
        "id_baller":id_baller,
        "name":name,
        "value":value
    }


def get_id_baller(baller):
    """
    function that returns the int id of the baller baller
    :param baller: a baller with an int id
    :return: id: the int id of the baller
    """
    return baller["id_baller"]


def get_name(baller):
    return baller["name"]


def get_value(baller):
    return baller["value"]


def are_equal_ballerz(baller_a,baller_b):
    return get_id_baller(baller_a)==get_id_baller(baller_b)


def validate_baller(baller):
    """
    function that checks if the id of the baller is positive, if the name is nonempty, and the value is >0.0
    :param baller: a baller with an int id str name and float value
    :return: -, if the baller information is valid
    :raises: Exception with str message:
                "invalid id!\n", if the id of the baller is <0
                "invalid name!\n" if the name of the baller is ""
                "invalid value!\n" if the value of the baller is <=0.0,
    """
    errors = ""
    if get_id_baller(baller)<0:
        errors+="invalid id!\n"
    if get_name(baller)=="":
        errors += "invalid name!\n"
    if get_value(baller)<=0.0:
        errors += "invalid value!\n"
    if len(errors)>0:
        raise Exception(errors)

def add_baller_to_team(team,baller):
    """
    function that tries to add a baller to a team of ballerz uniquely identified by their int id
    :param team: a team of ballerz uniquely identified by their int id
    :param baller: a baller with an int id
    :return: -, if the id of the baller baller does not appear already in the team
    :raises: Exception with str message "existing id!\n" otherwise
    """
    for _baller in team:
        if are_equal_ballerz(_baller,baller):
            raise Exception("existing id!\n")
    team.append(baller)

def manage_add_baller_to_team(team,id_baller,name,value):
    """
    function that creates a baller based on the int id_baller, the string name and the float value
    validates the created baller and if it is valid
    tries to add it to the team if the team does not already contain a baller with the same id
    :param team: a team of ballerz uniquely identified by their int id
    :param id_baller: int
    :param name: string
    :param value: float
    :return: -, it the baller is valid and its id is not already present in the team
    :raises:Exception with str message:
                "invalid id!\n", if the id of the baller is <0
                "invalid name!\n" if the name of the baller is ""
                "invalid value!\n" if the value of the baller is <=0.0,
            Exception with str message "existing id!\n" if its id is already present in the team
    """
    baller = create_baller(id_baller,name,value)
    validate_baller(baller)
    add_baller_to_team(team,baller)

def test_manage_add_baller_to_team():
    team = []

    id_baller = 23
    name = "Jordan"
    value = 9000.1
    manage_add_baller_to_team(team,id_baller,name,value)
    baller = create_baller(id_baller, name, value)
    assert len(team) == 1
    are_equal_ballerz(baller,team[0])
    inv_id_baller = -23
    inv_name = ""
    inv_value = -9000.1
    try:
        manage_add_baller_to_team(team,inv_id_baller,inv_name,inv_value)
        assert False
    except Exception as ex:
        assert str(ex)=="invalid id!\ninvalid name!\ninvalid value!\n"
    try:
        manage_add_baller_to_team(team,id_baller,name,value)
        assert False
    except Exception as ex:
        assert str(ex) == "existing id!\n"

def test_add_baller_to_team():
    team = []
    id_baller = 23
    name = "Jordan"
    value = 9000.1
    baller = create_baller(id_baller, name, value)
    add_baller_to_team(team,baller)
    assert len(team) == 1
    are_equal_ballerz(baller,team[0])
    try:
        add_baller_to_team(team, baller)
        assert False
    except Exception as ex:
        assert str(ex)=="existing id!\n"

def test_validate_baller():
    id_baller = 23
    name = "Jordan"
    value = 9000.1
    baller = create_baller(id_baller, name, value)
    validate_baller(baller)
    inv_id_baller = -23
    inv_name = ""
    inv_value = -9000.1
    inv_baller = create_baller(inv_id_baller, inv_name, inv_value)
    try:
        validate_baller(inv_baller)
        assert False
    except Exception as ex:
        assert str(ex)=="invalid id!\ninvalid name!\ninvalid value!\n"


def test_create_baller():
    id_baller = 23
    name = "Jordan"
    value = 9000.1
    epsilon = 0.0001
    baller = create_baller(id_baller,name,value)
    assert id_baller == get_id_baller(baller)
    assert name == get_name(baller)
    assert abs(value - get_value(baller) ) < epsilon


def run_all_tests():
    test_create_baller()
    test_validate_baller()
    test_add_baller_to_team()
    test_manage_add_baller_to_team()

def main():
    run_all_tests()

main()