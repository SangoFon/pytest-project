import pytest


@pytest.fixture(scope= "module")
def dict_prime():
    yield{2,3,5,7,11,13,17,19}

def test_dict_prime(dict_prime):
    assert 5 in dict_prime

def test_dict_prime2(dict_prime):
    assert len(dict_prime)==8

@pytest.fixture(scope="module")
def member_tag():
    tag = {"one":"Marie", "two":"Calvin","three":"jordan","four":"nsangou"}
    print("\nBefore yield1\n")
    yield tag
    print("\nafter yield1\n")

def test_member_tag(member_tag):
    assert "four","nsangou" in tag

@pytest.fixture(scope="module")
def member_info(member_tag):
    lastname={'one':"Boys",'two':"nicholson",'three':"tyler",'four':"abdou",}
    team_member= {i:[member_tag[i],lastname[i]] for i in member_tag.keys()}
    print("\n\nBefore yield2\n")
    yield team_member
    print("\nafter yield2\n")

def test_member_info(member_info):
    assert member_info["one"]==["Marie","Boys"]

def test_member_infos(member_info):
    assert member_info["two"]==["Calvin","nicholson"]
