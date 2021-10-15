# 백엔드 서버

## 환경변수 처리

- **python-dotenv** 패키지 설치

  ```sh
  pip3 install python-dotenv
  ```

- `.env` 파일에 다음과 같이 작성

  ```txt
  BACKEND_SERVER_IP=서버IP
  RPI_IP=라즈베리파이IP
  ```

## MQTT

- django 서버 실행 전에 mqtt 브로커 먼저 실행시킬 것
