from fastapi import APIRouter
import random
from .monetaryluck_schema import FortuneResponse

router = APIRouter(
    prefix="/monetaryluck",
    tags=["monetaryluck"]
)

# 운세 리스트 정의
FORTUNES = [
    "오늘은 길가다가 만원을 줍는날 !!\n엄청난 운이 따를 것입니다.",
    "오늘 많은 돈을 잃을 수도 있겠어요,,\n주머니 조심하세요 !!",
    "많은 유혹이 있을 수도 있겠어요 ! 충동구매 조심 !!",
    "뭔가 이루어질 것 같은 날입니다.\n과감한 투자를 해도 좋겠으나 너무 무리는 하지 마세요 !",
    "지갑이 세는 느낌일 것입니다,,\n가계부를 꼼꼼히 따져보고 계획을 세우세요 !",
    "그동안 당신이 수고한 일에 대한 대가가 들어오는 날 !\n많은 부가 생길 거에요 ! ",
    "생각지도 못했던 공돈이 생기거나\n공짜 혜택을 이룰 수 있는 날입니다 !!",
    "큰 것은 아니어도 소득이 생기니 기쁘겠군요.\n금액의 크고 작고는 그리 중요한 것이 아닙니다 !",
    "기대를 조금만 낮춘다면 현재의 수익에 만족할 수 있을 것이고\n그만큼 운도 많이 따를 것입니다 !",
    "이예람 신지민 파이팅"
]

@router.get("/random", response_model=FortuneResponse)
def get_random_fortune():
    """
    랜덤 운세를 반환합니다.
    """
    random_fortune = random.choice(FORTUNES)
    return {"fortune": random_fortune}
