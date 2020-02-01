def split_log(log):
        return log.split(" ")
    
def minor_words_set(words1, words2):
    if len(words1) == 0 or len(words2) == 0:
        return 0
    elif words1[0] < words2[0]:
        return 1
    elif words1[0] > words2[0]:
        return 2
    elif words1[0] == words2[0]:
        return minor_words_set(words1[1:],words2[1:])
            
def reorder_letter_logs(ordered_letter_logs, log_words):
    if(len(ordered_letter_logs) == 0):
        return [log_words]
    
    ordered_words = []
    minor_param_words = minor_words_set(ordered_letter_logs[0], log_words)
    
    if minor_param_words == 1:
        ordered_words.insert(0, ordered_letter_logs[0])
        ordered_words = ordered_words + reorder_letter_logs(ordered_letter_logs[1:],log_words)
    else:
        ordered_words.insert(0, log_words)
        ordered_words = ordered_words + ordered_letter_logs
    
    return ordered_words

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs = []
        letter_logs = []
        
        for l in logs:
            log_words = split_log(l)
            words_with_id_at_end = log_words[1:]+[log_words[0]]
            if words_with_id_at_end[0][0].isdigit():
                digit_logs.append(l)
            else:
                letter_logs = reorder_letter_logs(letter_logs, words_with_id_at_end)  
        
        ordered_letters = []
        for l in letter_logs:
            l_with_id_at_start = [l[-1]]+l[:-1]
            ordered_letters.append(" ".join(l_with_id_at_start))

        return ordered_letters+digit_logs