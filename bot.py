import random

# 이 리스트에는 랜덤 응답들이 있습니다 (원하는 대로 추가하거나 번역해도 됩니다)
random_responses = ["그것은 정말 흥미로워요. 더 말해주세요.",
                    "그렇군요. 계속 이야기해 주세요.",
                    "왜 그렇게 말하시나요?",
                    "요즘 날씨가 참 신기하죠, 그렇죠?",
                    "주제를 바꾸죠.",
                    "어제 경기 보셨어요?"]

print("안녕하세요, 저는 Marvin이라고 합니다, 간단한 로봇입니다.")
print("'안녕'을 입력하여 언제든 이 대화를 끝낼 수 있습니다.")
print("각 답변을 입력한 후 '엔터'를 누르세요.")
print("오늘 기분은 어떠세요?")

while True:
    # 사용자가 텍스트를 입력할 때까지 기다립니다.
    user_input = input("> ")
    if user_input.lower() == "안녕":
        # '안녕'을 입력하면 (대소문자 상관없이), 루프를 빠져나옵니다.
        break
    else:
        response = random.choices(random_responses)[0]
        print(response)

print("대화해 주셔서 감사합니다, 안녕히 가세요!")
