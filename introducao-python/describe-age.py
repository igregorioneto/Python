describe_age = lambda a:"You're a(n) "+["kid", "teenager", "adult", "elderly"][(a>12)+(a>17)+(a>64)]
print(describe_age(70))

def describe_age2(a):
  s="kid"if a<13 else "teenager" if a<18 else "adult" if a<64 else "elderly"
  return f"You're a(n) {s}"

print(describe_age2(70))

describe_age3=lambda a:"You're a(n) " + ("kid" if a<13 else"teenager" if a<18 else "adult" if a<64 else"elderly")
print(describe_age3(70))