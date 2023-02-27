find_needle = lambda haystack: f"found the needle at position {haystack.index('needle')}"
print(find_needle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]))