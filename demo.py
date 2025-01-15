import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# 定义输入数据模型
class TestInput(BaseModel):
    A: float
    B: float

# 初始化 FastAPI 应用
app = FastAPI(servers=[{"url": "http://0.0.0.0:8000"}])

def test(A: float, B: float) -> float:
    return A + B

# 定义 API 路由
@app.post("/test")
async def add_numbers(input_data: TestInput):
    try:
        result = test(input_data.A, input_data.B)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)