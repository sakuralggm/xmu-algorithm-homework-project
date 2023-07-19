import sys
import string

# 将输入重定向到新生成的result.txt中
sys.stdout = open('result.txt', 'w', encoding='GBK')

# 读入文件
file1, file2 = sys.argv[1], sys.argv[2]
detail = []
with open(file1, 'r', encoding='utf-8') as f:
    res = f.readlines()
    detail.append(res)
with open(file2, 'r', encoding='utf-8') as f:
    res = f.readlines()
    detail.append(res)

# 解析文件中的代码
str = []
for cppFile in detail:
    t = ''
    for i in range(len(cppFile)):
        line = cppFile[i].strip()
        if line == '' or line.startswith('#include') or line.startswith('using') or line.startswith('//') or line.startswith('printf') or line.startswith('return') or line.startswith('cin') or line.startswith('cout') or line.startswith('scanf') or line.startswith('ios::sync_with_stdio(false)') or line.startswith('const') or line.startswith('#define'):
            continue
        else:
            for j in range(len(line)):
                if line[j: j + 2] == '//':
                    break
                if line[j] not in string.whitespace:
                    t += line[j]
    str.append(t)

# 计算最短编辑距离
def check(a, b):
    a, b = ' ' + a, ' ' + b
    f = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
    for i in range(0, len(a) + 1):
        f[i][0] = i
    for i in range(0, len(b) + 1):
        f[0][i] = i
    for i in range(1, len(a)):
        for j in range(1, len(b)):
            f[i][j] = min(f[i - 1][j] + 1, f[i][j - 1] + 1)
            if a[i] == b[j]:
                f[i][j] = min(f[i - 1][j - 1], f[i][j])
            else:
                f[i][j] = min(f[i][j], f[i - 1][j - 1] + 1)
    return f[len(a) - 1][len(b) - 1]

editDist = check(str[0], str[1])    

# 得到结果
duplicateCheckRate = editDist / min(len(str[0]), len(str[1]))
if duplicateCheckRate <= 0.5:
    print(f'\n可疑，重复率为{(1 - duplicateCheckRate) * 100:.2f}%\n')
    for i in range(len(detail)):
        print('-'* 50)
        print('\n')
        for j in range(len(detail[i])):
            print(detail[i][j], end = "")
        print('\n')
else:
    print(f'\n不可疑')

