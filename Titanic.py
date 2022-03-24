# Titanic in Kaggle.
# 1️⃣ Setting packages ✨
# 1. Install numpy and Pandas.
#    → File → New project setup → Preferences for New projects → Phython interpreter → Serching package and install.

# 2. What is numpy (Numerical Python)?
#    → C언어로 구현된 파이썬 라이브러리로써, 고성능의 수치계산을 위해 제작
#      벡터 및 행렬 연산에 편리한 기능 제공
#      데이터 분석 시 사용되는 라이브러리 pandas와 matplotlib의 기반으로 사용
#      numpy에서는 기본적으로 array라는 단위로 데이터를 관리하며 이에 대해 연산을 수행 (array = 행렬 개념)

# 3. What is pandas?
#    → Python 자료구조와 호환 (List ,Tuple, Dict, NumpyArray 등)
#      큰 데이터의 빠른 Indexing, Slicing, Sorting 기능
#      두 데이터 간 Join(행,열 방향) 기능
#      데이터의 피봇팅 및 그룹핑, 통계 및 시각화 기능
#      외부 데이터를 입력 받아 Pandas 자료구조로 저장 및 출력 (CSV, 구분자가 있는 txt, 엑셀, SQL database, XML 등)

# 2️⃣ Explain about rawdata file. 👩🏻‍💻
# 1. Train.csv
#     1) This file contains detail of a subset of the passengers on board. (891 passengers)
#     2) The values in the second column (Survived) can be used to determine wheather each passenger survived or not :
#         → If it's a "1", the passenger survived and "0", the passenger died.

# 2. test.csv
#    1) Using the patterns I find in this file, I have to predict wheter the other 418 passengers on board survived.
#    2) This file does not have a "Survived" column.
#        → This information is hidden and how well I do at predicting these hidden values will help to me.

# 3. gender_submission.csv
#    1) This file is provided as an example that show how I should structure my predictions. (예측 구성 방법)
#    2) It predicts that all female survival, and male died. But my hypotheses regarding survival will be different.
#    3) My submission should have :
#       → a "PassengerID" column containing the IDs of each passenger from test.csv.
#       → a "Survived" column (that I will create) with a "1" for the rows where I think the passenger survived, and a "0" where my predict that the passenger died.
