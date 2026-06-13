"""
نموذج تجريبي لتقييم أداء فرق التطوير الرشيقة
"""


def calculate_velocity(completed_points, planned_points):
    """حساب سرعة الفريق (Velocity Rate)"""
    if planned_points == 0:
        return 0
    return round((completed_points / planned_points) * 100, 2)


def calculate_defect_rate(num_bugs, total_issues):
    """حساب معدل الأخطاء البرمجية"""
    if total_issues == 0:
        return 0
    return round((num_bugs / total_issues) * 100, 2)


def calculate_completion_rate(completed_tasks, total_tasks):
    """حساب نسبة إنجاز المهام لكل عضو"""
    if total_tasks == 0:
        return 0
    return round((completed_tasks / total_tasks) * 100, 2)


def calculate_team_performance_score(velocity, defect_rate, completion_rate):
    """حساب نقاط الأداء الكلية للفريق بمعادلة مرجحة"""
    score = (velocity * 0.4) + ((100 - defect_rate) * 0.3) + (completion_rate * 0.3)
    return round(score, 2)


if __name__ == "__main__":
    velocity = calculate_velocity(38, 45)
    defect_rate = calculate_defect_rate(8, 67)
    completion_rate = calculate_completion_rate(10, 12)
    score = calculate_team_performance_score(velocity, defect_rate, completion_rate)

    print(f"Velocity Rate: {velocity}%")
    print(f"Defect Rate: {defect_rate}%")
    print(f"Completion Rate: {completion_rate}%")
    print(f"Team Performance Score: {score}")
