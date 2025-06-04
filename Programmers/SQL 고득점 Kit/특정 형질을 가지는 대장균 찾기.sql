SELECT COUNT(*) AS COUNT
FROM ECOLI_DATA
WHERE 
  -- 2번 형질이 없는 개체: 두 번째 비트가 0이어야 함 (2 AND GENOTYPE = 0)
  (GENOTYPE & 2) = 0
  AND (
    -- 1번 형질 또는 3번 형질이 있는 경우
    (GENOTYPE & 1) != 0 OR (GENOTYPE & 4) != 0
  );
