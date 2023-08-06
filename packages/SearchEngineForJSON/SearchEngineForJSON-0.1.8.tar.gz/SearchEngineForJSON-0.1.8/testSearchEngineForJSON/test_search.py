
from SearchEngineForJSON.search import Search

data = {
    "name1": "Nakamura",
    "name2": {
        "name2-1": "Aoi",
        "name2-2": [
            "listA",
            "listB",
            {
                True: "listInDict1",
                2: "listInDict2",
                2.2: {
                    "listC-3-1": "hello",
                    "listC-3-2": "world",
                    "listC-3-3": [
                        "Sunday",
                        "Monday",
                        "Tuesday"
                    ],
                    "listC-3-4": 5,
                    "listC-3-5": True,
                    "listC-3-6": False,
                    "listC-3-7": None
                },
                "->": "listInDict3",
                "->->": "listInDict4",
                "->->->": "listInDict5",
                "->hello": "listInDict6",
                "hello->": "listInDict7",
                "->hello->": "listInDict8",
                "he->llo": [
                    "in",
                    "out"
                ],
                "2.2": "string",
                "2.3": 2,
                "2.4": 2.2,
                "2.5": "listInDict6"
            },
            "listD",
            "listE"
        ],
        "name2-3": "python",
        "name2-4": [
            "Docker",
            "kubernetes",
            "Docker-compose"
        ]
    },
    "name3": "json",
    "name4": "search"
}

typeSearchAnswer = [
    ['name1', 'Nakamura'],
    ['name3', 'json'],
    ['name4', 'search'],
    ['name2->name2-1', 'Aoi'],
    ['name2->name2-3', 'python'],
    ['name2->name2-2->list(0)', 'listA'],
    ['name2->name2-2->list(1)', 'listB'],
    ['name2->name2-2->list(3)', 'listD'],
    ['name2->name2-2->list(4)', 'listE'],
    ['name2->name2-2->list(2)->bool(True)', 'listInDict1'],
    ['name2->name2-2->list(2)->int(2)', 'listInDict2'],
    ['name2->name2-2->list(2)->(>)', 'listInDict3'],
    ['name2->name2-2->list(2)->(>)(>)', 'listInDict4'],
    ['name2->name2-2->list(2)->(>)(>)(>)', 'listInDict5'],
    ['name2->name2-2->list(2)->(>)hello', 'listInDict6'],
    ['name2->name2-2->list(2)->hello(>)', 'listInDict7'],
    ['name2->name2-2->list(2)->(>)hello(>)', 'listInDict8'],
    ['name2->name2-2->list(2)->2.2', 'string'],
    ['name2->name2-2->list(2)->2.5', 'listInDict6'],
    ['name2->name2-2->list(2)->float(2.2)->listC-3-1', 'hello'],
    ['name2->name2-2->list(2)->float(2.2)->listC-3-2', 'world'],
    ['name2->name2-2->list(2)->float(2.2)->listC-3-3->list(0)', 'Sunday'],
    ['name2->name2-2->list(2)->float(2.2)->listC-3-3->list(1)', 'Monday'],
    ['name2->name2-2->list(2)->float(2.2)->listC-3-3->list(2)', 'Tuesday'],
    ['name2->name2-2->list(2)->he(>)llo->list(0)', 'in'],
    ['name2->name2-2->list(2)->he(>)llo->list(1)', 'out'],
    ['name2->name2-4->list(0)', 'Docker'],
    ['name2->name2-4->list(1)', 'kubernetes'],
    ['name2->name2-4->list(2)', 'Docker-compose'],
]

