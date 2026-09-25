s = input().lower()
print(sorted(set(s), key=lambda x:s.count(x), reverse=True)[:3])
