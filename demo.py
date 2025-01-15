from fastapi import FastAPI
import uvicorn
from fastapi.responses import JSONResponse
from types import Union

# 在实例化FastAPI时，通过servers参数指定OpenAPI文档的服务器地址
app = FastAPI(servers=[{"url": "http://0.0.0.0:8000"}])

# 你的接口函数
@app.get("/test")
async def test(A: Union[int, float], B: Union[int, float]):
    result = A + B
    return JSONResponse(content={"result": result})


if __name__=="__main__":
    
    uvicorn.run(app, host="0.0.0.0", port=8000)