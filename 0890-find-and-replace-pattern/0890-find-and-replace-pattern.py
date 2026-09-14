class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        def get_structure_pattern(word): 
            structure = []
            char_to_id = {}
            current_id = 0
            
            for char in word:
                if char not in char_to_id:
                    current_id += 1
                    char_to_id[char] = current_id
                
                structure.append(char_to_id[char])
            return structure

        target_pattern = get_structure_pattern(pattern)
        matched_words = []
        
        for word in words:
            if get_structure_pattern(word) == target_pattern:
                matched_words.append(word)        
        return matched_words