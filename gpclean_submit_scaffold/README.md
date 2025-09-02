# gpclean_submit

Blender & Maya 공통 Deadline 제출 스캐폴딩.

## 설치
```bash
pip install -e .
```

## 사용 (Maya)
```python
from gpclean_submit.cli import submit_job
submit_job("maya", name="MyJob")
```

## 사용 (Blender)
```python
from gpclean_submit.cli import submit_job
submit_job("blender", name="MyJob")
```
