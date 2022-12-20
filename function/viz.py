import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns


## 1. 대시보드에 각 데이터 항목별로 시각화

# 캡스톤 프로젝트 설문 자료 불러오기
job = pd.read_excel('캡스톤_data_final.xlsx')


# 전공만족도에 따른 전공학점 scatter 그래프로 시각화
plt.figure(figsize=(13, 11))
x = job['major_satisfaction']  # x축: 전공만족도
y = job['major_grade']         # y축: 전공학점
plt.scatter(x, y)              # scatter 그래프
plt.show()                     # 그래프 출력

# # 두 등급으로 구분된 데이터 프레임 만들기
job['employment'] = [1 if i >= 2 else 0 for i in job['employment_status']]   # 취업 상태를 기준으로 한 class column 생성
print(job)

# 두 등급으로 구분된 설문 데이터 항목 간의 pair plot
job_data = job.drop(['타임스탬프', 'identity', 'age', 'major', 'employment_status'],axis=1)   # 가설검증에 필요하지 않은 데이터 열 삭제
sns.pairplot(job_data, hue='employment',markers=['o', 's'])  # sns tool 이용
plt.show()  # 그래프 출력


## 2. 데이터 연관도를 기반으로 한 시각화


# 데이터셋 불러오기
survey_result = pd.read_excel("캡스톤_data_final.xlsx", sheet_name="설문응답")
# survey_result_df1 = survey_result[['major_satisfaction', 'major_grade']]

# 한글 글씨 깨짐 해결
matplotlib.rcParams['font.family'] ='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] =False

# 각 데이터컬럼간 연관도 계산(corr)
corr_df = survey_result.corr(method='pearson')
print(corr_df)

# 그래프 크기 설정
plt.figure(figsize=(15, 8))
plt.subplot(1, 1, 1)

# seaborn을 이용하여 히트맵 생성
sns.heatmap(corr_df, annot=True, cmap='Blues')

plt.show()
