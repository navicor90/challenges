class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs = []
        letter_logs = {}
        for l in logs:
            log_words = l.split(" ")
            words_with_id_at_end = log_words[1:]+[log_words[0]]
            if words_with_id_at_end[0][0].isdigit():
                digit_logs.append(l)
            else:
                letter_logs[" ".join(words_with_id_at_end)] = l
        
        new_letter_logs = [letter_logs[k] for k in sorted(letter_logs.keys())]
        return new_letter_logs+digit_logs