import pandas as pd

# 데이터셋 불러오기
employment_status_df = pd.read_excel("산업_전공계열별_취업자.xlsx", sheet_name="데이터")

# 데이터프레임을 전공계열별로 분리
groups = employment_status_df.groupby(employment_status_df.전공계열)

total_df = groups.get_group("총계")
subtotal_df = groups.get_group("계")
education_df = groups.get_group("교육")
art_df = groups.get_group("예술")
social_science_df = groups.get_group("사회과학, 언론ㆍ정보학")
business_admin_df = groups.get_group("경영, 행정ㆍ법학")
natural_science_df = groups.get_group("자연과학, 수학ㆍ통계학")
information_df = groups.get_group("정보통신기술")
engineering_df = groups.get_group("공학, 제조ㆍ건설")
agriculture_df = groups.get_group("농림어업ㆍ수의학")
health_df = groups.get_group("보건")
welfare_df = groups.get_group("복지")
service_df = groups.get_group("서비스")

## 백분율 구하기 (총계)
# Object타입을 float 타입으로 변경
total_df2 = total_df['취업자(2021.2/2) (천명)'].astype('float')
# 백분율 구하기 위해 전체 '취업자수' 합
sum = total_df2.sum(axis = 0)
# 각 산업별 취업자수를 전체 취업자수로 나누면 백분율 (소숫점 2자리까지만)
total_df3 = round((total_df2.div(sum) * 100), 2)
# 백분율 컬럼값을 기존 데이터프레임에 추가
total_df4 = pd.concat([total_df['취업자(2021.2/2) (천명)'], total_df3], axis=1, join='inner')
total_df4.columns = ['취업자(2021.2/2) (천명)', '취업자(2021.2/2) (백분율)']
print(total_df4)

## 백분율 구하기 (계)
# Object타입을 float 타입으로 변경
subtotal_df2 = subtotal_df['취업자(2021.2/2) (천명)'].astype('float')
# 백분율 구하기 위해 전체 '취업자수' 합
sum = subtotal_df2.sum(axis = 0)
# 각 산업별 취업자수를 전체 취업자수로 나누면 백분율 (소숫점 2자리까지만)
subtotal_df3 = round((subtotal_df2.div(sum) * 100), 2)
# 백분율 컬럼값을 기존 데이터프레임에 추가
subtotal_df4 = pd.concat([subtotal_df['취업자(2021.2/2) (천명)'], subtotal_df3], axis=1, join='inner')
subtotal_df4.columns = ['취업자(2021.2/2) (천명)', '취업자(2021.2/2) (백분율)']
print(subtotal_df4)

## 백분율 구하기 (교육)
# 결측치 변경 : replace (- ==> 0)
education_df1 = education_df['취업자(2021.2/2) (천명)'].replace('-', '0')
# Object타입을 float 타입으로 변경
education_df2 = education_df1.astype('float')
# 백분율 구하기 위해 전체 '취업자수' 합
sum = education_df2.sum(axis = 0)
# 각 산업별 취업자수를 전체 취업자수로 나누면 백분율 (소숫점 2자리까지만)
education_df3 = round((education_df2.div(sum) * 100), 2)
# 백분율 컬럼값을 기존 데이터프레임에 추가
education_df4 = pd.concat([education_df['취업자(2021.2/2) (천명)'], education_df3], axis=1, join='inner')
education_df4.columns = ['취업자(2021.2/2) (천명)', '취업자(2021.2/2) (백분율)']
print(education_df4)

## 백분율 구하기 (예술)
# 결측치 변경 : replace (- ==> 0)
art_df1 = art_df['취업자(2021.2/2) (천명)'].replace('-', '0')
# Object타입을 float 타입으로 변경
art_df2 = art_df1.astype('float')
# 백분율 구하기 위해 전체 '취업자수' 합
sum = art_df2.sum(axis = 0)
# 각 산업별 취업자수를 전체 취업자수로 나누면 백분율 (소숫점 2자리까지만)
art_df3 = round((art_df2.div(sum) * 100), 2)
# 백분율 컬럼값을 기존 데이터프레임에 추가
art_df4 = pd.concat([art_df['취업자(2021.2/2) (천명)'], art_df3], axis=1, join='inner')
art_df4.columns = ['취업자(2021.2/2) (천명)', '취업자(2021.2/2) (백분율)']
print(art_df4)

