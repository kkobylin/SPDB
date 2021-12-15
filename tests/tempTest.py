dict = {
  "a": 1,
  "b": 2,
  "c": 3
}



nr = dict.get("c")

if nr is None:
    dict["c"] = 1
else:
    dict["c"] += 1

print(dict)