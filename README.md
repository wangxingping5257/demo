### 接口说明

1. 客户端上传分数接口
```dockerfile
path: http://127.0.0.1:8000/client/score/
method : post
入参： {
	"client_name": "客户端2",
	"client_score": 200300
}
出参：
{
	"code": 0,
	"msg": "success"
}
```
2. 分数排行榜查询接口
```dockerfile
path: http://127.0.0.1:8000/client/list/
method: get
入参：{"start": 1, "end": 2}
出参：[
    {
        "client_name": "客户端2",
        "client_score": 200300,
        "rank": 1
    },
    {
        "client_name": "客户端1",
        "client_score": 1,
        "rank": 2
    }
]
入参不传返回全量数据，传入参返回排行范围内的数据。
```
------------------
##### 附加题在tests.py 文件中