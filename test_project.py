from project import creating, updating, deleting


def test_creating(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "walk the dog")
    table, c = creating([], 0)
    assert table == [{"Task ID": 1, "Task": "walk the dog"}] and c == 1


def test_updating(monkeypatch):
    inputs = iter(["1", "do homework"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    table = updating([{"Task ID": 1, "Task": "walk the dog"}])
    assert table == [{"Task ID": 1, "Task": "do homework"}]


def test_deleting(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "1")
    table = deleting([{"Task ID": 1, "Task": "do homework"}])
    assert table == []

