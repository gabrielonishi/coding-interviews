class Solution:
    def reorderSpaces(self, text: str) -> str:
        num_spaces = 0
        
        for char in text:
            if char == " ":
                num_spaces += 1

        words = text.split()
        result_text = ""
        
        if num_spaces == 0:
            return text
        if len(words) == 1:
            result_text += words[0] + (num_spaces * " ")
            return result_text

        spaces_between = " " * (num_spaces // (len(words)-1))
        spaces_end = " " * (num_spaces % (len(words)-1))

        for word in words[:-1]:
            result_text += word
            result_text += spaces_between

        result_text += words[-1]
        result_text += spaces_end

        return result_text