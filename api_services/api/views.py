from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET", "POST"])
def test(request):
    if request.method == "GET":
        return Response({"result": "OK BRO"}, status=status.HTTP_200_OK)

    if request.method == "POST":
        data = request.data
        return Response({"Data": data}, status=status.HTTP_200_OK)
