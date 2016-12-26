if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    if query_name in student_marks:
        reslist=student_marks[query_name]
    len1=len(reslist)
    sum1=sum(reslist)
    res=sum1/len1
    print(format(res,'.2f'))
