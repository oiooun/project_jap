import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# 데이터셋 불러오기
survey_result = pd.read_excel("C:/Users/syk19/PycharmProjects/pythonProject21/캡스톤_설문_final.xlsx", sheet_name="설문응답")


# 한글 글씨 깨짐 해결
matplotlib.rcParams['font.family'] ='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] =False



# 1. 전공만족도와 전공학점 간의 상관관계를 그래프로 나타냄 (종속변수(y): 전공학점, 고정변인(x): 전공만족도)
#survey_result_df1 = survey_result[(survey_result['major_satisfaction']) | (survey_result['major_grade'])]
survey_result_df1 = survey_result[['major_satisfaction', 'major_grade']]
# survey_result_df1 = survey_result_df1.set_index('major_satisfaction')
print(survey_result_df1)
# survey_result_df1.plot.scatter(x='major_satisfaction', y='major_grade')

plt.figure(figsize=(200, 100))
plt.subplot(2, 2, 1)
# plt.plot(survey_result_df1)
plt.scatter(x=survey_result_df1['major_satisfaction'], y=survey_result_df1['major_grade'], color='blue', alpha=0.4, s=150)
plt.title('전공만족도와 전공학점 간의 상관관계')  # 제목
plt.xlim([0,6])
plt.ylim([0,7])
plt.xlabel('전공만족도')  # x축레이블
plt.ylabel('전공학점')  # y축레이블



# 2. 전공학점과 취업자신감 간의 상관관계를 그래프로 나타냄 (종속변수(y): 취업자신감, 고정변인(x): 전공학점)

survey_result_df2 = survey_result[['major_grade', 'job_confidence']]
# survey_result_df1 = survey_result_df1.set_index('major_satisfaction')
print(survey_result_df2)
# survey_result_df1.plot.scatter(x='major_satisfaction', y='major_grade')

plt.figure(figsize=(200, 100))
plt.subplot(2, 2, 2)
# plt.plot(survey_result_df1)
plt.scatter(x=survey_result_df2['major_grade'], y=survey_result_df2['job_confidence'], color='blue', alpha=0.4, s=150)
plt.title('전공학점과 취업자신감 간의 상관관계')  # 제목
plt.xlim([0,7])
plt.ylim([0,7])
plt.xlabel('전공학점')  # x축레이블
plt.ylabel('취업자신감')  # y축레이블


# 3. 전공만족도와 취업상태 간의 상관관계를 그래프로 나타냄 (종속변수(y): 취업상태, 고정변인(x): 전공만족도)

survey_result_df3 = survey_result[['major_satisfaction', 'employment_status']]
# survey_result_df1 = survey_result_df1.set_index('major_satisfaction')
print(survey_result_df3)
# survey_result_df1.plot.scatter(x='major_satisfaction', y='major_grade')

plt.figure(figsize=(200, 100))
plt.subplot(2, 2, 3)
# plt.plot(survey_result_df1)
plt.scatter(x=survey_result_df3['major_satisfaction'], y=survey_result_df3['employment_status'], color='blue', alpha=0.4, s=150)
plt.title('전공만족도와 취업 간의 상관관계')  # 제목
plt.xlim([0,6])
plt.ylim([0,4])
plt.xlabel('전공만족도')  # x축레이블
plt.ylabel('취업')  # y축레이블

# 4. 대학생활만족도와 취업상태 간의 상관관계를 그래프로 나타냄 (종속변수(y): 취업상태, 고정변인(x): 대학생활만족도)

survey_result_df4 = survey_result[['univ_life_satisfaction', 'employment_status']]
# survey_result_df1 = survey_result_df1.set_index('major_satisfaction')
print(survey_result_df4)
# survey_result_df1.plot.scatter(x='major_satisfaction', y='major_grade')

plt.figure(figsize=(200, 100))
plt.subplot(2, 2, 4)
# plt.plot(survey_result_df1)
plt.scatter(x=survey_result_df4['univ_life_satisfaction'], y=survey_result_df4['employment_status'], color='blue', alpha=0.4, s=150)
plt.title('전공만족도와 전공학점 간의 상관관계')  # 제목
plt.xlim([0,6])
plt.ylim([0,4])
plt.xlabel('전공만족도')  # x축레이블
plt.ylabel('전공학점')  # y축레이블


plt.show()
