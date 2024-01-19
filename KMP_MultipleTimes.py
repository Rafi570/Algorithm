def KMP(pat,text):
    l_p=len(pat)
    l_t=len(text)
    lps=[0]*l_p
    j=0
    compute_lps(pat,l_p,lps)
    i=0
    while i< len(text):
        if text[i]==pat[j]:
            i+=1
            j+=1
        else:
            if j !=0 :
                j=lps[j-1]
            else:
                i+=1
        if j==len(pat):
            print(f"Found pattern at index: {i -len(pat)}")
            j=lps[j-1]
        


def compute_lps(pat,l_p,lps):
    len=0
    lps[0]=0
    i=1
    while i < l_p:
        if pat[i]==pat[len]:
            len+=1
            lps[i]=len
            i+=1
        else:
            if len!=0:
                len=lps[len-1]
            else:
                lps[i]=0
                i+=1
if __name__ == "__main__":
    text="hasan rafi ahmed rafi rafi"
    pat="rafi"
    KMP(pat,text)
