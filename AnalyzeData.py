import pandas as pd
from csv import reader
import csv

SCORES_VER1 = ['Strongly Agree', 'Agree', 'Neutral', 'Disagree', 'Strongly Disagree']
SCORES_VER2 = ['Extremely Satisfied', 'Satisfied', 'Neutral', 'Dissatisfied', 'Extremely Dissatisfied']
SCORES_VER3 = ['Very Likely', 'Likely', 'Neutral', 'Unlikely', 'Very Unlikely']
SCORES_VER4 = ['Strongly agree', 'Agree', 'Neutral', 'Disagree', 'Strongly disagree']

OVERALL = ['QID1']
JOB_IMPACT = ['QID2']
CONTENT = ['QID31', 'QID32', 'QID67', 'QID145']
INSTRUCTOR = ['QID127', 'QID128', 'QID129']
VIRTUAL_CLASSROOM = ['QID130', 'QID131', 'QID132', 'QID59']

def main():

    with open("./tempDir/106377.csv") as file:
        # file = file.read().decode('utf-8')
        cols = pd.read_csv('./tempDir/106377.csv', nrows=0).columns
        print(type(file))
        csvreader = csv.reader(file)
        print(len(cols))
        # file = pd.read_csv('tempDir/106377.csv')
        # for line in file:
        #     print(line)
        df = pd.DataFrame(csvreader, columns=cols)
        res = []
        res.append(overall(df))
        res.append(job_impact(df))
        res.append(content(df))
        res.append(instructor(df))
        res.append(virtual_classroom(df))
        
        print(res)
        print(df.shape)


def overall(scores):
    res = 0
    cnt = 0
    for factor in OVERALL:
        for score in scores[factor].values:
            for i in range(5):
                if score == SCORES_VER1[i] or score == SCORES_VER2[i] or score == SCORES_VER3[i] or score == SCORES_VER4[i]:
                    res += (5 - i)
                    cnt += 1

    return round(res / cnt, 2)

def job_impact(scores):
    res = 0
    cnt = 0
    for factor in JOB_IMPACT:
        for score in scores[factor].values:
            for i in range(5):
                if score == SCORES_VER1[i] or score == SCORES_VER2[i] or score == SCORES_VER3[i] or score == SCORES_VER4[i]:
                    res += (5 - i)
                    cnt += 1
    # print("res : ", res)
    # print("cnt : ", cnt)
    return round(res / cnt, 2)

def content(scores):
    res = 0
    cnt = 0
    for factor in CONTENT:
        print(scores[factor].values)
        for score in scores[factor].values:
            for i in range(5):
                if score == SCORES_VER1[i] or score == SCORES_VER2[i] or score == SCORES_VER3[i] or score == SCORES_VER4[i]:
                    res += (5 - i)
                    cnt += 1
    print("res : ", res)
    print("cnt : ", cnt)    
    return round(res / cnt, 2)

def instructor(scores):
    res = 0
    cnt = 0
    for factor in INSTRUCTOR:
        for score in scores[factor].values:
            for i in range(5):
                if score == SCORES_VER1[i] or score == SCORES_VER2[i] or score == SCORES_VER3[i] or score == SCORES_VER4[i]:
                    res += (5 - i)
                    cnt += 1
    
    return round(res / cnt, 2)

def virtual_classroom(scores):
    res = 0
    cnt = 0
    for factor in VIRTUAL_CLASSROOM:
        for score in scores[factor].values:
            for i in range(5):
                if score == SCORES_VER1[i] or score == SCORES_VER2[i] or score == SCORES_VER3[i] or score == SCORES_VER4[i]:
                    res += (5 - i)
                    cnt += 1
    
    return round(res / cnt, 2)

if __name__ == "__main__":
    main() 