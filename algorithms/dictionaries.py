def merge_dicts(
    a: dict,
    b: dict,
    result: dict = None
) -> dict:
    if a == {} or type(b) != dict:
        return b
    if b == {} or type(a) != dict:
        return a

    if result == None:
        result = {}
    keys = set(a.keys()).union(set(b.keys()))

    for key in keys:
        if a.get(key):
            b.setdefault(key, a[key])
        elif b.get(key):
            a.setdefault(key, b[key])
        
        if a.get(key) == b.get(key):
            result[key] = a[key]
            continue

        result[key] = merge_dicts(
            a[key],
            b[key],
            result.setdefault(key, {})
        )

    return result

def test_merge_dicts() -> None:
    assert merge_dicts({}, {}) == {}, "[1] Bad"
    print("[1] Ok")
    
    assert merge_dicts(
        {
            "dict":
            {
                "a": 1,
                "c": 3
            },
            "key": "value"
        },
        {}
    ) == {
            "dict":
            {
                "a": 1,
                "c": 3
            },
            "key": "value"
        }, "[2] Bad"
    print("[2] Ok")
    
    assert merge_dicts(
        {},
        {
            "dict":
            {
                "a": 1,
                "c": 3
            },
            "key": "value"
        }
    ) == {
            "dict":
            {
                "a": 1,
                "c": 3
            },
            "key": "value"
        }, "[3] Bad"
    print("[3] Ok")
    
    assert merge_dicts(
        {
            "dict":
            {
                "a": 1,
                "c": 3
            },
            "key": "value"
        },
        {
            "dict":
            {
                "b": 2
            }
        }
    ) == {
            "dict":
            {
                "a": 1,
                "b": 2,
                "c": 3
            },
            "key": "value"
        }, "[4] Bad"
    print("[4] Ok")
    
    assert merge_dicts(
        {
            "dict_1":
            {
                "a": 1,
                "c": 3
            },
            "dict_2":
            {
                "a": 1,
                "c": 3
            },
            "key": "value",
        },
        {
            "dict_1":
            {
                "b": 2
            }
        }
    ) == {
            "dict_1":
            {
                "a": 1,
                "b": 2,
                "c": 3
            },
            "dict_2":
            {
                "a": 1,
                "c": 3
            },
            "key": "value",
        }, "[5] Bad"
    print("[5] Ok")
    
    assert merge_dicts(
        {
            "dict_1":
            {
                "a": 1,
                "c": 3
            },
            "key": "value",
        },
        {
            "dict_2":
            {
                "b": 2
            }
        }
    ) == {
            "dict_1":
            {
                "a": 1,
                "c": 3
            },
            "key": "value",
            "dict_2":
            {
                "b": 2
            },
        }, "[6] Bad"
    print("[6] Ok")

def normalize_key(
    key: str,
    value,
    result: dict = None
) -> dict:
    """
    **Normalized only string key**
    
    **Key variants**:
        `normal` - key
        `complicated`: some__nested__levels__key

    Translated complicated keys to common view and generates dictionary with passed `value`

    **Example**:
    ```python
        key = "some__nested__levels"
        value = 123

        print(normalize_key(key, value))  # { "some": { "nested": { "levels": 123 } } }
    ```

    **Returns**:
        Dictionary with simplifyed `key` with the passed `value`
    """

    assert type(key) == str, "The `key` argument must be of string type!"
    
    if result == None:
        result = {}

    if "__" in key:
        normalize_key(
            key[key.index("__") + 2:],
            value,
            result.setdefault(key[:key.index("__")], {})
        )
        return result
    
    result.setdefault(key, value)
    return result

def test_normalize_key() -> None:
    assert normalize_key("key", 1) == { "key": 1 },\
        "[1] Bad"
    print("[1] Ok")

    assert normalize_key("some__nested__levels", 123) ==\
        { "some": { "nested": { "levels": 123 } } },\
        "[2] Bad"
    print("[2] Ok")


if __name__ == "__main__":
    test_merge_dicts()
    test_normalize_key()
