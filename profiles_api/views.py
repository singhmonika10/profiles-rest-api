from rest_framework.views import APIView
from rest_framework.response import Response




class HelloApiView(APIView):
    """Test API View"""

    def get(self,request, format=None):
        """returns a list of APIView features"""
        an_apiview = [
        'uses HTTTP mothod as function(get, post, patch, put, delete) ',
        'Is simmilar to Traditional Django View',
        'Gives you the most control over your application logic',
        'Is mapped manually to URLs',

        ]
        return Response({'message':'Hello!','an_apiview':an_apiview})
