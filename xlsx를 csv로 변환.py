import numpy as np
import pandas as pd

SRC = "정시_대학학과별_결과_25학년도_추가_261009.xlsx"   # 원본 엑셀 파일
DST = "정시_대학학과별_결과_25학년도_추가_261009.csv"   # 저장할 CSV 파일

# 전부 문자열로 읽어서 값이 바뀌지 않게 함
df = pd.read_excel(SRC, sheet_name=0, dtype=str)

# 앞뒤 공백 제거, "-"와 빈 문자열은 빈 값(NULL)으로 처리
df = df.apply(lambda s: s.str.strip())
df = df.replace({"-": np.nan, "": np.nan})

# UTF-8로 저장 (‧ 같은 특수문자 유지)
df.to_csv(DST, index=False, encoding="utf-8")
print(f"완료: {len(df)}행, {len(df.columns)}컬럼 -> {DST}")