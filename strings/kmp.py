def KMPSearch(pat,txt):
  M=len(pat)
  N=len(txt)

  # array to hold the longest prefixes
  lps =[0]*M
  j = 0 # index for the pattern
  computeLPSarray(pat, M, lps)
  i =0 #index for txt

  while i<N:
    if pat[j] == txt[i]:
      i +=1
      j +=1
    if j==M:
        print "found pattern at "+ str(i-j)
        j =lps[j-1]
    elif i<N  and pat[j] != txt[i]:
      if j!=0:
        j=lps[j-1]
      else:
        i +=1

def computeLPSarray(pat, M , lps):
    len=0; 3#length of tht previous longest suffix
    lps[0]=0
    i=1

    while i<M:
        if pat[i]==pat[len]:
            len+=1
            lps[i]=len
            i +=1
        else:
            if len!=0:
                len=lps[len-1]
            else:
                lps[i]=0
                i +=1

txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
KMPSearch(pat, txt)
                    

