# aifund
aifund

# 版本更新步骤

1. 生成版本文件
```
python setup.py sdist
```

2. 从 dist 删除除去本版本之外的其他版本内容

3. 将版本文件推送到pypi云端

```
twine upload dist/*
```
