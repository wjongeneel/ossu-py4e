score = float(input("Enter Score: "))

def get_result(score):
    
    if score >= 0.0 and score <= 1.0: 
        if score >= 0.9:
            return "A"
        elif score >= 0.8:
            return "B"
        elif score >= 0.7:
            return "C"
        elif score >= 0.6:
            return "D"
        elif score < 0.6:
            return "F"
        else:
            pass
    else:
        return "score out of range"

print(get_result(score))