from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from client import models
from client import serializers

# Create your views here.


class ScoreCreateView(generics.CreateAPIView):
    """
    入参
     {
        "client_name": "客户端1",
        "client_score": 20000
    }
    """
    queryset = models.ClientScore.objects.filter(state=1)
    serializer_class = serializers.ClientListSerializer

    def post(self, request, *args, **kwargs):
        req_data = request.data
        serializer = self.get_serializer(data=req_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({"code": 0, "msg": "success"})


class ClientListView(generics.ListAPIView):
    """
    入参
    start=1&end=2
    """
    queryset = models.ClientScore.objects.filter(state=1).order_by("-client_score")
    serializer_class = serializers.ClientListSerializer

    def list(self, request, *args, **kwargs):
        start, end = self.validate_params(request)
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        if end > len(serializer.data):
            raise Exception("数据校验失败-排行榜总数为：%s" % len(serializer.data))
        data_list = self.get_data(serializer.data, start, end)

        return Response(data_list)

    def validate_params(self, request):
        try:
            start = int(request.query_params.get("start", 0))
            end = int(request.query_params.get("end", 0))
        except Exception:
            raise Exception("参数类型错误-必须是int类型")
        if start > end:
            raise Exception("start必须小于end")
        return start, end

    def get_data(self, data_list, start=0, end=0):
        if end:
            data_list = data_list[start if start==0 else start-1: end]
        for index, data in enumerate(data_list, start+1 if start == 0 else start):
            data["rank"] = index
        return data_list


