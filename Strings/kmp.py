# Kunth-Morris-Pratt Pattern Finding

def gen_lps(pattern):
  lps = [0]
  j = 0
  for i in range(1, len(pattern)):
    while(j > 0 and pattern[i] != pattern[j]):
      j = lps[j - 1]
    if(pattern[i] == pattern[j]):
      j += 1
    lps.append(j)
  return lps

def kmp(text, pattern):
  lps = gen_lps(pattern)
  i = 0 # i for text
  j = 0 # j for pattern
  len_t = len(text)
  len_p = len(pattern)
  for i in range(len_t):
    while(j > 0 and text[i] != pattern[j]):
      j = lps[j - 1]
    if(text[i] == pattern[j]):
      j += 1
    if(j == len_p):
      break
  return j == len_p

print(gen_lps("abcdabca"))
print(gen_lps("abcaby"))
print(gen_lps("aabaabaaa"))
print(kmp("abxabcabcaby", "abcaby"))