## 백분율 구하기 (사회과학, 언론ㆍ정보학)
# 결측치 변경 : replace (- ==> 0)
social_science_df1 = social_science_df['취업자(2021.2/2) (천명)'].replace('-', '0')
# Object타입을 float 타입으로 변경
social_science_df2 = social_science_df1.astype('float')
# 백분율 구하기 위해 전체 '취업자수' 합
sum = social_science_df2.sum(axis = 0)
# 각 산업별 취업자수를 전체 취업자수로 나누면 백분율 (소숫점 2자리까지만)
social_science_df3 = round((social_science_df2.div(sum) * 100), 2)
# 백분율 컬럼값을 기존 데이터프레임에 추가
social_science_df4 = pd.concat([social_science_df['취업자(2021.2/2) (천명)'], social_science_df3], axis=1, join='inner')
social_science_df4.columns = ['취업자(2021.2/2) (천명)', '취업자(2021.2/2) (백분율)']
print(social_science_df4)

## 백분율 구하기 (경영, 행정ㆍ법학)
# 결측치 변경 : replace (- ==> 0)
business_admin_df1 = business_admin_df['취업자(2021.2/2) (천명)'].replace('-', '0')
# Object타입을 float 타입으로 변경
business_admin_df2 = business_admin_df1.astype('float')
# 백분율 구하기 위해 전체 '취업자수' 합
sum = business_admin_df2.sum(axis = 0)
# 각 산업별 취업자수를 전체 취업자수로 나누면 백분율 (소숫점 2자리까지만)
business_admin_df3 = round((business_admin_df2.div(sum) * 100), 2)
# 백분율 컬럼값을 기존 데이터프레임에 추가
business_admin_df4 = pd.concat([business_admin_df['취업자(2021.2/2) (천명)'], business_admin_df3], axis=1, join='inner')
business_admin_df4.columns = ['취업자(2021.2/2) (천명)', '취업자(2021.2/2) (백분율)']
print(business_admin_df4)

## 백분율 구하기 (자연과학, 수학ㆍ통계학)
# 결측치 변경 : replace (- ==> 0)
natural_science_df1 = natural_science_df['취업자(2021.2/2) (천명)'].replace('-', '0')
# Object타입을 float 타입으로 변경
natural_science_df2 = natural_science_df1.astype('float')
# 백분율 구하기 위해 전체 '취업자수' 합
sum = natural_science_df2.sum(axis = 0)
# 각 산업별 취업자수를 전체 취업자수로 나누면 백분율 (소숫점 2자리까지만)
natural_science_df3 = round((natural_science_df2.div(sum) * 100), 2)
# 백분율 컬럼값을 기존 데이터프레임에 추가
natural_science_df4 = pd.concat([natural_science_df['취업자(2021.2/2) (천명)'], natural_science_df3], axis=1, join='inner')
natural_science_df4.columns = ['취업자(2021.2/2) (천명)', '취업자(2021.2/2) (백분율)']
print(natural_science_df4)

## 백분율 구하기 (정보통신기술)
# 결측치 변경 : replace (- ==> 0)
information_df1 = information_df['취업자(2021.2/2) (천명)'].replace('-', '0')
# Object타입을 float 타입으로 변경
information_df2 = information_df1.astype('float')
# 백분율 구하기 위해 전체 '취업자수' 합
sum = information_df2.sum(axis = 0)
# 각 산업별 취업자수를 전체 취업자수로 나누면 백분율 (소숫점 2자리까지만)
information_df3 = round((information_df2.div(sum) * 100), 2)
# 백분율 컬럼값을 기존 데이터프레임에 추가
information_df4 = pd.concat([information_df['취업자(2021.2/2) (천명)'], information_df3], axis=1, join='inner')
information_df4.columns = ['취업자(2021.2/2) (천명)', '취업자(2021.2/2) (백분율)']
print(information_df4)

