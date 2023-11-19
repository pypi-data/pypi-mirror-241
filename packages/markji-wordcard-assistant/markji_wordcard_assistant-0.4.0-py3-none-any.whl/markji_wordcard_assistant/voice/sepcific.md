# Voice 函数规范

接口

```python
async def tts(text: str, *, ...):
    # TODO
```

`*`后面的参数为可选参数,
若为必填项目,需要在函数中判断,不符合直接抛出异常