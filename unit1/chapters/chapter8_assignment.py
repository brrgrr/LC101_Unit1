def course_grader(test_scores):
    avg_score = sum(test_scores) / len(test_scores)
    if avg_score < 70 or min(test_scores) < 50:
        message = 'fail'
    elif avg_score >= 70 and min(test_scores) > 50:
        message = 'pass'
    return message