## 백분율 구하기 (공학, 제조ㆍ건설)
# 결측치 변경 : replace (- ==> 0)
engineering_df1 = engineering_df['취업자(2021.2/2) (천명)'].replace('-', '0')
# Object타입을 float 타입으로 변경
engineering_df2 = engineering_df1.astype('float')
# 백분율 구하기 위해 전체 '취업자수' 합
sum = engineering_df2.sum(axis = 0)
# 각 산업별 취업자수를 전체 취업자수로 나누면 백분율 (소숫점 2자리까지만)
engineering_df3 = round((engineering_df2.div(sum) * 100), 2)
# 백분율 컬럼값을 기존 데이터프레임에 추가
engineering_df4 = pd.concat([engineering_df['취업자(2021.2/2) (천명)'], engineering_df3], axis=1, join='inner')
engineering_df4.columns = ['취업자(2021.2/2) (천명)', '취업자(2021.2/2) (백분율)']
print(engineering_df4)

## 백분율 구하기 (농림어업ㆍ수의학)
# 결측치 변경 : replace (- ==> 0)
agriculture_df1 = agriculture_df['취업자(2021.2/2) (천명)'].replace('-', '0')
# Object타입을 float 타입으로 변경
agriculture_df2 = agriculture_df1.astype('float')
# 백분율 구하기 위해 전체 '취업자수' 합
sum = agriculture_df2.sum(axis = 0)
# 각 산업별 취업자수를 전체 취업자수로 나누면 백분율 (소숫점 2자리까지만)
agriculture_df3 = round((agriculture_df2.div(sum) * 100), 2)
# 백분율 컬럼값을 기존 데이터프레임에 추가
agriculture_df4 = pd.concat([agriculture_df['취업자(2021.2/2) (천명)'], agriculture_df3], axis=1, join='inner')
agriculture_df4.columns = ['취업자(2021.2/2) (천명)', '취업자(2021.2/2) (백분율)']
print(agriculture_df4)

## 백분율 구하기 (보건)
# 결측치 변경 : replace (- ==> 0)
health_df1 = health_df['취업자(2021.2/2) (천명)'].replace('-', '0')
# Object타입을 float 타입으로 변경
health_df2 = health_df1.astype('float')
# 백분율 구하기 위해 전체 '취업자수' 합
sum = health_df2.sum(axis = 0)
# 각 산업별 취업자수를 전체 취업자수로 나누면 백분율 (소숫점 2자리까지만)
health_df3 = round((health_df2.div(sum) * 100), 2)
# 백분율 컬럼값을 기존 데이터프레임에 추가
health_df4 = pd.concat([health_df['취업자(2021.2/2) (천명)'], health_df3], axis=1, join='inner')
health_df4.columns = ['취업자(2021.2/2) (천명)', '취업자(2021.2/2) (백분율)']
print(health_df4)

## 백분율 구하기 (복지)
# 결측치 변경 : replace (- ==> 0)
welfare_df1 = welfare_df['취업자(2021.2/2) (천명)'].replace('-', '0')
# Object타입을 float 타입으로 변경
welfare_df2 = welfare_df1.astype('float')
# 백분율 구하기 위해 전체 '취업자수' 합
sum = welfare_df2.sum(axis = 0)
# 각 산업별 취업자수를 전체 취업자수로 나누면 백분율 (소숫점 2자리까지만)
welfare_df3 = round((welfare_df2.div(sum) * 100), 2)
# 백분율 컬럼값을 기존 데이터프레임에 추가
welfare_df4 = pd.concat([welfare_df['취업자(2021.2/2) (천명)'], welfare_df3], axis=1, join='inner')
welfare_df4.columns = ['취업자(2021.2/2) (천명)', '취업자(2021.2/2) (백분율)']
print(welfare_df4)

## 백분율 구하기 (서비스)
# 결측치 변경 : replace (- ==> 0)
service_df1 = service_df['취업자(2021.2/2) (천명)'].replace('-', '0')
# Object타입을 float 타입으로 변경
service_df2 = service_df1.astype('float')
# 백분율 구하기 위해 전체 '취업자수' 합
sum = service_df2.sum(axis = 0)
# 각 산업별 취업자수를 전체 취업자수로 나누면 백분율 (소숫점 2자리까지만)
service_df3 = round((service_df2.div(sum) * 100), 2)
# 백분율 컬럼값을 기존 데이터프레임에 추가
service_df4 = pd.concat([service_df['취업자(2021.2/2) (천명)'], service_df3], axis=1, join='inner')
service_df4.columns = ['취업자(2021.2/2) (천명)', '취업자(2021.2/2) (백분율)']
print(service_df4)
