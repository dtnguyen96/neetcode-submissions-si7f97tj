class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        combinations = []

        def backtracking(index, path):
            
            if len(digits) == len(path):
                combinations.append("".join(path))
                return 
            
            possible_letters = digitToChar[digits[index]]
            for letter in possible_letters:
                path.append(letter)
                backtracking(index + 1, path)
                path.pop()
        
        
        if digits:
            backtracking(0, [])
        return combinations