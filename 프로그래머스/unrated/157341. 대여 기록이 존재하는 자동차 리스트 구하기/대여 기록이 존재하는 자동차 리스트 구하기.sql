-- 코드를 입력하세요
# SELECT * FROM CAR_RENTAL_COMPANY_RENTAL_HIST
SELECT DISTINCT CC.CAR_ID FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY AS CH JOIN CAR_RENTAL_COMPANY_CAR AS CC ON CH.CAR_ID = CC.CAR_ID WHERE CC.CAR_TYPE='세단' AND CH.START_DATE >= '2022-10-01' ORDER BY CH.CAR_ID DESC;