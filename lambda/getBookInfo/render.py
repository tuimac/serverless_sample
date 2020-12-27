import traceback
import config

class Render:
    @staticmethod
    def render(data, method):
        try:
            response = dict()
            response['header'] = Render.__header(method)
            response['body'] = data
            response['statusCode'] = '200'
        except:
            response = dict()
            response['header'] = Render.__header(method)
            response['body'] = traceback.print_exc()
            response['statusCode'] = '500'
    
    @staticmethod
    def __header(method):
        if method == 'OPTION':
            header = dict()
            header['Content-Type'] = 'application/json'
            header['Access-Control-Allow-Origin'] = config.ORIGIN
            header['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
            header['Access-Control-Allow-Headers'] = 'X-PINGOTHER, Content-Type'
            header['Access-Control-Max-Age'] = '86400'
            header['Vary'] = 'Accept-Encoding, Origin'
            header['Keep-Alive'] = 'timeout=2, max=100'
            header['Connection'] = 'Keep-Alive'
            return header
        else:
            header = dict()
            header['Content-Type'] = 'application/json'
            header['Access-Control-Allow-Origin'] = config.ORIGIN
            header['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'

