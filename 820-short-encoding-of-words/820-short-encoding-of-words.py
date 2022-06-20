class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key=len,reverse=True)
        ans=''
        for w in words:
            if w+'#' not in ans:
                ans+=w+'#'
        return len(ans)