getAllAnswear = [
    ['name1', 'Nakamura'],
    ['name3', 'json'],
    ['name4', 'search'],
    ['name2->name2-1', 'Aoi'],
    ['name2->name2-3', 'python'],
    ['name2->name2-2->list(0)', 'listA'],
    ['name2->name2-2->list(1)', 'listB'],
    ['name2->name2-2->list(3)', 'listD'],
    ['name2->name2-2->list(4)', 'listE'],
    ['name2->name2-2->list(2)->bool(True)', 'listInDict1'],
    ['name2->name2-2->list(2)->int(2)', 'listInDict2'],
    ['name2->name2-2->list(2)->(>)', 'listInDict3'],
    ['name2->name2-2->list(2)->(>)(>)', 'listInDict4'],
    ['name2->name2-2->list(2)->(>)(>)(>)', 'listInDict5'],
    ['name2->name2-2->list(2)->(>)hello', 'listInDict6'],
    ['name2->name2-2->list(2)->hello(>)', 'listInDict7'],
    ['name2->name2-2->list(2)->(>)hello(>)', 'listInDict8'],
    ['name2->name2-2->list(2)->2.2', 'string'],
    ['name2->name2-2->list(2)->2.3', 2],
    ['name2->name2-2->list(2)->2.4', 2.2],
    ['name2->name2-2->list(2)->2.5', 'listInDict6'],
    ['name2->name2-2->list(2)->float(2.2)->listC-3-1', 'hello'],
    ['name2->name2-2->list(2)->float(2.2)->listC-3-2', 'world'],
    ['name2->name2-2->list(2)->float(2.2)->listC-3-4', 5],
    ['name2->name2-2->list(2)->float(2.2)->listC-3-5', True],
    ['name2->name2-2->list(2)->float(2.2)->listC-3-6', False],
    ['name2->name2-2->list(2)->float(2.2)->listC-3-7', None],
    ['name2->name2-2->list(2)->float(2.2)->listC-3-3->list(0)', 'Sunday'],
    ['name2->name2-2->list(2)->float(2.2)->listC-3-3->list(1)', 'Monday'],
    ['name2->name2-2->list(2)->float(2.2)->listC-3-3->list(2)', 'Tuesday'],
    ['name2->name2-2->list(2)->he(>)llo->list(0)', 'in'],
    ['name2->name2-2->list(2)->he(>)llo->list(1)', 'out'],
    ['name2->name2-4->list(0)', 'Docker'],
    ['name2->name2-4->list(1)', 'kubernetes'],
    ['name2->name2-4->list(2)', 'Docker-compose']
]


valueSearchAnswear = [
    ['name2->name2-2->list(2)->(>)hello', 'listInDict6'],
    ['name2->name2-2->list(2)->2.5', 'listInDict6']
]

subStringSearchAnswear = [
    ['name2->name2-2->list(0)', 'listA'],
    ['name2->name2-2->list(1)', 'listB'],
    ['name2->name2-2->list(3)', 'listD'],
    ['name2->name2-2->list(4)', 'listE'],
    ['name2->name2-2->list(2)->bool(True)', 'listInDict1'],
    ['name2->name2-2->list(2)->int(2)', 'listInDict2'],
    ['name2->name2-2->list(2)->(>)', 'listInDict3'],
    ['name2->name2-2->list(2)->(>)(>)', 'listInDict4'],
    ['name2->name2-2->list(2)->(>)(>)(>)', 'listInDict5'],
    ['name2->name2-2->list(2)->(>)hello', 'listInDict6'],
    ['name2->name2-2->list(2)->hello(>)', 'listInDict7'],
    ['name2->name2-2->list(2)->(>)hello(>)', 'listInDict8'],
    ['name2->name2-2->list(2)->2.5', 'listInDict6']
]

startStringSearchAnswear = [
    ['name2->name2-2->list(2)->bool(True)', 'listInDict1'],
    ['name2->name2-2->list(2)->int(2)', 'listInDict2'],
    ['name2->name2-2->list(2)->(>)', 'listInDict3'],
    ['name2->name2-2->list(2)->(>)(>)', 'listInDict4'],
    ['name2->name2-2->list(2)->(>)(>)(>)', 'listInDict5'],
    ['name2->name2-2->list(2)->(>)hello', 'listInDict6'],
    ['name2->name2-2->list(2)->hello(>)', 'listInDict7'],
    ['name2->name2-2->list(2)->(>)hello(>)', 'listInDict8'],
    ['name2->name2-2->list(2)->2.5', 'listInDict6']
]


endStringSearchAnswear = [
    ['name2->name2-2->list(2)->(>)hello', 'listInDict6'],
    ['name2->name2-2->list(2)->2.5', 'listInDict6']
]



def test_typeSearch():
    assert Search.typeSearch(data, str) == typeSearchAnswer


def test_getAll():
    assert Search.getAll(data) == getAllAnswear


def test_valueSearch():
    assert Search.valueSearch(data, "listInDict6") == valueSearchAnswear
    assert Search.valueSearch(data, "listInDict6gbar@urba@") == []

def test_subStringSearch():
    assert Search.subStringSearch(data, "list") == subStringSearchAnswear
    assert Search.subStringSearch(data, "lisgpewbu@piub4er") == []

def test_startStringSearch():
    assert Search.startStringSearch(data, "listIn") == startStringSearchAnswear
    assert Search.startStringSearch(data, "gh@reaugaburgbe@ru") == []


def test_endStringSearch():
    assert Search.endStringSearch(data, "Dict6") == endStringSearchAnswear
    assert Search.endStringSearch(data, "ga@oubvaourb@iu") == []








