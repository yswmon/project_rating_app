# Python 이미지를 베이스로 사용
FROM python:3.11-slim

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 파일 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 전체 프로젝트 복사
COPY . .

# 포트 개방
EXPOSE 8000

# 장고 개발 서버 실행
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
